import os
import marshal
import builtins as pp
import time;os.system('clear')

def restart_program():
    start()

banner = '''
\t\t\t\t \x1b[31mDecrypt by : Ferly Afriliyan
           \x1b[33m___________ @ @\x1b[0m\t \x1b[34mGithub : https://github.com/Amriez/MamangKey
          \x1b[33m/         (\x1b[0m@\x1b[33m\\\x1b[0m   @a\t \x1b[31mWeb : https://ferlyafriliyan.vercel.app
          \x1b[33m\\___________/  _\x1b[0m @ \x1b[34mUpdate to Py3 by : Ferly Afriliyan z
                    @ \x1b[33m _/\x1b[0m@\x1b[33m\\_____
   \x1b[31mANTI   \x1b[0m           @\x1b[33m/ \x1b[0m\\__/\x1b[0m-="="`
   \x1b[31mRE-CODE \x1b[0m           \x1b[33m\\_ /
   \x1b[31mRE-CODE \x1b[0m            <\x1b[33m| \x1b[31mTukang-Kunci(c)
   \x1b[31mCLUB       \x1b[0m         <\x1b[33m|
                      \x1b[0m <\x1b[33m|
                      \x1b[33m ` \x1b[35m
'''

def marsha():
    os.system('clear')
    print(banner)
    file = input('Enter the input file name: ')
    f = open(file).read()
    s = f.replace('\r\n', '\n')
    s = s.replace('\r', '\n')
    if s and s[-1] != '\n':
        s = s + '\n'
    asade = pp.compile(s, '<s>', 'exec')
    todi = marshal.dumps(asade)
    awal = "\nimport marshal\nexec(marshal.loads("
    akhir = "))"
    output_file = input('Enter the output file name: ')
    open(output_file, 'w').write(awal + repr(todi) + akhir)
    time.sleep(3)
    try:
        print(f'  \x1b[32m[+] Success! File saved as {output_file}\x1b[0m')
    except ImportError:
        print('\x1b[31m  [-] Failed...\x1b[0m')


def start():
    print(banner)
    print('         ~\x1b[33m[1]\x1b[0m--\x1b[32mCompile             \x1b[0m')
    print('         ~\x1b[33m[2]\x1b[0m--\x1b[31mExit              \x1b[0m')
    zz = input('MamangKey >~# ')
    if zz == '1':
        marsha()
    elif zz == '2':
        os.system('clear')
    else:
        time.sleep(3)
        restart_program()

start()
