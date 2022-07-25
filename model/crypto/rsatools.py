import gmpy2 as gp
# 已知dp，n，e，c求明文m


def necdp(n, e, c, dp):
    e = e
    n = gp.mpz(n)
    dp = gp.mpz(dp)
    c = gp.mpz(c)

    for x in range(1, e):
        if(e*dp % x == 1):
            p = (e*dp-1)//x+1
            if(n % p != 0):
                continue
            q = n//p
            phin = (p-1)*(q-1)
            d = gp.invert(e, phin)
            m = gp.powmod(c, d, n)
            if(len(hex(m)[2:]) % 2 == 1):
                continue
            print('--------------')
            print(m)
            print(hex(m)[2:])
            print(bytes.fromhex(hex(m)[2:]))


# e = 65537
# n = 85413323752199019806030766630760449394238054889872415531186815348349883843039718091361611175963675771467536496812507338620957273406076058263122453235926619595761737396698699834116678598534261542535530241537247151318756003375573850725841254167462648747492270335084402716816450008370008491069875351593380154253
# dp = 1576424214336939000475035870826282526256046059505538052583882122452307602095912733650442447289122473348318614749578285418144935611098423641334952097553125
# c = 53653254613997095145108444611576166902006080900281661447007750088487109015427510365774527924664116641019490904245926171500894236952984157500461367769566121581870986304353174732328118576440353500038670030097108081972287049673200783198844842527470746431369314585103203118824985764754487936404004696485346196488

# necdp(n, e, c, dp)


# !已知n,dp,dq,c求d和明文m
# p = gp.mpz()
# q = gp.mpz()
# dp = gp.mpz()
# dq = gp.mpz()
# c = gp.mpz()

# n = p*q
# phin = (p-1)*(q-1)
# dd = gp.gcd(p-1, q-1)
# d=(dp-dq)//dd * gp.invert((q-1)//dd, (p-1)//dd) * (q-1) +dq
# print(d)

# m = gp.powmod(c, d, n)
# print('-------------------')
# print(m)
# print(hex(m)[2:])

# 已知n,e,c求m

# def Decrypt(c,e,p,q):
# 	L=(p-1)*(q-1)
# 	d=gmpy2.invert(e,L)
# 	n=p*q
# 	m=gmpy2.powmod(c,d,n)
# 	flag=str(m)
# 	print("flag{"+flag+"}")
# if __name__ == '__main__':
# 	p =  9648423029010515676590551740010426534945737639235739800643989352039852507298491399561035009163427050370107570733633350911691280297777160200625281665378483
# 	q =  11874843837980297032092405848653656852760910154543380907650040190704283358909208578251063047732443992230647903887510065547947313543299303261986053486569407
# 	e =  65537
# 	c =  83208298995174604174773590298203639360540024871256126892889661345742403314929861939100492666605647316646576486526217457006376842280869728581726746401583705899941768214138742259689334840735633553053887641847651173776251820293087212885670180367406807406765923638973161375817392737747832762751690104423869019034
# 	Decrypt(c,e,p,q)

# 已知n,e求秘钥d
# from Crypto.Util import number
# p = 473398607161
# q = 4511491
# e = 17
# d = gmpy2.invert(e,(p-1)*(q-1))
# print (d)


# 已知n,e求秘钥d和key
# import gmpy2
# import rsa

# p = 285960468890451637935629440372639283459
# q = 304008741604601924494328155975272418463
# e = 65537
# n = 86934482296048119190666062003494800588905656017203025617216654058378322103517

# d = gmpy2.invert(e,(q-1)*(p-1))
# print(d)

# d = 81176168860169991027846870170527607562179635470395365333547868786951080991441

# key = rsa.PrivateKey(n,e,d,p,q)
# print(key)

# with open("flag.enc","rb") as f:
# 	print(rsa.decrypt(f.read(),key).decode())

# 已知c1,c2,e1,e2,n求明文m（共模攻击）

# from gmpy2 import *
# import libnum

