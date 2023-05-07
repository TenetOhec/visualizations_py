import matplotlib.pyplot as plt	

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9,16, 25]

"""
subplots()函数可在一张图片上绘制一个或多个图表
变量fig表示一张图片
变量ax表示各个图表

"""
#使用内置样式
"""
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

"""
plt.style.use('_mpl-gallery')

fig, ax = plt.subplots(figsize=(8.8, 5), facecolor='lightskyblue',
                       layout='constrained')
ax.plot(input_values, squares,linewidth=3)

#设置图片的标题
fig.suptitle('My first picture')

#设置图表标题并给坐标轴加上标签
ax.set_title('square number', loc='center', fontstyle='oblique', fontsize='medium')
ax.set_xlabel('value', fontsize=14, labelpad=1, loc='right')
ax.set_ylabel('values\'square', fontsize=14,loc='top')

#设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)


plt.show()


