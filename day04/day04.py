import hashlib as hl

def day4():

    print("DAY 04")

    file = open("day04/input.txt")
    text = file.readline()
    file.close()

    hashtext = ""
    index = 1
    while(hashtext[0:6] != "000000"):
        encoded = text + (str)(index)
        hashtext = hl.md5(encoded.encode()).hexdigest()
        index+=1
    
    print(index-1)