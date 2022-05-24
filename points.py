import datetime as dt
import sys
FI = (5 ** 0.5 - 1) / 2


def calculate(a, d1, b, d2):
    delta = dt.timedelta(abs((d2 - d1).days))
    sp = [0, 0, 0, 0]
    sp[a - 1] = d1
    sp[b - 1] = d2
    if a == 1 and b == 2:
        d = dt.timedelta(round(FI * delta.days))
        sp[3] = sp[0] + d
        sp[2] = sp[1] - d
    elif a == 1 and b == 3:
        d = dt.timedelta(round(delta.days / (1 - FI)))
        sp[1] = sp[0] + d
        sp[3] = sp[1] - delta
    elif a == 1 and b == 4:
        d = dt.timedelta(round(delta.days / FI))
        sp[1] = sp[0] + d
        sp[2] = sp[1] - delta
    elif a == 2 and b == 3:
        d = dt.timedelta(round(delta.days / FI))
        sp[0] = sp[1] - d
        sp[3] = sp[0] + delta
    elif a == 2 and b == 4:
        d = dt.timedelta(round(delta.days / (1 - FI)))
        sp[0] = sp[1] - d
        sp[2] = sp[0] + delta
    elif a == 3 and b == 4:
        d = dt.timedelta(round(delta.days * (1 - FI) / (2 * FI - 1)))
        sp[0] = sp[2] - d
        sp[1] = sp[3] + d
    return sp


def check(d, m, y):
    if y == '' or not (y.isdigit() or (y[0] == '-' and y[1:].isdigit())):
        return -1
    y = int(y)
    if (d == 31 and m in [2, 4, 6, 9, 11]) or (d == 30 and m == 2):
        return -1
    if m == 2 and d == 29 and not ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        return -1
    return 0

def age(d1, d2):
    m = (d2.year - d1.year) * 12 + (d2.month - d1.month)
    
    d = d2.day - d1.day
    if d < 0 and d1.month == 12:
        d += 31
        m -= 1
    elif d < 0:
        d += (dt.date(d1.year, d1.month + 1, 1) - dt.date(d1.year, d1.month, 1)).days
        m -=1
    y = m // 12
    m = m % 12
    
    return (d, m, y)
