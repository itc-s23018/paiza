def index_numbers(N, numbers):
    numbers.sort(reverse=True)

    index = (N + 1) // 2
    index_number = numbers[index - 1]

    return index_number


N = int(input())
numbers = list(map(int, input().split()))

result = index_numbers(N, numbers)
print(result)
