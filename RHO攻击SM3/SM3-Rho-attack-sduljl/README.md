## SM3-Rho-attack

### 算法思路：    
        首先要实现SM3国密算法，这个在之前的项目中已经实现过了。Rho攻击的精髓就是寻找循环。我们对随机选择的明文进行加密，
        得到的密文再次进行加密，并且把每一次加密得到的hash值存储在一个空的集合里面。每次循环迭代都进行判断，看看得到的   
        新的hash值是否已经存在集合当中了，如果已经在了，那么就代表我们攻击成功。    
### 代码运行结果：    
        因为SM3输出的结果是256比特，根据生日攻击的碰撞原理，最多循环1.17*2^128次，可以找到一对碰撞。我们可以由此规定循环   
        的最大次数。想要攻击出所有的比特是困难的，本实验设置了变量n。n代表的是hash值的前n比特。通过运行代码发现，当n的值大
        于20的时候，运行时间增加非常明显。       
###  攻击长度为8bit     
   
![4BS1B}6$RDB27 B$L6VGWY7](https://user-images.githubusercontent.com/109323169/181492762-5ef1b286-9435-4205-9d55-121eb5bcdca7.png)

###  攻击长度为16bit   
![8LHEP6BM9C_75ME 1WXECFD](https://user-images.githubusercontent.com/109323169/181493051-ae14cb95-5bb0-4d88-af41-521ff8173686.png)

###  攻击长度为20bit    
![L$%`CWE6DUM@$ZS1S4P~W@D](https://user-images.githubusercontent.com/109323169/181493106-ae11c50d-e8c5-404e-be5c-59891b2cbea1.png)

###  攻击长度为24bit 
![$V34@8)K$CMPDW7 BIO65GD](https://user-images.githubusercontent.com/109323169/181493175-91b119e3-4c8a-4ea6-9695-6416699b0ad4.png)

###  攻击长度为28bit    
![W%}{W WO8 `)(WM~4W9{P 6](https://user-images.githubusercontent.com/109323169/181493270-7d19eeb9-adba-40d4-990f-b6b4014909dd.png)


### 参考代码网址：   
https://blog.csdn.net/qq_33439662/article/details/121635423?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165922678016780357281011%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=165922678016780357281011&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-24-121635423-null-null.142^v35^experiment_2_v1&utm_term=python%E5%AE%9E%E7%8E%B0SM3&spm=1018.2226.3001.4187
