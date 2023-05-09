import matplotlib.pyplot as plt

from random_walk import RandomWalk


#创建一个RandomWalk实例
rw = RandomWalk()
rw.fill_walk()

#将所有点绘制出来,按生成顺序使用颜色映射，并删除每个点点黑的轮廓
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(7,7))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
#突出起点和终点
ax.scatter(0, 0, c='green')
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red')

#隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

