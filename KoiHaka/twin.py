def bar(s, t):
    progress_bar = '-' * s
    progress_bar = progress_bar[:t-1] + '+' + progress_bar[t:]
    return progress_bar


s = int(input())
t = int(input())


result = bar(s, t)
print(result)
