#!/usr/bin/env python3
import os, fnmatch
import subprocess
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time
import random
import wget
import shutil
import pyautogui
from stat import S_IREAD, S_IRGRP, S_IROTH
import pyperclip



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("TestUpdateBeta-dbbd302b4f47.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("IncercareBetaUpdates").sheet1

data = sheet.get_all_records()

def updateareNumeProfil(numar):
    file = open("resources/profilename.txt","w")
    value = "Primut"+str(numar)
    file.write(value)
    file.close()
    return value

def schimbatNume(propertyName):
    number = int(propertyName[6:len(propertyName)])+1
    return updateareNumeProfil(number)

file = open("resources/profilename.txt")
my_env = file.readline()

print(my_env)
file.close()

for statusFisier in os.listdir("C:\\Users\\dani\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"):
    x = "Primut" in statusFisier
    if (x):
        my_env = schimbatNume(my_env)
        print("Nume profil: " + my_env)
        break

def create_user_js(new_path_to_my_env):
    os.chdir(new_path_to_my_env)
    user_js = open("User.js", "w")
    user_js.write('user_pref("app.update.enabled", false);\n'
                  'user_pref("app.update.auto", false);\n'
                  'user_pref("app.update.log", true);\n'
                  'user_pref("app.update.log.file", true);\n'
                  'user_pref("app.update.BITS.enabled", true);\n'
                  'user_pref("browser.shell.checkDefaultBrowser", false);\n'
                  'user_pref("browser.tabs.warnOnClose", false);\n'
                  'user_pref("browser.tabs.warnOnCloseOtherTabs", false);\n')
    user_js.close()
    os.chmod("User.js", S_IREAD)

def get_folder_name(my_string_env):
    list_of_profiles = os.listdir("C:\\Users\\dani\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
    pattern = my_string_env
    for x in list_of_profiles:
        if fnmatch.fnmatch(x, pattern):
            print(x)
            return str(x)

def copy_AUS_SVC_Clipboard():
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.press("h")
    time.sleep(1)
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.press("enter");
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.click(x=1154, y=588)
    time.sleep(1)
    pyautogui.click(x=1358, y=587)
    time.sleep(1)
    pyautogui.click()

def create_folder():
    get_ver = str(sheet.cell(34, 5).value)
    parent_dir = "D:\Test_Firefox"
    path = os.path.join(parent_dir,get_ver)
    os.mkdir(path)
    os.chdir(path)
    nume_build = path
    return nume_build

#GETS VERSION FROM GOOGLE SHEETS
#first_test_starting_version = sheet.cell(34, 5).value
#first_test_starting_version_string = str(first_test_starting_version)
#print(os.getcwd())
##CREATES FOLDER
#parent_dir = "D:\Test_Firefox"
#path = os.path.join(parent_dir, first_test_starting_version_string)
#os.mkdir(path)
#os.chdir(path)
#print(os.getcwd())

#DOWNLOADS THE BUILD
URL = "https://archive.mozilla.org/pub/firefox/candidates/"+first_test_starting_version_string+"-candidates/build1/win64/en-US/"
print(URL)
zip = ".zip"
firefox_exe_msi_prefix = "firefox-"
filename = firefox_exe_msi_prefix+first_test_starting_version_string+zip
print(filename)
var_wgt = URL + filename
print(var_wgt)
print(wget.download(var_wgt, filename))

def get_build(nume_build):
    URL = "https://archive.mozilla.org/pub/firefox/candidates/"+nume_build+"-candidates/build1/win64/en-US/"
    

#EXTRACTS THE ZIP
subprocess.call(["tar", "-xf", "D:/Test_Firefox/80.0b7/{0}".format(filename)])#DE CE AM  SCRIS ASTA IN LOC SA FOLOSESC VARIABILA PATH ?
firefox = "firefox"
new_path = os.path.join(parent_dir, first_test_starting_version_string, firefox)
print(new_path)
os.chdir(new_path)
print(os.getcwd())
#VERIFICA VERSIUNEA DE FX
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
profile_path = str("C:\\Users\\dani\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
#CAUTA FOLDERUL DE PROFIL THANK YOU FX
subprocess.call(["firefox", "-CreateProfile", my_env])
os.chdir(profile_path)
my_string_env = "*."+my_env
full_profile_folder = get_folder_name(my_string_env)
print(type(full_profile_folder))
print(type(profile_path))
#CREAZA USER.JS
full_profile_path = os.path.join(profile_path, full_profile_folder)
os.chdir(full_profile_path)
create_user_js(full_profile_path)
print(os.getcwd())
##change working directorie to where firefox is!!! fixed ?
last_path = path + "\\firefox"
os.chdir(last_path)
print(os.getcwd())
#AICI SE INTAMPLA FUTAI-UL CAND PORNESC FIREFOX
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
subprocess.call(["firefox", "-P", "{0}".format(my_env), "-jsconsole"])
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
copy_AUS_SVC_Clipboard()