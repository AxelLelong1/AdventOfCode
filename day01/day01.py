def day1():

    f = open("day01/input.txt", "r")

    output = 0
    line = f.readlines()
    f.close()

    for c in line[0]:
        if (c =='('):
            output+=1
        elif (c == ')'):
            output-=1

    print("DAY 01 : PART 1")
    print(output)

    output = 0
    index = 1

    for c in line[0]:
        if (c =='('):
            output+=1
        elif (c == ')'):
            output-=1
        if output == -1:
            break
        index+=1

    print("DAY 01 : PART 2")
    print(index)