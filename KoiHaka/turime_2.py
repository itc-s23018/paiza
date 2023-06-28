def point(p):
    point = p // 100
    bonus = 0

    if p > 1000:
        bonus = 10

    return point + bonus


p = int(input())
result = point(p)
print(result)
