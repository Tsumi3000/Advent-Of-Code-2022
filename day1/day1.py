
snacks = [0]

for ligne in open('input.txt').readlines():
    if ligne == "\n": snacks.append(0)
    else: snacks[len(snacks) - 1] += int(ligne)

def stape1(): return sorted(snacks)[len(snacks) - 1]

def stape2(): return sum(sorted(snacks)[-3:])

print(stape1, stape2())