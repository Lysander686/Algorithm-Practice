# time complexity: O(n)
# reason: Assume input length is 8n,  every interation deal with 1 8-digit cluster, it needs n times interation to finish.
def parse(str):
    if not str:
        str = input()
    remaining = '0'
    if (len(str) > 8):
        remaining = str[8:]
        print(str[:8])
        parse(remaining)
    else:
        #  需要补充的个数
        append_len = 8 - len(str)
        str += append_len*remaining
        print(str)


while True:
    try:
        parse(input())
    except:
        break
