import sys

cnt = [0] * 26
for ch in sys.stdin.read():
    if 'a' <= ch <= 'z':
        cnt[ord(ch) - 97] += 1

m = max(cnt)
print(''.join(chr(i + 97) for i, v in enumerate(cnt) if v == m))
