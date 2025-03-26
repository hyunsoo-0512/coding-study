x=int(input())
k=0
while (k*(k+1))//2<x:
    k+=1
k-=1  

pos=x-(k*(k+1))//2

if (k+1)%2==0:
    분자=pos
    분모=k+2-pos
else:
    분자=k+2-pos
    분모=pos

print(f"{분자}/{분모}")