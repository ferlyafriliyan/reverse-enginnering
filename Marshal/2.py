import marshal, os, time

m11 = '\033[1m'
m00 = '\033[0;0m'
m31 = '\033[31m'
m32 = '\033[32m'
m33 = '\033[33m'
m34 = '\033[34m'
m35 = '\033[35m'
m36 = '\033[36m'
m37 = '\033[37m'
m90 = '\033[90m'
m91 = '\033[91m'
m92 = '\033[92m'
m93 = '\033[93m'
m94 = '\033[94m'
m95 = '\033[95m'
m96 = '\033[96m'
m97 = '\033[97m'
flag = '\033[1;97;41m'

def logo():
	os.system("clear")
	print(f"""\n\n{m11}{m96}
  ┬─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ┬─┐┌─┐┌┬┐┌─┐┬┬  ┌─┐┬─┐
  ├─┘└┬┘ │ ├─┤│ ││││  │  │ ││││├─┘││  ├┤ ├┬┘
  ┴   ┴  ┴ ┴ ┴└─┘┘└┘  └─┘└─┘┴ ┴┴  ┴┴─┘└─┘┴└─
  {flag} Simple marshal compiler by NjankSoekamti {m00}
  {m11}{m95}------------------------------------------{m00}""");time.sleep(0.1)

try:
	logo()
	a=input("  [+] Path : ")
	x=open(a).read()
	b=compile(x,"","exec")
	c=marshal.dumps(b)
	d=open("_"+a,"w")
	d.write("import marshal\n")
	d.write("# https://ferlyafriliyan.vercel.app\n")
	d.write("exec(marshal.loads("+repr(c)+"))")
	d.close()
	print('  [+] Files encrypted : _'+a)
	print()
except FileNotFoundError:
	print("  [x] File not found\n")
except KeyboardInterrupt:
	print("  [x] Exit\n")
	exit()
