gd = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

ts = 0.0  
tc = 0.0  

for i in range(20):
    a, c, g = input().split()
    c = float(c)

    if g == "P":  
        continue

    ts += c * gd[g]
    tc += c  

tt = ts / tc  
print("{0:.6f}".format(tt))