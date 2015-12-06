"""
    Solution to day 6
    Cameron Clark
"""

def part1(f):

    grid = [[0 for x in range(1000)] for x in range(1000)]
    total = 0
    
    for line in f:
        temp = line.split()
        if "turn off" in line:
            cor1 = temp[2]
            cor2 = temp[4]
            cor1temp = cor1.split(",")
            cor2temp = cor2.split(",")
            x1 = int(cor1temp[0])
            y1 = int(cor1temp[1])
            x2 = int(cor2temp[0])
            y2 = int(cor2temp[1])
            for x in range(x1,x2 + 1):
                for i in range(y1, y2 + 1):
                    grid[x][i] = 0
                        
        elif "turn on" in line:
            cor1 = temp[2]
            cor2 = temp[4]
            cor1temp = cor1.split(",")
            cor2temp = cor2.split(",")
            x1 = int(cor1temp[0])
            y1 = int(cor1temp[1])
            x2 = int(cor2temp[0])
            y2 = int(cor2temp[1])
            for x in range(x1,x2 + 1):
                for i in range(y1, y2 + 1):
                    grid[x][i] = 1
                    
        elif "toggle" in line:
            cor1 = temp[1]
            cor2 = temp[3]
            cor1temp = cor1.split(",")
            cor2temp = cor2.split(",")
            x1 = int(cor1temp[0])
            y1 = int(cor1temp[1])
            x2 = int(cor2temp[0])
            y2 = int(cor2temp[1])
            for x in range(x1,x2 + 1):
                for i in range(y1, y2 + 1):
                    if grid[x][i] == 1:
                        grid[x][i] = 0
                    else:
                        grid[x][i] = 1
                

    for x in range(0,1000):
        for i in range(0,1000):
                total += grid[x][i]
            
    return total

def part2(f):

    grid = [[0 for x in range(1000)] for x in range(1000)]
    total = 0
    
    for line in f:
        temp = line.split()
        if "turn off" in line:
            cor1 = temp[2]
            cor2 = temp[4]
            cor1temp = cor1.split(",")
            cor2temp = cor2.split(",")
            x1 = int(cor1temp[0])
            y1 = int(cor1temp[1])
            x2 = int(cor2temp[0])
            y2 = int(cor2temp[1])
            for x in range(x1,x2 + 1):
                for i in range(y1, y2 + 1):
                    if grid[x][i] != 0:
                        grid[x][i] -= 1
                        
        elif "turn on" in line:
            cor1 = temp[2]
            cor2 = temp[4]
            cor1temp = cor1.split(",")
            cor2temp = cor2.split(",")
            x1 = int(cor1temp[0])
            y1 = int(cor1temp[1])
            x2 = int(cor2temp[0])
            y2 = int(cor2temp[1])
            for x in range(x1,x2 + 1):
                for i in range(y1, y2 + 1):
                    grid[x][i] += 1
                    
        elif "toggle" in line:
            cor1 = temp[1]
            cor2 = temp[3]
            cor1temp = cor1.split(",")
            cor2temp = cor2.split(",")
            x1 = int(cor1temp[0])
            y1 = int(cor1temp[1])
            x2 = int(cor2temp[0])
            y2 = int(cor2temp[1])
            for x in range(x1,x2 + 1):
                for i in range(y1, y2 + 1):
                    grid[x][i] += 2
                

    for x in range(0,1000):
        for i in range(0,1000):
                total += grid[x][i]
            
    return total


if __name__ == '__main__':
    f = open("day6.txt", "r")
    num = part1(f)
    print num
    f.close()
    f = open("day6.txt", "r")
    num = part2(f)
    print num
