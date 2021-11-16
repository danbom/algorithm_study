def solution(scoville, K):
    
    mix_time = 0
    
    scoville.sort()
    
    while (scoville[0] < K):
        if len(scoville) < 2:
            return -1
        else:
            scoville.append(scoville[0]+2*scoville[1])
            scoville.remove(scoville[0])
            scoville.remove(scoville[0])
            scoville.sort()
            mix_time += 1
    
    return mix_time
