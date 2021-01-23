
def func(num):
    prime_num = 1
    tra = int(num**0.5+2)
    for i in range(2, tra):
        if num % i == 0:
            prime_num = 0
            b = int(num/i)
            print(str(i), end=' ')
            func(b)
            break
    if prime_num == 1:
        print(str(num), end=' ')


while True:
    try:
        num = int(input())
        func(num)
    except:
        break
