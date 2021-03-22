# N, M, K를 공백으로 구분하여 입력받기
# input() 함수는 한 줄의 문자열을 입력 받는 함수다
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용함
# ex) map(int, input().split())
# 이 경우에는 문제에서 특정 N, M, K를 지정하였기 때문에
# or 공백을 기준으로 구분된 데이터의 개수가 많지 않다면
# -> 각각 지정해서 사용
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
# 개수가 많으므로 배열로 받아서 사용
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기 (디폴트는 오름차순)
first = data[n - 1] # 정렬한 수 중에 가장 큰 수
second = data[n - 2] # 정렬한 수 중에 두 번째로 큰 수

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 m - 1 수행
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 m - 1 수행

print(result)