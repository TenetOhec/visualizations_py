import plotly.express as px
import pandas as pd
from explore_data import ExploreData

my_data = ExploreData('data/eq_data_30_day_m1.json')

data = pd.DataFrame(data=zip(my_data.lons, my_data.lats, my_data.titles, my_data.mags), columns=["longitude", "dimension", "local", "level"])
#data.head()


fig = px.scatter(
	#x=my_data.lons,
	#y=my_data.lats,
	#labels={'x': 'longitude', 'y': 'dimension'},
	data,
	x="longitude",
	y="dimension",
	range_x=[-200,200],
	range_y=[-90,90],
	width=800,
	height=800,
	title='Global Seismic Scatter Map',
	size = "level",
	size_max=10,
	color="level",
	hover_name="local",

)
fig.write_html('global_earthquakes.html')
fig.show()