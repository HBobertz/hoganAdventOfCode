import math

def part1():
    input = open('input.txt','r')
    sum = 0
    for line in input.readlines():
        line = line.strip()
        mid = math.floor(len(line)/2)
        rucksacks = [line[:mid], line[mid:]]
        set_key = set()
        for c in rucksacks[0]:
            set_key.add(c)
        for c in rucksacks[1]:
            if c in set_key:
                if c.isupper():
                    sum+= (ord(c)-38)
                else:
                    sum += (ord(c)-96)
                break
    print(sum)
    
def part2():
    input = open('input.txt','r')
    sum = 0
    key = [set(),set(),set()]
    counter = 0
    for line in input.readlines():
        for c in line.strip():
            key[counter].add(c)
        counter+=1
        if counter >= 3:
            key[0] = key[0] & key[1] & key[2]
            print(key[0])
            for c in key[0]:
                if c.isupper():
                    sum+= (ord(c)-38)
                else:
                    sum += (ord(c)-96)
            key = [set(),set(),set()]
            counter = 0
    print(sum)
   
part2() 
part1()