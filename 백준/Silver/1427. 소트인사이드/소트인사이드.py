import sys
input=sys.stdin.readline

numbers=input()

list(numbers)

numbers=sorted(numbers)
numbers=reversed(numbers)
numbers=''.join(numbers)

print(numbers)