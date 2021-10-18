def solution(participant, completion):
    # 헐... 개쉬운방법이 있었음 
    # 왜 까먹고있었지
    
    # 근데 효율성 통과 못함..
    # for _ in participant:
    #     if participant.count(_) != completion.count(_):
    #         return _
    #     if _ not in completion:
    #         return _
    
    # 배열 비교 (빼기)는 set() - set() 으로 가능!
    answer = list(set(participant) - set(completion))
    
    if len(answer) != 0 :
        return answer[0]
    else :
        for _ in participant:
            if participant.count(_) != 1:
                if participant.count(_) != completion.count(_):
                    return _
                
# 다른 사람 코드...? 겁나 간결하네
# 모듈을 공부하자...^^
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # collections.Counter(participant)를 하면 {"mislav":2,"stanko":1,"ana":1} 이런식으로 key값 : 개수
    # collections.Counter 끼리 뺄 수 있음
    # 뺐을 때 answer = {"mislav" : 1}
    # list(answer.keys()) = ["mislav"]
    return list(answer.keys())[0]
