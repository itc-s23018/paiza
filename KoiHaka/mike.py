def weeks(n, m):
    events = n * 2
    weeks = m // events
    if m % events != 0:
        weeks += 1

    return weeks


[n, m] = [int(input()) for _ in range(2)]
result = weeks(n, m)
print(result)
