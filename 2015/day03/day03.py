def day3():
    
    print("DAY 03")
    
    file = open("day03/input.txt", "r")
    line = file.readline()
    file.close()
    
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    santaRobot = False
    
    houses = {(x1,y1): 1}

    for c in line:

        if (not santaRobot):
            if (c == '^'):
                y1 += 1
            elif (c == 'v'):
                y1 -= 1
            elif (c == '<'):
                x1 -= 1
            elif (c == '>'):
                x1 += 1
    
        else:
            if (c == '^'):
                y2 += 1
            elif (c == 'v'):
                y2 -= 1
            elif (c == '<'):
                x2 -= 1
            elif (c == '>'):
                x2 += 1

        if (not santaRobot and (x1,y1) not in houses):
            houses[(x1,y1)] = 1
        if (santaRobot and (x2, y2) not in houses):
            houses[(x2, y2)] = 1
        
        santaRobot = not santaRobot

    print("House with at least one present", len(houses))