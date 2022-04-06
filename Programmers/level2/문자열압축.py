# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = []
    batch_size = 1

    while batch_size <= len(s):
        slices = []
        for batch_i in range(0, len(s), batch_size):
            batch_str = s[batch_i: batch_i + batch_size]
            slices.append(batch_str)

        zip_s = ""
        while slices:
            pop_list = []
            cur_pop = slices.pop(0)
            pop_list.append(cur_pop)
            while slices and (cur_pop == slices[0]):
                cur_pop = slices.pop(0)
                pop_list.append(cur_pop)

            if len(pop_list) >= 2:
                zip_s += f"{len(pop_list)}{pop_list[0]}"
            else:
                zip_s += pop_list[0]

        answer.append(len(zip_s))
        batch_size += 1

    return min(answer)

s = "aabbaccc"
print(f"{s} - {solution(s)}")
s = "ababcdcdababcdcd"
print(f"{s} - {solution(s)}")
s = "abcabcdede"
print(f"{s} - {solution(s)}")
s = "abcabcabcabcdededededede"
print(f"{s} - {solution(s)}")
s = "xababcdcdababcdcd"
print(f"{s} - {solution(s)}")
