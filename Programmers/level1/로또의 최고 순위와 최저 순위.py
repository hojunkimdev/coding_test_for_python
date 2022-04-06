# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    corrects = 0
    zero_cnt = lottos.count(0)

    for num in win_nums:
        if num in lottos:
            corrects += 1

    best = corrects + zero_cnt
    worst = corrects

    answer.append(rank[best])
    answer.append(rank[worst])

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
