def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    if is_prime(num):
        count += 1

print(count)