import datetime

from my_package.__version__ import __version__


class MyClass:
    def __init__(self):
        print("MyClass object is created.")

    def my_func(self):
        print(f"This library is {__version__}")
        print(datetime.datetime.now().strftime("%Y年%m月%d日 %H時%M分%S秒"))
