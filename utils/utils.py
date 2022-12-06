def aoc_boiler(*args, **kwargs):
    def wrap(func):
        fname = kwargs['fname']
        input = open(f'inputs/{fname}','r')
        sum = 0
        if 'after' in kwargs:
            after = kwargs['after']
            for line in input.readlines()[after:]:
                line = line.strip()
                sum+=func(line)
        else:
            for line in input.readlines():
                line = line.strip()
                ret = func(line)
                if ret == 'win':
                    print(f'{func.__name__}: {sum}')
                else:
                    sum+=func(line)
        print(f'{func.__name__}: {sum}')
    return wrap

def basic_boiler(*args, **kwargs):
    def wrap(func):
        fname = kwargs['fname']
        input = open(f'inputs/{fname}','r')
        lines = input.readlines()
        func(lines)
    return wrap
        