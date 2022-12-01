
file = open('input.txt')
values = file.readlines()
file.close()
dictionnary = {0:0}
iter = 0

for ligne in values:
    if ligne == "\n":
        dictionnary[iter] = 0
        iter+=1
    else:
        add = dictionnary[iter]
        dictionnary[iter] = (int(ligne[:-1]) + add)

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