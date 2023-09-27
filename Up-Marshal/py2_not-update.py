# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Feb 18 2023, 19:45:05) 
# [GCC Android (9352603, based on r450784d1) Clang 14.0.7 (https://android.google
# Embedded file name: <s>
import os, sys, marshal, __builtin__ as pp, time

def restartprogram():
    mulai()


banner = '\n\x1b[31m\t\t\t\t Author : AMRiezz\n\x1b[33m           ___________\x1b[0m @ @\x1b[34m\t Github : https://github.com/Amriez\n\x1b[33m          /         (\x1b[0m@\x1b[33m\\ \x1b[0m   @a\x1b[31m\t Blog\t: http://anrwiki.blogspot.com\n\x1b[33m          \\___________/  _\x1b[0m @ \x1b[34m\t youtube: AMRiezz z\n\x1b[0m                    @ \x1b[33m _/\x1b[0m@ \x1b[33m\\_____\n\x1b[31m   ANTI   \x1b[0m           @\x1b[33m/ \\__/\x1b[0m-="="`\n\x1b[31m   RE-CODE \x1b[33m           \\_ /\n\x1b[31m   RE-CODE \x1b[0m            <\x1b[33m| \x1b[31m\t Tukang-Kunci(c)\n\x1b[31m   CLUB       \x1b[0m         <\x1b[33m|\n                      \x1b[0m <\x1b[33m|\n                      \x1b[33m ` \x1b[35m\n'

def marsha():
    os.system('clear')
    print banner
    file = raw_input('MamangKey >~# ')
    f = open(file).read()
    s = f.replace('\r\n', '\n')
    s = s.replace('\r', '\n')
    if s and s[(-1)] != '\n':
        s = s + '\n'
    asade = pp.compile(s, '<s>', 'exec')
    todi = marshal.dumps(asade)
    awal = "\nimport marshal\nexec(marshal.loads(''"
    akhir = "''))"
    open(file[:-3] + '-AMR.py', 'w').write(awal + repr(todi) + akhir)
    time.sleep(3)
    try:
        print '  [+]Succes...'
    except ImportError:
        print '  [-]Failed...'


def mulai():
    print banner
    print '         ~{1}--Start             '
    print '         ~{2}--Exit              '
    zz = raw_input('MamangKey >~# ')
    if zz == '1':
        marsha()
    elif zz == '2':
        os.system('clear')
    else:
        time.sleep(3)
        restartprogram()


mulai()