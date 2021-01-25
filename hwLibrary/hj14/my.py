try:
    n = int(input())
    result = []
    for i in range(n):
        str1 = input()
        result.append(str1)
    result = sorted(result)
    for i in result:
        print(i)
except:
    pass
