
n = input()
plans = input.split()
x, y = 1, 1
move_types = ['L', 'R', 'U', 'D']
# 이동 방향에 대한 x, y 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(move_types):
        if plan[i] == move_types[i]:
            nx = x + dx
            ny = y + dy
            break

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > y:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)

