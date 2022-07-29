from argon2 import PasswordHasher

#假设初始服务器里面记录了如下的账号，密码对
data_records={
    "abc202000":"123456789",
    "efc202001":"2868346ab33",
    "cdc3490111":"ab34868de",
    "011121ad":"3213a444554",
    "001121ad":"3213a444444"
    }

data_list1=[]
data_list2=[]

#16进制转化为2进制
def bin_hex(m):
    san=''
    for i in range(len(m)):
        data=m[i]
        dd =bin(int(data,16))[2:]
        while len(dd) < 4:
            dd = '0' + dd
        san += dd   
    return san
                            
for i,j in data_records.items():
    b=bin_hex(i)
    data_list1.append(b)
    b=bin_hex(j)
    data_list2.append(b)

#异或操作
def xor(a,b):
    a=list(a)
    b=list(b)
    if len(a)>len(b):
        for i in range(len(b)):
            if a[i]!=b[i]:
                a[i]='i'
            else:
                a[i]='0'
        a=''.join(a)
        return a
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                b[i]='1'
            else:
                b[i]='0'
        b=''.join(b)
        return b
data_xor=[]
for i in range(len(data_list1)):
    data_xor.append(xor(data_list1[i],data_list2[i]))

data_hash=[]
ph=PasswordHasher()
for i in data_xor:
    data_hash.append(ph.hash(i))


u1=input("请输入账户")
q1=input("请输入密码")

U=bin_hex(u1)
Q=bin_hex(q1)
K=xor(U,Q)
for i in data_hash:
    try:
        if(ph.verify(i,K)==True):
            print("是合法账户")
            break
    except:
        pass

    
