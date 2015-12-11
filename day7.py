"""
    Day 7 solution
    Cameron Clark
"""

results = dict()
c = dict()
    
def part1(n):
    try:
        return int(n)
    except ValueError:
        pass

    if n not in results:
        ops = c[n]
        if len(ops) == 1:
            res = part1(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res = part1(ops[0]) & part1(ops[2])
            elif op == 'OR':
                res = part1(ops[0]) | part1(ops[2])
            elif op == 'LSHIFT':
                res = part1(ops[0]) << part1(ops[2])
            elif op == 'RSHIFT':
                res = part1(ops[0]) >> part1(ops[2])
            elif op == 'NOT':
                res = ~part1(ops[1]) & 0xffff
        results[n] = res
    return results[n]


if __name__ == '__main__':

    f = open("day7.txt", "r")
    for line in f:
        (op, ans) = line.split('->')
        c[ans.strip()] = op.strip().split(' ')
    results['b'] = 3176
    
    num = part1('a')
    print num
