h = 22
m = 55

def alram(h, m):
    if m < 45:
        h -= 1
        m -= 45

    else :
        m -= 45

    if m < 0:
        m = -m

    return h, int(m)

print(alram(h, m))
