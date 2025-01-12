a, b= map(int, input().split())
c=int(input())

tm=b+c
nh=a+tm//60
nm=tm%60

if nh>24:
    nh=nh-24
elif nh==24:
    nh=0
print(nh,nm)