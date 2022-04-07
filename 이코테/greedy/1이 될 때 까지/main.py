"""
- Time complexity
  - O(logn)
"""

# n, k = list(map(int, input.split()))
n, k = 14, 3
count = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    count += (n - target)  # 1을 뺀 횟수 카운팅
    n = target  # 1씩 뺸 후, k로 나눌 수 있는 상태

    if n < k:
        break

    n //= k
    count += 1

count += (n - 1)
print(count)
