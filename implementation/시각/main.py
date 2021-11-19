
hour = int(input())
count = 0

for hour in range(hour + 1):
    for min in range(60):
        for sec in range(60):
            if '3' in f"{hour}{min}{sec}":
                count += 1
print(count)
