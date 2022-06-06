# WebIpy Copyright (c) Boubajoker 2022. All right reserved. Project under MIT License.
# See https://github.com/Boubajoker/WebIpy/CopyRight.txt for more info.
import sys as _sys
from typing import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class WebIPyAppEngine(QMainWindow):
    def __init__(self, width, height, main_url, min_width=None, min_height=None, max_width=None, max_height=None) -> QApplication:
        super(WebIPyAppEngine, self).__init__()

        self.MAIN_URL = "file:///" + main_url
        self.global_url = main_url

        self.WEB_ENGINE = QWebEngineView()
        self.WEB_ENGINE.setUrl(QUrl(self.MAIN_URL))
        self.setCentralWidget(self.WEB_ENGINE)
        self.show()

        if width == None:
            raise Exception('Invalid `width` value: `width` value cannot be a `NoneType` / `boolean` value.')
        elif height == None:
            raise Exception('Invalid `height` value: `height` value cannot be a `NoneType` / `boolean` value.')
        else:
            self.setBaseSize(width, height)

        if min_width == None:
            pass
        elif min_height == None:
            pass
        else:
            self.setMinimumSize(min_width, min_height)

        if max_width == None:
            pass
        elif max_height == None:
            pass
        else:
            self.setMaximumSize(max_width, max_height)

        self.WEB_ENGINE.urlChanged.connect(self.update_url)
        
    def debug_crash(self, crash_reason=None):
        if (crash_reason == 'real_crash'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://inducebrowsercrashforrealz/'))
        
        if (crash_reason == 'page_crash'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://crash/'))

        if (crash_reason == 'page_freeze'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://hang/'))
        
        if (crash_reason == 'memory_excess'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://memory-exhaust/'))
    
    def update_url(self, q) -> QUrl:
        self.WEB_ENGINE.setUrl(QUrl(q.toString()))

        return 0

    def customize_cursor(self, posX=None, posY=None) -> QCursor:
        self.mouse = self.cursor()
        self.mouse.setPos(posX, posY)

        return 0

    def preset(self, preset_name=None) -> Any:
        if (preset_name == 'blank'):
            with open(self.global_url, 'w+') as f:
                f.write('<!--!APP ENGINE Powered by WebIpy and PyQt5.WebEngine. WARNING: DO NOT DELETE THIS COMMAND EXCEPT FOR RESET THE FILE. IF DELETED THE FILE WILL BE RESET AT RELAUNCH !-->')
                f.close()
        return 0

APP_ENGINE = QApplication(_sys.argv)