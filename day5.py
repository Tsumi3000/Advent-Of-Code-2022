
file = open('input.txt').readlines()
dico = {"1": [""], "2": [""], "3": [""], "4": [""], "5": [""], "6": [""], "7": [""], "8": [""], "9": [""]}
instructions = []
for ligne in file:   
    if len(ligne) != 36 and len(ligne) != 1: instructions.append([ligne[5:-(len(ligne)%2+12)], ligne[len(ligne)-7:-6], ligne[len(ligne)-2:-1]])
    for i in dico.keys():
        if len(ligne) == 36 and ligne[(int(i)-1)*4:-(len(ligne)-3-(4*(int(i)-1)))] != '   ': dico[i].append(ligne[(int(i)-1)*4:-(len(ligne)-3-(4*(int(i)-1)))])

for i in dico.keys():
    dico[i].pop(0)
    dico[i].pop()

def stape1():
    phrase = ""
    for actions in instructions:
        for _ in range(int(actions[0])):
            dico[actions[2]].insert(0, dico[actions[1]][0])
            dico[actions[1]].pop(0)

    for i in dico.keys(): phrase+=dico[i][0][1:-1]
    return phrase

def stape2():
    phrase = ""
    for actions in instructions:
        for move in range(int(actions[0])):
            dico[actions[2]].insert(move, dico[actions[1]][0])
            dico[actions[1]].pop(0)
    for i in dico.keys(): phrase+=dico[i][0][1:-1]
    return phrase
    
print(stape1(), stape2())