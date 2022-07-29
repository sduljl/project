###  Google Password Checkup

###  算法思路：   
![TI0~RXABW9(M{PR_JSGN98W](https://user-images.githubusercontent.com/109323169/181669812-c3ee1260-dde8-4c7c-9dac-2fdefbc61fce.png)
按照上述流程逐一实现即可  

### 代码运行结果：  
     首先我们创建了一个初始化好的（用户名：密码）的字典组，作为验证的判断依据。为了使用argon2函数，查询了有关文档，引入python第三方库   
     from argon2 import PasswordHasher 。与流程有区别的一点是，计算hash值的时候只需要一个输入即可。因此将用户名和密码异或后作为输入值  
     这里要求用户名和密码必须由字母和数字组成。由于加密函数每一次的加密结果都不同，本项目借用了verify(hash1,m)来判断，hash1是否是m经过   
     argon2函数得到的hash值。    
   #### 当账户信息正确时：  
![BFDCTI` OZ6)0_{(`920GLS](https://user-images.githubusercontent.com/109323169/181670837-de0c52e5-57cd-41f5-a742-77aa8e268f87.png)
   #### 当账户信息不正确时：   
![@5W`%0~Y6UT5}QKA{L`S00F](https://user-images.githubusercontent.com/109323169/181670892-e3d35057-b043-4f42-ab99-28f3945a0217.png)

