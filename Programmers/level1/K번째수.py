# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2] - 1], commands))

a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a, c))