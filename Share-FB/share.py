#######

#            AUTHOR : SHELLY SCOTT.
 #           TEAM   : HUMMING BIRD CREW
 #           JAY JO, VINNY HONG ,ADITYA, MIA , DOM
#
########




import os,json,re,sys,hashlib
import threading
import requests
from requests import post
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import time
os.system("git pull")
a=requests.get('https://raw.githubusercontent.com/ShellyScot/Share/main/__shelly__').text
if '__shelly__' in a:
    print('╔══════════════════════════════════════════════════════')
    print('╠══[✾] Server Aktif')
    print('╚══════════════════════════════════════════════════════')
    sleep(5)
else:
	print('Jaringan bermasalah')
	time.sleep(100)
	quit()
try:
	import requests
except:
	os.system('pip install pystyle && pip install requests')
	import requests
token_live=[]
cookie=[]
cv=[]
def convert(list_cookie):
  for ck in list_cookie:
    try:
      get_rp = requests.get('https://business.facebook.com/business_locations/',headers={'cookie': ck}).text
      text = get_rp.split('EAAG')[1].split('"')[0]
      token = f'EAAG{text}'
      token_live.append(token)
      oo=open('share.txt',"a+")
      oo.write(token+"\n")
      o.close()
    except:
      print('Cookie mati')
      cv.remove(ck)
    return len(cv)
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear')
def get_id(url):
	try:
		rp=post('https://id.traodoisub.com/api.php',data={'link': url}).json()
		if 'success' in rp:
			return True,rp['id']
		elif 'error' in rp:
			return None,rp['error']
	except:
		return False,"Terjadi kesalahan"
def check_token(list_token):
  for to in list_token:
    check=json.loads(requests.get(f'https://graph.facebook.com/me/?access_token={to}').text)
    if "id" in check:
      token_live.append(to)
    else:
      pass
  return len(token_live)



def logo():
    log="""
______________                                __________________ 
__  ___/___  /_ ______ ______________         ___  ____/___  __ )
_____ \ __  __ \_  __ `/__  ___/_  _ \__________  /_    __  __  |
____/ / _  / / // /_/ / _  /    /  __/_/_____/_  __/    _  /_/ / 
/____/  /_/ /_/ \__,_/  /_/     \___/         /_/       /_____/  
╔══════════════════════════════════════════════════════
╠══[✾]Author : Shelly Scott.
╠══[✾]Shelly X Jay Jo
╚══════════════════════════════════════════════════════
"""
    
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.003)

clr()
logo()
o=open('tokenfb.txt',mode="a+", encoding="utf-8-sig")
o.close()
a = 0
stt=0
tttt=0
dulieu=[]
if os.path.exists('share.txt') == True:
	for x in open('share.txt',mode="r",encoding="utf-8-sig").read().split('\n'):
		if x != '':
			dulieu.append(x)
		else:
			pass
elif os.path.exists('share.txt') == False or len(dulieu) == '':
  while(True):
    tttt+=1
    toke=input(f' Masukan Token Atau Cookie {tttt} : ')
    if 'datr=' in toke:
      cv.append(toke)
    else:
      if toke != '':
         dulieu.append(toke)
         oo=open('share.txt',"a+")
         oo.write(toke+"\n")
         oo.close()
      else:
         break
sl_ck=len(cv)
if sl_ck == 0:
  pass
else:
  print('Menemukan '+str(sl_ck)+' Cookie')
  print(' Mengonver...')
  chuyen=convert(cv)
print('',end="\r")
token_li=check_token(dulieu)
if token_li == 0:
  print('Token mati ')
  if os.path.exists('share.txt')==True:
    os.remove('share.txt')
  else:
    pass
  quit() 
else:
  print('╔═══════════════════════════════════════════════')
  print('╠══[✾]Berhasil Login      ')
  print('╚═══════════════════════════════════════════════')
  sleep(1)
  os.system("clear")
sleep(1)
logo()
print("                 [✾]BACA DI BAWAH INI[✾] ")
print("╔══════════════════════════════════════════════════════")
print("╠══[✾] Jika token mati atau limit tapi masih bisa login kelik")
print("╠══[✾] CTRL + Z lalu nano share.txt hapus token lama kalau udah kelik")
print("╠══[✾] CTRL + X |CTRL + Y|CTRL + M Lalu tinggal jalankan tool ulang")
print("╚══════════════════════════════════════════════════════")
print("╔══════════════════════════════════════════════════════")
i=input('╠══[✾] Enter untuk melanjutkan :  ')
if i == '':
  print('╠══[✾] Pilih "y" lambat')
  print('╠══[✾] Pilih "n" cepet (recommended)')
  p=input('╠══[✾] (y/n): ')
  if p == 'y' or p == "Y":
    url = input("╠══[✾] Masukan link post : ")
    print('║')
    sleep(2)    
    print('║')
    sleep(2)
    id=get_id(url)
    id_bv='https://facebook.com/'+str(id[1])
    if id[0] == True:
    	print('╠══[✾] 100%')
    	sleep(2)
    elif id[0] == None:
    	print(' '+id[1])
    	quit()
    else:
    	print(' '+id[1])
    	quit()
  else:
    id_bv=input('╠══[✾] Masukan link post :')
elif i == 'id':
  idd=input('Loading ')
  id_bv=f"https://facebook.com/{idd}"
g_id=id_bv.split('.com/')[1]
clr()
logo()
print('╔═══════════════════════════════════════════════')
print('╠══[✾] Link/Id postingan : '+str(g_id)) 
print('╠══[✾] Token aktif       : '+str(token_li))
print('╚═══════════════════════════════════════════════')
def share(i):
      headers ={
         'authority': 'graph.facebook.com',
         'cache-control': 'max-age=0', 
         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
         'sec-ch-ua-mobile': '?0', 
         'upgrade-insecure-requests': '1',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
         'sec-fetch-site': 'none',
         'sec-fetch-mode': 'navigate',
         'sec-fetch-user': '?1', 
         'sec-fetch-dest': 'document', 
         'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5' }
      access_token = token_live[i]
      retu = requests.post(f"https://graph.facebook.com/me/feed?link={id_bv}&published=0&access_token={access_token}",headers=headers).json()
      if 'id' in retu:
          print('✾ S H E L L Y ✾',retu,'✾ N O A H C A V A L R Y ✾')
      elif 'You cannot access the app till you log in to www.facebook.com and follow the instructions given' in retu:
        print('Akun terkena chekpoint')
      elif "User request limit reached" in retu:
        print('Token mati')
      else:
         print('Periksa token dan cookie anda')
         print(retu)
         quit()
while (True):
  for i in range(len(token_live)):
           khoitao = threading.Thread(target=share,args=(i,)).start()
           

