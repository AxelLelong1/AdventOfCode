word = 'XMAS'
mas = "MAS"

def try_right(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(X + 1 < len(data) and data[Y][X + 1] == word[letter + 1]):
        return try_right(data, X+1, Y, letter+1)
    return 0

def try_left(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(X - 1 >= 0 and data[Y][X - 1] == word[letter + 1]):
        return try_left(data, X-1, Y, letter+1)
    return 0

def try_up(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(Y - 1 >= 0 and data[Y - 1][X] == word[letter + 1]):
        return try_up(data, X, Y-1, letter+1)
    return 0

def try_down(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(Y + 1 < len(data) and data[Y + 1][X] == word[letter + 1]):
        return try_down(data, X, Y+1, letter+1)
    return 0

def try_DownRight(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(Y + 1 < len(data) and X + 1 < len(data) and data[Y + 1][X + 1] == word[letter + 1]):
        return try_DownRight(data, X + 1, Y+1, letter+1)
    return 0

def try_DownLeft(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(Y + 1 < len(data) and X - 1 >= 0 and data[Y + 1][X - 1] == word[letter + 1]):
        return try_DownLeft(data, X - 1, Y+1, letter+1)
    return 0

def try_UpRight(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(Y - 1 >= 0 and X +1 < len(data) and data[Y - 1][X + 1] == word[letter + 1]):
        return try_UpRight(data, X+1, Y-1, letter+1)
    return 0

def try_UpLeft(data, X, Y , letter):
    if(letter == 3):
        return 1
    elif(Y - 1 >= 0 and X - 1 >= 0 and data[Y - 1][X - 1] == word[letter + 1]):
        return try_UpLeft(data, X - 1, Y-1, letter+1)
    return 0

def CrossMas(data, X, Y, letter):
    return 1

def day4():
    with open("day04/input.txt") as file:
        data = file.readlines()

    XMAS = 0
    MAS = 0
    positionY = 0
    size = len(data)
    for positionY in range(size):
        positionX = 0
        for positionX in range(size):
            # print(positionX, positionY)
            if (data[positionY][positionX] == 'X'):
                XMAS += try_left(data, positionX, positionY, 0) + try_right(data, positionX, positionY, 0)
                XMAS += try_up(data, positionX, positionY, 0) + try_down(data, positionX, positionY, 0)
                XMAS += try_UpRight(data, positionX, positionY, 0) + try_UpLeft(data, positionX, positionY, 0)
                XMAS += try_DownRight(data, positionX, positionY, 0) + try_DownLeft(data, positionX, positionY, 0)

            if (data[positionY][positionX] == 'A'):
                MAS += CrossMas(data, positionX, positionX, 1)

    print(XMAS, MAS)
    return (XMAS, MAS)

day4()