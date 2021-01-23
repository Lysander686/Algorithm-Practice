#!/usr/bin/python
# -*- coding: UTF-8 -*-

b = {}
a = int(input())
c = set()
for i in range(a):
    contents = input().split(" ")
    key = int(contents[0])
    value = int(contents[1])

    if key not in c:
        c.add(key)
        b[key] = value
    else:
        b[key] = b[key] + value

result = sorted(b.keys(), reverse=False)


for key in result:
    print(key, b[key])
