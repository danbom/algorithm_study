# 숫자가 크므로 이진탐색 이용하자

def binary_search(n, times, mid):
    # mid분 동안 검사할 수 있는 최대 사람 수 >= n 인지 검사
    
    # 전체 검사할 수 있는 사람 수 담을 변수
    p = 0
    
    # 각 검사관마다 mid분 동안 검사할 수 있는 사람 수 더하기
    for i in times:
        p += mid//i
        
    # mid분 동안 검사할 수 있는 사람의 최대 수가 n보다 크면
    # 통과 -> 더 작은 mid값을 구해야함
    # right = mid
    if p>=n:
        return True
    else:
        return False
    

def solution(n, times):
    left = 1
    right = max(times)*n
    
    while (left < right -1):
        
        mid = (left + right) // 2
        
        if binary_search(n, times, mid):
            right = mid
        else:
            left = mid
    
    # 최솟값 구할 땐 return right
    # 최댓값 구할 땐 return left
    return right
