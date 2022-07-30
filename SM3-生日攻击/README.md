
## SM3 birthday attack   

### 基本思想：                        
       首先我们要实现sm3加密算法，这一部分我们参考相应的国密加密标准即可。生日攻击的目的是找到两个明文m,m'使得hash(m)=hash(m')      
       我们知道sm3输出的杂凑值是64字节，即256bit.根据生日攻击理论。为了满足碰撞要求，至少需要1.17*2^128次。显然搜索的过程是非常     
       缓慢的。因此笔者这里寻找的是两个hash前8bit相同的碰撞。      
### 代码运行：   
##### C++版本
       具体的代码在源文件里面，本实验执行的环境是 vs2022。   
       运行结果如图所示：   
   ![results](https://user-images.githubusercontent.com/109323169/181401455-5f503870-ab30-4b19-8e49-8cacaaa9934c.png)
##### python版本
       代码文件为当前目录下的`attack.py`
       运行结果（10bit）如图所示：
   ![results](https://github.com/sduljl/project/blob/main/SM3-%E7%94%9F%E6%97%A5%E6%94%BB%E5%87%BB/10.png)
