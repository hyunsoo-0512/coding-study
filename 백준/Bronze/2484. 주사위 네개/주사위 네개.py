import sys

N = int(sys.stdin.readline())
max_prize = 0

for i in range(N):
    dice = list(map(int, sys.stdin.readline().split()))
    cnt = {}
    for d in dice:
        cnt[d] = cnt.get(d, 0) + 1

    if 4 in cnt.values():
        eye = next(k for k, v in cnt.items() if v == 4)
        prize = 50000 + eye * 5000
    elif 3 in cnt.values():
        eye = next(k for k, v in cnt.items() if v == 3)
        prize = 10000 + eye * 1000
    elif list(cnt.values()).count(2) == 2:
        pair_eyes = [k for k, v in cnt.items() if v == 2]
        prize = 2000 + sum(e * 500 for e in pair_eyes)
    elif 2 in cnt.values():
        eye = next(k for k, v in cnt.items() if v == 2)
        prize = 1000 + eye * 100
    else:
        prize = max(dice) * 100

    if prize > max_prize:
        max_prize = prize

print(max_prize)
