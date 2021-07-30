import time
import pyautogui
import fnmatch


def copy_AUS_SVC_Clipboard():
    print("US")

def copy_AUS_SVC_Clipboard_AR():
    print("AR")

def copy_AUS_SVC_Clipboard_RU():
    print("RU")

def copy_AUS_SVC_Clipboard_zh_CH():
    print("Zh")

def copy_AUS_SVC_Clipboard_es_ES():
    print("ES")

def copy_AUS_SVC_Clipboard_JA():
    print("JA")

def copy_AUS_SVC_Clipboard_DE():
    print("DE")

def copy_AUS_SVC_Clipboard_FR():
    print("FR")

def copy_AUS_SVC_Clipboard_KO():
    print("KO")

def copy_AUS_SVC_Clipboard_PT():
    print("PT")

def copy_AUS_SVC_Clipboard_PL():
    print("PL")

def copy_AUS_SVC_Clipboard_VI():
    print("VI")

def copy_AUS_SVC_Clipboard_TR():
    print("TR")


def Choose_lang(x):
        if x == "en-US":
                copy_AUS_SVC_Clipboard()
        elif x == "zh-CN":
                copy_AUS_SVC_Clipboard_zh_CH()
        elif x == "es-ES":
                copy_AUS_SVC_Clipboard_es_ES()
        elif x == "ja":
                copy_AUS_SVC_Clipboard_JA()
        elif x == "de":
                copy_AUS_SVC_Clipboard_DE()
        elif x == "fr":
                copy_AUS_SVC_Clipboard_FR()
        elif x == "ru":
                copy_AUS_SVC_Clipboard_RU()
        elif x == "ar":
                copy_AUS_SVC_Clipboard_AR()
        elif x == "ko":
                copy_AUS_SVC_Clipboard_KO()
        elif x == "pt-PT":
                copy_AUS_SVC_Clipboard_PT()
        elif x == "vi":
                copy_AUS_SVC_Clipboard_VI()
        elif x == "tr":
                copy_AUS_SVC_Clipboard_TR()

locale= "ru"
Choose_lang(locale)