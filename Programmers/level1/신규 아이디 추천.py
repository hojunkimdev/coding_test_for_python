# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    special_chr = '-_.'

    lower_id = new_id.lower()
    for i, c in enumerate(lower_id):
        if c.isalnum() or c in special_chr:
            answer += c

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.' or answer[-1] == '.':
        answer = answer.strip('.')

    if answer == "":
        return 'a' * 3

    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer.rstrip('.')
    if len(answer) <= 2:
        answer = answer + (3-len(answer)) * answer[-1]

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
new_id = "z-+.^."
print(solution(new_id))
new_id = "=.="
print(solution(new_id))
new_id = "123_.def"
print(solution(new_id))
new_id = "abcdefghijklmn.p"
print(solution(new_id))
