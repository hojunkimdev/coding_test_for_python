# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()

    check = scoville[0]
    while check <= K:
        if len(scoville) <= 1:
            return -1
        mix_k = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix_k)
        answer += 1
        check = scoville[0]

    return answer

s = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(s, k))
