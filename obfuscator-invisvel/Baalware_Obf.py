import os
import logging
from pystyle import *
import colorama
from pystyle import Box
from pystyle import Colors, Colorate

baalware = """

██████╗  █████╗  █████╗ ██╗     ██╗    ██╗ █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║     ██║    ██║██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║███████║██║     ██║ █╗ ██║███████║██████╔╝█████╗  
██╔══██╗██╔══██║██╔══██║██║     ██║███╗██║██╔══██║██╔══██╗██╔══╝  
██████╔╝██║  ██║██║  ██║███████╗╚███╔███╔╝██║  ██║██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                     [+] Updated By : Ferly Afriliyan   \n                 
"""
os.system("cls")
print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(baalware)))

def modo1(arquivos, string):
    with open(arquivos, encoding='utf-8') as f:
        s = f.read()
    z = []
    for i in s:
        z.append(ord(i))
    pea = []
    for i in z:
        pea.append(string.replace("'", "").replace('"', '')*i)
    arquivo = """#Modified By Baalware

d={};exec("".join([chr(len(i)) for i in d]))
    """.format(pea)
    
    # Memastikan direktori "baalware obfs" sudah ada
    if not os.path.exists("baalware obfs"):
        os.makedirs("baalware obfs")
    
    arquivo_saida = os.path.join("baalware obfs", os.path.splitext(os.path.basename(arquivos))[0] + "diubah.py")
    with open(arquivo_saida, "w", encoding='utf-8') as f:
        f.write(arquivo)
        os.system("cls")
    print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(baalware)))
    logging.info("File converted successfully to '{}'".format(arquivo_saida))
    print(Center.XCenter("File converted successfully to '{}'".format(arquivo_saida)))

while True:
    arquivo = input("\nthe name of the file to change: ")
    if arquivo.lower() == 'keluar':
        break
    string = ("ㅤ")
    modo1(os.path.join(os.path.dirname(__file__), arquivo), string)
