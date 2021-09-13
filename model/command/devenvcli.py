#!/usr/bin/env python
"""
Command-line tool using fire
"""
import fire
import os
import sys
import platform
# Define a class for the ships commands.
print(os.name)

cmd = 'winget -v'
res = os.popen(cmd)
output_str = res.read()
print(output_str)
print(sys.platform)
# os.name——判断现在正在实用的平台，Windows 返回 ‘nt'; Linux 返回’posix
# windows win32
# linux linux
# Windows/Cygwin cygwin
# Mac OS X darwin
print(platform.platform())
# 获取操作系统名称及版本号

print(platform.version())
# 获取操作系统版本号

print(platform.architecture())
# 获取操作系统的位数

print(platform.machine())
# 计算机类型

print(platform.node())
# 计算机的网络名称'

print(platform.processor())
# 计算机处理器信息'

print(platform.uname())
# 包含上面所有的信息汇总


class Ships():
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")

# sailors has no subcommands, so it can be defined as a function.


def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

# Define a class to act as the top group. Add the sailors function and the Ships as attributes of the class.


class Cli():

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == '__main__':

    # Call fire.Fire on the class acting as the top-level group.
    fire.Fire(Cli)
