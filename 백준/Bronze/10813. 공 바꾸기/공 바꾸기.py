a, b = map(int, input().split())
baguni=[]
for v in range(a):
    baguni.append(v+1)

for o in range(b):
    i, j = map(int, input().split())
    i1=baguni[i-1]
    j1=baguni[j-1]
    baguni[i-1]=j1
    baguni[j-1]=i1

print(*baguni)