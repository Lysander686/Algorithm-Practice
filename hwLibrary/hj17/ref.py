A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
while True:
    try:
        arr = [__.split(".") for __ in input().split("~")]
        assert(len(arr) == 2)
        assert(len(arr[0]) == 4)
        assert(len(arr[1]) == 4)
        for i in arr:
            for j in i:
                assert(0 <= int(j) <= 255)
        temp = 0
        for i in arr[1]:
            temp += int(i)
            temp *= 256
        temp //= 256
        temp = (1 << 32) - temp
        assert((temp - 1).bit_length() < temp.bit_length())
        assert(temp != 1)
        assert(temp != 1 << 32)
        num = int(arr[0][0])
        if 1 <= num <= 126:
            A += 1
        elif 128 <= num <= 191:
            B += 1
        elif 192 <= num <= 223:
            C += 1
        elif 224 <= num <= 239:
            D += 1
        elif 240 <= num <= 255:
            E += 1
        if int(arr[0][0]) == 10 or (int(arr[0][0]) == 172 and 16 <= int(arr[0][1]) <= 31) or (int(arr[0][0]) == 192 and int(arr[0][1]) == 168):
            G += 1
    except BaseException as e:
        if isinstance(e, EOFError):
            print(A, B, C, D, E, F, G)
            break
        else:
            F += 1
