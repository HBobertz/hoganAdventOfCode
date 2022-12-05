from utils.utils import aoc_boiler

@aoc_boiler(fname='input4.txt')
def part1(line):
    ranges = [int(x) for x in re.split(',|-', line)]
    if (ranges[0] >= ranges[2] and ranges[1] <= ranges[3]) or \
        (ranges[2] >= ranges[0] and ranges[3] <= ranges[1]):
            return 1
    return 0

@aoc_boiler(fname='input4.txt')
def part2(line):
    # if python was smart the 1 liner could have been:
    # with sorted([[int(y) for y in x.split('-')] for x in line.split(',')]) as ranges: return 1 if ranges[0][1] >= ranges[1][0] else 0
    return 1 if sorted([[int(y) for y in x.split('-')] for x in line.split(',')])[0][1] >= sorted([[int(y) for y in x.split('-')] for x in line.split(',')])[1][0] else 0