def create_rules(data):
    rules = []
    for line in data:
        if '|' in line:
            one, two = line.split('|')
            rules.append(((one), (two.split()[0])))
    return rules

def parse_correct_lines(data):
    return 0

def swap(line, i, j):
    temp = line[i]
    line[i] = line[j]
    line[j] = temp
    return line

def day5():
    with open("day05/input.txt") as file:
        data = file.readlines()

    rules = create_rules(data)
    while('|' in data[0] or data[0] == '\n'): #skip empty line and rules
        data.pop(0)
    
    middle_add = 0
    linecounter = 0
    for line in data:
        line = line.split()[0]
        line = line.split(",")
        correct_rule = True
        i = 0
        while(i < len(line)-1):
            changed = False
            for j in range(i+1,len(line)):
                if((line[j],line[i]) in rules):
                    print(linecounter,"  BEFORE ",line)
                    correct_rule = False
                    changed = True
                    line = swap(line, i, j)
                    print(linecounter,"  AFTER ", line)
                    print()
                    break
            if(changed):
                i = -1
            i+=1

        if(not correct_rule):
            middle_add += int(line[len(line)//2])
        linecounter +=1
        
    print(middle_add)


day5()