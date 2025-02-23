a=int(input())

b=1
c=2*a-2
for i in range(a):
    print(' '*(a-b)+'*'*(2*a-1-c))
    b+=1
    c=c-2


d=a-1
e=1
for o in range(a-1):
    print(' '*(a-d)+'*'*(2*a-2-e))
    d-=1
    e=e+2