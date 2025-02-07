a, b = map(int, input().split())

baguni=[0]*a


for m in range(b):
    c, d, e = map(int, input().split())
    for n in range(c-1,d):
        baguni[n]=e

print(*baguni)