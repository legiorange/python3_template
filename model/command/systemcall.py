import os
import sys
import platform
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
