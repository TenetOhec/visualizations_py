import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10,5))

#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
#使用颜色映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#设置图表标题并给坐标轴加上标签
ax.set_title('square', fontsize=24)
ax.set_xlabel('value', loc='right', fontsize=14)
ax.set_ylabel('value\'s square', rotation=0,loc='top', labelpad=-20, fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])


#plt.show()

#自动保存图表 第一个实参指定文件名 第二个实参指定将图表多余的空白区域裁剪掉（保留则省略）
plt.savefig('square_plot.png', bbox_inches='tight')