snacks = [sum([int(x) for x in group.split()]) for group in ''.join(open('input.txt').readlines()).split('\n\n')]
snacks.sort()
print(snacks[-1], sum(snacks[-3:]))
