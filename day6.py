
file = open('input.txt').readline()

def stapes(number):
    for i in range(len(file)-number+1):
        current = file[i:i+number]
        check = True
        for k in range(len(current)):
            for m in range(1,number):
                if current[k] == current[(k+m)%number]: check = False
        if check: return i+number

print(stapes(4 or 14))