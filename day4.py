import re
from utils.utils import aoc_boiler

@aoc_boiler(fname='input4.txt')
def part1(line):
    ranges = [int(x) for x in re.split(',|-', line)]
    if (ranges[0] >= ranges[2] and ranges[1] <= ranges[3]) or \
        (ranges[2] >= ranges[0] and ranges[3] <= ranges[1]):
            return 1
    return 0