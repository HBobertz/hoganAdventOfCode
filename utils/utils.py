def aoc_boiler(*args, **kwargs):
    def wrap(func):
        fname = kwargs['fname']
        input = open(f'inputs/{fname}','r')
        sum = kwargs['sum']
        if kwargs['after']:
            after = kwargs['after']
            for line in input.readlines()[after:]:
                line = line.strip()
                sum+=func(line)
        else:
            for line in input.readlines():
                line = line.strip()
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
        