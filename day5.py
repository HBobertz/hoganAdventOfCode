from utils.utils import aoc_boiler, basic_boiler
import math

@basic_boiler(fname='input5.txt')
def part1(lines):
    key = lines[:8]
    key_list = [[] for _ in range(9)]
    instruction_list = []
    # build the starting key
    for line in key[::-1]:
        for i, v in enumerate(line):
            if v.isalpha():
                key_list[math.floor((i-1)/4)].append(v)

    # build the instructions
    for line in lines[10:]:
        line = line.split()
        temp = []
        for word in line:
            if word.isdigit():
                temp.append(int(word))
        instruction_list.append(temp)
    
    # perform instructions
    for ins in instruction_list:
        ins[1]-=1
        ins[2]-=1
        while ins[0] > 0:
            if len(key_list[ins[1]]) > 0:            
                key_list[ins[2]].append(key_list[ins[1]].pop())
                ins[0]-=1
            else:
                break
            
    for st in key_list:
        if st:
            print(st.pop(), end='')
    print('\n')

@basic_boiler(fname='input5.txt')         
def part2(lines):
    key = lines[:8]
    key_list = [[] for _ in range(9)]
    instruction_list = []
    # build the starting key
    for line in key[::-1]:
        for i, v in enumerate(line):
            if v.isalpha():
                key_list[math.floor((i-1)/4)].append(v)
    
    # build the instructions
    for line in lines[10:]:
        line = line.split()
        temp = []
        for word in line:
            if word.isdigit():
                temp.append(int(word))
        instruction_list.append(temp)
    
    # perform instructions
    for ins in instruction_list:
        ins[1]-=1
        ins[2]-=1
        temp = []
        while ins[0] > 0:
            if len(key_list[ins[1]]) > 0:            
                temp.append(key_list[ins[1]].pop())
                ins[0]-=1
            else:
                break
        key_list[ins[2]]+= temp[::-1]
            
    for st in key_list:
        if st:
            print(st.pop(), end='')
    print('\n')