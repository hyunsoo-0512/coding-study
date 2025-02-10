n, m = map(int, input().split())
numbers=[i for i in range(1,n+1)]
p=0


for o in range(m):
    i, j = map(int, input().split())
    p=numbers[i-1:j]
    p.reverse()
    numbers[i-1:j]=p

print(*numbers)