def part1():
    """_summary_    A, X = Rock
                    B, Y = Paper
                    C, Z = Scissors
    """
    key = {'A X': 4,
           'A Y': 8,
           'A Z': 3,
           'B X': 1,
           'B Y': 5,
           'B Z': 9,
           'C X': 7,
           'C Y': 2,
           'C Z': 6}
    sum = 0
    input = open('input.txt','r')
    for line in input.readlines():
        sum+= key[line.strip()]
    print(sum)

def part2():
    key = {'A X': 3,
           'A Y': 4,
           'A Z': 8,
           'B X': 1,
           'B Y': 5,
           'B Z': 9,
           'C X': 2,
           'C Y': 6,
           'C Z': 7}
    sum = 0
    input = open('input.txt','r')
    for line in input.readlines():
        sum+= key[line.strip()]
    print(sum)

part2()
part1()