import sys

vowels = set("aeiouAEIOU")
for line in sys.stdin:
    if line.rstrip() == "#":
        break
    cnt = sum(ch in vowels for ch in line)
    print(cnt)