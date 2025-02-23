a = input().strip()
b = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
count = 0

for cro in b:
    while cro in a:
        count += 1
        a = a.replace(cro, " ", 1) 

count += len(a.replace(" ", "")) 

print(count)