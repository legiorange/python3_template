import os
import sys
import platform

winget = 'winget '
cmd = 'winget -v'
res = os.popen(cmd)
output_str = res.read()
print(output_str)
# print(sys.platform)
# os.name——判断现在正在实用的平台，Windows 返回 ‘nt'; Linux 返回’posix
# windows win32
# linux linux
# Windows/Cygwin cygwin
# Mac OS X darwin


def cmdRun(CMD):
    res = os.popen(CMD)
    return res


def infoPlatform():
    info_platform = platform.uname()
    if(info_platform.system == 'Windows'):
        print("win")
    elif (info_platform.system == 'Linux'):
        print("linux")
    elif (info_platform.system == 'Mac'):
        print("mac")
    else:
        print('Others')
    return info_platform.system


platforminfo = infoPlatform()
print(platforminfo)

# winget export a json for install list


def wexport(URLPath):
    if(URLPath != ''):
        cmdRun(winget + "export "+URLPath)

# winget inport a json for install list
# winget import [-i] <import-file> [<options>]
# [<options>] --ignore-unavailable --ignore-versions


def wimport(URLPath):
    if(URLPath != ''):
        cmdRun(winget + "-i "+URLPath +
               " --ignore-unavailable --ignore-versions")


def wupgrade():
    cmdRun(winget + "upgrade "+"--all")
