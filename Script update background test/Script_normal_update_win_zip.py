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
import threading



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
                  'user_pref("app.update.doorhanger", false);\n'
                  'user_pref("browser.shell.checkDefaultBrowser", false);\n'
                  'user_pref("browser.tabs.warnOnClose", false);\n'
                  'user_pref("browser.aboutwelcome.enabled", false);\n'
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
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.press("h")
    time.sleep(1)
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1154, y=588)
    time.sleep(5)
    pyautogui.click(x=1358, y=587)
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460 )
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard")

def copy_AUS_SVC_Clipboard_AR():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=1035, y=17)#Help
    time.sleep(1)
    pyautogui.click(x=1008, y=228)#About Fx
    time.sleep(1)
    pyautogui.press(x=618, y=407)#Update Fx
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1232, y=679)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1172, y=673)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_AR")

def copy_AUS_SVC_Clipboard_RU():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=368, y=14)#Help
    time.sleep(1)
    pyautogui.click(x=461, y=173)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1227, y=595)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1443, y=598)#Clipboard
    time.sleep(30)
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    time.sleep(2)
    pyautogui.click(x=174, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_RU")

def copy_AUS_SVC_Clipboard_zh_CH():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=334, y=12)#Help
    time.sleep(1)
    pyautogui.click(x=382, y=230)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1200, y=631)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1291, y=631)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_zh-CH")

def copy_AUS_SVC_Clipboard_es_ES():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=363, y=14)#Help
    time.sleep(1)
    pyautogui.click(x=473, y=224)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1209, y=631)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1364, y=629)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_es-ES")

def copy_AUS_SVC_Clipboard_JA():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=422, y=14)#Help
    time.sleep(1)
    pyautogui.click(x=459, y=231)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1215, y=630)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1408, y=628)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_JA")

def copy_AUS_SVC_Clipboard_DE():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=355, y=13)#Help
    time.sleep(1)
    pyautogui.click(x=447, y=221)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1228, y=633)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1431, y=624)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_DE")

def copy_AUS_SVC_Clipboard_FR():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=384, y=11)#Help
    time.sleep(1)
    pyautogui.click(x=465, y=227)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1215, y=631)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1410, y=630)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_FR")

def copy_AUS_SVC_Clipboard_KO():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=353, y=12)#Help
    time.sleep(1)
    pyautogui.click(x=405, y=225)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1196, y=634)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1348, y=624)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_KO")

def copy_AUS_SVC_Clipboard_PT():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=361, y=12)#Help
    time.sleep(1)
    pyautogui.click(x=436, y=228)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1220, y=631)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1419, y=630)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_PT")

def copy_AUS_SVC_Clipboard_PL():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=329, y=14)#Help
    time.sleep(1)
    pyautogui.click(x=420, y=231)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1220, y=629)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1396, y=630)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_PL")

def copy_AUS_SVC_Clipboard_VI():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=466, y=12)#Help
    time.sleep(1)
    pyautogui.click(x=511, y=226)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1212, y=630)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1400, y=630)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_VI")

def copy_AUS_SVC_Clipboard_TR():
    time.sleep(60)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=347, y=17)#Help
    time.sleep(1)
    pyautogui.click(x=399, y=226)#About Fx
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=1106, y=489)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    time.sleep(5)
    pyautogui.click(button='right')
    time.sleep(5)
    pyautogui.click(x=1198, y=630)#Copy to clipboard
    time.sleep(5)
    pyautogui.click(x=1353, y=627)#Clipboard
    time.sleep(30)
    pyautogui.click()
    time.sleep(5)
    paste_in_new_File()
    time.sleep(5)
    BITS_check()
    pyautogui.click(x=291, y=460)
    pyautogui.hotkey('ctrl', 'shift', 'q')
    print("Done running copy_AUS_SVC_Clipboard_TR")

def paste_in_new_File():
    os.chdir(new_path)
    BITS_testing = open('BITS_testing.txt', "w", encoding='utf-8')
    BITS_testing.write(pyperclip.paste())
    BITS_testing.close()
    os.chmod("BITS_Testing.txt", S_IREAD)

def BITS_check():
    os.chdir(new_path)
    with open("BITS_testing.txt", encoding="UTF-8") as bits:
        if "Starting BITS download with url" in bits.read():
            print("BITS WAS USED")
        else:
            print("BITS was not used/ERROR")

