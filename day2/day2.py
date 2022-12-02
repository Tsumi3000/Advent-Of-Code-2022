
file = open("input.txt").readlines()
ennemySet = []
mySet = []
for i in file:
    ennemySet.append(i.split(" ")[0])
    mySet.append(i.split(" ")[1][:-1])

def stape1():
    points = 0
    for i in range(len(ennemySet)):
        if ennemySet[i] == "A":
            if mySet[i] == "X": points+=4
            elif mySet[i] == "Y": points+=8
            elif mySet[i] == "Z": points+=3
        elif ennemySet[i] == "B":
            if mySet[i] == "X": points+=1
            elif mySet[i] == "Y": points+=5
            elif mySet[i] == "Z": points+=9
        elif ennemySet[i] == "C":
            if mySet[i] == "X": points+=7
            elif mySet[i] == "Y": points+=2
            elif mySet[i] == "Z": points+=6
    return points

def stape2():
    points = 0
    for i in range(len(ennemySet)):
        if ennemySet[i] == "A":
            if mySet[i] == "X": points+=3
            elif mySet[i] == "Y": points+=4
            elif mySet[i] == "Z": points+=8
        elif ennemySet[i] == "B":
            if mySet[i] == "X": points+=1
            elif mySet[i] == "Y": points+=5
            elif mySet[i] == "Z": points+=9
        elif ennemySet[i] == "C":
            if mySet[i] == "X": points+=2
            elif mySet[i] == "Y": points+=6
            elif mySet[i] == "Z": points+=7
    return points

print(stape1(), stape2())