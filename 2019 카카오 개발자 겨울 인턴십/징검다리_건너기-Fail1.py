def solution(stones, k):
    answer = 0
    
    # 디딤돌의 숫자는 한 번 밟을 때 마다 1씩 줄어듦
    # 0이 되면 더이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러칸을 건너 뛸 수 있음
    # 다음으로 밟을 수 있는 디딤돌 여러개 경우 가장 가까운 디딤돌로만

    # stones : 디딤돌 적힌 숫자 순서대로 담긴 배열 
    # k : 최대로 뛸 수 있는 거리
    # answer : 최대 몇 명
    
    n = len(stones)
    
    # 반복문 멈출 변수
    breaker = 0
    
    # 연속된 0 돌의 개수 변수
    continuity = 0
    
    while (breaker == 0):
        
        answer +=1
        for i in range(n):
            if (stones[i] == 0):
                continuity +=1
                if (continuity == k):
                    breaker = 1
                    answer -=1
                    continuity = 0
                
            else:
                stones[i] -= 1
                continuity = 0
        
    
    return answer
