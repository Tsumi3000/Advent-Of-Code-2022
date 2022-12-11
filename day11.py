

def stapes(stape):
    file = open("input.txt").readlines()
    monkeysItems = {}
    monkeysOP = {}
    monkeysTest = {}
    monkeysTrue = {}
    monkeysFalse = {}
    monkeysInspect = {i:0 for i in range(int(len(file)/7)+1)}

    for i in range(int(len(file)/7)+1):
        monkeysItems[i] = file[i*7+1].split(": ")[1][:-1].split(",")
        monkeysOP[i] = file[i*7+2].split("= old ")[1][:-1]
        monkeysTest[i] = file[i*7+3].split("by ")[1][:-1]
        monkeysTrue[i] = file[i*7+4].split("monkey ")[1][:-1]
        monkeysFalse[i] = file[i*7+5].split("monkey ")[1][:-1]

    modulo = 1
    for test in monkeysTest.values(): modulo*=int(test)

    for _ in range((10000 if stape == 2 else 20)):
        for monkey in monkeysItems.keys():
            for _ in range(len(monkeysItems[monkey])):
                monkeysInspect[monkey]+=1
                op = (monkeysOP[monkey] if monkeysOP[monkey] != "* old" else  "**2")
                new = eval(str(monkeysItems[monkey][0]) + op)
                new = (str(int((new%modulo if stape == 2 else new/3))))
                if int(new)%int(monkeysTest[monkey]) == 0: monkeysItems[int(monkeysTrue[monkey])].append(new)
                else: monkeysItems[int(monkeysFalse[monkey])].append(new)
                monkeysItems[monkey].pop(0)

    return sorted(monkeysInspect.values())[-2:][0]*sorted(monkeysInspect.values())[-2:][1]

stapes(1 or 2)