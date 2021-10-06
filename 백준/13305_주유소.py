#  최소 비용의 주유값으로 최대한 멀리 가는 것이 목적
# 상황별 최선의 선택을 하는 그리디 알고리즘 사용하기

# 그리디 알고리즘
# 어떤 문제에 대한 최적의 결과값을 찾기 위해 사용하는 메소드
# 순간의 최선의 선택을 하기 때문에
# 항상 최적의 결과를 가져온다고 할 수는 없음

# 지금까지의 최소 주유값과 현도시 주유값을 비교했을 때
# 더 싼 주유값 x 다음 도시로 가는 거리
# 더해간다

def solution(cities, distance, price):
    cost = 0
    minimium = price[0]
    for i in range(cities-1):
        minimium = min(minimium, price[i])
        cost += minimium*distance[i]

    return cost

if __name__=='__main__':
    cities = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))
    print(solution(cities, distance, price))
