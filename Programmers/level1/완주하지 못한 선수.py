import collections

# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    p_cnt = collections.Counter(participant)
    c_cnt = collections.Counter(completion)

    for p_name, p_cnt in p_cnt.items():
        if p_cnt - c_cnt[p_name] != 0:
            return p_name

p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
print(solution(p, c))