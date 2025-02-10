numbers=[]
b=0
for i in range(10):
    a=int(input())
    b=a%42
    numbers.append(b)

numbers.sort()

b=1
for o in range(9):
    numbers.sort()
    if numbers[o]!=numbers[o+1]:
        b+=1

print(b)