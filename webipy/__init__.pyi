# WebIpy Copyright (c) Boubajoker 2022. All right reserved. Project under MIT License.
# See https://github.com/Boubajoker/WebIpy/CopyRight.txt for more info.
r"""
# WebIPyModule

## WebIPyAppEngine SuperClass:

The main class that contain's the render engine under PyQt5 web-engine.
here is a Quick start:

```py
import webipy

webipy.APP_ENGINE.setApplicationName('[app name]')
webipy.APP_ENGINE.setApplicationVersion('[app version]')
webipy.APP_ENGINE.setWindowIcon(webipy.QIcon('[favicon path]'))
root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="[html file path]")
root.customize_cursor(960, 540)
# root.preset(preset_name='blank')

if __name__ == '__main__':
    webipy.APP_ENGINE.exec()
```

## `APP_ENGINE` variable:

The `APP_ENGINE` variable is the variable that contain's the `QApplication` SuperClass.
"""
from typing import *
import typing
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class WebIPyAppEngine(QApplication):
    r"""
    ## WebIPyAppEngine SuperClass:

    The main class that contain's the render engine under PyQt5 web-engine.
    here is a Quick start:
    
    ```py
    import webipy

    webipy.APP_ENGINE.setApplicationName('[app name]')
    webipy.APP_ENGINE.setApplicationVersion('[app version]')
    webipy.APP_ENGINE.setWindowIcon(webipy.QIcon('[favicon path]'))
    root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="[html file path]")
    root.customize_cursor(960, 540)
    # root.preset(preset_name='blank')

    if __name__ == '__main__':
        webipy.APP_ENGINE.exec()
    ```
    """
    def __init__(width: int, height: int, main_url: str, min_width: int | None = None, min_height: int | None = None, max_width: int | None = None, max_height: int | None = None) -> QApplication: ...
    def update_url(self, q: Any) -> QUrl: ...
    def customize_cursor(self, posX: int | None = None, posY: int | None = None) -> QCursor: 
        """
        ## `customize_cursor` function:

        to customize the cursor 
        """
        pass
    def preset(self, preset_name: str | None = None) -> Any: ...
    def debug_crash(self, crash_reason: str | None = None) -> QUrl: ...
    
    typing.Optional[update_url]

r"""
## `APP_ENGINE` variable:

The `APP_ENGINE` variable is the variable that contain's the `QApplication` SuperClass.
"""
APP_ENGINE = QApplication()