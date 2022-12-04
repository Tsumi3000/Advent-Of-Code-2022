file = open('input.txt').readlines()

def stape1():
    add = 0
    for ligne in range(len(file)):
        first = file[ligne].split(",")[0]
        second = file[ligne].split(",")[1]
        if int(first.split("-")[0]) <= int(second.split("-")[0]) and int(first.split("-")[1]) >= int(second.split("-")[1]): add+=1
        elif int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[1]) <= int(second.split("-")[1]): add+=1
    return add

def stape2():
    add = 0
    for ligne in range(len(file)):
        first = file[ligne].split(",")[0]
        second = file[ligne].split(",")[1]
        if int(first.split("-")[0]) <= int(second.split("-")[0]) and int(first.split("-")[1]) >= int(second.split("-")[0]): add+=1
        elif int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[0]) <= int(second.split("-")[1]): add+=1
        elif int(first.split("-")[0]) <= int(second.split("-")[0]) and int(first.split("-")[1]) >= int(second.split("-")[1]): add+=1
        elif int(first.split("-")[0]) >= int(second.split("-")[0]) and int(first.split("-")[1]) <= int(second.split("-")[1]): add+=1
    return add
