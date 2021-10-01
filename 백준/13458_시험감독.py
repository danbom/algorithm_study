# n : 시험장 개수
# a : 각 시험장 별 응시자 수 배열
# b, c : 총감독이 감독 가능한 응시자 수 / 부감독이 감독 가능한 응시자 수


def solution():
  # 먼저 시험장 개수만큼 총감독 넣어놓고 시작
    answer = n
    for i in a:
        # 응시자 수가 총감독이 감독 가능한 응시자 수보다 적을 때는 
        # 총감독 한명으로 충분하기 때문에 아무것도 안하기
        if (i >= b):
            answer += (i-b)//c
            if ((i-b)%c != 0):
                answer += 1
        

    return answer

n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())
print(solution())
