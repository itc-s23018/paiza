def correct_answers():
    answers = []
    for i in range(5):
        answer = input().split()
        answers.append(answer)
    count = 0

    for answer in answers:
        shape = answer[0]
        given_answer = answer[1]

        if shape == given_answer:
            count += 1

    if count >= 3:
        return 'OK'
    else:
        return 'NG'


result = correct_answers()
print(result)

