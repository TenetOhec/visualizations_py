import json

class ExploreData:
	"""docstring for ExploreData"""
	def __init__(self, filename):
		self.mags, self.titles, self.lons, self.lats = [], [], [], []
		self.filename = filename
		self.create_data()

	def create_data(self):
		"""按需得到数据"""
		with open(self.filename) as f:
			all_eq_data = json.load(f)
		all_eq_dicts = 	all_eq_data['features']
		

		for eq_dict in all_eq_dicts:
			mag = eq_dict['properties']['mag']
			title = eq_dict['properties']['title']
			lon = eq_dict['geometry']['coordinates'][0]
			lat = eq_dict['geometry']['coordinates'][1]
			self.mags.append(mag)
			self.titles.append(title)
			self.lons.append(lon)
			self.lats.append(lat)
