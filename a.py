# -*- coding: utf-8 -*-
import urllib.request, json 
import os, sys
os.system('clear')


try:
 if os.path.exists("link.txt"):
  with open('link.txt') as f:
    toplam_link = (sum(1 for _ in f))
    print(a)
except Exception:
     pass

try:
    if toplam_link > 0:
     sil = input('önceki listeden ' + str( toplam_link) + ' adet link var.silmek istermisin? (e/h): ')
except NameError:
    pass
 
try:
 if toplam_link > 0:
    if sil == "e":
        if os.path.exists("link.txt"):
            os.remove("link.txt")
            print("silindi")
    if sil == "h":
        pass
except Exception:
     pass

                  
def sadece_indir():
    os.system("youtube-dl -i -o '~/video/%(title)s.%(ext)s' -a link.txt")
def arama():
 os.system('clear')
 kelime = input("anahtar kelime? : ")
 
 url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&q=" + kelime + "&safeSearch=none&key=API KEY GİR"

 url = urllib.request.urlopen(url)
 data = json.load(url)   
 for arama in data['items']:
  try:
   print('https://www.youtube.com/watch?v=' + arama['id']['videoId'], file=open("link.txt", "a"))
  except KeyError:
   continue
  
  try:
      with open('link.txt') as f:
          a = (sum(1 for _ in f))
  except Exception:
     pass
 print('bulunan link sayısı = '+ str(a))
def indirme():
 while True:
  try:
      with open('link.txt') as f:
          b = (sum(1 for _ in f))
  except Exception:
      pass
  os.system('clear')
  print('devam edersen ' + str(b) + ' video indirilecek.')
  soru = """
  (y) yeni link eklemek için.
  (i) indirmek için.
  (a) ana menüye dönmek için.
  (q) çıkmak için"""
  print(soru)
  
  soru = input("Yapmak istediğiniz işlemin harfini girin: ")
  
  if soru == "a":
      bas()
  if soru == "y":
      tekrar()
  if soru == "x":
     print("çıkılıyor...")
     sys.exit(0)
  if soru == "i":
     os.system("youtube-dl -i -o '~/video/%(title)s.%(ext)s' -a link.txt")
def tekrar():
 arama()
 indirme()
def bas():
 giris = """
 (i) sadece listeyi indir.
 (a) arama 
 (x) ara ve indir
 (q) çıkmak için
 (u) indirilen videoları google photo'a yükle"""
 print(giris)
 soru = input("Yapmak istediğiniz işlemin harfini girin: ")
 if soru == "u":
        upload()
 if soru == "i":
        sadece_indir()
 if soru == "q":
     os._exit(0)
 if soru == "a":
        arama()
        bas()
 if soru == "x":
        tekrar()
def upload():
	os.system('mkdir video')
	os.system('clear')
	
	if len(os.listdir('video') ) == 0:
		print("hiç video indirmemişşin.seni başa alıyoruz")
		basa()
		
	if len(os.listdir('video') ) > 0:
		a = len(os.listdir('video') )
		print("""daha önceden """ + str(a) + """ tane indirilmiş video bulundu
        
        """)
		bas = """
		(s) önceden indirilenleri sil.
		(i) silmeden devam et.
            
		"""
		print(bas)
        
	soru = input("Yapmak istediğiniz işlemin harfini girin: ")
	if soru =="s":
		dirPath = "video"
		fileList = os.listdir(dirPath)
		for fileName in fileList:
			os.remove(dirPath+"/"+fileName)
		os.system('clear')
		print("önceden indirdiklerin silindi")
		basa()
	if soru =="i":
		os.system("./gpup video")
		os.system('clear')
		basa()
def basa():
	bas()
bas()

