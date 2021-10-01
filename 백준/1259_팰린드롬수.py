# 백준은 솔루션 코드가 따로 주어지지 않는다...
# input은 string 형태로 주어지는 듯하다
# while문 안에 i = input() 형식으로 넣으면
# 순서대로 첫번째, 두번째, ... 원소가 들어가면서 반복한다

while True:
    i = input()
    
    if (i=="0"):
        break
        
    # 파이썬의 slice 함수를 이용해 str[::-1]을 하면 문자열을 거꾸로!
    if (i == i[::-1]):
        print("yes")
    else:
        print("no")
