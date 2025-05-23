numbers=[]
for n in range(5):
    num=int(input())
    numbers.append(num)

numbers.sort()
avg=(sum(numbers)/5)

avg=int(avg)

print(avg)
print(numbers[2])