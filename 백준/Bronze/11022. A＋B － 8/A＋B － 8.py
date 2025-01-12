c=0
import sys
input = lambda: sys.stdin.readline().rstrip()

n=int(input())

for i in range(n):
    a, b = map(int, input().split())
    c=c+1
    print('Case #'+str(c)+':',a,'+',b,'=',a+b)