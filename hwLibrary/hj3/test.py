
while True:
    try:
        line_num, num = int(input()), set()
        for i in range(line_num):
            num.add(int(input()))
        for j in sorted(list(num)):
            print(j)
    except:
        break
