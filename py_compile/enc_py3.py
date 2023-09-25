#  Update code python2 to python3 by : Ferly Afriliyan
#  Cantumin Nama Gw Bangsat
import os, sys;import random
import marshal, base64, zlib, py_compile
import time;from os import system;from time import sleep

try:
    import requests
except ImportError:
    print('\nModule Requests Not Installed')
    os.sys.exit()

def JembutNgePrint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.01)
logo = '_______ __   _ _______  ______ __   __  _____  _______\n |______ | \\  | |       |_____/   \\_/   |_____]    |   \n |______ |  \\_| |_____  |    \\_    |    |          |\n'

def Fer():
    system('clear')
    JembutNgePrint(logo)
    file_path = input('\nExample > /storage/elumulet/pyc.py\n\nName File > ')
    if not os.path.isfile(file_path):
        print('File not found!')
        return
    
    output_file_path = input('Output File Name > ')
    
    Fer2 = open(file_path).read()
    file = open(output_file_path, 'w')  # Buka file output
    file.write('Kontol=(\n')
    for i in range(5000):
        file.write('"Kontolivo","Kontolivo","Kontolivo","Kontolivo","Kontolivo",\n')
    file.write(')\n\n\n')
    file.write('Kontolivo=[')
    for i in range(random.randint(140, 4409)):
    	file.write('"Kontolivo","Kontolivo","Kontolivo","Kontolivo","Kontolivo",')
    file.write(']\n\n')
    
    Fer4 = compile(Fer2, 'Kontolivo', 'exec')
    Fer5 = marshal.dumps(Fer4)
    Fer6 = zlib.compress(Fer5)
    Fer7 = base64.b64encode(Fer6)
    Fer8 = repr(Fer7)
    Fer9 = f'# Created by : Boy HamzaH\n# Deobfuscate by : Ferly Afriliyan\n\n\nimport marshal,zlib,base64\n__Jawir__=(marshal.loads(zlib.decompress(base64.b64decode({Fer8}))));exec(__Jawir__)'
    Fer10 = compile(Fer9, 'Kontolivo', 'exec')
    Fer11 = marshal.dumps(Fer10)
    Fer12 = repr(Fer11)
    
    file.write(f'# Created by : Boy HamzaH\n# Deobfuscate by : Ferly Afriliyan\n\n\nimport marshal\n__Jawir__XDEH=(marshal.loads({Fer12}));exec(__Jawir__XDEH)\n\n\n')
    file.write('Kontol=(\n')
    for i in range(5000):
        file.write('"Kontolivo","Kontolivo","Kontolivo","Kontolivo","Kontolivo",\n')
    file.write(')\n')
    file.close()
    print(f'File saved as: {output_file_path}')  # Memberikan pesan file disimpan

if __name__ == '__main__':
    Fer()
