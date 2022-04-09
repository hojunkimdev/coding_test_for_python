# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''

    n_dict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    temp = ''
    for c in s:
        if c.isdigit():
            answer += c
        else:
            temp += c
            if temp in n_dict.keys():
                answer += str(n_dict[temp])
                temp = ''

    return int(answer)

s = "one4seveneight"
print(solution(s))
s = "23four5six7"
print(solution(s))
s = "2three45sixseven"
print(solution(s))
s = "123"
print(solution(s))

