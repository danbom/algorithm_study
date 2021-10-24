# phone_book 의 길이가 1 이상 1,000,000 이하...
# 하나씩 비교는 무조건 시간초과 날 거 같은데


def solution(phone_book):
    
    # 문자열 sort 결과는 ASKII 코드 순
    phone_book = sorted(phone_book)
    
    # zip함수는 리스트끼리 짝지어주는 것
    for i, j in zip(phone_book, phone_book[1:]):
        # startswith 함수...
        if j.startswith(i):
            return False
    return True
