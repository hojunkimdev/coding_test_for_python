
input = input()

cur_x = ord(input[0]) - ord('a') + 1
cur_y = int(input[1])

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for dx, dy in steps:
    next_x = cur_x + dx
    next_y = cur_y + dy

    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        count += 1

print(count)
