a='1'

while a!='0':
    a=input()
    b=a[::-1]
    if a=='0':
        break
    elif a==(b) and a!='0':
        print('yes')
    else:
        print('no')