"""
    Day 3 solution
    Cameron Clark
"""



def part1(l):
    total = 1
    x = 0
    y = 0
    lst = []

    for ch in line:
        if ch == '>':
            x += 1
        elif ch == '<':
            x -= 1
        elif ch == '^':
            y += 1
        else:
            y -= 1

        coor = (x ,y)
        if coor not in lst:
            lst += [coor]
            total += 1  
    return total

def part2(l):
    total = 1
    x = 0
    y = 0
    robx = 0
    roby = 0
    lst = [(0,0)]

    turn = 0

    for ch in l:
        if ch == '>':
            if turn%2 == 0:
                x += 1
            else:
                robx += 1
        elif ch == '<':
            if turn%2 == 0:
                x -= 1
            else:
                robx -= 1
        elif ch == '^':
            if turn%2 == 0:
                y += 1
            else:
                roby += 1
        else:
            if turn%2 == 0:
                y -= 1
            else:
                roby -= 1

        coor = (x ,y)
        robcoor = (robx, roby)

        if turn%2 == 0:
            if coor not in lst:
                lst += [coor]
                total += 1
        else:
            if robcoor not in lst:
                lst += [robcoor]
                total += 1
        turn += 1
                
    return total

if __name__ == '__main__':
    f = open("day3.txt", "r")
    line = ""
    for l in f:
        line += l
        
    num = part1(l)
    print num
    num = part2(l)
    print num
