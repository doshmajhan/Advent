"""
    Cameron Clark
    Solution to day 2 of advent
"""

def test(f):
    total = 0
    ribbon = 0
    
    for line in f:
        lst = line.split('x')
        l = int(lst[0])
        w = int(lst[1])
        h = int(lst[2])
        
        side1 = (l*w)
        p1 = l+l+w+w
        side2 = (w*h)
        p2 = w+w+h+h
        side3 = (h*l)
        p3 = h+h+l+l
        bow = l*w*h
        
        ribbon += bow + min(p1, p2, p3)
        
        total += ((2*side1) + (2*side2) + (2*side3) + min(side1, side2, side3))

    print "Ribbon: " + str(ribbon)
    return total

if __name__ == '__main__':
    f = open("day2.txt", "r")
    num = test(f);
    print "Paper: " + str(num)
