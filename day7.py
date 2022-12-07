
file = open("input.txt").readlines()
dirInto = {}
sumDir = {}
currentDirectory = ""

for ligne in file:
    ligne = ligne[:-1]
    if ligne.startswith("$ cd"):
        if ligne == "$ cd /": currentDirectory = "/"
        elif ligne[5:].startswith(".."): currentDirectory = currentDirectory[:-len(currentDirectory.split("/")[-2])-1]
        else: currentDirectory+=ligne[5:]+"/"

    elif not ligne.startswith("$"):
        if ligne.startswith("dir"):
            if currentDirectory+ligne[4:]+"/" in dirInto: dirInto[currentDirectory+ligne[4:]+"/"].append(currentDirectory)
            else: dirInto[currentDirectory+ligne[4:]+"/"] = [currentDirectory]
            if currentDirectory in dirInto: dirInto[currentDirectory+ligne[4:]+"/"] = dirInto[currentDirectory+ligne[4:]+"/"] + dirInto[currentDirectory]

        else:
            if not currentDirectory in sumDir: sumDir[currentDirectory] = int(ligne.split()[0])
            else: sumDir[currentDirectory]+=int(ligne.split()[0])
            if currentDirectory in dirInto:
                for i in dirInto[currentDirectory]:
                    if not i in sumDir: sumDir[i] = int(ligne.split()[0])
                    else: sumDir[i]+=int(ligne.split()[0])

def stape1():
    sumTotal = 0
    for somme in sumDir.keys():
        if sumDir[somme] <= 100000: sumTotal+=sumDir[somme]
    return sumTotal

def stape2():
    need = 30000000 - 70000000 + sumDir["/"]
    min = 70000000
    for i in sumDir.keys():
        if sumDir[i] >= need and sumDir[i] < min: min = sumDir[i]
    return min

print(stape1(), stape2())