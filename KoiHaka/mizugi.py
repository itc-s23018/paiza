def signs(n, m, s, t):
    return max(n - len(set(s) & set(t)), m - len(set(s) & set(t)))


n, m = map(int, input().split())
s = input().rstrip()
t = input().rstrip()

result = signs(n, m, s, t)
print(result)
