from itertools import combinations

def solution(numbers):
    _sum = list(combinations(numbers,2))
    answer = []
    for i in _sum:
        answer.append(sum(i))
    
    return list(sorted(set(answer)))
  
  # sorted()를 쓰지 않아 4,5번 테스트 케이스에서 헤맸다
  # Python의 set은 해시셋이기 때문에 정렬된 리스트가 나오는 것이 보장되지 않는다한다
  # 따라서 set()을 sorted로 감싸 정렬시켜줘야한다
