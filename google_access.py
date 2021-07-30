import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("My Project 91964-e9479ebe9e7e.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("Incercare").sheet1

data = sheet.get_all_records()

import random

# mi-am numarat pozitiat in lista a elementelor
migration_last = 6;
normal_last = 51;
last = 67;
mac_pkg = 45;


versions = [54.0, 54.01, 55.0, 55.01, 55.02, 55.03, 56.0, 56.01, 56.02, 57.0, 57.01, 57.02, 57.03, 57.04, 58.0, 58.01,
            58.02, 59.0, 59.01, 59.02, 59.03, 60.0, 60.01, 60.02, 61.0, 61.01, 61.02, 62.0, 62.01, 62.02, 62.03, 63.0,
            63.01, 63.02, 63.03, 64.0, 64.02, 65.0, 65.01, 65.02, 66.0, 66.01, 66.02, 66.03, 66.04, 66.05, 67.0, 67.01,
            67.02, 67.03, 67.04, 68.0, 68.01, 68.02, 69.0, 69.01, 69.02, 69.03, 70.0, 70.01, 71.0, 72.0, 72.01, 72.02,
            73.0, 73.0, 73.01, 74.0]


locale = ["be", "cak", "cy", "da", "de", "dsb", "en-CA", "en-GB", "es-AR", "es-CL", "es-ES", "fr", "fy-NL", 'gn', 'hr',
          'hsb', 'hu', 'ia', 'id', 'it', 'ka', 'ko', 'nl', 'nn-NO', 'pa-IN', 'pl', 'pt-BR', 'pt-PT', 'ro', 'sk', 'sl',
          'sq', 'sv-SE', 'tr', 'uk', 'vi', 'zh-CN', 'zh-TW']

prima_lista_locale = []
while len(prima_lista_locale) < 35:
    un_element = random.randrange(0, 37)
    prima_lista_locale.append(locale[un_element])

primul_set = set(prima_lista_locale)

a_doua_lista_elemente_unice = [*primul_set]
print('Lista de locale pentru tabel:')
print(a_doua_lista_elemente_unice[0:20])

verssion_given = random.choice(versions)



# 1. acum ce trebuie sa fac  e  sa creez o variabila globala  care sa  ia ver_from adica"="

# 2. trebuie sa fac o functie care sa ia variabila globala si sa o treaca prin reguli.
def reguli_win_10(verssion_given):
    # sa ma gandesc cum scriu regulile de mig
    if verssion_given <= 56:
        return (str(verssion_given))
    elif verssion_given >= 56 and verssion_given < 68:
        return (str(verssion_given))
    elif verssion_given >= 68:
        return (str(verssion_given))


def reguli_mac_os(verssion_given):
    if verssion_given <= 69:
        return (str(verssion_given))
    else:
        return (str(verssion_given))


def reguli_ubuntu(verssion_given):
    return (str(verssion_given))


#RELEASE-LOCALTEST

Win_10_lista = []
while len(Win_10_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(migration_last + 1, normal_last);
    normal_version2 = random.randrange(migration_last + 1, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(migration_last + 1, normal_last);
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_10_lista.append(reguli_win_10(versions[migration_version]))
    sheet.update_cell(46, 6, (reguli_win_10(versions[migration_version])))
    sheet.update_cell(46, 3, "zip")
    Win_10_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(47, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(47, 3, "exe")
    Win_10_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(48, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(48, 3, "zip")
    Win_10_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(49, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(49, 3, "msi")
else:
    print("Win_10_lista:")
    print(Win_10_lista)

Win_7_lista = []
while len(
        Win_7_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(migration_last + 1, normal_last);
    normal_version2 = random.randrange(migration_last + 1, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(migration_last + 1, normal_last);
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_7_lista.append(reguli_win_10(versions[migration_version]))
    sheet.update_cell(42, 6, (reguli_win_10(versions[migration_version])))
    sheet.update_cell(42, 3, "zip")
    Win_7_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(43, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(43, 3, "exe")
    Win_7_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(44, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(44, 3, "exe")
    Win_7_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(45, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(45, 3, "zip")
else:
    print("Win_7_lista:")
    print(Win_7_lista)


Win_Arm_lista = []
while len(Win_Arm_lista) < 4:
    ## Iau versiunile
    normal_version1 = random.randrange(normal_last + 1, last);
    normal_version2 = random.randrange(normal_last + 1, last);
    normal_version3 = random.randrange(normal_last + 1, last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(normal_last + 1, last);
        while normal_version3 == normal_version2 or normal_version3 == normal_version1:
            normal_version3 = random.randrange(normal_last + 1, last)
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_Arm_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(50, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(50, 3, "zip")
    Win_Arm_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(51, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(51, 3, "exe")
    Win_Arm_lista.append(reguli_win_10(versions[normal_version3]))
    sheet.update_cell(52, 6, (reguli_win_10(versions[normal_version3])))
    sheet.update_cell(52, 3, "exe")
    Win_Arm_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(53, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(53, 3, "msi")
else:
    print('Win_ARM_Lista:')
    print(Win_Arm_lista)


Mac_OS_lista = []
while len(Mac_OS_lista) < 4:
    mac_version1 = random.randrange(0, migration_last)
    mac_version2 = random.randrange(migration_last, mac_pkg)
    mac_version3_pkg = random.randrange(mac_pkg, last)
    mac_version3 = random.randrange(migration_last + 1, last)
    while mac_version3 == mac_version2:
        normal_version3 = random.randrange(migration_last + 1, last)
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version1]))
    sheet.update_cell(54, 6, (reguli_mac_os(versions[mac_version1])))
    sheet.update_cell(54, 3, "dmg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version2]))
    sheet.update_cell(55, 6, (reguli_mac_os(versions[mac_version2])))
    sheet.update_cell(55, 3, "dmg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version3_pkg]))
    sheet.update_cell(56, 6, (reguli_mac_os(versions[mac_version3_pkg])))
    sheet.update_cell(56, 3, "pkg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version3]))
    sheet.update_cell(57, 6, (reguli_mac_os(versions[mac_version3])))
    sheet.update_cell(57, 3, "dmg")
else:
    print("Mac_OS_Lista:")
    print(Mac_OS_lista)


Ubuntu_lista = []
while len(Ubuntu_lista) < 4:
    ubuntu_version1 = random.randrange(0, migration_last)
    ubuntu_version2 = random.randrange(migration_last + 1, normal_last)
    ubuntu_version3 = random.randrange(normal_last + 1, last)
    ubuntu_version4 = random.randrange(normal_last + 1, last)
    while ubuntu_version4 == ubuntu_version3:
        ubuntu_version4 = random.randrange(normal_last + 1, last)

    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version1]))
    sheet.update_cell(58, 6, (reguli_ubuntu(versions[ubuntu_version1])))
    sheet.update_cell(58, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version2]))
    sheet.update_cell(59, 6, (reguli_ubuntu(versions[ubuntu_version2])))
    sheet.update_cell(59, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version3]))
    sheet.update_cell(60, 6, (reguli_ubuntu(versions[ubuntu_version3])))
    sheet.update_cell(60, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version4]))
    sheet.update_cell(61, 6, (reguli_ubuntu(versions[ubuntu_version4])))
    sheet.update_cell(61, 3, "tar.bz2")
else:
    print("Ubuntu_Lista:")
    print(Ubuntu_lista)

#RELEASE-CDNTEST

Win_10_lista = []
while len(Win_10_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(migration_last + 1, normal_last);
    normal_version2 = random.randrange(migration_last + 1, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(migration_last + 1, normal_last);
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_10_lista.append(reguli_win_10(versions[migration_version]))
    sheet.update_cell(71, 6, (reguli_win_10(versions[migration_version])))
    sheet.update_cell(71, 3, "zip")
    Win_10_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(72, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(72, 3, "exe")
    Win_10_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(73, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(73, 3, "zip")
    Win_10_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(74, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(74, 3, "msi")
else:
    print("Win_10_lista:")
    print(Win_10_lista)

Win_7_lista = []
while len(
        Win_7_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(migration_last + 1, normal_last);
    normal_version2 = random.randrange(migration_last + 1, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(migration_last + 1, normal_last);
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_7_lista.append(reguli_win_10(versions[migration_version]))
    sheet.update_cell(67, 6, (reguli_win_10(versions[migration_version])))
    sheet.update_cell(67, 3, "zip")
    Win_7_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(68, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(68, 3, "exe")
    Win_7_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(69, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(69, 3, "exe")
    Win_7_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(70, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(70, 3, "zip")
else:
    print("Win_7_lista:")
    print(Win_7_lista)


Win_Arm_lista = []
while len(Win_Arm_lista) < 4:
    ## Iau versiunile
    normal_version1 = random.randrange(normal_last + 1, last);
    normal_version2 = random.randrange(normal_last + 1, last);
    normal_version3 = random.randrange(normal_last + 1, last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(normal_last + 1, last);
        while normal_version3 == normal_version2 or normal_version3 == normal_version1:
            normal_version3 = random.randrange(normal_last + 1, last)
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_Arm_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(75, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(75, 3, "zip")
    Win_Arm_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(76, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(76, 3, "exe")
    Win_Arm_lista.append(reguli_win_10(versions[normal_version3]))
    sheet.update_cell(77, 6, (reguli_win_10(versions[normal_version3])))
    sheet.update_cell(77, 3, "exe")
    Win_Arm_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(78, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(78, 3, "msi")
else:
    print('Win_ARM_Lista:')
    print(Win_Arm_lista)


Mac_OS_lista = []
while len(Mac_OS_lista) < 4:
    mac_version1 = random.randrange(0, migration_last)
    mac_version2 = random.randrange(migration_last, mac_pkg)
    mac_version3_pkg = random.randrange(mac_pkg, last)
    mac_version3 = random.randrange(migration_last + 1, last)
    while mac_version3 == mac_version2:
        normal_version3 = random.randrange(migration_last + 1, last)
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version1]))
    sheet.update_cell(79, 6, (reguli_mac_os(versions[mac_version1])))
    sheet.update_cell(79, 3, "dmg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version2]))
    sheet.update_cell(80, 6, (reguli_mac_os(versions[mac_version2])))
    sheet.update_cell(80, 3, "dmg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version3_pkg]))
    sheet.update_cell(81, 6, (reguli_mac_os(versions[mac_version3_pkg])))
    sheet.update_cell(81, 3, "pkg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version3]))
    sheet.update_cell(82, 6, (reguli_mac_os(versions[mac_version3])))
    sheet.update_cell(82, 3, "dmg")
else:
    print("Mac_OS_Lista:")
    print(Mac_OS_lista)


Ubuntu_lista = []
while len(Ubuntu_lista) < 4:
    ubuntu_version1 = random.randrange(0, migration_last)
    ubuntu_version2 = random.randrange(migration_last + 1, normal_last)
    ubuntu_version3 = random.randrange(normal_last + 1, last)
    ubuntu_version4 = random.randrange(normal_last + 1, last)
    while ubuntu_version4 == ubuntu_version3:
        ubuntu_version4 = random.randrange(normal_last + 1, last)

    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version1]))
    sheet.update_cell(83, 6, (reguli_ubuntu(versions[ubuntu_version1])))
    sheet.update_cell(83, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version2]))
    sheet.update_cell(84, 6, (reguli_ubuntu(versions[ubuntu_version2])))
    sheet.update_cell(84, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version3]))
    sheet.update_cell(85, 6, (reguli_ubuntu(versions[ubuntu_version3])))
    sheet.update_cell(85, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version4]))
    sheet.update_cell(86, 6, (reguli_ubuntu(versions[ubuntu_version4])))
    sheet.update_cell(86, 3, "tar.bz2")
else:
    print("Ubuntu_Lista:")
    print(Ubuntu_lista)

#RELEASE

time.sleep(2)

Win_10_lista = []
while len(Win_10_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(migration_last + 1, normal_last);
    normal_version2 = random.randrange(migration_last + 1, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(migration_last + 1, normal_last);
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_10_lista.append(reguli_win_10(versions[migration_version]))
    sheet.update_cell(96, 6, (reguli_win_10(versions[migration_version])))
    sheet.update_cell(96, 3, "zip")
    Win_10_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(97, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(97, 3, "exe")
    Win_10_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(98, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(98, 3, "zip")
    Win_10_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(99, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(99, 3, "msi")
else:
    print("Win_10_lista:")
    print(Win_10_lista)

Win_7_lista = []
while len(
        Win_7_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(migration_last + 1, normal_last);
    normal_version2 = random.randrange(migration_last + 1, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(migration_last + 1, normal_last);
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_7_lista.append(reguli_win_10(versions[migration_version]))
    sheet.update_cell(92, 6, (reguli_win_10(versions[migration_version])))
    sheet.update_cell(92, 3, "zip")
    Win_7_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(93, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(93, 3, "exe")
    Win_7_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(94, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(94, 3, "exe")
    Win_7_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(95, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(95, 3, "zip")
else:
    print("Win_7_lista:")
    print(Win_7_lista)


Win_Arm_lista = []
while len(Win_Arm_lista) < 4:
    ## Iau versiunile
    normal_version1 = random.randrange(normal_last + 1, last);
    normal_version2 = random.randrange(normal_last + 1, last);
    normal_version3 = random.randrange(normal_last + 1, last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(normal_last + 1, last);
        while normal_version3 == normal_version2 or normal_version3 == normal_version1:
            normal_version3 = random.randrange(normal_last + 1, last)
    update_version = random.randrange(normal_last, len(versions));

    ##am lista asta versions = [ 1,2,3,4,5,6,7]
    ##daca dau print(versions[0]) imi returneaza 1
    Win_Arm_lista.append(reguli_win_10(versions[normal_version1]))
    sheet.update_cell(100, 6, (reguli_win_10(versions[normal_version1])))
    sheet.update_cell(100, 3, "zip")
    Win_Arm_lista.append(reguli_win_10(versions[normal_version2]))
    sheet.update_cell(101, 6, (reguli_win_10(versions[normal_version2])))
    sheet.update_cell(101, 3, "exe")
    Win_Arm_lista.append(reguli_win_10(versions[normal_version3]))
    sheet.update_cell(102, 6, (reguli_win_10(versions[normal_version3])))
    sheet.update_cell(102, 3, "exe")
    Win_Arm_lista.append(reguli_win_10(versions[update_version]))
    sheet.update_cell(103, 6, (reguli_win_10(versions[update_version])))
    sheet.update_cell(103, 3, "msi")
else:
    print('Win_ARM_Lista:')
    print(Win_Arm_lista)


Mac_OS_lista = []
while len(Mac_OS_lista) < 4:
    mac_version1 = random.randrange(0, migration_last)
    mac_version2 = random.randrange(migration_last, mac_pkg)
    mac_version3_pkg = random.randrange(mac_pkg, last)
    mac_version3 = random.randrange(migration_last + 1, last)
    while mac_version3 == mac_version2:
        normal_version3 = random.randrange(migration_last + 1, last)
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version1]))
    sheet.update_cell(104, 6, (reguli_mac_os(versions[mac_version1])))
    sheet.update_cell(104, 3, "dmg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version2]))
    sheet.update_cell(105, 6, (reguli_mac_os(versions[mac_version2])))
    sheet.update_cell(105, 3, "dmg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version3_pkg]))
    sheet.update_cell(106, 6, (reguli_mac_os(versions[mac_version3_pkg])))
    sheet.update_cell(106, 3, "pkg")
    Mac_OS_lista.append(reguli_mac_os(versions[mac_version3]))
    sheet.update_cell(107, 6, (reguli_mac_os(versions[mac_version3])))
    sheet.update_cell(107, 3, "dmg")
else:
    print("Mac_OS_Lista:")
    print(Mac_OS_lista)


Ubuntu_lista = []
while len(Ubuntu_lista) < 4:
    ubuntu_version1 = random.randrange(0, migration_last)
    ubuntu_version2 = random.randrange(migration_last + 1, normal_last)
    ubuntu_version3 = random.randrange(normal_last + 1, last)
    ubuntu_version4 = random.randrange(normal_last + 1, last)
    while ubuntu_version4 == ubuntu_version3:
        ubuntu_version4 = random.randrange(normal_last + 1, last)

    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version1]))
    sheet.update_cell(108, 6, (reguli_ubuntu(versions[ubuntu_version1])))
    sheet.update_cell(108, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version2]))
    sheet.update_cell(109, 6, (reguli_ubuntu(versions[ubuntu_version2])))
    sheet.update_cell(109, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version3]))
    sheet.update_cell(110, 6, (reguli_ubuntu(versions[ubuntu_version3])))
    sheet.update_cell(110, 3, "tar.bz2")
    Ubuntu_lista.append(reguli_ubuntu(versions[ubuntu_version4]))
    sheet.update_cell(111, 6, (reguli_ubuntu(versions[ubuntu_version4])))
    sheet.update_cell(111, 3, "tar.bz2")
else:
    print("Ubuntu_Lista:")
    print(Ubuntu_lista)