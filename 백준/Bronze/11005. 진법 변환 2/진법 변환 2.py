num, base=map(int, input().split())

import string

temp = string.digits+string.ascii_uppercase
def change(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return temp[r] 
    else :
        return change(q, base) + temp[r]

print(change(num,base))