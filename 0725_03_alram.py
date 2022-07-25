h = 22
m = 20

def alram(h, m):
    if m < 45:
        h -= 1
        m -= 45

    else :
        m -= 45

    return h, int(-m)

print(alram(h, m))
