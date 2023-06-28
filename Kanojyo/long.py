def yes_no():
    yes = 0
    no = 0

    for _ in range(5):
        answer = input().split()

        for i in answer:
            if i == 'yes':
                yes += 1
            elif i == 'no':
                no += 1

    if yes > no:
        return 'yes'
    else:
        return 'no'


result = yes_no()
print(result)
