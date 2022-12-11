
sum, X, i = 0, 1, 1
for ligne in open('input.txt').readlines():
    if ligne != "noop\n": X+=int(ligne.split()[1])
    i+=(1 if ligne == 'noop\n' else 2)
    if int((i-20)/40) == (i-20)/40 or (int((i-21)/40) == (i-21)/40 and ligne != 'noop\n'):  sum+=(X if i%2==0 else X-int(ligne.split()[1]))*(i if i%2==0 else i-1)

print(sum) 