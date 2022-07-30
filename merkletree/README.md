# Merkle_tree

## 基本思想
实现merkle tree
重点在于某一级两个元素进行相加再hash作为上一级的内容
以及单数问题，出现单数就将其提到上一级即可
![](vx_images/3503028127062.png)

## 代码运行
对a,b,c,d进行merkle tree
![](vx_images/779832147228.png)
得到结果如下，每一个索引是一层中从左到右的数据
![](vx_images/5645132139897.png)


另一版本的运行结果，Messages为自定义元素，从0到3为由根节点向下的每一层，并从messages中随机挑选一个原始数据进行校验，打印校验结果:
![](https://github.com/sduljl/project/blob/main/merkletree/res.png)
