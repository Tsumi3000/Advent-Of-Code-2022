
def stape1():
    first = []
    second = []
    mySum = 0
    passi = False
    for i in open('input.txt').readlines():
        first.append(i[:int((len(i))/2)])
        second.append(i[int((len(i))/2):-1])

    for i in range(len(first)):
        passi = False
        for m in first[i]:
            for k in second[i]:
                if(not passi):
                    if(m == k and k.upper() == k):
                        mySum+=ord(k) - 38
                        passi = True
                    elif(m == k and k.upper() != k):
                        mySum+=ord(k) - 96
                        passi = True
    return mySum

def stape2():
    first = []
    second = []                 
    third = []
    iter=0
    mySum=0
    passi = False
    for i in open('input.txt').readlines():
        if(iter==0): first.append(i[:-1])
        if(iter==1): second.append(i[:-1])
        if(iter==2): third.append(i[:-1])
        iter=(iter+1)%3

    for i in range(len(first)):
        passi = False
        for m in first[i]:
            for k in second[i]:
                for o in third[i]:
                    if(not passi):
                        if(m == k and k == o and o.upper() == o):
                            mySum+=ord(k) - 38
                            passi = True
                        elif(m == k and k == o and o.upper() != o):
                            mySum+=ord(k) - 96
                            passi = True
    return mySum

print(stape1(), stape2())