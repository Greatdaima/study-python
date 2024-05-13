import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 创建一个图形框
fig = plt.figure(figsize=(5,5))
# 在其中创建一个子图
ax1 = fig.add_subplot(1,1,1)

# 生成初始图像数据
data = np.zeros((5, 5))

im = ax1.imshow(data, cmap='gray')

# 更新图像的函数
def update(i):
    global data
    # 随机生成一个5x5的图像
    data = np.random.rand(5, 5)
    # 更新图像数据
    im.set_array(data)

# 创建动画
ani = animation.FuncAnimation(fig, update, frames=range(20), interval=200)
plt.show()