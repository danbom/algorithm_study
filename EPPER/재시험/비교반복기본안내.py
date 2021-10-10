total_arr = []

for i in range(1,10):
    string = ""
    for j in range(1,10):
        string += str(i) + " * " + str(j) + " = " + str(i*j)
        string += "\t"
    total_arr.append(string)

for i in range(9):
    print(total_arr[i])

print("\n")

total_arr = []

for i in range(1,10):
    string = ""
    for j in range(1,10):
        string += str(j) + " * " + str(i) + " = " + str(i*j)
        string += "\t"
    total_arr.append(string)

for i in range(9):
    print(total_arr[i])

