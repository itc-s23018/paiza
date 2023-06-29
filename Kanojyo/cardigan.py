def multiplication(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


n = int(input())
result = multiplication(n)
print(result)
