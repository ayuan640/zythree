import random #随机
random.seed(2023)
# 生成随机点的数量
n = 100000
# 统计圆内的点数
count = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        count += 1
# 计算圆周率
pi = 4 * count / n
print("圆周率的近似值为：{:.2f}".format(pi))
