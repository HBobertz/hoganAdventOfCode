def aoc_boiler(*args, **kwargs):
    def wrap(func):
        fname = kwargs['fname']
        input = open(f'inputs/{fname}','r')
        sum = 0
        for line in input.readlines():
            line = line.strip()
            sum+=func(line)
        print(sum)
    return wrap