# n=22708078815885011462462049064339185898712439277226831073457888403129378547350292420267016551819052430779004755846649044001024141485283286483130702616057274698473611149508798869706347501931583117632710700787228016480127677393649929530416598686027354216422565934459015161927613607902831542857977859612596282353679327773303727004407262197231586324599181983572622404590354084541788062262164510140605868122410388090174420147752408554129789760902300898046273909007852818474030770699647647363015102118956737673941354217692696044969695308506436573142565573487583507037356944848039864382339216266670673567488871508925311154801
# e1=11187289
# e2=9647291
# s = gcdext(e1, e2)
# s1 = s[1]
# s2 = -s[2]

# c1=22322035275663237041646893770451933509324701913484303338076210603542612758956262869640822486470121149424485571361007421293675516338822195280313794991136048140918842471219840263536338886250492682739436410013436651161720725855484866690084788721349555662019879081501113222996123305533009325964377798892703161521852805956811219563883312896330156298621674684353919547558127920925706842808914762199011054955816534977675267395009575347820387073483928425066536361482774892370969520740304287456555508933372782327506569010772537497541764311429052216291198932092617792645253901478910801592878203564861118912045464959832566051361
# c2=18702010045187015556548691642394982835669262147230212731309938675226458555210425972429418449273410535387985931036711854265623905066805665751803269106880746769003478900791099590239513925449748814075904017471585572848473556490565450062664706449128415834787961947266259789785962922238701134079720414228414066193071495304612341052987455615930023536823801499269773357186087452747500840640419365011554421183037505653461286732740983702740822671148045619497667184586123657285604061875653909567822328914065337797733444640351518775487649819978262363617265797982843179630888729407238496650987720428708217115257989007867331698397
# e2=9647291
# c2 = invert(c2, n)
# m = (pow(c1,s1,n) * pow(c2 , s2 , n)) % n
# print (m)
# print (libnum.n2s(m))

# e=1

# import binascii
# import gmpy2
# N_hex=0x180be86dc898a3c3a710e52b31de460f8f350610bf63e6b2203c08fddad44601d96eb454a34dab7684589bc32b19eb27cffff8c07179e349ddb62898ae896f8c681796052ae1598bd41f35491175c9b60ae2260d0d4ebac05b4b6f2677a7609c2fe6194fe7b63841cec632e3a2f55d0cb09df08eacea34394ad473577dea5131552b0b30efac31c59087bfe603d2b13bed7d14967bfd489157aa01b14b4e1bd08d9b92ec0c319aeb8fedd535c56770aac95247d116d59cae2f99c3b51f43093fd39c10f93830c1ece75ee37e5fcdc5b174052eccadcadeda2f1b3a4a87184041d5c1a6a0b2eeaa3c3a1227bc27e130e67ac397b375ffe7c873e9b1c649812edcd
# e_hex=0x1
# c_hex=0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d

# c_hex = gmpy2.mpz(c_hex)
# N_hex = gmpy2.mpz(N_hex)

# i = 0
# while i<10:
#     m_hex = hex(c_hex + gmpy2.mpz(hex(i))*N_hex)
#     print(m_hex[2:])
#     try:
#         print(binascii.a2b_hex(m_hex[2:]).decode("utf8"))
#     except binascii.Error as e:
#         print("位数非偶数，跳过...")
#     i += 1

# e=2
#!/usr/bin/python
# coding=utf-8
# 适合e=2
# import gmpy
# import string
# from Crypto.PublicKey import RSA

# # 读取公钥参数
# with open('./tmp/pubkey.pem', 'r') as f:
#     key = RSA.importKey(f)
#     N = key.n
#     e = key.e

# p = 275127860351348928173285174381581152299
# q = 319576316814478949870590164193048041239
# with open('./tmp/flag.enc', 'r') as f:
#     cipher = f.read().encode('hex')
#     cipher = string.atoi(cipher, base=16)
#     # print cipher

# # 计算yp和yq
# yp = gmpy.invert(p,q)
# yq = gmpy.invert(q,p)

# # 计算mp和mq
# mp = pow(cipher, (p + 1) / 4, p)
# mq = pow(cipher, (q + 1) / 4, q)

# # 计算a,b,c,d
# a = (yp * p * mq + yq * q * mp) % N
# b = N - int(a)
# c = (yp * p * mq - yq * q * mp) % N
# d = N - int(c)

# for i in (a,b,c,d):
#     s = '%x' % i
#     if len(s) % 2 != 0:
#         s = '0' + s
#     print s.decode('hex')

