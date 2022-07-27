import random
import time


iv=0x7380166F4914B2B9172442D7DA8A0600A96F30BC163138AAE38DEE4DB0FB0E4E

def time_test(func):
    def wrapper(*args,**kw):
        start = time.time()
        res=func(*args, **kw)
        end = time.time()
        print(f"{func.__name__} Running time:{end-start}")
        return res
    return wrapper


def rol(a, k):
    res = list(int2bin(a, 32))
    for i in range(k):
        temp = res.pop(0)
        res.append(temp)
    return int(''.join(res), 2)

def P0(x):
    return x^rol(x,9)^rol(x,17)

def P1(x):
    return x^rol(x,15)^rol(x,23)

def FF(x,y,z,j):
    if j<16:
        return x^y^z
    else:
        return (x&y) | (x&z) | (y&z)
    
def GG(x,y,z,j):
    if j<16:
        return x^y^z
    else:
        return (x&y) | ((~x)&z)

def int2bin(x,n):
    res=list(bin(x)[2:])
    for i in range(n-len(res)):
        res.insert(0,'0')
    return ''.join(res)

def padding(mes):
    mes=bin(mes)[2:]
    for i in range(0,4):
        if len(mes)%4==0:
            break
        else:
            mes='0'+mes
    length=len(mes)
    l_bin=int2bin(length,64)
    temp=448-(length+1)%512
    res=mes+'1'+'0'*temp+l_bin
    return res

def message_Expend(mes):  
    W=[]
    W1=[]
    for i in range(0,16):
        W.append(int(mes[i*32:(i+1)*32],2))
    for j in range(16,68):
        W.append(P1(W[j-16]^W[j-9]^rol(W[j-3],15))^rol(W[j-13],7)^W[j-6])
    for i in range(0,64):
        W1.append(W[i]^W[i+4])
    return W,W1

def iterfunc(mes):
    n=int(len(mes)/512)
    v=[]
    v.append(int2bin(iv,256))
    for i in range(n):
        W,W1 = message_Expend(mes[512 * i:512 * (i + 1)])
        temp = CF(v[i], W, W1)
        temp = int2bin(temp, 256)
        v.append(temp)
    return v[n]

def CF(digest,W,W1):
    A=int(digest[0:32],2)
    B=int(digest[32:64],2)
    C=int(digest[64:96],2)
    D=int(digest[96:128],2)
    E=int(digest[128:160],2)
    F=int(digest[160:192],2)
    G=int(digest[192:224],2)
    H=int(digest[224:256],2)
    for j in range(0,64):
        if j<16:
            t=0x79CC4519
        else:
            t=0x7A879D8A
        SS1 = rol((rol(A, 12) + E + rol(t, j%32))%pow(2,32), 7)
        SS2 = SS1 ^ rol(A, 12)
        TT1 = (FF(A, B, C,j) + D + SS2 + W1[j])%pow(2,32)
        TT2 = (GG(E, F, G,j) + H + SS1 + W[j])%pow(2,32)
        D = C
        C = rol(B, 9)
        B = A
        A = TT1
        H = G
        G = rol(F, 19)
        F = E
        E = P0(TT2)
    temp = int(int2bin(A, 32) + int2bin(B, 32) + int2bin(C, 32) + int2bin(D, 32) + int2bin(E, 32) + int2bin(F, 32) + int2bin(G, 32) + int2bin(H, 32),2)
    return temp ^ int(digest, 2)

def sm3(mes):
    mes_=padding(mes)
    res=iterfunc(mes_)
    res_=hex(int(res,2))
    return res_[2:]

@time_test
def attack(n=24):
    h=random.randint(0,pow(2,64))
    h_=[]
    for i in range(0,pow(2,32)):
        h_.append(sm3(h)[:int(n/4)])
        h=2*h+1
        if(sm3(h)[:int(n/4)] in h_):
            print("Succeed")
            return
    print("Failed")
    
if __name__ == '__main__':
    attack(12)



