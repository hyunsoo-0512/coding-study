t=int(input())
for i in range(t):
    c=int(input())
    for i in range(4):
        q=c//25
        q_r=c%25

        d=q_r//10
        d_r=q_r%10

        n=d_r//5

        p=d_r%5

    print(q,d,n,p)