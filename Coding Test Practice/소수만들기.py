# 배열에서 3개를 더해서 소수를 만들어야한다
# 고냥 모든 경우의 수 구하기.. 였네

# 저번 itertools의 permutations는 순열, combinations는 조합
from itertools import combinations

# 소수인지 확인하는 함수
def prime(num):
    for i in range(2,num):
        # 나눠지는 수가 있으면 소수가 아니므로 바로 0 리턴
        if num%i == 0:
            return 0
    # 나눠지는 수가 없으면 소수이므로 1 리턴
    return 1
    

def solution(nums):
    answer = 0
    # 입력 배열 숫자들 세개로 이루어진 조합 생성
    num = list(combinations(nums, 3))
    for i in num:
        # 조합의 원소들의 합을 prime 함수에 넣어 소수인지 확인
        _sum = sum(i)
        answer += prime(_sum)

    return answer
