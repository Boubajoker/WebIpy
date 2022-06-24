import webipy

webipy.APP_ENGINE.setApplicationName('Debug Menu')
webipy.APP_ENGINE.setApplicationVersion('0.0.1 Alpha A-1')
webipy.APP_ENGINE.setWindowIcon(webipy.QIcon('./assets/icon/favicon.png'))
root = webipy.WebIPyAppEngine(width=1080, height=700, main_url="webipy/test/index.html")
root.customize_cursor(960, 540)
# root.preset(preset_name='debug')

if __name__ == '__main__':
    webipy.APP_ENGINE.exec()