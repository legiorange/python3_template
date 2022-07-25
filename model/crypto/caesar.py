from json.tool import main
import re
from string import ascii_uppercase

# 加密代换：
# c = Ekey(m)  ≡ a, + key(mod 26) 0≤m≤25

#         解密代换：
# m = Dkey(c) ≡ c - key(mod 26) 0≤m≤25


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


stra = "Ebgbp uto xiooynu sy fkpp qjoy sqe xcuc dioozhg cz gwms njke sqe uoud hupd ei rsne vrpg hbzg ayfl fbpuoc lhf rfa vrpg hyc lgkw! Znkr cu BRVEDQ{S0w_wf3n_d3_wj_Z1t3d} Olgkx qjke sqe hupd ei fbpuo;qz qjocy ayf qcxe nq qz;vg gsuv izo ykyn vy my,donuwcp sqe suxo zhni zhg vtzg kyx qxp wjkywg dz xq kwf vrp njsyau izo ykyn vy oi."
caesarHacker(stra)
