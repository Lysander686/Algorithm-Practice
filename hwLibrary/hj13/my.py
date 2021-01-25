arr = input().split(' ')
res = ''
len = len(arr)
for i in range(1, len+1):
    res += arr[-i] + ' '
res = res.strip()
print(res)
