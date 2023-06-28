def amount(n, p, m, q):
    paper = p * n
    pen = q * ((n + m - 1) // m)
    return paper + pen


[[n, p], [m, q]] = [map(int, input().split()) for _ in range(2)]

result = amount(n, p, m, q)
print(result)
