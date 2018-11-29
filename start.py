import sys
import os
import mainEvent
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtGui import QFont, QFontDatabase
import multiprocessing


if __name__ == '__main__':
    multiprocessing.freeze_support()
    if os.path.exists('config.ini'):
        pass
    else:
        with open('config.ini', 'w', encoding='UTF-8') as fp:
            fp.write('[domains]\n\n[keywords]\n\n[proxies]\nused=1\nip=127.0.0.1:1080')

    app = QApplication(sys.argv)
    fontId = QFontDatabase.addApplicationFont("./res/方正喵呜.ttf")
    msyh = QFontDatabase.applicationFontFamilies(fontId);
    app.setFont(QFont(msyh[0]))

    ui = mainEvent.allevent()
    ui.show()
    sys.exit(app.exec_())