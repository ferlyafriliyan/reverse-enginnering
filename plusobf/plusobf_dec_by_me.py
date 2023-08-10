import random,sys,logging

logging.basicConfig(level=logging.INFO)
__banner__="""
\t[ plusobf by deray ]\n"""
def main(files,string):
        s=open(files).read()
        z=[]
        for i in s:
                z.append(ord(i))
        pea=[]
        for i in z:
                pea.append(string.replace("'","").replace('"','')*i)
        file="""
# coding=utf-8
# obfuscated with plusobf: https://github.com/loolzec/plusobf



d={};exec("".join([chr(len(i)) for i in d]))
        """.format(pea)
        open(files.replace(".py","encypt.py"),"w").write(file)
        logging.info(" saved as "+files.replace(".py","encrypt.py"))

try:
        print(__banner__)
        logging.info(" obfuscating "+sys.argv[1]+" ...")
        main(sys.argv[1],sys.argv[2])
except:
        print("""

[!] ussage: plusobf.py <filename> 'string'
Example:
        python plusobf.py myscript.py '+'
""")
