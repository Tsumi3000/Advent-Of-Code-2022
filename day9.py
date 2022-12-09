
file = open('input.txt').readlines()

def stape1():
    actualTAIL = actualHEAD = (0,0)
    moves = [actualTAIL]
    for ligne in file: 
        decompose = ligne.split()
        for _ in range(int(decompose[1])):
            if decompose[0] == "U": move = (0,1)
            elif decompose[0] == "D": move = (0,-1)
            elif decompose[0] == "R": move = (1,0)
            elif decompose[0] == "L": move = (-1,0)
            actualHEAD = (actualHEAD[0]+move[0], actualHEAD[1]+move[1])
            if (abs(actualHEAD[0] - actualTAIL[0]) >= 2 or abs(actualHEAD[1] - actualTAIL[1]) >= 2): actualTAIL = (actualHEAD[0]-move[0], actualHEAD[1]-move[1])
            moves.append(actualTAIL)
            
    occurence = []
    for i in moves:
        if i not in occurence: occurence.append(i)
    return len(occurence)

def stape2():
    actualHEAD = {i:(0,0) for i in range(10)}
    moves = [actualHEAD[9]]
    for ligne in file: 
        decompose = ligne.split()
        for _ in range(int(decompose[1])):
            if decompose[0] == "U": move = (0,1)
            elif decompose[0] == "D": move = (0,-1)
            elif decompose[0] == "R": move = (1,0)
            elif decompose[0] == "L": move = (-1,0)
            actualHEAD[0] = (actualHEAD[0][0]+move[0], actualHEAD[0][1]+move[1])
            for i in range(1,10):
                H = actualHEAD[i-1]
                T = actualHEAD[i]
                if (abs(H[0] - T[0]) >= 2) and (abs(H[1] - T[1]) >= 2): actualHEAD[i] = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
                elif (abs(H[0] - T[0]) >= 2): actualHEAD[i] = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
                elif (abs(H[1] - T[1]) >= 2): actualHEAD[i] = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
            moves.append(actualHEAD[9])
            
    occurence = []
    for i in moves:
        if i not in occurence: occurence.append(i)
    return len(occurence)

print(stape1(), stape2())