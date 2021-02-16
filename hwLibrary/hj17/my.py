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
        # 如果不存在0, 1
        if ym2.find('0') == -1 or ym2.find('1') == -1 or \
                ym2.find('0') != ym2.rfind('1') + 1:  #
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
    sysStdin = """10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
"""

    classdic = defaultdict(int)

    for line in sysStdin:
        res = line.split('~')
        if len(res) >= 2:
            ip, ym = res[0].strip(), res[1].strip()
            resprint(ip, ym, classdic)
    res = []
    for key in ['a', 'b', 'c', 'd', 'e', 'wrong', 'private']:
        res.append(classdic[key])

    res = [str(x) for x in res]
    print(' '.join(res))
    # print(result_str)
    # print(sys.stdin)


def test():
    a_list = ["h", "e", "l", "l", "o"]

    print(" ".join(a_list))


if __name__ == '__main__':
    main()
    # test()
    pass
