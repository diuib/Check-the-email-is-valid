import random
import mainUI
import func
from PyQt5.QtWidgets import (QMainWindow)
from PyQt5 import QtGui
from PyQt5.QtCore import *


class allevent(QMainWindow, mainUI.Ui_MainWindow):

    _dragflag = False
    _dragPosition = 0

    def __init__(self):
        super(allevent, self).__init__()
        self.setupUi(self)
        self.initialization()

    def initialization(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget.setMouseTracking(True)
        self.setMouseTracking(True)

        self.keywordEdit.setPlainText('\n'.join(func.get_keywords_from_file()))
        self.siteEdit.setPlainText('\n'.join(func.get_domains_from_file()))

        self.checkButton_Label.installEventFilter(self)
        self.check_button_gif = QtGui.QMovie("./res/check_button.gif")
        self.check_button_gif.setCacheMode(QtGui.QMovie.CacheAll)
        self.check_button_gif.setSpeed(100)
        self.checkButton_Label.setMovie(self.check_button_gif)
        self.check_button_gif.start()

        self.mycheck = Checking()
        self.mycheck._signal.connect(self.stop_gif)

        self.show_message('输入网址，点本喵~~~')

    # 以下为触发事件
    @pyqtSlot()
    def on_hidenButton_clicked(self):
        self.setWindowState(Qt.WindowMinimized)

    @pyqtSlot()
    def on_closeButton_clicked(self):
        func.set_domains_to_file([d for d in self.get_domains().split('\n')])
        func.set_keywords_to_file([k for k in self.get_keywords().split('\n')])
        QCoreApplication.instance().quit()

    # 以下为继承事件
    def eventFilter(self, widget, event):
        if widget == self.checkButton_Label:
            if event.type() == QEvent.MouseButtonPress:
                if self.get_domains()=='':
                    self.show_message('给我个网站，我好帮你问问嘛~~')
                    return False
                if self.get_keywords()=='':
                    self.show_message('没有关键字我怎么问嘛~~')
                    return False
                self.msgLabel.hide()
                self.play_gif()
            return False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.titleBar.frameRect().contains(event.globalPos() - self.frameGeometry().topLeft()):
                self._dragflag = True
                self._dragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        self.funny(event)
        if Qt.LeftButton and self._dragflag:
            self.move(event.globalPos() - self._dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._dragflag = False

    def closeEvent(self, event):
        func.set_domains_to_file([d for d in self.get_domains().split('\n')])
        func.set_keywords_to_file([k for k in self.get_keywords().split('\n')])

    # 以下为自写函数
    def get_domains(self):
        return self.siteEdit.toPlainText()

    def get_keywords(self):
        return self.keywordEdit.toPlainText()

    def play_gif(self):
        self.loading_gif = QtGui.QMovie("./res/loading.gif")
        self.loading_gif.setCacheMode(QtGui.QMovie.CacheAll)
        self.loading_gif.setSpeed(100)
        self.checkButton_Label.setMovie(self.loading_gif)
        self.loading_gif.start()


        self.resultEdit.setPlainText('')
        domains = self.get_domains()
        keywords = self.get_keywords()

        self.mycheck._domains = [d for d in domains.split('\n')]
        self.mycheck._keywords = [k for k in keywords.split('\n')]
        self.show_message('我一边吃东西，一边给你问问哈...')
        self.mycheck.start()

    def stop_gif(self):
        if len(self.mycheck._wrongmsg)==0:
            self.resultEdit.setPlainText('\n'.join(self.mycheck._emails))
            self.show_message('快来看，快来看，我问到了~~')
        else:
            self.msgLabel.show()
            self.show_message('糟糕，网络故障，你用网页试试喵~~')
        self.loading_gif.stop()

    def show_message(self, msgtxt):
        self.msgLabel.show()
        self.msgLabel.setText('  '+ msgtxt)
        QTimer.singleShot(3000, lambda: self.msgLabel.hide())

    def funny(self,event):
        coords = [[780,320,21,21], # 右触角
                [740,320,21,21],  # 左触角
                [800,340,41,21],  # 右耳朵
                [720,340,41,21],  # 左耳朵
                [730,350,81,51],  # 额头
                [750,420,31,21],  # 嘴
                [740,460,31,31],  # 罐子
                [770,450,101,71]]  # 裙子
        for index, coord in enumerate(coords):
            if QRect(*coord).contains(event.globalPos() - self.frameGeometry().topLeft()):
                if self.msgLabel.isHidden():
                    self.msgLabel.show()
                    self.msgLabel.setText('  ' + self.getfunny_word(index))
                    QTimer.singleShot(1500, lambda: self.msgLabel.hide())

    def getfunny_word(self, index):
        # 0 右触角  # 1 左触角  # 2 右耳朵  # 3 左耳朵  # 4 额头  # 5 嘴  # 6 罐子  # 7 裙子
        words = [['这是我的小触角，啦啦啦',
                  '我头上戴这个，小黑会喜欢吗？',
                  '小黑说他喜欢萌萌的那种，我这样算吗？',
                  '右面这个小触角是不是歪了呀'],
                 ['帮我看一下左面这个小触角戴正了吗',
                  '小黑看看我的这对小触角，萌不萌呀',
                  '听说，做这个软件的大哥哥超级爱你呦，小\n黑什么时候能喜欢上我呀',
                  '小心点嘛，别碰掉了，好不容易戴上的'],
                 ['为什么我右面的耳朵比左边的大呢？',
                  '咯咯，好痒痒……',
                  '上次小黑说他觉得我的耳朵好看，他也想要\n一对大大的耳朵',
                  '我的耳朵好敏感，会痒的……'],
                 ['你看我左面的耳朵是不是小一点，画师太不\n走心了',
                  '小黑的吃相傻萌傻萌的，哈哈',
                  '猫咪的耳多都是这样的吗？',
                  '别摸了嘛，耳朵超级痒的'],
                 ['我这……算不算大背头呀',
                  '嘻嘻，好舒服',
                  '喵~喵~，姐姐你这样抚摸我好舒服呢~~',
                  '姐姐你好漂亮呀~~'],
                 ['不要唔我的嘴嘛~',
                  '小黑吃的好开心，我也想吃……',
                  '为什么我的嘴是菱形的呢？',
                  '为什么我的嘴和小黑的不一样呢？'],
                 ['这是给小黑准备的，你不可以吃呦',
                  '看着小黑吃的好开心，我也很开心呢！',
                  '你猜猜看里面是什么呢？',
                  '我才不告诉你里面是什么呢，哼~'],
                 ['我的裙子漂亮吗？',
                  '小黑会喜欢我穿成这样吗？',
                  '小黑一直在吃，也不看看我的花裙子，\n唔……',
                  '姐姐你穿裙子的样子好漂亮，听说大哥哥都\n迷上你了呢']]
        n = random.randint(0, 3)
        return words[index][n]

class Checking(QThread):

    _domains = []
    _keywords = []
    _emails = []
    _wrongmsg = []
    _signal = pyqtSignal()

    def __init__(self, parent=None):
        super(Checking, self).__init__()

    def run(self):
        emails = func.combine_mail(self._domains, self._keywords)
        self._emails, _, self._wrongmsg = func.check_email_usable_thread(emails)
        self._signal.emit()
