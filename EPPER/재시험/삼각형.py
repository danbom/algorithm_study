def wow(n):
    string = ""
    for i in range(n+1):
        string += str(i) + " "
    return string

def star1(n):
    string = ""
    for i in range(n+1):
        string += "☆"
    return string
    
def star2(n):
    string = ""
    for i in range(n+1):
        string += "★"
    return string

user_input = input("삼각형의 높이를 입력하세요 : ")

for i in range(int(user_input)):
    if (i%2 == 0):
        print(str(i) + " : " + star1(i))
    else:
        print(str(i) + " : " + star2(i))

for i in range(int(user_input)):
    if (i%2 == 0):
        print(str(i) + " : " + " "*(int(user_input)-i) + star1(i))
    else:
        print(str(i) + " : " + " "*(int(user_input)-i) + star2(i))

for i in range(int(user_input)):
    if (i%2 == 0):
        print(str(i) + " : " + " "*((int(user_input)-i)//2) + star1(i))
    else:
        print(str(i) + " : " + " "*((int(user_input)-i)//2) + star2(i))
