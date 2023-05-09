from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


#创建一个D6
die_1 = Die()
die_2 = Die(10) 
#掷几次骰子并将结果存储在一个列表里
results=[]
for roll_num in range(5000):
	result1 = die_1.roll()
	result2 = die_2.roll()
	results.append(result1+result2)

#分析结果
""""
frequencies = []
for value in range(2, die_1.num_sides+die_2.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
"""
#使用列表解析
frequencies =[results.count(value) for value in range(2,die_1.num_sides + die_2.num_sides + 1)]	

#对结果可视化
x_values = list(range(2, die_1.num_sides+die_2.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'results','dtick': 1}
y_axis_config = {'title': 'results\'s frequency'}
my_layout = Layout(title='results of rool D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d10_5000.html')



		