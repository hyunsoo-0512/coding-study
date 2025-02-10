n= int(input())
score = list(map(int, input().split()))

score.sort()
ts=0
for i in range(n):
    a=score[i]/score[-1]*100
    ts=ts+a

ts=ts/n

print(ts)