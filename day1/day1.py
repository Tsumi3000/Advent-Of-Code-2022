
file = open("day1_input.txt", "r")
values = file.readlines()
file.close()
dictionnary = {}
iter = 0
block = True

for ligne in values:
    if ligne == "\n":
        iter+=1
        block=True
    else:
        if block: dictionnary[str(iter)] = 0
        add = dictionnary[str(iter)]
        dictionnary[str(iter)] = (int(ligne[:-1]) + add)
        block=False

def stape1():
    max = 0
    for i in dictionnary.keys():
        if dictionnary[i] > max: max = dictionnary[i]
    return max

def stape2():
    top = {0:0,1:0,2:0}
    for i in dictionnary.keys():
        if dictionnary[i] > top[0]:
            top[2] = top[1]
            top[1] = top[0]
            top[0] = dictionnary[i]
        elif dictionnary[i] > top[1]:
            top[2] = top[1]
            top[1] = dictionnary[i]
        elif dictionnary[i] > top[2]:
            top[2] = dictionnary[i]

    somme = 0
    for i in top.keys(): somme+=top[i]
    return somme