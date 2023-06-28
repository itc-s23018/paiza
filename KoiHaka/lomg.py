def luck(N):
    if N % 7 == 0:
        return "lucky"
    else:
        return "unlucky"


N = int(input())
print(luck(N))
