a= list(map(int, input().split()))
b=[1, 1, 2, 2, 2, 8]
c=0
d=[]
for i in (a):
    if i!=b[c]:
        e=b[c]-i
        d.append(e)
        c=c+1
    else:
      d.append(0)
      c=c+1

print(*d)