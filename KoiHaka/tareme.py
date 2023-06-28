def movie(s, n):
    if s >= n or s == n:
        return "OK"
    else:
        return "NG"


s, n = map(int, input().split())
print(movie(s, n))
