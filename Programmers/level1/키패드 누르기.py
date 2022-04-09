# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''

    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    cur_L = '*'
    cur_R = '#'
    for i, target in enumerate(numbers):
        if target in [1, 4 ,7]: #L
            answer += 'L'
            cur_L = target
        elif target in [3, 6, 9]: #R
            answer += 'R'
            cur_R = target
        else: #N
            for x, l1 in enumerate(m):
                for y, val in enumerate(l1):
                    if target == val:
                        target_xy = (x, y)
                    if cur_L == val:
                        L_xy = (x, y)
                    if cur_R == val:
                        R_xy = (x, y)
            dist_L = abs(L_xy[0] - target_xy[0]) + abs(L_xy[1] - target_xy[1])
            dist_R = abs(R_xy[0] - target_xy[0]) + abs(R_xy[1] - target_xy[1])

            if dist_L == dist_R:
                answer += 'L'if hand == 'left' else 'R'
            else:
                answer += 'L' if dist_L < dist_R else 'R'

            if answer[-1] == 'L':
                cur_L = target
            else:
                cur_R = target
    return answer

n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = 'right'
print(solution(n,h))