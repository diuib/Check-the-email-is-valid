import requests
import re
import configparser
import multiprocessing
import frozen


WEBSITE = 'http://www.mailtester.com/testmail.php'
INIPATH = 'config.ini'
THREADNUM = 5                                                       #并发线程数

def check_email_usable(emails):
    """传入email数组
    返回[正确email[]，[错误email， 错误原因]]
    """
    correct_emails = []  # 存放正确的email
    errors = []
    wrongmsg = ''
    used, ip = get_proxies_from_file()
    pattern = re.compile(r'(?<=<td bgcolor="#FF4444">).+(?=</td>)')  # 匹配网页结果的正则表达式

    for email in emails:
        data = {'lang': 'en', 'email': email}                        # post的数据包
        try:
            if used=='1':
                proxie = {"http":ip}
                r = requests.post('http://ip-api.com/json/', data=data, proxies=proxie)
                r = requests.post(WEBSITE, data=data, proxies = proxie)                        # 进行POST
            else:
                r = requests.post('http://ip-api.com/json/', data=data)
                r = requests.post(WEBSITE, data=data)  # 进行POST
        except:
            wrongmsg = '异常'
        else:
            webpage = re.sub(r'\s+|<br />|<br/>|<br>', ' ', r.text)      # 格式化网页，去掉换行
            errortext = pattern.findall(webpage)                         # 使用正则匹配，查找是否有未成功的关键字, errortext保存结果
            if len(errortext) == 0:
                correct_emails.append(email)
            else:
                errors.append([email, ';'.join(errortext)])
            if r.text.find('403') > 0 and r.text.find('IP') > 0:
                wrongmsg = r.text

    return [correct_emails, errors, wrongmsg]


def check_email_usable_thread(emails):
    """check_email_usable()的并发版，能够更快的执行完毕。
    并发线程数使用 THREADNUM 调节
    """
    pool_arg = []
    correct_emails = []
    errors = []
    wrongmsg = []
    n = round(len(emails)/THREADNUM+0.4999)
    for i in range(0, len(emails), n):
        pool_arg.append(emails[i:i + n])
    pool = multiprocessing.Pool(THREADNUM)
    result = pool.map(check_email_usable, pool_arg)
    for r in result:
        if r[0]:
            correct_emails.extend(r[0])
    for r in result:
        if r[1]:
            errors.extend(r[1])
    for r in result:
        if r[2]:
            wrongmsg.extend(r[2])
    pool.close()
    pool.join()
    return [correct_emails, errors, wrongmsg]


def combine_mail(domains, keywords):
    """传入域名和关键字
    返回组合后的邮箱列表
    """
    emails = [key + '@' + domain for key in keywords for domain in domains]
    return emails


def get_domains_from_file():
    """读取配置文件中的网址
    """
    cf = configparser.ConfigParser(strict=False, allow_no_value=True)
    cf.read(INIPATH, encoding='UTF-8')
    domains = cf.options('domains')
    return domains


def get_keywords_from_file():
    """读取配置文件中的关键字
        """
    cf = configparser.ConfigParser(strict=False, allow_no_value=True)
    cf.read(INIPATH, encoding='UTF-8')
    keywords = cf.options('keywords')
    return keywords

def get_proxies_from_file():
    """读取配置文件中的代理
            """
    cf = configparser.ConfigParser(strict=False, allow_no_value=True)
    cf.read(INIPATH, encoding='UTF-8')
    used = cf.get("proxies", "used")
    ip = cf.get("proxies", "ip")
    return [used, ip]

def set_domains_to_file(domains):
    """把网址写入配置文件
    """
    cf = configparser.ConfigParser(strict=False, allow_no_value=True)
    cf.read(INIPATH, encoding='UTF-8')
    cf.remove_section('domains')
    cf.add_section('domains')
    for domain in domains:
        cf.set('domains', domain)
    with open(INIPATH, 'w', encoding='utf-8') as configfile:
        cf.write(configfile)


def set_keywords_to_file(keywords):
    """把关键词写入配置文件
    """
    cf = configparser.ConfigParser(strict=False, allow_no_value=True)
    cf.read(INIPATH, encoding='UTF-8')
    cf.remove_section('keywords')
    cf.add_section('keywords')
    for keyword in keywords:
        cf.set('keywords', keyword)
    with open(INIPATH, 'w', encoding='utf-8') as configfile:
        cf.write(configfile)


if __name__ == '__main__':

    # 模块测试
    example = {'test_help@smzdm.com':1,
              'server@sdfsdfsdfd,com':0,
              'hezuo_gn@smzdm.com':1,
              'hezuo_hw@smzdm.com': 1,
              'auto@zmail.smzdm.com':1,
              'nono@zmail.smzdm.com':0}
    emails = []
    pos = []
    neg = []
    for key, value in example.items():
        emails.append(key)
        if value == 1:
            pos.append(key)
        else:
            neg.append(key)
    correct_email, errors = check_email_usable_thread(emails)
    print('correct_email:', '\n'.join(correct_email))
    print('errors:', '\n'.join([i[0]+':'+i[1] for i in errors]))
    if len([i for i in  correct_email if i not in pos])>0 or len([i for i in [j[0] for j in errors] if i not in neg])>0:
        print('check_email_usable()异常')
    else:
        print('check_email_usable()正常')
    print('----------------------------------------')

    keywords = ['server', 'test', 'pay']
    domains = ['126.com', 'smzdm.com']
    emails = combine_mail(domains, keywords)
    print('combine_mail:','\n'.join(emails))
    if len(emails) == len(keywords)*len(domains):
        print('combine_mail()正常')
    else:
        print('combine_mail()异常')
    print('----------------------------------------')

    set_domains = ['126.com', 'smzdm.com']
    set_domains_to_file(set_domains)
    set_keywords = ['purchase', 'order']
    set_keywords_to_file(set_keywords)
    read_domains = get_domains_from_file()
    read_keywords = get_keywords_from_file()

    print('domains读到：', get_domains_from_file())
    print('keywords读到：', get_keywords_from_file())

    if set_domains != read_domains:
        print("set_domains_to_file()或read_domains()异常")
    else:
        print("set_domains_to_file()正常")
        print("read_domains()正常")

    if set_keywords != read_keywords:
        print("set_keywords_to_file()read_keywords()异常")
    else:
        print("set_keywords_to_file()正常")
        print("read_keywords()正常")
    print('----------------------------------------')