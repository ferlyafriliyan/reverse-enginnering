#  Update to Python3 by  :  Ferly Afriliyan
#  File Python2  :  https://github.com/ferlyafriliyan/reverse-enginnering/blob/main/Encrypt-Python2/Py2-reverse.py
#  Follow and Give Star in All Repositories !!
import os
import sys
import time
import base64
import marshal
import zlib
import binascii
import py_compile

R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

def slowprintxx(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
\x1b[1;35m---------------------------------------
\x1b[1;35m|  \x1b[1;31m   ____         ___          ___ \x1b[1;35m  |
|  \x1b[1;31m  / __/__  ____/ _ \\__ __   |_  | \x1b[1;35m |
|  \x1b[1;37m / _// _ \\/ __/ ___/ // /   / __/ \x1b[1;35m |
|  \x1b[1;37m/___/_//_/\\__/_/   \\_, /   /____/ \x1b[1;35m |
|     \x1b[1;37m               /___/      \x1b[1;35m      |
\x1b[1;35m---------------------------------------
\x1b[1;31m• \x1b[1;33mUpdate Py3 \x1b[1;31m: \x1b[1;33mFerly Afriliyan
\x1b[1;31m•\x1b[1;33m Decrypt  \x1b[1;31m  :\x1b[1;33m Ferly Afriliyan
\x1b[1;31m• \x1b[1;33mGithub \x1b[1;31m    : \x1b[1;33mKang-Berontak/Encrypt-Python2
\x1b[1;35m---------------------------------------

\x1b[1;35m[ \x1b[1;37mEncrypt python3 \x1b[1;35m]      '''

os.system('clear')
print(logo)
slowprint(f'''
\x1b[1;97m[\x1b[1;93m01\x1b[1;97m] Encrypt\x1b[1;93m Marshal
\x1b[1;97m[\x1b[1;93m02\x1b[1;97m] Encrypt \x1b[1;93mBase64
\x1b[1;97m[\x1b[1;93m03\x1b[1;97m] Encrypt\x1b[1;93m Base32
\x1b[1;97m[\x1b[1;93m04\x1b[1;97m] Encrypt \x1b[1;93mBase16
\x1b[1;97m[\x1b[1;93m05\x1b[1;97m] Encrypt \x1b[1;93mZlib
\x1b[1;97m[\x1b[1;93m06\x1b[1;97m] Encrypt \x1b[1;93mPy \x1b[1;91m> \x1b[1;93mPyc
\x1b[1;97m[\x1b[1;93m07\x1b[1;97m] Encrypt \x1b[1;93mMarshal\x1b[1;31m,\x1b[1;33mZlib\x1b[1;31m,\x1b[1;33mBase64
\x1b[1;97m[\x1b[1;93m08\x1b[1;97m] Encrypt \x1b[1;93mMarshal\x1b[1;31m,\x1b[1;33mZlib\x1b[1;31m,\x1b[1;33mBase32
\x1b[1;97m[\x1b[1;93m09\x1b[1;97m] Encrypt \x1b[1;93mMarshal\x1b[1;31m,\x1b[1;33mZlib\x1b[1;31m,\x1b[1;33mBase16
\x1b[1;97m[\x1b[1;93m10\x1b[1;97m] Encrypt \x1b[1;93mZlib\x1b[1;31m,\x1b[1;33mBase64
\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Exit
''')

mainmenu = input(G + '\x1b[1;91m[\x1b[1;93m+\x1b[1;91m] \x1b[1;97mPilih' + R + ' > ' + Y)
if mainmenu == '1' or mainmenu == '01':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    a = compile(fileopen, 'dg', 'exec')
    m = marshal.dumps(a)
    s = repr(m)
    b = '#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + s + '))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '2' or mainmenu == '02':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    a = base64.b64encode(fileopen.encode()).decode()
    b = "#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '3' or mainmenu == '03':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    a = base64.b32encode(fileopen.encode()).decode()
    b = "#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport base32\nexec(base64.b32decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + '\nEncryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '4' or mainmenu == '04':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    a = base64.b16encode(fileopen.encode()).decode()
    b = "#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport base16\nexec(base64.b16decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '5' or mainmenu == '05':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    a = zlib.compress(fileopen.encode()).hex()
    b = "#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport zlib\nexec(zlib.decompress(bytes.fromhex('" + a + "')).decode())"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '6' or mainmenu == '06':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    py_compile.compile(file)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W)
elif mainmenu == '7' or mainmenu == '07':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b64encode(sc).decode()
    b = '#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + sd + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '8' or mainmenu == '08':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b32encode(sc).decode()
    b = '#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + sd + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '9' or mainmenu == '09':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b16encode(sc).decode()
    b = '#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + sd + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
elif mainmenu == '10':
    file = input(W + '\nFile Name' + R + ' > ' + Y)
    c = input(W + 'Output File Name' + R + ' > ' + Y)
    slowprint(Y + 'Encrypting ...')
    fileopen = open(file).read()
    sa = zlib.compress(fileopen.encode()).hex()
    sb = base64.b64encode(bytes.fromhex(sa)).decode()
    b = '#  Encrypt By  :  Ganz-XD\n#  Github  :  https://github.com/Kang-Berontak\n#  Update Python3 by  :  Ferly Afriliyan\nimport zlib,base64\nexec(zlib.decompress(base64.b64decode("' + sb + '")).decode())'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + 'Encryption Completed...')
    time.sleep(3)
    print(W + 'Output File Name : ' + Y, c)
    print(W)
