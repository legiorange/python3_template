# coding=utf-8

import getopt

import sys


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hn:w:', ['name=', 'word=', 'help'])

    name = 'No Name'

    word = 'Hello'

for key, value in opts:

    if key in ['-h', '--help']:

        print('一个向人打招呼的程序')

        print('参数：')

        print ('-h\t显示帮助')

        print('-n\t你的姓名')

        print('-w\t想要说的话')

        sys.exit(0)

if key in ['-n', '--name']:

    name = value

if key in ['-w', '--word']:

    word = value

print('你好，我叫', name, '，', word)

# 返回样例
def make_complex(x, y):
    return {'x': x, 'y': y}



def complex_function(a, b, c):
    if not a:
        return None  # 抛出一个异常可能会更好
    if not b:
        return None  # 抛出一个异常可能会更好

    # 一些复杂的代码试着用a,b,c来计算x
    # 如果成功了，抵制住返回x的诱惑
    if not x: # 一些关于x的计算的Plan-B
        return x  # 返回值x只有一个出口点有利于维护代码

