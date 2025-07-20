best, idx = 0, 0
for i in range(5):
    s = sum(map(int, input().split()))
    if s > best:
        best, idx = s, i + 1
print(idx, best)
