a, b, v= map(int, input().split())

if a >= v:
    print(1)
else:
    d= (v-b-1)//(a-b)+1
    print(d)