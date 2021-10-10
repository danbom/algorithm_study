# 2차배열 회전!
# ⚪⚪⚫⚪⚪⚪⚪⚪⚫⚪⚪
# ⚪⚫⚪⚫⚪⚪⚪⚫⚪⚫⚪
# ⚫⚪⚪⚪⚫⚪⚫⚪⚪⚪⚫
# ⚫⚪⚪⚪⚪⚫⚪⚪⚪⚪⚫
# ⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫
# ⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫
# ⚪⚫⚪⚪⚪⚪⚪⚪⚪⚫⚪
# ⚪⚪⚫⚪⚪⚪⚪⚪⚫⚪⚪
# ⚪⚪⚪⚫⚪⚪⚪⚫⚪⚪⚪
# ⚪⚪⚪⚪⚫⚪⚫⚪⚪⚪⚪
# ⚪⚪⚪⚪⚪⚫⚪⚪⚪⚪⚪

heart = [
[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

def rotate90(heart):
    new_heart = [[0 for i in range(11)] for i in range(11)]
    for i in range(len(heart)):
        for j in range(len(heart)):
            new_heart[i][j] = heart[10-j][i]

    return new_heart

def print_heart(arr):
    n = 0
    string = ""
    for i in range(len(arr)):
        if arr[i] == 0:
            string += "⚪"
        else:
            string += "⚫"
            n += 1

    print(string)
    return n

total_n = 0

for i in range(len(heart)):
    total_n += print_heart(heart[i])

print(total_n)

total_n = 0

heart = rotate90(heart)

for i in range(len(heart)):
    total_n += print_heart(heart[i])

print(total_n)

total_n = 0

heart = rotate90(heart)

for i in range(len(heart)):
    total_n += print_heart(heart[i])

print(total_n)

total_n = 0

heart = rotate90(heart)

for i in range(len(heart)):
    total_n += print_heart(heart[i])

print(total_n)
