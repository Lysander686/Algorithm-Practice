
def parse():
    str = input()[2:]
    actual_num = int(str, base=16)
    print(actual_num)


while True:
    try:
        parse()
    except:
        break
