def day5():

    print("DAY 05")

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = ["a", "e", "i", "o", "u"]
    naughty = ["ab", "cd", "pq", "xy"]
    doubles = [c+c for c in alphabet]

    file = open("day05/input.txt", "r")
    lines = file.readlines()
    file.close

    good = 0

    for line in lines:

        vowelcount = 0
        doublecount = 0
        naughtyList = False

        for n in naughty:
            if (n in line):
                naughtyList = True
                break
        
        if (naughtyList):
            continue #no need to continue with this line

        for v in vowels:
            vowelcount += line.count(v)
        
        if(vowelcount < 3):
            continue # no need to continue with this line
        
        for d in doubles:
            if (d in line):
                doublecount+=1
        
        if(doublecount < 1):
            continue # no need to continue with this line

        good += 1
    
    print("Number of good children : ", good)