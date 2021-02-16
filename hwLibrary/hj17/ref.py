def checkvalid(ip, ym):
    # 若ip错误，则掩码无需判断
    ip1 = filter(None, ip.split('.'))
    ip2 = [int(x) for x in ip1]
    if len(ip2) < 4:
        return False
    else:
        # 子网掩码去掉分隔符'.'
        ym1 = list(map(int, ym.split('.')))
        # 二进制转换和高位补0
        ym2 = ''.join(['{:08b}'.format(i) for i in ym1])
        if ym2.find('0') == -1 or ym2.find('1') == -1 or ym2.find('0') != ym2.rfind('1') + 1:
            return False
        return True

def publicip(ip):
    ipn = [int(n) for n in ip.split('.')]
    if 1 <= ipn[0] <= 126:
        return 'a'
    elif 128 <= ipn[0] <= 191:
        return 'b'
    elif 192 <= ipn[0] <= 223:
        return 'c'
    elif 224 <= ipn[0] <= 239:
        return 'd'
    elif 240 <= ipn[0] <= 255:
        return 'e'
    else:
        return 'ignore'

def privateip(ip):
    ipn = [int(n) for n in ip.split('.')]
    if (ipn[0] == 10) or (ipn[0] == 172 and (16 <= ipn[1] <= 31)) or (ipn[0] == 192 and ipn[1] == 168):
        return True
    return False

def resprint(ip, ym, classdic):
    if checkvalid(ip, ym):
        classdic[publicip(ip)] += 1
        if privateip(ip):
            classdic['private'] += 1
    else:
        classdic['wrong'] += 1
    return classdic


import sys
from collections import defaultdict
def main():
    classdic = defaultdict(int)
    for line in sys.stdin:
        ip, ym = line.split('~')
        resprint(ip, ym, classdic)
    res = []
    for key in ['a', 'b', 'c', 'd', 'e', 'wrong', 'private']:
        res.append(classdic[key])
    print(' '.join(res))

main()