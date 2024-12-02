def day1():

    # Open file
    f = open("day01/input.txt", "r")

    # init data
    lines = f.readlines()
    f.close()

    left, right = [], []

    # Collect data
    for line in lines:
        l,r = line.split()
        left.append(l)
        right.append(r)
    
    left.sort()
    right.sort()

    # Get distance for each couple
    distance = 0
    for i in range(len(left)):
        distance += abs(int(left[i]) - int(right[i]))
    
    # Get the similarity score for each left numbers (left * numberofappearces in right)
    simi = 0
    for i in range(len(left)):
        # Filter all the similar nuumbers we're looking for
        r = list(filter(lambda x: left[i] == x, right))
        simi += int(left[i]) * len(r)

    print("Distance Score == ", distance)
    print("Similaritude Score == ", simi)
    return (distance, simi)