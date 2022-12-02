
values = open('input.txt').readlines()
snacks = [0]
iter = 0

for ligne in values:
    if ligne == "\n":
        snacks.append(0)
        iter+=1
    else: snacks[iter] += int(ligne[:-1])

def stape1(): return sorted(snacks)[len(snacks) - 1]

def stape2(): return sum(sorted(snacks)[-3:])

print(stape1, stape2())