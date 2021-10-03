def solution(absolutes, signs):
    answer = 0
    j=0
    
    for i in absolutes:
        if signs[j]==True:
            answer += i
        else:
            answer -= i
        j +=1
    
    return answer
