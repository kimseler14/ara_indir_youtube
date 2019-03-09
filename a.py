# -*- coding: utf-8 -*-
import urllib.request, json 
import os
import subprocess

os.system('clear')

try:
  with open('link.txt') as f:
    toplam_link = (sum(1 for _ in f))
    print(a)
except Exception:
     pass


if toplam_link > 1:
        sil = input('önceki listeden ' + str( toplam_link) + ' adet link var.silmek istermisin? (e/h): ')


if toplam_link > 1:
    if sil == "e":
        if os.path.exists("link.txt"):
            os.remove("link.txt")
            print("silindi")
    if sil == "h":
        pass



 

def arama():
 kelime = input("anahtar kelime?: ")
 
 url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&order=date&q=" + kelime + "&safeSearch=none&key=AIzaSyDK6F-uGwnB5OJAbwN2iL3Nz5icptYTwm4"

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
  
  print('devam edersen ' + str(b) + ' video indirilecek.')
  a = input('yeni link eklemek için "y". indirmek için "i" . çıkmak için "x". : ')

  if a == "y":
      tekrar()
  if a == "x":
     print("çıkılıyor...")
     break
  if a == "i":
     os.system("youtube-dl -o '%(title)s.%(ext)s' -a link.txt")

def tekrar():
 arama()
 indirme()
 
tekrar()
