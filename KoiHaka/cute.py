def ok_ng(n, m):
    if m % n == 0:
        return 'ok'
    else:
        return 'ng'


n, m = map(int, input().split())
result = ok_ng(n, m)
print(result)
