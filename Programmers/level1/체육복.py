# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost_new = list(set(lost) - set(reserve))
    reserve_new = list(set(reserve)-set(lost))
    answer = n - len(lost_new)
    for i in lost_new:
        if i-1 in reserve_new:
            answer += 1
            reserve_new.pop(reserve_new.index(i-1))
        elif i+1 in reserve_new:
            answer += 1
            reserve_new.pop(reserve_new.index(i+1))

    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(5, [2,3, 4], [1,3,5]))
print(solution(3, [3], [1]))
