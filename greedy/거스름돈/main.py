"""
- Time complexity
  - 화폐의 종류 n이면, 시간 복잡도 O(n)
  - 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받음
"""

n = 1260
count = 0

# 큰 단위부터 계산하기 위해, 내림차순 coin 리스트 생성
descending_coins = [500, 100, 50, 10]

for coin in descending_coins:
    count += n // coin
    n %= coin

print(count)
