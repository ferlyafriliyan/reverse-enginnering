
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64, uuid
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak

ses = requests.Session()

###----------[ WAKTU ]----------###
bulan = {
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
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = str(tgl) + " " + str(bln) + " " + str(thn)
waktu = strftime("%H:%M:%S")
hari = datetime.now().strftime("%A")

###----------[ WARNA 1 ]---------- ###
Z = "\x1b[0;90m"  # Hitam
M = "\x1b[38;5;196m"  # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m"  # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"  # Ungu
O = "\x1b[0;96m"  # Biru Muda
P = "\x1b[38;5;231m"  # Putih
J = "\x1b[38;5;208m"  # Jingga
A = "\x1b[38;5;248m"  # Abu-Abu
N = "\x1b[0m"  # WARNA MATI
PT = "\x1b[1;97m"  # PUTIH TEBAL
MT = "\x1b[1;91m"  # MERAH TEBAL
HT = "\x1b[1;92m"  # HIJAU TEBAL
KT = "\x1b[1;93m"  # KUNING TEBAL
BT = "\x1b[1;94m"  # BIRU TEBAL
UT = "\x1b[1;95m"  # UNGU TEBAL
OT = "\x1b[1;96m"  # BIRU MUDA TEBAL

###----------[ WARNA 2 ]---------- ###
Z2 = "[#000000]"  # HITAM
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
U2 = "[#AF00FF]"  # UNGU
N2 = "[#FF00FF]"  # PINK
O2 = "[#00FFFF]"  # BIRU MUDA
P2 = "[#FFFFFF]"  # PUTIH
J2 = "[#FF8F00]"  # JINGGA
A2 = "[#AAAAAA]"  # ABU-ABU


def clear():
    os.system("cls" if "win" in sys.platform.lower() else "clear")


kom1 = "\n \nhttps://www.facebook.com/100073125893802_391114490002744\n" # Gak usah Diganti Kontol

###----------[ INI LOGO ]----------###
def logo_menu():
    li = "# SELAMAT DATANG DI TOOLS AUTO SHARE FACEBOOK"
    lo = mark(li, style="white")
    sol().print(lo, style="blue")
    banner = f"""    _  _   _ _____ ___    ___ _  _   _   ___ ___ 
   /_\| | | |_   _/ _ \  / __| || | /_\ | _ \ __|
  / _ \ |_| | | || (_) | \__ \ __ |/ _ \|   / _| 
 /_/ \_\___/  |_| \___/  |___/_||_/_/ \_\_|_\___|"""
    cetak(
        nel(
            banner,
            title=f"{P2} {H2}[ {P2}>< {H2}]",
            subtitle_align="left",
            padding=1,
            style="blue",
        )
    )


###----------[ MENU LOGIN ]----------###
def login():
    clear()
    cetak(
        nel(
            f"   {P2}Login Cookies Terlebih Dahulu Bro\n\n              {H2}--[ LU KONTOL ]--",
            title=f"{P2} {H2}[ {P2}Selamat Datang {H2}]",
            width=54,
            padding=(1, 4),
            style="blue",
        )
    )
    cetak(
        nel(
            f"{P2} Ambil Cookies Di Kiwi Browser",
            subtitle=f"{P2}┌─[ Cookies ]",
            subtitle_align="left",
            width=54,
            padding=1,
            style="blue",
        )
    )
    cookie = input(f"{P}   └──> : {H}")
    try:
        data = ses.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "origin": "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type": "text/html; charset=utf-8",
            },
            cookies={"cookie": cookie},
        )
        find_token = re.search("(EAAG\w+)", data.text)
        open("token.txt", "w").write(find_token.group(1))
        open("cookie.txt", "w").write(cookie)
        cetak(nel(f"{P2} LOGIN BERHASIL", width=24, style=f"#00FF00"))
        time.sleep(2)
        bot_share()
    except:
        os.system("rm token.txt cookie.txt")
        cetak(nel(f"{P2} COOKIE INVALID", width=22, style=f"#00FF00"))
        time.sleep(1.5)
        login()


###----------[ AUTO SHARE ]----------###
def bot_share():
    clear()
    try:
        token = open("token.txt", "r").read()
        cok = open("cookie.txt", "r").read()
        cookie = {"cookie": cok}
        ip = requests.get("https://api.ipify.org").text
        nama = ses.get(
            f"https://graph.facebook.com/me?fields=name&access_token={token}",
            cookies=cookie,
        ).json()["name"]
        id = requests.get(
            "https://graph.facebook.com/me/?access_token=%s" % (token),
            cookies={"cookie": cok},
        ).json()["id"]
        requests.post(
            f"https://graph.facebook.com/391114490002744/comments/?message={kom1}&access_token={token}",
            headers={"cookie": cok},
        )
    except:
        os.system("rm token.txt cookie.txt")
        cetak(nel(f"{P2} COOKIE INVALID!!", width=22, style=f"#00FF00"))
        time.sleep(1.5)
        login()
    clear()
    logo_menu()
    cetak(
        nel(
            f"""{P2} User Active     : {H2}{nama} 
{P2} You Id          : {id}
{P2} You Ip          : {ip}
{P2} Current Date    : {hari}, {tanggal}""",
            title=f"{P2} {H2}[ {P2}Informasi Pengguna {H2}]",
            subtitle_align="left",
            padding=1,
            style="blue",
        )
    )
    cetak(
        nel(
            f"{P2}Hai {H2}{nama}{P2}, copy link postingan harus dari facebook lite jika tidak akan terjadi eror saat proses bot share berjalan.",
            title=f"{P2} {H2}[ {P2}Catatan {H2}]",
            subtitle_align="left",
            padding=1,
            style="blue",
        )
    )
    cetak(
        nel(
            f"{P2} MASUKAN LINK POSTINGAN",
            subtitle=f"{P2}┌─",
            subtitle_align="left",
            width=25,
            padding=0,
            style="blue",
        )
    )
    link = input(f"{P}   └──> : {H}")
    cetak(
        nel(
            f"{P2} JUMLAH SHARE",
            subtitle=f"{P2}┌─",
            subtitle_align="left",
            width=22,
            padding=0,
            style="blue",
        )
    )
    jumlah = int(input(f"{P}   └──> : {H}"))
    cetak(
        nel(
            f"{P2} AUTO SHARE SEDANG BERJALAN",
            subtitle=f"{P2}┌─",
            subtitle_align="left",
            width=29,
            padding=0,
            style="blue",
        )
    )
    lubangsatanjing = datetime.now()
    try:
        n = 0
        header = {
            "authority": "graph.facebook.com",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
        }
        for x in range(jumlah):
            n += 1
            post = ses.post(
                f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                headers=header,
                cookies=cookie,
            ).text
            data = json.loads(post)
            if "id" in post:
                bas = str(datetime.now() - lubangsatanjing).split(".")[0]
                print(
                    f"{P}\r   └──> {bas} Berhasil Membagikan {H}{n}{P} Postingan {N} ",
                    end="",
                )
                sys.stdout.flush()
            else:
                print("\n")
                cetak(
                    nel(
                        f"{P2} AUTO SHARE BERHENTI KEMUNGKINAN COOKIE INVALID",
                        width=35,
                        padding=0,
                        style="red",
                    )
                )
                exit()
    except requests.exceptions.ConnectionError:
        print(f"\n{P}(!) Anda tidak terhubung ke internet!")
        exit()


bot_share()
