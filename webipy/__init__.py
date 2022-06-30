# WebIpy Copyright (c) Boubajoker 2022. All right reserved. Project under MIT License.
# See https://github.com/Boubajoker/WebIpy/CopyRight.txt for more info.
import sys as _sys
from typing import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class Components(object):
    class Presets(object):
        debug_page_file_content = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test</title>
    </head>
    <body>
        <h1 class="main-title" id="main_title">WEBIPY DEBUG PAGE</h1>
        <h1 class="test-h1" id="test_h1">H1_DEBUG_TEST: Hello, World !</h1>
        <h2 class="test-h2" id="test_h2">H2_DEBUG_TEST: Hello, World !</h2>
        <h3 class="test-h3" id="test_h3">H3_DEBUG_TEST: Hello, World !</h3>
        <p class="test-p" id="test_p">P_DEBUG_TEST: Hello, World !</p>
        <a href="./hworld.html" class="test-a" id="test_a">A_DEBUG_TEST: Click Me !</a>
        <br>
        <br>
        <span class="test-span" id="test_span">SPAN_DEBUG_TEST: Hello, World !</span>
        <br>
        <br>
        <button class="test-btn" id="test_btn">BUTTON_DEBUG_TEST: Click Me !</button>
    <script>
        let test_btn = document.querySelector('#test_btn');
        test_btn.addEventListener('click', ()=>{
            test_btn.innerText = "Hello, World !";
            setTimeout(()=>{
                test_btn.innerText = "BUTTON_DEBUG_TEST: Click Me !";
            }, 1500);
        });
    </script>
    </body>
</html>
"""

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

        self.WEB_ENGINE.urlChanged.connect(self.set_url)
        
    def debug_crash(self, crash_reason=None):
        if (crash_reason == 'real_crash'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://inducebrowsercrashforrealz/'))
        elif (crash_reason == 'page_crash'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://crash/'))
        elif (crash_reason == 'page_freeze'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://hang/'))
        elif (crash_reason == 'memory_excess'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://memory-exhaust/'))
        elif (crash_reason == 'page_kill'):
            self.WEB_ENGINE.setUrl(QUrl('chrome://kill/'))
        else:
            raise Exception(f'invalid expresion {crash_reason}')       
    
    def set_url(self, q) -> QUrl:
        self.WEB_ENGINE.setUrl(QUrl(q))

        return 0

    def customize_cursor(self, posX=None, posY=None) -> QCursor:
        self.mouse = self.cursor()
        self.mouse.setPos(posX, posY)

        return 0

    def preset(self, preset_name) -> Any:
        if (preset_name == 'blank'):
            with open(self.global_url, 'w+') as f:
                f.write('<!--!APP ENGINE Powered by WebIpy and PyQt5.WebEngine. WARNING: DO NOT DELETE THIS COMMAND EXCEPT FOR RESET THE FILE. IF DELETED THE FILE WILL BE RESET AT RELAUNCH !-->')
                f.close()
        
        if (preset_name == 'debug'):
            with open(self.global_url, 'w+') as f:
                f.write('<!--!APP ENGINE Powered by WebIpy and PyQt5.WebEngine. WARNING: DO NOT DELETE THIS COMMAND EXCEPT FOR RESET THE FILE. IF DELETED THE FILE WILL BE RESET AT RELAUNCH !-->')
                f.write(Components.Presets.debug_page_file_content)
                f.close()
                
        return 0
    
    def custom_preset(self, file_content) -> Any:
        with open(self.global_url, 'w+') as f:
            f.write(file_content)
            f.close()
    
    def redirect_to_chrome_url(self, url_name) -> QUrl:
        self.WEB_ENGINE.setUrl(QUrl(f'chrome://{url_name}'))

APP_ENGINE = QApplication(_sys.argv)