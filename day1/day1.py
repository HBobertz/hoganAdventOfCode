def main():
    cur_max = 0
    input = open('input.txt','r')
    cur_elf = 0
    for line in input.readlines():
        if line in ['\n', '\r\n']:
            cur_max= max(cur_max,cur_elf)
            cur_elf=0
        else:
            cur_elf+=int(line.strip())
    print(cur_max)

main()