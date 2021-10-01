# stones 배열의 크기는 1 이상 200,000 이하
# 완전 탐색으로 풀기엔 너무 크다

# 이진 탐색으로 풀자!
def binary_search(stones, k, niniz):
    
    # 먼저 0이 적힌 돌이 연속되는 횟수를 담을 변수
    continuity = 0
    
    # stones 배열을 돌 동안
    for stone in stones:
        # stone에 적힌 수가 강을 건널 니니즈의 수보다 작으면
        # 그 돌은 0이 된다
        if (stone < niniz):
            continuity += 1
            
        else:
            # 그렇지 않으면 continuity를 초기화시킨다
            continuity = 0
            
        # 돌 하나를 지날때마다 continuity를 검사해 
        # continuity의 값이 k 이상일 경우 실패
        if (continuity >= k):
            return False
        
    return True

def solution(stones, k):
    
    # 이 코드 없으면 첫번째 테스트케이스 오류
    # k=1인 경우 예외처리
    if (k==1):
        return min(stones)
    
    # left, right 변수
    # 돌에 적힌 숫자의 최소값 = 1
    left = 1
    right = max(stones)
    
    # 이진 탐색을 쓸 땐
    # left와 right의 차이가 1인 경우 탐색을 종료하는 코드를 작성한다
    while(left < right-1):
        
        # mid 값 계속 업데이트 돼야하므로 여기에 위치!
        mid = (left+right) // 2
        
        if (binary_search(stones, k, mid)):
            # True일 경우
            # mid명이 건널 수 있는 거 확인했으므로 그 이상도 찾기
            left = mid
            
        else:
            # False일 경우
            # mid명이 건널 수 없으므로 그 미만 찾기
            right = mid
    
    return left
