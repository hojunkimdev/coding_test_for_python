
num_strings = input()

result = int(num_strings[0])

for i in range(1, len(num_strings)):
    # 두 수 중에서 하나라도 0 or 1이면, 곱하기가 아닌 더하기 수행
    num = num_strings[i]
    if num <= 1 or result<= 1:
        result += num
    else:
        result *= num

print(result)
