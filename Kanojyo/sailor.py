def n_str(word):
    return '_'.join(word)


n = int(input())
word_list = []
for i in range(n):
    word = input()
    word_list.append(word)


result = n_str(word_list)
print(result)
