from json.tool import main
import re
from string import ascii_uppercase


def caesarHacker(message, SourceCode=ascii_uppercase):
    r_lst = []
    if message:
        for key in range(len(SourceCode)):
            translated = ''
            for word in message:
                if word in SourceCode:
                    num = SourceCode.find(word)
                    num = num - key
                    if num < 0:
                        num = num + len(SourceCode)
                    translated = translated+SourceCode[num]
                else:
                    translated = translated + word
            s = '#密钥 {}: 原文,{}'.format(key, translated)
            print(s)
            r_lst.append(s)
    else:
        print("pls input")
        return None
    return r_lst


caesarHacker("GRWHI3RUKJGTK2JT")


