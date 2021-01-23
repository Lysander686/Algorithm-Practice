num = input()[::-1]
res = ''
c = set()

len = len(num)
for i in range(len):
    if (i+1) <= len and num[i] not in c:
        res += str(num[i])
    c.add(num[i])

if num[len-1] not in c:
    res += str(num[len-1])

print(res)
