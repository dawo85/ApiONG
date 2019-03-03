import requests

class ApiOpenaid(object):

	URL = 'http://datastore.iatistandard.org/api/1/access/activity'
	HEADERS = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	} 
	DIFF_YEAR = 5
	LIMIT = 500

	def get_beetween_years(self, year):
		self.year_end = str(int(year)-1)
		self.year_initial = str(int(year)-self.__class__.DIFF_YEAR)
		return self.year_initial, self.year_end

	def get_params(self, code_country, year):
		self.get_beetween_years(year)
		start_date = '{0}-01-01'.format(self.year_initial)
		end_date = '{0}-12-31'.format(self.year_end)
		params ={
			'recipient-country': code_country,
			'start-date__gt': start_date,
			'end-date__lt': end_date,
			'limit': self.__class__.LIMIT
		}
		return params

	def get_session(self):
		session = requests.session()
		return session


	def get_activities(self, code_country, year):
		session = self.get_session()
		params = self.get_params(code_country, year)
		print(params)
		response = session.get(self.__class__.URL, params=params, headers=self.__class__.HEADERS)
		return response