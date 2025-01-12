tp=int(input())

n=int(input())

c=0

for i in range(n):
    a, b = map(int, input().split())
    d=a*b
    c=c+d

if tp==c:
    print('Yes')

else:
    print('No')