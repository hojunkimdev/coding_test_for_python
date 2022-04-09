def solution(record):
    answer = []

    recent_id2name = {}
    actions = []
    ids = []

    for i, v in enumerate(record):
        r = v.split()
        actions.append(r[0])
        ids.append(r[1])
        if r[0] in ['Enter', 'Change']:
            recent_id2name[r[1]] = r[2]

    for i, action in enumerate(actions):
        if action == 'Enter':
            answer.append(f'{recent_id2name[ids[i]]}님이 들어왔습니다.')
        elif action =='Leave':
            answer.append(f'{recent_id2name[ids[i]]}님이 나갔습니다.')

    return answer

r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))
