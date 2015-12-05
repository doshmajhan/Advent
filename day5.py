"""
    Solution to day 5 puzzle
    Cameron Clark
"""

def part1(f):
    total = 0
    vowelCount = 0
    vlst = ['a', 'e', 'i', 'o', 'u']
    nlst = ['ab', 'cd', 'pq', 'xy']
    seen = []
    vValid = False
    no = True
    
    for line in f:
        no = True
        vValid = False
        valid = False
        seen = []
        vowelCount = 0
        for ch in line:
            if ch in vlst:
                vowelCount+=1
            if vowelCount >= 3:
                vValid = True
        for x in range(0,len(line)):
            if x != (len(line) - 1):
                if line[x] == line[x+1]:
                    valid = True
        for x in nlst:
            if x in line:
                no = False

        if valid and vValid and no:
            total += 1
            
    return total

def part2(f):

    valid1 = False
    valid2 = False
    pos1 = 0
    pos2 = 0
    total = 0
    for line in f:
        pos1 = 0
        post2 = 0
        valid1 = False
        valid2 = False
        for x in range(0, len(line)):
            if x != (len(line) -1):
                temp = line[x] + line[x+1]
                count = line.count(temp)
                if count > 1:
                    if pos1 != (pos2 + 1):
                        valid1 = True
            pos1 = x
            pos1 = x- 1

        for x in range(0, len(line) - 2):
            a = line[x]
            b = line[x+2]
            if a == b:
                valid2 = True
                
        if valid1 and valid2:
            total+=1
                    

    return total  
        
if __name__ == '__main__':
    f = open("day5.txt", "r")
    num = part1(f)
    print num
    f.close()
    f = open("day5.txt", "r")
    num = part2(f)
    print num
    f.close()
