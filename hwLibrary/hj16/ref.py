str = input()

str_list = str.split(';')

d = {}

for command in str_list:
    if(len(command) > 1 and command[0] in list('ADSW') and command[1:].isdecimal()):
        d[command[0]] = d.get(command[0], 0) + int(command[1:])


x, y = (d['D'] - d['A']), (d['W']-d['S'])

print('%d,%d' % (x, y))
