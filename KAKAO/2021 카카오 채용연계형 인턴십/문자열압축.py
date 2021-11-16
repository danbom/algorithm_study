def check(temp):
    continuity = 1
    letter = ""
    
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            continuity += 1
        else :
            if continuity != 1:
                letter += str(continuity)
                continuity = 1
            letter += temp[i]
    
    if continuity != 1:
        letter += str(continuity)
    letter += temp[-1]
    
    return len(letter)

def solution(s):
    answer = []
    
    for unit in range(1,len(s)//2+1):
        temp = [s[i:i+unit] for i in range(0, len(s), unit)]
        answer.append(check(temp))
        
    if len(s) == 1:
        return 1
    else:
        return min(answer)
