def countdown(n):
    result = []
    while n >= 0:
        if n == 0:
            result.append('0!!')
        else:
            result.append(str(n))
        n -= 1
    return result


n = int(input())
result = countdown(n)
for i in result:
    print(i)
