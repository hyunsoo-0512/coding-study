a=input().strip()
b=['dz=','c=','c-','d-','lj','nj','s=','z=']
e=0


for i in b:
  while i in a:
    e += 1
    a= a.replace(i, ' ', 1)
  
e += len(a.replace(' ', ''))
print(e)