import os
import binascii
import struct
# 爆破crc校验所需要了解到的PNG文件头知识
# - （固定）八个字节89 50 4E 47 0D 0A 1A 0A为png的文件头
# - （固定）四个字节00 00 00 0D（即为十进制的13）代表数据块的长度为13
# - （固定）四个字节49 48 44 52（即为ASCII码的IHDR）是文件头数据块的标示（IDCH）
# - （可变）13位数据块（IHDR)
#     - 前四个字节代表该图片的宽
#     - 后四个字节代表该图片的高
#     - 后五个字节依次为：
#     Bit depth、ColorType、Compression method、Filter method、Interlace method
# - （可变）剩余四字节为该png的CRC检验码，由从IDCH到IHDR的十七位字节进行crc计算得到。
# misc = open("D:\gitvip\python3_template\model\crypto\png.py", "rb").read()

# for i in range(1024):
#     data = misc[12:16] + struct.pack('>i', i) + misc[20:29]
#     crc32 = binascii.crc32(data) & 0xffffffff
#     if crc32 == 0x932f8a6b:  # CRS校验
#         print(i)
# E8 D3 C1 43 00


fi = open('D:\gitvip\python3_template\model\crypto\png.py', 'rb').read()

# 12-15字节代表固定的文件头数据块的标示，16-19字节代表宽度，20-23字节代表高度，24-28字节分别代表
# Bit depth、ColorType、Compression method、Filter method、Interlace method
# 29-32字节为CRC校验和
print("start")
# 若PNG文件宽度出现错误，我们可以根据CRC码对文件进行校验,还原出正确的图片宽度
# 下面是一个对宽度受损的图片根据CRC值进行宽度搜索的例子：
for i in range(10000):  # 宽度0-9999搜索
    # pack函数将int转为bytes,>表示大端00 00 00 02,I表示4字节无符号int;<表示小端 02 00 00 00
    data = fi[12:16]+struct.pack('>I', i)+fi[20:29]
    # byte的大小为8bits而int的大小为32bits,转换时进行与运算避免补码问题0x932f8a6b
    crc = binascii.crc32(data) & 0xffffffff
    if crc == struct.unpack('>I', fi[29:33])[0] & 0xffffffff:  # 解开为无符号整数
        print(i)
