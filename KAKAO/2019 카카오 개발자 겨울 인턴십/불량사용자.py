# permutations : 순열
# permutations('ABCD', 2) -> AB, AC, AD, BA, BC, BD ...
# permutations(range(3)) -> 012, 021, 102 ...

# list는 해시할 수 없습니다 에러 시
# list 대신 tuple 사용하기

# 배열에서 중복을 제거하기 위해선
# set 메서드를 활용해 집합으로 변경하기

from itertools import permutations

# user_id로 만든 순열이 banned_id에 해당되는지 체크하는 함수
def check(user_pi, banned_id):
    # ex.
    # user_pi : ["frodo","fradi"]
    # banned_id : ["fr*d*", "abc1**"]
    
    for i in range(len(user_pi)):
        # 길이 검사
        if len(user_pi[i]) != len(banned_id[i]) :
            return False
        
        # 길이 검사 통과 후
        for j in range(len(user_pi[i])):
            
            if banned_id[i][j] == "*":
                continue
            elif banned_id[i][j] != user_pi[i][j]:
                return False
        
    return True

def solution(user_id, banned_id):
    
    answer = []
    
    # user_id를 순열로 만들기
    user_p = list(permutations(user_id, len(banned_id)))
    
    for user_pi in user_p:
        # user_p가 banned_id에 해당되는지 체크
        if check(user_pi, banned_id):
            # True면 정답배열에 추가
            # set으로 정렬 후
            answer.append(tuple(set(user_pi)))
    
    return len(tuple(set(answer)))