# e=3


# import gmpy2
# from Crypto.PublicKey import RSA

# public_key = "./tmp/pubkey.pem"
# cipher_file = "./tmp/flag.enc"

# #读入公钥
# with open(public_key, "r") as f:
#     key = RSA.importKey(f)
#     n = key.n
#     e = key.e

# #读入密文
# with open(cipher_file, "r") as f:
#     cipher = f.read().encode("hex")
#     cipher = int(cipher, 16)
#     #print(cipher)

# #破解密文
# def get_flag():
#     i = 0
#     while True:
#         if(gmpy2.iroot(cipher+i*n, 3)[1] == True):
#             flag_bin = int(gmpy2.iroot(cipher+x*n, 3)[0])
#             flag = hex(flag_bin)[2:-1].decode("hex")
#             print(flag)
#             break
#         i += 1

# def get_flag_for():
#     for x in xrange(118600000, 118720000):
#         if(gmpy2.iroot(cipher+x*n, 3)[1] == 1):
#             flag_bin = int(gmpy2.iroot(cipher+x*n, 3)[0])
#             flag = hex(flag_bin)[2:-1].decode("hex")
#             print(flag)
#             break

# if __name__ == "__main__":
#     get_flag_for()
#     #get_flag()

# 低解密指数攻击（e较大）

# import  RSAwienerHacker
# n=
# e=
# d =  RSAwienerHacker.hack_RSA(e,n)
# if d:
#     print(d)
# import hashlib
# flag = "flag{" + hashlib.md5(hex(d)).hexdigest() + "}"
# print flag


# e,m相同，存在两个n有公约数

# import gmpy2
# from gmpy2 import invert, iroot
# import gmpy2 as gp
# from libnum import xgcd, invmod

# n=[,,,,,,,,,,,,,,,,,,,]
# for i in n:
#     for j in n:
#         if (i<>j):
#             pub_p=gmpy2.gcdext(i,j)
#             if (pub_p[0]<>1)&(i>j):
#                 print i
#                 print j
#                 print pub_p[0]
#                 a=i,p=pub_p[0]
# q=a/p
# p =  gp.mpz()
# q =  gp.mpz()
# e =  gp.mpz()
# c =  gp.mpz()
# n = p*q
# phi = (p-1) * (q-1)
# d = gp.invert(e, phi)
# m = pow(c, d, n)
# print hex(m)

# e取随机数自减至与欧拉函数互质

# from gmpy2 import invert,gcd
# from binascii import a2b_hex

# p = 177077389675257695042507998165006460849
# q = 211330365658290458913359957704294614589
# c = 2373740699529364991763589324200093466206785561836101840381622237225512234632

# n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
# phi = (p-1) * (q-1)

# print(p,q,n,phi)

# for e in range(70100,39000,-1):
#     if gcd(e,phi) != 1:
#         continue
#     try:
#         d = invert(e,phi)
#         m = pow(c,d,n)
#         m = "%x" % m
#         m = a2b_hex(m.encode())
#         print(m.decode("ASCII"))
#     except Exception:
#         pass
# part2
# import random
# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         return 404            #因为20000个数中不是每个e都能求出d，所以这里对求d报错时进行了简单处理
#     else:
#         return x % m
# fw=open("plaintext.txt","w")
# p = 177077389675257695042507998165006460849
# q = 211330365658290458913359957704294614589
# n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
# c  = 2373740699529364991763589324200093466206785561836101840381622237225512234632
# phi=(p-1)*(q-1)
# for e in range(50000,70000):
#         d=modinv(int(e),(p-1)*(q-1))
#         if(d==404):
#                 continue
#         else:
#                 fw.writelines(hex(int(pow(c,d,p*q))))
#                 fw.writelines("n")

# 最优非对称加密填充
#!/usr/bin/python
# coding=utf-8

# 最优非对称加密填充
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

# with open('./tmp/pubkey.pem', 'r') as f:
#     key = RSA.importKey(f)
#     N = key.n
#     e = key.e
# print N
# print e

# with open('./tmp/private.pem', 'r') as f:
#     private = RSA.importKey(f)
#     oaep = PKCS1_OAEP.new(private)

# with open('./tmp/flag.enc', 'r') as f:
#     print oaep.decrypt(f.read())
