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

def get_upper_left(data, x, y):
    if x - 1 >= 0 and y - 1 >= 0:
        return data[y - 1][x - 1]
    return '0'


def get_upper_right(data, x, y):
    if x + 1 < len(data) and y - 1 >= 0:
        return data[y - 1][x + 1]
    return '0'


def get_bottom_right(data, x, y):
    if x + 1 < len(data) and y + 1 < len(data):
        return data[y + 1][x + 1]
    return '0'


def get_bottom_left(data, x, y):
    if x - 1 >= 0 and y + 1 < len(data):
        return data[y + 1][x - 1]
    return '0'


def is_xmas(data, x, y):
    """Check if there is an X-MAS pattern centered at (x, y)."""
    # Check the diagonals from the center point (x, y)
    ul = get_upper_left(data, x, y)  # Upper-left
    ur = get_upper_right(data, x, y)  # Upper-right
    bl = get_bottom_left(data, x, y)  # Bottom-left
    br = get_bottom_right(data, x, y)  # Bottom-right

    # Check the two diagonals for MAS or SAM
    diag1 = ul + data[y][x] + br  # Top-left to bottom-right
    diag2 = ur + data[y][x] + bl  # Top-right to bottom-left

    # Valid X-MAS patterns
    valid_patterns = {"MAS", "SAM"}

    # Check if both diagonals form valid MAS/SAM patterns
    if diag1 in valid_patterns and diag2 in valid_patterns:
        return 1  # Found a valid X-MAS
    return 0  # Not an X-MAS

def count_xmas(data):
    """Count all X-MAS patterns in the grid."""
    count = 0

    # Loop through the grid and check each position as a possible center of X-MAS
    for y in range(len(data)):
        for x in range(len(data)):
            count += is_xmas(data, x, y)

    return count

def day4():
    with open("day04/input.txt") as file:
        data = file.readlines()

    xmas_count = count_xmas(data)

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

    print(XMAS, xmas_count)
    return (XMAS, xmas_count)

day4()