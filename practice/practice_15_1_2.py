import matplotlib.pyplot as plt

x_inputs = range(1, 5000)
y_inputs = [x**2 for x in x_inputs]

def catter_500_plt(ax):
	#设置轴
	ax.set_xlabel('value', loc='right')
	ax.set_ylabel('square',rotation=0,labelpad=-3, loc='top')
	ax.axis([1, 5000,0,10000000])

	#设置图表标题
	ax.set_title('5000\'s square')

	ax.scatter(x_inputs, y_inputs,c=y_inputs, cmap=plt.cm.Blues, s=3)


fig ,ax = plt.subplots(figsize=(10, 5),layout='constrained')
catter_500_plt(ax)

plt.show()




