import requests

class ApiOpenaid(object):

	URL = 'http://datastore.iatistandard.org/api/1/access/activity'
	HEADERS = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	} 
	DIFF_YEAR = 5

	def get_params(self, code_country, year):
		year = int(year)
		start_date = '{0}-01-01'.format(str(year-self.__class__.DIFF_YEAR))
		end_date = '{0}-12-31'.format(str(year-1))
		params ={
			'recipient-country': code_country,
			'start-date__gt': start_date,
			'end-date__lt': end_date
		}
		return params

	def get_session(self):
		session = requests.session()
		return session


	def get_activities(self, code_country, year):
		session = self.get_session()
		params = self.get_params(code_country, year)
		response = session.get(self.__class__.URL, params=params, headers=self.__class__.HEADERS)
		return response