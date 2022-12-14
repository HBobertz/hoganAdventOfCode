from utils.utils import basic_boiler

@basic_boiler(fname='input6.txt')
def part1(lines):
    line = lines[0]
    sum = 0
    for i in range(len(line)-4):
        if len(set(line[i:i+4])) == 4:
            print(f'sum of {sum+4} at {line[i:i+4]}') 
            break
        else:
            sum+=1
            
@basic_boiler(fname='input6.txt')
def part2(lines):
    line = lines[0]
    sum = 0
    for i in range(len(line)-14):
        if len(set(line[i:i+14])) == 14:
            print(f'sum of {sum+14} at {line[i:i+4]}') 
            break
        else:
            sum+=1