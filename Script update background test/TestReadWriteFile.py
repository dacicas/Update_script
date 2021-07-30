import os.path

def updateareNumeProfil(numar):
    file = open("resources/profilename.txt","w")
    value = "test"+str(numar)
    file.write(value)
    file.close()
    return value

def schimbatNume(propertyName):
    number = int(propertyName[4:len(propertyName)])+1
    return updateareNumeProfil(number)

file = open("resources/profilename.txt")
my_env = file.readline()

print(my_env)
file.close()

for statusFisier in os.listdir("C:\\Users\\dani\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"):
    x = "fgdgdfg" in statusFisier
    if (x):
        my_env = schimbatNume(my_env)
        print("The LAST SETP " + my_env)

def new_path_to_profile(Primut):
    for toate_profilele in os.listdir("C:\\Users\\dani\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"):
        x = "Primut" in toate_profilele
        if (x):


# cautaProfil("fgdgdfg")
