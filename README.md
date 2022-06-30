# WebIpy 

WebIpy is a python module that can render your web-apps into desktop apps under PyQt5 WebEngine.

## User Notice:

### **Dependencies**:

- Python 3.8.10 (minimum)
    - PyQt5 python module
    - PyQt5.WebEngine

This part of the documentation will help you to install and use WebIpy. Follow the steps behavior:

### Downlaoding & Installing WebIpy:

To install WebIpy follow the steps behavior:

1. Downlaod it on the [WebIpy web-page](https://boubajoker.github.io/WebIpy/?Link=Downlaods).

2. Once the file `webipy_v[package version].zip` is installed, extract it on the python interpreter path : `C:\Program Files\Python[Interpreter version]\Lib\`.

### Using WebIpy module:

To use WebIpy follow the steps behavior:

1. Create a new python file and a new html file.

2. Write this base code to initialize the app engine:

```py
import webipy

webipy.APP_ENGINE.setApplicationName('[app name]')
webipy.APP_ENGINE.setApplicationVersion('0.0.1 Alpha A-1')
webipy.APP_ENGINE.setWindowIcon(webipy.QIcon('./assets/icon/favicon.png'))
root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="[html file path]")

if __name__ == '__main__':
    webipy.APP_ENGINE.exec()
```

And that's it, happy coding :+1: !!