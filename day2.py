
file = open("input.txt").readlines()
ennemySet = []
mySet = []
for i in file:
    ennemySet.append(i.split()[0])
    mySet.append(i.split()[1][:-1])

def stape1():
    points = 0
    for i in range(len(ennemySet)):
        if ord(ennemySet[i]) - 64 == (ord(ennemySet[i]) - 87): points+=3 + ord(mySet) - 87
        elif ord(ennemySet[i]) - 64 < (ord(ennemySet[i]) - 87) or (ennemySet[i] == "C" and mySet[i] == "X"): points+=6 + ord(mySet) - 87
        elif ord(ennemySet[i]) - 64 > (ord(ennemySet[i]) - 87) or (ennemySet[i] == "A" and mySet[i] == "Z"): points+=ord(mySet) - 87
    return points

def stape2():
    points = 0
    for i in range(len(ennemySet)):
        if mySet[i] == "Y": points+=3 + ord(ennemySet) - 64
        elif mySet[i] == "X" and ennemySet[i] == "A": points+=3
        elif mySet[i] == "X" and ennemySet[i] != "A": points+=ord(ennemySet) - 65
        elif mySet[i] == "Z" and ennemySet[i] == "C": points+=7
        elif mySet[i] == "Z" and ennemySet[i] == "C": points+=6 + ord(ennemySet) - 63
    return points

print(stape1(), stape2())
