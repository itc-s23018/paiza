def steps(M, N):
    number_steps = M - N

    if number_steps <= 0:
        number_steps = 0

    return number_steps


M, N = map(int, input().split())
retult = steps(M, N)
print(retult)
