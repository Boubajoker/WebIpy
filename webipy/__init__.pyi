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
    here is a quick start:
    
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
    def set_url(self, q: Any) -> QUrl: ...
    def customize_cursor(self, posX: int | None = None, posY: int | None = None) -> QCursor: 
        """
        ## `customize_cursor` function:

        To customize the cursor's position, style...
        e.g:

        - position set:

        ```py
        >>> root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="example.html")
        >>> root.customize_cursor(960, 540) # will set the X and Y position given in the args.
        ```

        More functions soon !
        """
        pass
    def preset(self, preset_name: str | None = None) -> Any: ...
    def debug_crash(self, crash_reason: str | None = None) -> QUrl:
        """
        ## `debug_crash` function:

        To generate fake crashes events.
        e.g:

        ### Fake browser crash event:

        Makes the browser simulate a real crash.

        ```py
        >>> root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="example.html")
        >>> root.debug_crash('real_crash')
        ```
        
        ### Fake page crash event:

        Makes the browser simulate a page crash.

        ```
        >>> root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="example.html")
        >>> root.debug_crash('page_crash')
        ```

        ### Fake page freeze event:

        Makes the browser simulate a page freeze.

        ```
        >>> root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="example.html")
        >>> root.debug_crash('page_freeze')
        ```

        ### Fake memory excess event:

        Makes the browser simulate a memory excess.

        ```
        >>> root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="example.html")
        >>> root.debug_crash('memory_excess')
        ```    

        ### Fake page kill event:

        Makes the browser kill the page.

        ```
        >>> root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="example.html")
        >>> root.debug_crash('page_kill')
        ```        
        """
        pass

APP_ENGINE = QApplication()