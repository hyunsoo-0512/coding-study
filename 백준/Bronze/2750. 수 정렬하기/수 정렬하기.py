import sys

input=sys.stdin.readline

n=int(input())

numbers=[int(input()) for a in range(n)]

numbers.sort()

print('\n'.join(map(str, numbers)))