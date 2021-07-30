import os
import time
import sys
import wget
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("My Project 91964-e9479ebe9e7e.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("Incercare").sheet1

data = sheet.get_all_records()


migration_last = 5;
normal_last = 5;
last = 5;
mac_pkg = 0;

versions = [85.0, 85.01, 85.02, 86.0, 86.01, 87.0]

locale = ["be", "cak", "cy", "da", "de", "dsb", "en-CA", "en-GB", "es-AR", "es-CL", "es-ES", "fr", "fy-NL", 'gn', 'hr',
          'hsb', 'hu', 'ia', 'id', 'it', 'ka', 'ko', 'nl', 'nn-NO', 'pa-IN', 'pl', 'pt-BR', 'pt-PT', 'ro', 'sk', 'sl',
          'sq', 'sv-SE', 'tr', 'uk', 'vi', 'zh-CN', 'zh-TW']

Version_demo = random.choice(versions)
Version_demo_str = str(Version_demo)
print(Version_demo)
version_demo_str_list = list(Version_demo_str)

def check_length_of_version_add_extra_dot():
    if len(version_demo_str_list) > 4:
        version_demo_str_list.insert(4,".")
    else:
        pass

def check_length_of_version_add_extra_dot_N(variabila):
    if len(variabila) > 4:
        variabila.insert(4,".")
    variabila = "".join(variabila)
    return variabila


check_length_of_version_add_extra_dot()
final_version_conversion = "".join(version_demo_str_list)

print(final_version_conversion)

#RELEASE  LOCALTEST
release_localtest_1= []
while len(release_localtest_1) < 40:
    un_local_ales_random = random.randrange(0, 37)
    release_localtest_1.append(locale[un_local_ales_random])
release_localtest_1_set = set(release_localtest_1)
release_localtest_2 = [*release_localtest_1_set]
print('LOCALE RELEASE-LOCALTEST:')
print(release_localtest_2[0:20])
sheet.update_cell(42, 4, (release_localtest_2[0]))
sheet.update_cell(43, 4, (release_localtest_2[1]))
sheet.update_cell(44, 4, (release_localtest_2[2]))
sheet.update_cell(45, 4, (release_localtest_2[3]))
sheet.update_cell(46, 4, (release_localtest_2[4]))
sheet.update_cell(47, 4, (release_localtest_2[5]))
sheet.update_cell(48, 4, (release_localtest_2[6]))
sheet.update_cell(49, 4, (release_localtest_2[7]))
sheet.update_cell(50, 4, (release_localtest_2[8]))
sheet.update_cell(51, 4, (release_localtest_2[9]))
sheet.update_cell(52, 4, (release_localtest_2[10]))
sheet.update_cell(53, 4, (release_localtest_2[11]))
sheet.update_cell(54, 4, (release_localtest_2[12]))
sheet.update_cell(55, 4, (release_localtest_2[13]))
sheet.update_cell(56, 4, (release_localtest_2[14]))
sheet.update_cell(57, 4, (release_localtest_2[15]))
sheet.update_cell(58, 4, (release_localtest_2[16]))
sheet.update_cell(59, 4, (release_localtest_2[17]))
sheet.update_cell(60, 4, (release_localtest_2[18]))
sheet.update_cell(61, 4, (release_localtest_2[19]))
time.sleep(100)

#Functie pentru crearea unei liste de versiuni pentru win7
Win_7_lista_versiuni_alea_finale = []
while len(Win_7_lista_versiuni_alea_finale) < 4:
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(0, normal_last);
    normal_version2 = random.randrange(0, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, normal_last);
    update_version = random.randrange(0, len(versions));
    Win_7_lista_versiuni_alea_finale.append(versions[migration_version])
    Win_7_lista_versiuni_alea_finale.append(versions[normal_version1])
    Win_7_lista_versiuni_alea_finale.append(versions[normal_version2])
    Win_7_lista_versiuni_alea_finale.append(versions[update_version])
else:
    pass

for x in Win_7_lista_versiuni_alea_finale:
    if isinstance(x,float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_7_lista_versiuni_alea_finale.append(y)
    else:
        break

Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
sheet.update_cell(42, 6, (Win_7_lista_versiuni_alea_finale[0]))
sheet.update_cell(42, 3, ".zip")
sheet.update_cell(43, 6, (Win_7_lista_versiuni_alea_finale[1]))
sheet.update_cell(43, 3, ".exe")
sheet.update_cell(44, 6, (Win_7_lista_versiuni_alea_finale[2]))
sheet.update_cell(44, 3, ".exe")
sheet.update_cell(45, 6, (Win_7_lista_versiuni_alea_finale[3]))
sheet.update_cell(45, 3, ".zip")
print("Lista Win 7:")
print(Win_7_lista_versiuni_alea_finale)

Win_10_lista = []
while len(Win_10_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(0, normal_last);
    normal_version2 = random.randrange(0, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, normal_last);
    update_version = random.randrange(normal_last, len(versions));
    Win_10_lista.append(versions[migration_version])
    Win_10_lista.append(versions[normal_version1])
    Win_10_lista.append(versions[normal_version2])
    Win_10_lista.append(versions[update_version])
else:
    pass

for x in Win_10_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_10_lista.append(y)
    else:
        break

Win_10_lista.pop(0)
Win_10_lista.pop(0)
Win_10_lista.pop(0)
Win_10_lista.pop(0)
sheet.update_cell(46, 6, (Win_10_lista[0]))
sheet.update_cell(46, 3, ".zip")
sheet.update_cell(47, 6, (Win_10_lista[1]))
sheet.update_cell(47, 3, ".exe")
sheet.update_cell(48, 6, (Win_10_lista[2]))
sheet.update_cell(48, 3, ".zip")
sheet.update_cell(49, 6, (Win_10_lista[3]))
sheet.update_cell(49, 3, ".msi")
print("Lista Win 10:")
print(Win_10_lista)

Win_Arm_lista = []
while len(Win_Arm_lista) < 4:
    ## Iau versiunile
    normal_version1 = random.randrange(0, last);
    normal_version2 = random.randrange(0, last);
    normal_version3 = random.randrange(0, last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, last);
        while normal_version3 == normal_version2 or normal_version3 == normal_version1:
            normal_version3 = random.randrange(0, last)
    update_version = random.randrange(normal_last, len(versions));
    Win_Arm_lista.append(versions[migration_version])
    Win_Arm_lista.append(versions[normal_version1])
    Win_Arm_lista.append(versions[normal_version2])
    Win_Arm_lista.append(versions[update_version])
else:
    pass
for x in Win_Arm_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_Arm_lista.append(y)
    else:
        break
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
sheet.update_cell(50, 6, (Win_Arm_lista[0]))
sheet.update_cell(50, 3, ".zip")
sheet.update_cell(51, 6, (Win_Arm_lista[1]))
sheet.update_cell(51, 3, ".exe")
sheet.update_cell(52, 6, (Win_Arm_lista[2]))
sheet.update_cell(52, 3, ".zip")
sheet.update_cell(53, 6, (Win_Arm_lista[3]))
sheet.update_cell(53, 3, ".exe")
print("Lista Win ARM:")
print(Win_Arm_lista)

time.sleep(100)

Mac_OS_lista = []
while len(Mac_OS_lista) < 4:
    mac_version1 = random.randrange(0, migration_last)
    mac_version2 = random.randrange(0, last)
    mac_version3_pkg = random.randrange(0, last)
    mac_version3 = random.randrange(0, last)
    while mac_version3 == mac_version2:
        normal_version3 = random.randrange(0, last)
    Mac_OS_lista.append(versions[mac_version1])
    Mac_OS_lista.append(versions[mac_version2])
    Mac_OS_lista.append(versions[mac_version3_pkg])
    Mac_OS_lista.append(versions[mac_version3])
else:
    pass
for x in Mac_OS_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Mac_OS_lista.append(y)
    else:
        break
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
sheet.update_cell(54, 6, (Mac_OS_lista[0]))
sheet.update_cell(54, 3, ".dmg")
sheet.update_cell(55, 6, (Mac_OS_lista[1]))
sheet.update_cell(55, 3, ".dmg")
sheet.update_cell(56, 6, (Mac_OS_lista[2]))
sheet.update_cell(56, 3, ".pkg")
sheet.update_cell(57, 6, (Mac_OS_lista[3]))
sheet.update_cell(57, 3, ".dmg")

print("Lista Mac OS:")
print(Mac_OS_lista)

Ubuntu_lista = []
while len(Ubuntu_lista) < 4:
    ubuntu_version1 = random.randrange(0, migration_last)
    ubuntu_version2 = random.randrange(0, normal_last)
    ubuntu_version3 = random.randrange(0, last)
    ubuntu_version4 = random.randrange(0, last)
    while ubuntu_version4 == ubuntu_version3:
        ubuntu_version4 = random.randrange(0, last)
    Ubuntu_lista.append(versions[ubuntu_version1])
    Ubuntu_lista.append(versions[ubuntu_version2])
    Ubuntu_lista.append(versions[ubuntu_version3])
    Ubuntu_lista.append(versions[ubuntu_version4])
else:
    pass
for x in Ubuntu_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Ubuntu_lista.append(y)
    else:
        break
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
sheet.update_cell(58, 6, (Ubuntu_lista[0]))
sheet.update_cell(58, 3, ".tar.bz2")
sheet.update_cell(59, 6, (Ubuntu_lista[1]))
sheet.update_cell(59, 3, ".tar.bz2")
sheet.update_cell(60, 6, (Ubuntu_lista[2]))
sheet.update_cell(60, 3, ".tar.bz2")
sheet.update_cell(61, 6, (Ubuntu_lista[3]))
sheet.update_cell(61, 3, ".tar.bz2")

print("Lista Ubuntu:")
print(Ubuntu_lista)

time.sleep(100)
#RELEASE CDNTEST
release_cdntest_1= []
while len(release_cdntest_1) < 40:
    un_local_ales_random = random.randrange(0, 37)
    release_cdntest_1.append(locale[un_local_ales_random])
release_cdntest_1_set = set(release_cdntest_1)
release_cdntest_2 = [*release_cdntest_1_set]
print('LOCALE RELEASE-LOCALTEST:')
print(release_cdntest_2)

print(release_cdntest_2[0:20])
sheet.update_cell(67, 4, (release_cdntest_2[0]))
sheet.update_cell(68, 4, (release_cdntest_2[1]))
sheet.update_cell(69, 4, (release_cdntest_2[2]))
sheet.update_cell(70, 4, (release_cdntest_2[3]))
sheet.update_cell(71, 4, (release_cdntest_2[4]))
sheet.update_cell(72, 4, (release_cdntest_2[5]))
sheet.update_cell(73, 4, (release_cdntest_2[6]))
sheet.update_cell(74, 4, (release_cdntest_2[7]))
sheet.update_cell(75, 4, (release_cdntest_2[8]))
sheet.update_cell(76, 4, (release_cdntest_2[9]))
sheet.update_cell(77, 4, (release_cdntest_2[10]))
sheet.update_cell(78, 4, (release_cdntest_2[11]))
sheet.update_cell(79, 4, (release_cdntest_2[12]))
sheet.update_cell(80, 4, (release_cdntest_2[13]))
sheet.update_cell(81, 4, (release_cdntest_2[14]))
sheet.update_cell(82, 4, (release_cdntest_2[15]))
sheet.update_cell(83, 4, (release_cdntest_2[16]))
sheet.update_cell(84, 4, (release_cdntest_2[17]))
sheet.update_cell(85, 4, (release_cdntest_2[18]))
sheet.update_cell(86, 4, (release_cdntest_2[19]))
time.sleep(100)
#sa bag  lista de locale  intre astea doua

Win_7_lista_versiuni_alea_finale = []
while len(Win_7_lista_versiuni_alea_finale) < 4:
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(0, normal_last);
    normal_version2 = random.randrange(0, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, normal_last);
    update_version = random.randrange(normal_last, len(versions));
    Win_7_lista_versiuni_alea_finale.append(versions[migration_version])
    Win_7_lista_versiuni_alea_finale.append(versions[normal_version1])
    Win_7_lista_versiuni_alea_finale.append(versions[normal_version2])
    Win_7_lista_versiuni_alea_finale.append(versions[update_version])
else:
    pass

for x in Win_7_lista_versiuni_alea_finale:
    if isinstance(x,float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_7_lista_versiuni_alea_finale.append(y)
    else:
        break

Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
sheet.update_cell(67, 6, (Win_7_lista_versiuni_alea_finale[0]))
sheet.update_cell(67, 3, ".zip")
sheet.update_cell(68, 6, (Win_7_lista_versiuni_alea_finale[1]))
sheet.update_cell(68, 3, ".exe")
sheet.update_cell(69, 6, (Win_7_lista_versiuni_alea_finale[2]))
sheet.update_cell(69, 3, ".exe")
sheet.update_cell(70, 6, (Win_7_lista_versiuni_alea_finale[3]))
sheet.update_cell(70, 3, ".zip")
print("Lista Win 7:")
print(Win_7_lista_versiuni_alea_finale)

Win_10_lista = []
while len(Win_10_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(0, normal_last);
    normal_version2 = random.randrange(0, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, normal_last);
    update_version = random.randrange(normal_last, len(versions));
    Win_10_lista.append(versions[migration_version])
    Win_10_lista.append(versions[normal_version1])
    Win_10_lista.append(versions[normal_version2])
    Win_10_lista.append(versions[update_version])
else:
    pass

for x in Win_10_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_10_lista.append(y)
    else:
        break

Win_10_lista.pop(0)
Win_10_lista.pop(0)
Win_10_lista.pop(0)
Win_10_lista.pop(0)
sheet.update_cell(71, 6, (Win_10_lista[0]))
sheet.update_cell(71, 3, ".zip")
sheet.update_cell(72, 6, (Win_10_lista[1]))
sheet.update_cell(72, 3, ".exe")
sheet.update_cell(73, 6, (Win_10_lista[2]))
sheet.update_cell(73, 3, ".zip")
sheet.update_cell(74, 6, (Win_10_lista[3]))
sheet.update_cell(74, 3, ".msi")
print("Lista Win 10:")
print(Win_10_lista)

Win_Arm_lista = []
while len(Win_Arm_lista) < 4:
    ## Iau versiunile
    normal_version1 = random.randrange(0, last);
    normal_version2 = random.randrange(0, last);
    normal_version3 = random.randrange(0, last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, last);
        while normal_version3 == normal_version2 or normal_version3 == normal_version1:
            normal_version3 = random.randrange(0, last)
    update_version = random.randrange(normal_last, len(versions));
    Win_Arm_lista.append(versions[migration_version])
    Win_Arm_lista.append(versions[normal_version1])
    Win_Arm_lista.append(versions[normal_version2])
    Win_Arm_lista.append(versions[update_version])
else:
    pass
for x in Win_Arm_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_Arm_lista.append(y)
    else:
        break
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
sheet.update_cell(75, 6, (Win_Arm_lista[0]))
sheet.update_cell(75, 3, ".zip")
sheet.update_cell(76, 6, (Win_Arm_lista[1]))
sheet.update_cell(76, 3, ".exe")
sheet.update_cell(77, 6, (Win_Arm_lista[2]))
sheet.update_cell(77, 3, ".zip")
sheet.update_cell(78, 6, (Win_Arm_lista[3]))
sheet.update_cell(78, 3, ".exe")
print("Lista Win ARM:")
print(Win_Arm_lista)

time.sleep(100)

Mac_OS_lista = []
while len(Mac_OS_lista) < 4:
    mac_version1 = random.randrange(0, migration_last)
    mac_version2 = random.randrange(0, last)
    mac_version3_pkg = random.randrange(0, last)
    mac_version3 = random.randrange(0, last)
    while mac_version3 == mac_version2:
        normal_version3 = random.randrange(0, last)
    Mac_OS_lista.append(versions[mac_version1])
    Mac_OS_lista.append(versions[mac_version2])
    Mac_OS_lista.append(versions[mac_version3_pkg])
    Mac_OS_lista.append(versions[mac_version3])
else:
    pass
for x in Mac_OS_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Mac_OS_lista.append(y)
    else:
        break
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
sheet.update_cell(79, 6, (Mac_OS_lista[0]))
sheet.update_cell(79, 3, ".dmg")
sheet.update_cell(80, 6, (Mac_OS_lista[1]))
sheet.update_cell(80, 3, ".dmg")
sheet.update_cell(81, 6, (Mac_OS_lista[2]))
sheet.update_cell(81, 3, ".pkg")
sheet.update_cell(82, 6, (Mac_OS_lista[3]))
sheet.update_cell(82, 3, ".dmg")

print("Lista Mac OS:")
print(Mac_OS_lista)

Ubuntu_lista = []
while len(Ubuntu_lista) < 4:
    ubuntu_version1 = random.randrange(0, migration_last)
    ubuntu_version2 = random.randrange(0, normal_last)
    ubuntu_version3 = random.randrange(0, last)
    ubuntu_version4 = random.randrange(0, last)
    while ubuntu_version4 == ubuntu_version3:
        ubuntu_version4 = random.randrange(0, last)
    Ubuntu_lista.append(versions[ubuntu_version1])
    Ubuntu_lista.append(versions[ubuntu_version2])
    Ubuntu_lista.append(versions[ubuntu_version3])
    Ubuntu_lista.append(versions[ubuntu_version4])
else:
    pass
for x in Ubuntu_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Ubuntu_lista.append(y)
    else:
        break
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
sheet.update_cell(83, 6, (Ubuntu_lista[0]))
sheet.update_cell(83, 3, ".tar.bz2")
sheet.update_cell(84, 6, (Ubuntu_lista[1]))
sheet.update_cell(84, 3, ".tar.bz2")
sheet.update_cell(85, 6, (Ubuntu_lista[2]))
sheet.update_cell(85, 3, ".tar.bz2")
sheet.update_cell(86, 6, (Ubuntu_lista[3]))
sheet.update_cell(86, 3, ".tar.bz2")

print("Lista Ubuntu:")
print(Ubuntu_lista)

#RELEASE
release_1= []
while len(release_1) < 40:
    un_local_ales_random = random.randrange(0, 37)
    release_1.append(locale[un_local_ales_random])
release_1_set = set(release_1)
release_2 = [*release_1_set]
print('LOCALE RELEASE:')
print(release_2)

print(release_2[0:20])
sheet.update_cell(92, 4, (release_2[0]))
sheet.update_cell(93, 4, (release_2[1]))
sheet.update_cell(94, 4, (release_2[2]))
sheet.update_cell(95, 4, (release_2[3]))
sheet.update_cell(96, 4, (release_2[4]))
sheet.update_cell(97, 4, (release_2[5]))
sheet.update_cell(98, 4, (release_2[6]))
sheet.update_cell(99, 4, (release_2[7]))
sheet.update_cell(100, 4, (release_2[8]))
sheet.update_cell(101, 4, (release_2[9]))
sheet.update_cell(102, 4, (release_2[10]))
sheet.update_cell(103, 4, (release_2[11]))
sheet.update_cell(104, 4, (release_2[12]))
sheet.update_cell(105, 4, (release_2[13]))
sheet.update_cell(106, 4, (release_2[14]))
sheet.update_cell(107, 4, (release_2[15]))
sheet.update_cell(108, 4, (release_2[16]))
sheet.update_cell(109, 4, (release_2[17]))
sheet.update_cell(110, 4, (release_2[18]))
sheet.update_cell(111, 4, (release_2[19]))

time.sleep(100)

#sa bag  lista de locale  intre astea doua

Win_7_lista_versiuni_alea_finale = []
while len(Win_7_lista_versiuni_alea_finale) < 4:
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(0, normal_last);
    normal_version2 = random.randrange(0, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, normal_last);
    update_version = random.randrange(normal_last, len(versions));
    Win_7_lista_versiuni_alea_finale.append(versions[migration_version])
    Win_7_lista_versiuni_alea_finale.append(versions[normal_version1])
    Win_7_lista_versiuni_alea_finale.append(versions[normal_version2])
    Win_7_lista_versiuni_alea_finale.append(versions[update_version])
else:
    pass

for x in Win_7_lista_versiuni_alea_finale:
    if isinstance(x,float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_7_lista_versiuni_alea_finale.append(y)
    else:
        break

Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
Win_7_lista_versiuni_alea_finale.pop(0)
sheet.update_cell(92, 6, (Win_7_lista_versiuni_alea_finale[0]))
sheet.update_cell(92, 3, ".zip")
sheet.update_cell(93, 6, (Win_7_lista_versiuni_alea_finale[1]))
sheet.update_cell(93, 3, ".exe")
sheet.update_cell(94, 6, (Win_7_lista_versiuni_alea_finale[2]))
sheet.update_cell(94, 3, ".exe")
sheet.update_cell(95, 6, (Win_7_lista_versiuni_alea_finale[3]))
sheet.update_cell(95, 3, ".zip")
print("Lista Win 7:")
print(Win_7_lista_versiuni_alea_finale)

Win_10_lista = []
while len(Win_10_lista) < 4:
    ## Iau versiunile
    migration_version = random.randrange(0, migration_last);
    normal_version1 = random.randrange(0, normal_last);
    normal_version2 = random.randrange(0, normal_last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, normal_last);
    update_version = random.randrange(normal_last, len(versions));
    Win_10_lista.append(versions[migration_version])
    Win_10_lista.append(versions[normal_version1])
    Win_10_lista.append(versions[normal_version2])
    Win_10_lista.append(versions[update_version])
else:
    pass

for x in Win_10_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_10_lista.append(y)
    else:
        break

Win_10_lista.pop(0)
Win_10_lista.pop(0)
Win_10_lista.pop(0)
Win_10_lista.pop(0)
sheet.update_cell(96, 6, (Win_10_lista[0]))
sheet.update_cell(96, 3, ".zip")
sheet.update_cell(97, 6, (Win_10_lista[1]))
sheet.update_cell(97, 3, ".exe")
sheet.update_cell(98, 6, (Win_10_lista[2]))
sheet.update_cell(98, 3, ".zip")
sheet.update_cell(99, 6, (Win_10_lista[3]))
sheet.update_cell(99, 3, ".msi")
print("Lista Win 10:")
print(Win_10_lista)

Win_Arm_lista = []
while len(Win_Arm_lista) < 4:
    ## Iau versiunile
    normal_version1 = random.randrange(0, last);
    normal_version2 = random.randrange(0, last);
    normal_version3 = random.randrange(0, last);
    while normal_version2 == normal_version1:
        normal_version2 = random.randrange(0, last);
        while normal_version3 == normal_version2 or normal_version3 == normal_version1:
            normal_version3 = random.randrange(0, last)
    update_version = random.randrange(normal_last, len(versions));
    Win_Arm_lista.append(versions[migration_version])
    Win_Arm_lista.append(versions[normal_version1])
    Win_Arm_lista.append(versions[normal_version2])
    Win_Arm_lista.append(versions[update_version])
else:
    pass
for x in Win_Arm_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Win_Arm_lista.append(y)
    else:
        break
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
Win_Arm_lista.pop(0)
sheet.update_cell(100, 6, (Win_Arm_lista[0]))
sheet.update_cell(100, 3, ".zip")
sheet.update_cell(101, 6, (Win_Arm_lista[1]))
sheet.update_cell(101, 3, ".exe")
sheet.update_cell(102, 6, (Win_Arm_lista[2]))
sheet.update_cell(102, 3, ".zip")
sheet.update_cell(103, 6, (Win_Arm_lista[3]))
sheet.update_cell(103, 3, ".exe")
print("Lista Win ARM:")
print(Win_Arm_lista)

time.sleep(100)

Mac_OS_lista = []
while len(Mac_OS_lista) < 4:
    mac_version1 = random.randrange(0, migration_last)
    mac_version2 = random.randrange(0, migration_last)
    mac_version3_pkg = random.randrange(0, last)
    mac_version3 = random.randrange(0, last)
    while mac_version3 == mac_version2:
        normal_version3 = random.randrange(0, last)
    Mac_OS_lista.append(versions[mac_version1])
    Mac_OS_lista.append(versions[mac_version2])
    Mac_OS_lista.append(versions[mac_version3_pkg])
    Mac_OS_lista.append(versions[mac_version3])
else:
    pass
for x in Mac_OS_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Mac_OS_lista.append(y)
    else:
        break
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
Mac_OS_lista.pop(0)
sheet.update_cell(104, 6, (Mac_OS_lista[0]))
sheet.update_cell(104, 3, ".dmg")
sheet.update_cell(105, 6, (Mac_OS_lista[1]))
sheet.update_cell(105, 3, ".dmg")
sheet.update_cell(106, 6, (Mac_OS_lista[2]))
sheet.update_cell(106, 3, ".pkg")
sheet.update_cell(107, 6, (Mac_OS_lista[3]))
sheet.update_cell(107, 3, ".dmg")

print("Lista Mac OS:")
print(Mac_OS_lista)

Ubuntu_lista = []
while len(Ubuntu_lista) < 4:
    ubuntu_version1 = random.randrange(0, migration_last)
    ubuntu_version2 = random.randrange(0, normal_last)
    ubuntu_version3 = random.randrange(0, last)
    ubuntu_version4 = random.randrange(0, last)
    while ubuntu_version4 == ubuntu_version3:
        ubuntu_version4 = random.randrange(0, last)
    Ubuntu_lista.append(versions[ubuntu_version1])
    Ubuntu_lista.append(versions[ubuntu_version2])
    Ubuntu_lista.append(versions[ubuntu_version3])
    Ubuntu_lista.append(versions[ubuntu_version4])
else:
    pass
for x in Ubuntu_lista:
    if isinstance(x, float):
        y = list(str(x))
        y = check_length_of_version_add_extra_dot_N(y)
        Ubuntu_lista.append(y)
    else:
        break
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
Ubuntu_lista.pop(0)
sheet.update_cell(108, 6, (Ubuntu_lista[0]))
sheet.update_cell(108, 3, ".tar.bz2")
sheet.update_cell(109, 6, (Ubuntu_lista[1]))
sheet.update_cell(109, 3, ".tar.bz2")
sheet.update_cell(110, 6, (Ubuntu_lista[2]))
sheet.update_cell(110, 3, ".tar.bz2")
sheet.update_cell(111, 6, (Ubuntu_lista[3]))
sheet.update_cell(111, 3, ".tar.bz2")

print("Lista Ubuntu:")
print(Ubuntu_lista)

