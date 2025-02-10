task = []
no_task = []
for i in range(28):
    a = int(input())
    task.append(a)

for o in range(1,31):
    a=task.count(o)
    if a==0:
        no_task.append(o)

no_task.sort()

print(no_task[0])
print(no_task[1])