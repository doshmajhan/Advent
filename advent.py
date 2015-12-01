"""
    Cameron Clark
    Advent day 1 solution
"""

def test(f):
    total = 0
    check = True
    x = 1
    for line in f:
        for ch in line:
            if ch == '(':
                total += 1
            else:
                total -= 1
            if total == -1 and check:
                print x
                check = False
            x+=1    
    return total


if __name__ == '__main__':
    f = open("adv.txt", 'r')
    num = test(f)
    print num
