a, b = map(int, input().split())

if a!=0 and b>=45:
    print(a,b-45)

elif a!=0 and b<=45:
    print(a-1,b+60-45)

elif a==0 and b>=45:
    print(a,b-45)

else:
    print(a+23, b+60-45)