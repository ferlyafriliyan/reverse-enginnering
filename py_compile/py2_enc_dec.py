# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Feb 18 2023, 19:45:05) 
# [GCC Android (9352603, based on r450784d1) Clang 14.0.7 (https://android.google
# Embedded file name: BOY_HAMZAH
import os, sys, py_compile, marshal, base64, zlib, time
from os import system
from time import sleep
try:
    import requests
except ImportError:
    print('\nModule Requests Not Installed')
    os.sys.exit()

def boyprint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.01)


logo = '_______ __   _ _______  ______ __   __  _____  _______\n |______ | \\  | |       |_____/   \\_/   |_____]    |   \n |______ |  \\_| |_____  |    \\_    |    |          |\n'

def boy():
    system('clear')
    boyprint(logo)
    file = input('\nexample > /sdcard/folder/file.py\n\nName File > ')
    boy2 = open(file).read()
    file = open('pyar-38.py', 'w')
    file.write('hamzah=(\n')
    for i in range(5000):
        file.write('"hamzah","hamzah","hamzah","hamzah",\n')

    file.write(')\n')
    boy4 = compile(boy2, 'BOY_HAMZAH', 'exec')
    boy5 = marshal.dumps(boy4)
    boy6 = zlib.compress(boy5)
    boy7 = base64.b64encode(boy6)
    boy8 = repr(boy7)
    boy9 = '# ECRYPT BY Boy HamzaH\n# Subscribe Cok Chanel YouTube Gua Anjing\n# Dan Jangan Lupa Follow Github Gua\n\n\nimport marshal,zlib,base64\nexec marshal.loads(zlib.decompress(base64.b64decode("' + str(boy8) + '")))'
    boy10 = compile(boy9, 'BOY_HAMZAH', 'exec')
    boy11 = marshal.dumps(boy10)
    boy12 = repr(boy11)
    file.write('# ECRYPT BY Boy HamzaH\n# Subscribe Cok Chanel YouTube Gua Anjing\n# Dan Jangan Lupa Follow Github Gua\n\n\nimport marshal\nexec marshal.loads(' + boy12 + ')\n\n\n')
    file.write('hamzah=(\n')
    for i in range(5000):
        file.write('\n"hamzah","hamzah","hamzah","hamzah",\n')

    file.write(')\n')
    file.close()


if __name__ == '__main__':
    boy()
