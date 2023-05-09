import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	inf = {}
	#枚举函数enumerate()可获取每个元素的索引及其值

	for index, column_header in enumerate(header_row):
		inf[column_header] = int(index)
	print(inf)	
	"""
	0 STATION
	1 NAME
	2 DATE
	3 PRCP
	4 TAVG
	5 TMAX
	6 TMIN
	"""
	#从文件中获取日期和最高温度
	dates,highs, lows = [],[],[]
	for row in reader:
		high = int(row[inf['TMAX']])
		low = int(row[inf['TMIN']])
		current_date = datetime.strptime(row[inf['DATE']], '%Y-%m-%d')
		dates.append(current_date)
		highs.append(high)
		lows.append(low)


#print(highs)

#根据最高温度绘制图形 alpha颜色透明度 0为完全透明 1位默认完全不透明	
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形格式
ax.set_title('2018 Everyday\'highest F', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('(F)', fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()
