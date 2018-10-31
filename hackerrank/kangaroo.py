def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 >= v1:
        return "NO"

    return "YES" if (x1 - x2) % (v2 - v1) == 0 else "NO"


