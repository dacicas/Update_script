#!/usr/bin/env python3
import os
import subprocess
import time

#1. creaza un folder pe desktop numit update tests cu un sub folder
os.chdir("C:/Users/dani/Desktop")
print(os.getcwd())
os.mkdir("C:/Users/dani/Desktop/70.0b_Update_test")
os.chdir("C:/Users/dani/Desktop/70.0b_Update_test")
print(os.getcwd())
#populeaza folderul cu FX ver .zip

subprocess.call(["curl", "https://archive.mozilla.org/pub/firefox/candidates/76.0b6-candidates/build1/win64/en-US/firefox-76.0b6.zip", "--output", "76test.zip" ])
subprocess.call(["tar", "-xf", "C:/Users/dani/Desktop/70.0b_Update_test/76test.zip"])
time.sleep(20)
os.chdir(r"C:\Users\dani\Desktop\70.0b_Update_test\firefox")
print(os.getcwd())
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
subprocess.call(["firefox", "-CreateProfile", "Primut"])
subprocess.call(["firefox", "-P", "Primut", "-jsconsole"])
time.sleep(180)
subprocess.call(["taskkill", "/F", "/IM", "firefox.exe"])
time.sleep(60)
subprocess.call(["firefox", "-P", "Primut"])
time.sleep(60)
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))

#WTF ACUMA PRIMESC EROARE CU  OLDER FIREFOX,  CRED CA TREBUIE SA MA SCAP DE TOATE PROFILELE SI CURATAT PRIN H_KEY + STERS CE INSTALURI MAI AM
