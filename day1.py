def main():
    cur_best = list()
    input = open('inputs/input1.txt','r')
    cur_elf = 0
    for line in input.readlines():
        if line in ['\n', '\r\n']:
            cur_best.append(cur_elf)
            if len(cur_best) >= 4:
                cur_best.sort(reverse=True)
                cur_best.pop()
            cur_elf=0
        else:
            cur_elf+=int(line.strip())
    print(sum(cur_best))

main()