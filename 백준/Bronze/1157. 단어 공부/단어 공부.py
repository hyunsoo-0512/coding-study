a = input().upper()
b = [0] * 26

for c in a:
    d = ord(c) - ord('A')
    b[d] += 1

e = max(b)
f = b.count(e)

if f > 1:
    print('?')
else:
    print(chr(b.index(e) + ord('A')))