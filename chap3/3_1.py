"""
n = 1260
count = 0
coin_list = [500, 100, 50, 10] # 동전의 종류

for coin in coin_list:
  count = n // coin  # 각 동전에 따른 소모 개수
  n %= count  # 거슬러주고 남는 금액 저장

print(count)
"""

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_list = [500, 100, 50, 10]
for coin in coin_list:
  count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin

print(count)