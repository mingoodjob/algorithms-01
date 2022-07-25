a = 472
b = 385

b_reverse = str(b)[::-1]

def mul(a, b):
    b_reverse = str(b)[::-1]
    for i in b_reverse:
        print(int(i) * a)
    print(a*b)


mul(a,b)