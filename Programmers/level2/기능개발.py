# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []

    q = deque(list(range(len(progresses))))

    recent_success_days = 0
    while q:
        i = q.popleft()

        result = divmod((100-progresses[i]), speeds[i])
        day = result[0]
        if result[1] != 0:
            day += 1
        if day <= recent_success_days:
            answer[-1] += 1
            continue
        recent_success_days = day
        answer.append(1)

    return answer

p = [93, 30, 55]
s = [1, 30, 5]
print(solution(p, s))

p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
print(solution(p, s))