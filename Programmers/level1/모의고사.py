# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    try_answers = ['12345', '21232425', '3311224455']
    try_len = [len(try_answers[0]), len(try_answers[1]), len(try_answers[2])]
    score = [0, 0, 0]

    for i, ans in enumerate(answers):
        for j, try_ans in enumerate(try_answers):
            if int(try_answers[j][i%try_len[j]]) == ans:
                score[j] += 1

    max_score = max(score)
    for i, s in enumerate(score):
        if s == max_score:
            answer.append(i+1)

    return answer


a = [1,2,3,4,5]
print(solution(a))