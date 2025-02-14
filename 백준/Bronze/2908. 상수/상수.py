a, b = input(). split()

a=''.join(reversed(a))
b=''.join(reversed(b))

a=int(a)
b=int(b)

if a>b:
    print(a)
else:
    print(b)