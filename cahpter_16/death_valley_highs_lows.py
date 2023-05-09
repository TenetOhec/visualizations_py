import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader =csv.reader(f)
	header_row = next(reader)

#	for index , column_header in enumerate(header_row):
#		print(index,column_header)

	#从文件中获取日期和最高温度
	dates,highs, lows = [],[],[]
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:				
			dates.append(current_date)
			highs.append(high)
			lows.append(low)	

	
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
