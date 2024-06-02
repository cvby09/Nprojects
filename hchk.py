import os
import sys
import re
try:
	import pycurl
except:
	os.system("pip3 install pycurl")
try:
	import httpx
except:
	os.system("pip3 install httpx")
try:
	import requests 
except:
	os.system("pip3 install requests")		 
import pycurl
from rich import print as t
from rich.panel import Panel as box
from datetime import datetime
from io import BytesIO
import uuid
import time

# Add import for 're'
import re

# Current date in YYYYMMDD format
tita = str(datetime.now()).split(" ")[0]
tic = tita.split("-")
timen = int(tic[0] + tic[1] + tic[2])
logo = ""
key1 = str(uuid.uuid4()).replace('-','').upper()
uid = str(os.geteuid())
h = uid+key1
mkey = str(h)
try:
    ke1 = open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/.http.py', 'r').read()
except:
    kok = open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/.http.py', 'w');kok.write(mkey);kok.close()
rk = open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/.http.py', 'r').read()
key = rk
server_url = "https://raw.githubusercontent.com/Mahobin-Universe/Importer/main/data/srvr.txt"
approval_expiry_url = "https://raw.githubusercontent.com/Mahobin-Universe/Importer/main/data/g.txt"
count = 0
path = '/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests'
path2 = '/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx'
files2 = os.listdir(path2)
files = os.listdir(path)
for file in files:
    if file.endswith('.py'):
        try:
            data = open(path + '/' + file, 'r').read()
            cch = re.search("print",data)
            if cch == None:
                pass
            else:
                print("[bold red] Turn off your bypass system")
                sys.exit()
        except:
            pass
for file in files2:
    if file.endswith('.py'):
        try:
            data = open(path2 + '/' + file, 'r').read()
            cch = re.search("print",data)
            if cch == None:
                pass
            else:
                print("[bold red] Turn off your bypass system")
                sys.exit()
        except:
            pass

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(logo)

def req(link):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, link)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HTTPHEADER, ['Cache-Control: no-cache'])
    try:
        c.perform()
        c.close()
    except pycurl.error as e:
        print("[bold red] Network Error.")
        print(f"[bold red] {e}")
        return []
    response_code = c.getinfo(pycurl.RESPONSE_CODE)
    if response_code != 200:
        print(f"[bold red] HTTP Error: {response_code}")
        return []
    data = buffer.getvalue().decode('utf-8')
    return data.splitlines()

def srvr():
    data = req(server_url)
    if "ON" in data:
        srvr2()
    else:
        clear()
        for _ in range(20000):
            print("[bright_white]|=| WAIT FOR NEXT NEW UPDATE ")
            time.sleep(0.5)
        sys.exit()

def srvr2():
    data = req("https://raw.githubusercontent.com/Mahobin-Universe/Importer/main/data/srvr2.txt")
    if "TRIAL" in data:
        main2()
    elif "PAID" in data:
        apv()
    else:
        print("[bold red] SOMETHING WENT WRONG")
        sys.exit()

def apv():
    data = req("https://raw.githubusercontent.com/Mahobin-Universe/Importer/main/data/g.txt")
    for line in data:
        k,date = line.split('|')[0],line.split('|')[1]
        if k == key:
            if int(date) > timen:
                main2()
            else:
                print(box.fit("[bold red] YOUR APPROVAL HAS EXPIRED"))
                print(box.fit(f"[bright_white] YOUR KEY : [green2]{key}"))
                sys.exit()
        else:
            print(box.fit("[bold red] THE TOOL IS PAID"))
            print(box.fit("[bold red] YOU ARE NOT APPROVED"))
            print(box.fit(f"[bright_white] YOUR KEY : [green2]{key}"))
            sys.exit()

def main2():
    clear()
    print(logo)
    print(box.fit("[bright_white] WELCOME"))
    print(box.fit(f"[bright_white] YOUR KEY : [green2]{key}"))
    sys.exit()

def main():
    srvr()

if __name__ == "__main__":
    main()
