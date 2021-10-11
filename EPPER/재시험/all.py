# 거스름돈 계산하기
product = int(input("물건 값 : "))
user_input = int(input("받은 돈 : "))

answer = user_input - product
print("오천원권 : ", answer//5000)
answer %= 5000
print("천원권 : ", answer//1000)
answer %= 1000
print("오백원 : ", answer//500)
answer %= 500
print("백원 : ", answer//100)
answer %= 100
print("오십원 : ", answer//50)
answer %= 50
print("남은 거스름돈 : ", answer)

# 맞아라 OX
user_input = input("입력 : ")
answer = 0
continuity = 0

for i in user_input:
    if i=="O":
        continuity += 1
    else:
        continuity = 0
    answer += continuity

print(answer)

# 팰린드롬수
while True:
    user_input = input("입력: ")

    if user_input == "0":
        break

    if user_input == user_input[::-1]:
        print("yes")
    else:
        print("no")

# 문자열압축
user_input = input("입력 : ")
answer = ""
continuity = 0

if user_input[0] == "1":
    answer += "1"

for i in range(1, len(user_input)):
    if user_input[i-1] == user_input[i]:
        continuity += 1
    else:
        answer += chr(ord("A") + continuity)
        continuity = 0
    if i == len(user_input)-1:
        answer += chr(ord("A") + continuity)

print(answer)
