A=input()
t=0
for a in A:
    if a in 'ABC':
        t=t+3
    elif a in 'DEF':
        t=t+4
    elif a in 'GHI':
        t=t+5
    elif a in 'JKL':
        t=t+6
    elif a in 'MNO':
        t=t+7
    elif a in 'PQRS':
        t=t+8
    elif a in 'TUV':
        t=t+9
    elif a in 'WXYZ':
        t=t+10  

print(t)