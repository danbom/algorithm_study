from itertools import permutations
# numbers는 길이 1 이상 7 이하인 문자열
# 먼저 한 자리 수 소수는 2,3,5,7 밖에 없으므로 조건문으로 걸러주자
# 두 자리 수 소수부턴 구하기 힘드니 for 문 돌려야할듯 오래걸릴거같은디..

# 중복 처리를 어떻게 하지

# 소수 판별 함수
def isPrime(num):
    
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    
    answer = 0
    length = len(numbers)
    prime = []
    
    # 한 자리수 소수 걸러주기
    if "2" in numbers:
        prime.append(2)
    if "3" in numbers:
        prime.append(3)
    if "5" in numbers:
        prime.append(5)
    if "7" in numbers:
        prime.append(7)
        
    if length>1:
        # 두 자리 소수
        two = list(permutations(numbers, 2))
        for i in two:
            if isPrime(int("".join(i))):
                prime.append(int("".join(i)))

    if length>2:
        # 세 자리 소수
        three = list(permutations(numbers, 3))
        for i in three:
            if isPrime(int("".join(i))):
                prime.append(int("".join(i)))
            
    if length>3:
        # 네 자리 소수
        four = list(permutations(numbers, 4))
        for i in four:
            if isPrime(int("".join(i))):
                prime.append(int("".join(i)))
            
    if length>4:
        # 다섯 자리 소수
        five = list(permutations(numbers, 5))
        for i in five:
            if isPrime(int("".join(i))):
                prime.append(int("".join(i)))
        
    if length>5:
        # 여섯 자리 소수
        six = list(permutations(numbers, 6))
        for i in six:
            if isPrime(int("".join(i))):
                prime.append(int("".join(i)))
            
    if length>6:
        # 일곱 자리 소수
        seven = list(permutations(numbers, 7))
        for i in seven:
            if isPrime(int("".join(i))):
                prime.append(int("".join(i)))
    
    return answer + len(sorted(set(prime)))
