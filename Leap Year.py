case = int(input())

for i in range(case):
    line = int(line[0])

    if (line % 400 == 0) and (line % 100 == 0):
        print("is a leap year")

    elif (line % 4 ==0) and (line % 100 != 0):
        print("is a leap year")

  
    else:
        print("is not a leap year")

