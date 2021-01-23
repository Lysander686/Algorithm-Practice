def parse():
    str = input()
    part2 = int(str.split('.')[1][0])
    num = int(str.split('.')[0])
    if (part2 >= 5):
        num += 1

    print(num)


parse()
