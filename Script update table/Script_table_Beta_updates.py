import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time
import random

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("TestUpdateBeta-dbbd302b4f47.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("IncercareBetaUpdates").sheet1

data = sheet.get_all_records()
#for easy  kep the migration variable even though we dont do migration anymore
migration_start=0
migration_end=9
last = 27

versions = [88.0, 89.0, 90.0]
candidates = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"]
versions_beta_candidates = []
x = 0
y = 0
for x in versions:
    for y in candidates:
        z = str(x)
        versions_beta_candidates.append(z+y)
print(versions_beta_candidates)


locale = ["en-US", "zh-CN", "es-ES", "ja", "de", "fr", "ru", "ar", "ko", "pt-PT", "vi", "pl", "tr"]

beta_locale= []
while len(beta_locale) < 30:
    un_element = random.randrange(0, 13)
    beta_locale.append(locale[un_element])

beta_locale_set = set(beta_locale)

beta_locale_2 = [*beta_locale_set]
print('Locale Beta:')
print(beta_locale_2)

sheet.update_cell(31, 4, (beta_locale_2[0]))
sheet.update_cell(32, 4, (beta_locale_2[1]))
sheet.update_cell(33, 4, (beta_locale_2[2]))
sheet.update_cell(34, 4, (beta_locale_2[3]))
sheet.update_cell(35, 4, (beta_locale_2[4]))
sheet.update_cell(36, 4, (beta_locale_2[5]))
sheet.update_cell(37, 4, (beta_locale_2[6]))
sheet.update_cell(38, 4, (beta_locale_2[7]))
sheet.update_cell(39, 4, (beta_locale_2[8]))
sheet.update_cell(40, 4, (beta_locale_2[9]))

Win_7_lista_versiuni_alea_finale = []
while len(Win_7_lista_versiuni_alea_finale) < 2:
    ver_1 = random.randrange(migration_start, last);
    ver_2 = random.randrange(migration_start, last);
    dev = random.randrange(migration_start, last)
    Win_7_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_1])
    Win_7_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_2])
    Win_7_lista_versiuni_alea_finale.append(versions_beta_candidates[dev])

sheet.update_cell(31, 5, (Win_7_lista_versiuni_alea_finale[0]))
sheet.update_cell(31, 3, ".exe")
sheet.update_cell(32, 5, (Win_7_lista_versiuni_alea_finale[1]))
sheet.update_cell(32, 3, ".zip")
sheet.update_cell(48, 5, (Win_7_lista_versiuni_alea_finale[2]))
sheet.update_cell(48, 3, ".zip")

Win_10_lista_versiuni_alea_finale = []
while len(Win_10_lista_versiuni_alea_finale) < 2:
    ver_1 = random.randrange(migration_start, last);
    ver_2 = random.randrange(migration_start, last);
    dev = random.randrange(migration_start, last);
    Win_10_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_1])
    Win_10_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_2])
    Win_10_lista_versiuni_alea_finale.append(versions_beta_candidates[dev])
sheet.update_cell(33, 5, (Win_10_lista_versiuni_alea_finale[0]))
sheet.update_cell(33, 3, ".exe")
sheet.update_cell(34, 5, (Win_10_lista_versiuni_alea_finale[1]))
sheet.update_cell(34, 3, ".zip")
sheet.update_cell(49, 5, (Win_10_lista_versiuni_alea_finale[2]))
sheet.update_cell(49, 3, ".zip")

Win_10_ARM_lista_versiuni_alea_finale = []
while len(Win_10_ARM_lista_versiuni_alea_finale) < 2:
    ver_1 = random.randrange(migration_start, last);
    ver_2 = random.randrange(migration_start, last);
    dev = random.randrange(migration_start, last);
    Win_10_ARM_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_1])
    Win_10_ARM_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_2])
    Win_10_ARM_lista_versiuni_alea_finale.append(versions_beta_candidates[dev])
sheet.update_cell(35, 5, (Win_10_ARM_lista_versiuni_alea_finale[0]))
sheet.update_cell(35, 3, ".exe")
sheet.update_cell(36, 5, (Win_10_ARM_lista_versiuni_alea_finale[1]))
sheet.update_cell(36, 3, ".zip")
sheet.update_cell(50, 5, (Win_10_ARM_lista_versiuni_alea_finale[2]))
sheet.update_cell(50, 3, ".zip")

Mac_OS_lista_versiuni_alea_finale = []
while len(Mac_OS_lista_versiuni_alea_finale) < 2:
    ver_1 = random.randrange(migration_start, last);
    ver_2 = random.randrange(migration_start, last);
    dev = random.randrange(migration_start, last)
    Mac_OS_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_1])
    Mac_OS_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_2])
    Mac_OS_lista_versiuni_alea_finale.append(versions_beta_candidates[dev])
sheet.update_cell(37, 5, (Mac_OS_lista_versiuni_alea_finale[0]))
sheet.update_cell(37, 3, ".dmg")
sheet.update_cell(38, 5, (Mac_OS_lista_versiuni_alea_finale[1]))
sheet.update_cell(38, 3, ".pkg")
sheet.update_cell(51, 5, (Mac_OS_lista_versiuni_alea_finale[2]))
sheet.update_cell(51, 3,".dmg")

Mac_OS_ARM_lista_versiuni_alea_finale = []
while len(Mac_OS_ARM_lista_versiuni_alea_finale) < 2:
    ver_1 = random.randrange(migration_start, last);
    ver_2 = random.randrange(migration_start, last);
    dev = random.randrange(migration_start, last)
    Mac_OS_ARM_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_1])
    Mac_OS_ARM_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_2])
    Mac_OS_ARM_lista_versiuni_alea_finale.append(versions_beta_candidates[dev])
sheet.update_cell(39, 5, (Mac_OS_ARM_lista_versiuni_alea_finale[0]))
sheet.update_cell(39, 3, ".dmg")
sheet.update_cell(40, 5, (Mac_OS_ARM_lista_versiuni_alea_finale[1]))
sheet.update_cell(40, 3, ".pkg")
sheet.update_cell(52, 5, (Mac_OS_ARM_lista_versiuni_alea_finale[2]))
sheet.update_cell(52, 3,".dmg")


Ubuntu_lista_versiuni_alea_finale = []
while len(Ubuntu_lista_versiuni_alea_finale) < 2:
    ver_1 = random.randrange(migration_start, last);
    ver_2 = random.randrange(migration_start, last);
    dev = random.randrange(migration_start, last)
    Ubuntu_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_1])
    Ubuntu_lista_versiuni_alea_finale.append(versions_beta_candidates[ver_2])
    Ubuntu_lista_versiuni_alea_finale.append(versions_beta_candidates[dev])
sheet.update_cell(41, 5, (Ubuntu_lista_versiuni_alea_finale[0]))
sheet.update_cell(41, 3, ".tar.bz2")
sheet.update_cell(42, 5, (Ubuntu_lista_versiuni_alea_finale[1]))
sheet.update_cell(42, 3, ".tar.bz2")
sheet.update_cell(53, 5, (Ubuntu_lista_versiuni_alea_finale[2]))
sheet.update_cell(53, 3, ".tar.bz2")

