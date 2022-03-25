import os,sys
try: import requests
except ModuleNotFoundError:print("[!] Sedang Install Module requests");os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError:print("[!] Sedang Install Module bs4");os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError:print("[!] Sedang Install Module mechanize");os.system("python -m pip install mechanize &> /dev/null")
try: import gTTS
except ModuleNotFoundError: os.system("python -m pip install gTTS &> /dev/null")
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import sys, os, subprocess, platform, struct
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json 
import requests as req
#import requests as re
import time,random,json
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup
from random import choice as pilih
from concurrent.futures import ThreadPoolExecutor as __Kiky__
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from datetime import datetime 
from urllib.parse import quote 
from datetime import date 
null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:os.system('pkg install play-audio -y &> /dev/null')
try:os.mkdir("dump")
except:pass
try:os.mkdir("Hasil")
except:pass
if ("linux" in sys.platform.lower()):
	II='\x1b[1;32m'
	I='\x1b[0;32m'
	C='\x1b[0;36m'
	M='\x1b[0;31m'
	U='\x1b[0;35m'
	K='\x1b[0;33m'
	P='\x1b[00m'
	H='\x1b[0;90m'
	Q="\x1b[00m"
	O='\033[38;2;255;127;0;1m' #ORANGE
	B = '\x1b[0;94m' # BIRU.
	war = f"[{C}•{Q}]-->"
else:
	II=''
	I=''
	C=''
	M=''
	U=''
	K=''
	P=''
	H=''
	Q=""
	O='' #ORANGE
	B='' # BIRU.
	war = "[•]-->"




jarak = "     "
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
loop = 0
ok = []
cp = []
ttl = []
id = []
nampung = []
data,data2={},{}
ubahP,pwBaru=[],[]



###### >>>> SETINGAN JAM ATAU TANGGAL
current = datetime.now()
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}




#####  BAGIAN DEF ATAU CLASS #####
def jalan(z):
	for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.009)
def play_mpv(x):
	try:os.popen("play-audio "+x)
	except:pass

import uuid
class menu:
	def __init__(self):
		os.system('clear')
		self.mani()
