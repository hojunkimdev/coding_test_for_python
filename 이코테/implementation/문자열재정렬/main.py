
input = input()

alpha_list = []
sum_of_nums = 0
output = ''

for c in input:
    if c.isalpha():
        alpha_list.append(c)
    else:
        sum_of_nums += int(c)

alpha_list.sort()
output = ''.join(alpha_list)
if sum_of_nums != 0:
    output += str(sum_of_nums)

print(output)
