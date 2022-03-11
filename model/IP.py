
# 将IP地址转换成整型--python实现


def int2ip(num):
    s = []
    for i in range(4):
        s.append(str(num % 256))
        num //= 256
    return '.'.join(s[::-1])


def ip2int(ip):
    res = 0
    for j, i in enumerate(ip.split('.')[::-1]):
        res += 256**j*int(i)
    return res


"""
print(int2ip(123456789))
print(ip2int('7.91.205.21'))
-> 192.168.1.1
-> 3232235777
"""

print(int2ip(236088193))
print(ip2int('14.18.107.129'))
