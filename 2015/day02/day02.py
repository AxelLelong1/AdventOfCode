def day2():

    file = open("day02/input.txt", "r")
    lines = file.readlines()
    file.close()

    print("DAY 02 : PART 1 AND 2")

    PresentPaper = 0
    RibbonPaper = 0

    for line in lines:
        numbers = line.split('x') # Split the equation a x b x c


        sideone =  (int)(numbers[0]) * (int)(numbers[1])
        sidetwo =  (int)(numbers[1]) * (int)(numbers[2])
        sidethree =  (int)(numbers[2]) * (int)(numbers[0])

        smallest = sideone

        if (sidetwo < smallest):
            smallest = sidetwo
            
        if(sidethree < smallest):
            smallest = sidethree
            

        ribbonAround = 2 * min((int)(numbers[0]) + (int)(numbers[1]), (int)(numbers[1]) + (int)(numbers[2]), (int)(numbers[0]) + (int)(numbers[2]))

        ribbonBow = (int)(numbers[0]) * (int)(numbers[1]) * (int)(numbers[2])

        PresentPaper+= sidethree * 2 + sidetwo * 2 + sideone * 2
        PresentPaper+=smallest # add leftover

        RibbonPaper += ribbonAround + ribbonBow

    print("Wrapping paper needed : ", PresentPaper)
    print("Ribbon paper needed : ", RibbonPaper)