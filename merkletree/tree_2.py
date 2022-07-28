import hashlib
#hash函数
def hash_data(data, hash_function = 'sha256'):
    hash_function = getattr(hashlib, hash_function)
    data = data.encode('utf-8')
    return hash_function(data).hexdigest()
#实现merkle tree
def Merkle(lst, hash_function = 'sha256'):
    #将传入数组所有内容hash传入temp中  
    temp = []
    for i in lst:
        temp.append(hash_data(i))
    if(len(temp)<=2):
        exit()
    #高度
    n = 0 
    #tree
    x=[[i for i in temp]]
    while len(temp) >1:
        n += 1
        #2的倍数
        if len(temp)%2 == 0:
            v = []
            while len(temp) >1 :
                #取前两个进行相加再hash作为上一级的内容
                a = temp.pop(0)
                b = temp.pop(0)
                v.append(hash_data(a+b, hash_function))
            temp = v
            #每一层内容保存在一个数组里添加到x中
            x.append([i for i in temp])
        #不是2的倍数
        else:
            v = []
            #先取出最后一个单独的再正常运行
            l = temp.pop(-1)
            while len(temp) >1 :
                a = temp.pop(0)
                b = temp.pop(0)
                v.append(hash_data(a+b, hash_function))
            #将取出的添加到取出时的上一层最后
            v.append(l)
            temp = v
            #添加到了上一级在原来的层中就要删除
            x[n-1].pop(-1)
            x.append([i for i in temp])
    return x, n+1


l = ['a', 'b', 'c','d']
x,height=Merkle(l)
print(x[::-1])