#		crackmenu("").check_opsi()
	def buat_tgl(self):
		global wak_
		os.system("clear")
		try:
			id1 = open(".datame1", "r").read()
			idl = open(".datame1", "r").read()
		except:
			self.konfo()
		gig = requests.get("https://github.com/GoodBoyC/GoodBoyC/blob/main/license").text.strip()
		if idl in gig:
			jok = gig.split(idl+"|")
			jokk = ("%s"%(jok[1]))
			jokkk = jokk.split("<")
			wakk = jokkk[0]
			if wakk == "":
				self.konfo()
		else:
			self.konfo()

	def lanjut_x(self):
		try:
			id1 = open(".datame1", "r").read()
		except:
			id1 = uuid.uuid4().hex[:43].upper()
			jaa = open(".datame1", "w")
			jaa.write(id1)
			jaa.close()
		no_wa = "2349067338953"
		url_wa = ("https://api.whatsapp.com/send?phone="+no_wa+"&text=") # UBAH NOMOR HP KAMU
		jalan(war+'Licese Anda : '+U+id1+Q)
		jalan(war+'Silahkan Chat *'+C+'Mr.Chinda'+Q+'* Untuk Membeli Key !')
		jalan(f"""{war}Method Pembayaran
 |
 |-->Dana   |--> {U}09067338953 {Q}
 |
{war}Informasi/Kontak
 |
 |-->Whatsapp ( {U}09067338953{Q})
 |
{war}Pesan Admin Tinggalkan
 |
 |-->Admin Tidak Bertanggung Jawab Atas Terjadinya Masalah !
 |-->Jika Anda Mau Membeli License/Key Harap Kirim Bukti Transaksi/Tranfer
 |-->Admin Tidak Menerima Penawaran/Tawar Menawar
 |
{war}Thanks to
 |-->{I}Arya{Q}
 |
 |
 |-->{C}Arya{Q}
 |.            X
 |-->{I}Mr.Chinda{Q}
{war}{O}Silahkan Pilih Harga License...{Q}
 |
 |-->1. 1 month      (${II}100{Q})
 |-->2. {M}Permanent  (${II}500{Q})
 |""")
		pok = input(' |-->Pilih : ')
		if pok in (""," "):
			jalan(" |-->Jangan Kosong...")
			time.sleep(2)
			self.lanjut_x()
		elif pok in ("1","01"):
			tks = ("Hello Sir, I want to buy 1 month key/license.\nKey/License : *"+id1+"*")
			subprocess.check_output(["am", "start", url_wa+tks])
		elif pok in ("2","02"):
			tks = ("Hello Sir, I want to buy a permanent key/license.\nKey/License : *"+id1+"*")
			subprocess.check_output(["am", "start", url_wa+tks])
		else:
			jalan(' |-->Maaf Pilihan Yang Anda Pilih Tidak Ada....')
			time.sleep(2)
			self.lanjut_x()
		os.sys.exit()

	def buat_key_gratis(self):

		key = requests.get("https://pastebin.com/raw/mjYSUq7E").text
		jaa = open(".datame1", "w")
		jaa.write(key)
		jaa.close()
		try:self.cek_tgl()
		except:pass
		jalan(war+"Berhasil Membuat Key Gratis Silahkan Jalankan Script Ini")
		os.sys.exit()

	def konfo(self):
		os.system("clear")
		try:
			id1 = open(".datame1", "r").read()
		except:
			id1 = uuid.uuid4().hex[:43].upper()
			jaa = open(".datame1", "w")
			jaa.write(id1)
			jaa.close()
		jalan(war+"Lihat Doaanngg Cuma Minta Trial")
		print(" |-->1. Beli Key/License");time.sleep(0.75)
		print(" |-->2. Gunakan Trial (Tidak Selama Gratis Kawan)");time.sleep(0.75)
		pul_ = input(" |-->Pilih : ")
		if pul_ in ([""," "]):jalan(war+"Isi Dengan Benar !!!!");time.sleep(1);self.konfo()

		elif pul_ in (["1","01"]):self.lanjut_x();os.sys.exit(),
		elif pul_ in (["2","02"]):self.buat_key_gratis();os.sys.exit()

		else:jalan(war+"Isi Dengan Benar !!!!");time.sleep(1);self.konfo()
		os.sys.exit()


	def cek_tgl(self):
		global infona
		try:
			id1 = open(".datame1", "r").read()
			idl = open(".datame1", "r").read()
		except:
			self.konfo()
		gig = requests.get("https://github.com/GoodBoyC/GoodBoyC/blob/main/license").text.strip()
		if idl in gig:
			jok = gig.split(idl+"|")
			jokk = ("%s"%(jok[1]))
			jokkk = jokk.split("<")
			wak = jokkk[0]
			jaa = open(".datame2", "w")
			jaa.write(wak)
			jaa.close()
			wak_ = open(".datame2", "r").read().split()
		else:
			self.konfo()
		try:
			tgl = datetime.now()
			bln = tgl.month
			thn = tgl.year
			day = tgl.day
			mulai = datetime(int(wak_[0]), int(wak_[1]), int(wak_[2]))
			seles = datetime(thn, bln, day)
			sisa = mulai - seles
			lim_dev_id = str(sisa).split()[0]
			if "KIKY" in "":
				infona = (II+"Ultimate/Tidak Habis²"+Q)
				return infona
			else:
				infona = (O+lim_dev_id+" Hari Lagi")
				if ":" in str(lim_dev_id) or "-" in str(lim_dev_id):
						exit(jalan(war+"Silahkan Hubungi Athour Untuk Memperpanjangankan License ! "))
						os.sys.exit()
				return infona
		except:
			jalan(f" |-->Key/License Anda : {O}{id1}{Q}")
			jalan(" |-->Maaf Key/License Anda Sudah Expires, Silahkan Hubungi Admin Script")
			jalan(f' |-->No Whatsapp : {O}6283893415477{Q}')
			print(" |")
			print(" |")
			zib = input(f' |-->Apakah Anda Mau Hapus License/Key ({O}Y/n{Q}):')
			if zib in (""," "):
				jalan(" |-->Jangan Kosong...")
				os.sys.exit()
			elif zib in ("Y","y"):
				try:
					os.remove(".datame1")
					os.remove(".datame2")
				except:pass
				jalan(' |-->File License/Key Anda Sudah Saya Hapus....')
				os.sys.exit()
			else:
				jalan(" |-->Isi Dengan Benar Dong...")
				os.sys.exit()
			os.sys.exit()