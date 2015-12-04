"""
    Solution to day 4
"""
import hashlib
import sys

def part1():

    key = "yzbqklnj"
    for x in range(1, 10000000):
        tempk = key + str(x)
        m = hashlib.md5(tempk)
        dig = m.hexdigest()
        if dig[:5] == '00000':
            print x
            return


def part2():

    key = "yzbqklnj"
    for x in range(1, 10000000):
        tempk = key + str(x)
        m = hashlib.md5(tempk)
        dig = m.hexdigest()
        if dig[:6] == '000000':
            print x
            return
            
if __name__ == '__main__':
    part1()
    part2()