def Screenshot():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.press("h")
    time.sleep(1)
    pyautogui.press("a")
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_AR():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=1035, y=17)
    time.sleep(1)
    pyautogui.click(x=1008, y=228)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_RU():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=368, y=14)
    time.sleep(1)
    pyautogui.click(x=461, y=234)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_zh_CH():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=334, y=12)
    time.sleep(1)
    pyautogui.click(x=382, y=230)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_es_ES():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=363, y=14)
    time.sleep(1)
    pyautogui.click(x=473, y=224)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_ja():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=422, y=14)
    time.sleep(1)
    pyautogui.click(x=459, y=231)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_DE():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=355, y=13)
    time.sleep(1)
    pyautogui.click(x=447, y=221)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_FR():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=384, y=11)
    time.sleep(1)
    pyautogui.click(x=465, y=227)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_KO():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=353, y=12)
    time.sleep(1)
    pyautogui.click(x=405, y=225)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_PT():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=361, y=12)
    time.sleep(1)
    pyautogui.click(x=436, y=228)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_PL():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=329, y=14)
    time.sleep(1)
    pyautogui.click(x=420, y=231)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_VI():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=466, y=12)
    time.sleep(1)
    pyautogui.click(x=511, y=226)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Screenshot_TR():
    print("Running screenshot...")
    time.sleep(20)
    pyautogui.click(x=1286, y=59)
    pyautogui.press("altleft")
    time.sleep(1)
    pyautogui.click(x=347, y=17)
    time.sleep(1)
    pyautogui.click(x=399, y=226)
    time.sleep(4)
    Screenshot = pyautogui.screenshot()
    Screenshot.save(r'{0}\\dovada_upd.png'.format(last_path))
    print("Done running screenshot.")

def Choose_screenshot():
    if locale == "en-US":
        Screenshot()
    elif locale == "zh-CN":
        Screenshot_zh_CH()
    elif locale == "es-ES":
        Screenshot_es_ES()
    elif locale == "ja":
        Screenshot_ja()
    elif locale == "de":
        Screenshot_DE()
    elif locale == "fr":
        Screenshot_FR()
    elif locale == "ru":
        Screenshot_RU()
    elif locale == "ar":
        Screenshot_AR()
    elif locale == "ko":
        Screenshot_KO()
    elif locale == "pt-PT":
        Screenshot_PT()
    elif locale == "vi":
        Screenshot_VI()
    elif locale == "tr":
        Screenshot_TR()
    elif locale == "pl":
        Screenshot_PL()


def Choose_lang():
            if locale == "en-US":
                copy_AUS_SVC_Clipboard()
            elif locale == "zh-CN":
                copy_AUS_SVC_Clipboard_zh_CH()
            elif locale == "es-ES":
                copy_AUS_SVC_Clipboard_es_ES()
            elif locale == "ja":
                copy_AUS_SVC_Clipboard_JA()
            elif locale == "de":
                copy_AUS_SVC_Clipboard_DE()
            elif locale == "fr":
                copy_AUS_SVC_Clipboard_FR()
            elif locale == "ru":
                copy_AUS_SVC_Clipboard_RU()
            elif locale == "ar":
                copy_AUS_SVC_Clipboard_AR()
            elif locale == "ko":
                copy_AUS_SVC_Clipboard_KO()
            elif locale == "pt-PT":
                copy_AUS_SVC_Clipboard_PT()
            elif locale == "vi":
                copy_AUS_SVC_Clipboard_VI()
            elif locale == "tr":
                copy_AUS_SVC_Clipboard_TR()
            elif locale == "pl":
                copy_AUS_SVC_Clipboard_PL()



print(os.getcwd())
first_test_starting_version = sheet.cell(34, 5).value
first_test_starting_version_string = str(first_test_starting_version)
locale = sheet.cell(34, 4).value

parent_dir = "D:\Test_Firefox"
path = os.path.join(parent_dir, first_test_starting_version_string)
os.mkdir(path)
os.chdir(path)
print(os.getcwd())

URL = "https://archive.mozilla.org/pub/firefox/candidates/"+first_test_starting_version_string+"-candidates/build1/win64/{0}/".format(locale)
print(URL)
zip = ".zip"
firefox_exe_msi_prefix = "firefox-"
filename = firefox_exe_msi_prefix+first_test_starting_version_string+zip
print(filename)
var_wgt = URL + filename
print(var_wgt)
print(wget.download(var_wgt, filename))
subprocess.call(["tar", "-xf", "D:/Test_Firefox/87.0b4/{0}".format(filename)])
firefox = "firefox"
new_path = os.path.join(parent_dir, first_test_starting_version_string, firefox)
print(new_path)
os.chdir(new_path)
print(os.getcwd())
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
profile_path = str("C:\\Users\\dani\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
subprocess.call(["firefox", "-CreateProfile", my_env])
time.sleep(10)
os.chdir(profile_path)
my_string_env = "*."+my_env
full_profile_folder = get_folder_name(my_string_env)
print(type(full_profile_folder))
print(type(profile_path))
full_profile_path = os.path.join(profile_path, full_profile_folder)
os.chdir(full_profile_path)
create_user_js(full_profile_path)
print(os.getcwd())
##change working directorie to where firefox is!!! fixed ?
last_path = path + "\\firefox"
os.chdir(last_path)
print(os.getcwd())

thread1 = threading.Thread(target=Choose_lang)
thread2 = threading.Thread(target=Choose_screenshot)

thread1.start()

print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
subprocess.call(["firefox", "-P", "{0}".format(my_env), "-jsconsole"])
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))

#asta e  ca  sa vad ca s-a facut update-ul ca sa nu trebuiasca sa aleg profilul
#FYI  daca dai restart atunci ma pune sa aleg profilul
time.sleep(10)
thread2.start()
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))
subprocess.call(["firefox", "-P", "{0}".format(my_env), "-jsconsole"])
print(subprocess.run(['firefox', "-version", "|", "more"], stdout=subprocess.PIPE).stdout.decode('utf-8'))