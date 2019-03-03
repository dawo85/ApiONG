from ApiOpenaid.apis.api_openaid import ApiOpenaid
from CallsRegisters.models import Register
from CallsRegisters.models import AidMonetary
from CallsRegisters.models import Country
import json
from ApiOpenaid.serializer.api_activities_serializer import ActivitiesSerializer
from django.db import transaction

class KeysApi(object):
	iati_activities = 'iati-activities'
	iati_activity = 'iati-activity'
	iso_date = 'iso-date'
	value = 'value'
	text = 'text'
	provider_org ='provider-org'
	transaction = 'transaction'
	transaction_date = 'transaction-date'
	ref = 'ref'
	narrative = 'narrative'


class AidMonetaryQueries(object):

	def get_list_year(self, year_initial, year_end):
		years = []
		for i in range(int(year_initial), int(year_end)+1):
			years.append(str(i))
		return years

	def delete(self, year_initial, year_end, country):
		years = self.get_list_year(year_initial, year_end)
		AidMonetary.objects.filter(year__in=years, country__code=country).delete()


	def get_info(self, country, year):
		year_initial, year_end = ApiOpenaid().get_beetween_years(year)
		years = self.get_list_year(year_initial, year_end)
		list_aids = AidMonetary.objects.filter(year__in=years, country__code=country)
		result = ActivitiesSerializer(list_aids).data
		return result

	def get_company_names(self, transaction):
		company = ''
		if KeysApi.ref in transaction[KeysApi.provider_org]:
			company = transaction[KeysApi.provider_org][KeysApi.ref]
		if KeysApi.narrative in transaction[KeysApi.provider_org]:
			narrative = transaction[KeysApi.provider_org][KeysApi.narrative]
			if type(narrative) == list:
				narrative = narrative[0]
			if company:
				company += ' - '
			company += narrative
		return company

	def create(self, country, data):
		for transaction in data:
			if type(transaction) == dict and KeysApi.provider_org in transaction:
				year = transaction[KeysApi.transaction_date][KeysApi.iso_date].split('-')[0]
				if KeysApi.value in transaction:
					company = self.get_company_names(transaction)
					budget_value = float(transaction[KeysApi.value][KeysApi.text])
					aid = AidMonetary.objects.filter(year=year, company=company, country=country).first()
					if aid:
						aid.add_budget(budget_value)
					else:
						aid = AidMonetary(company=company, country=country, budget=budget_value, year=year)
						aid.save()


class CountryQueries(object):

	def create_aids_from_country(self, country, data):
		queries = AidMonetaryQueries()
		for activity in data[KeysApi.iati_activities]:
			if KeysApi.iati_activity in activity and KeysApi.transaction in activity[KeysApi.iati_activity]:
				queries.create(country, activity[KeysApi.iati_activity][KeysApi.transaction])

	def create(self, country, data):
		country_obj = Country.objects.filter(code=country).first()
		if not country_obj:
			country_obj = Country(code=country)
			country_obj.save()
		self.create_aids_from_country(country_obj, data)


class RegisterQueries(object):

	def create(self, country, year):
		year = str(int(year) + 1)
		register = Register(country=country, year=year)
		register.save()


class UpdateData(object):

	def update(self, country, year_initial, year_end, data):
		AidMonetaryQueries().delete(year_initial, year_end, country)
		CountryQueries().create(country, data)
		RegisterQueries().create(country, year_initial)



class ActivitiesData(object):

	CODE_OK = 200

	def exist_last_search(self, country, year):
		check = Register.objects.filter(country=country, year=year).first()
		return check

	def update_datas(self, country, year):
		api = ApiOpenaid()
		response = api.get_activities(country, year)
		if response.status_code == self.__class__.CODE_OK:
			data = json.loads(response.content)
			UpdateData().update(country, api.year_initial, api.year_end, data)
			result = AidMonetaryQueries().get_info(country, year)
		else:
			result = json.loads(response.content)
		return result

	def get_data(self, country, year):
		if self.exist_last_search(country, year):
			result = AidMonetaryQueries().get_info(country, year)
		else:
			result = self.update_datas(country, year)
		return result
