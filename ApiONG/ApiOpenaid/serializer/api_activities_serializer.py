from rest_framework import serializers
from rest_framework.fields import empty
from CallsRegisters.models import AidMonetary
from django.db.models.query import QuerySet



class YearSerializer(object):

	def add_company(self, instance):
		setattr(self, instance.company, instance.budget)
		self.fields.append(instance.company)

	def __init__(self, instance):
		self.fields = []
		self.add_company(instance)

	def __dict__(self):
		result = {}
		for field in self.fields:
			result[field] = getattr(self, field)
		return result

	@property
	def data(self):
		result = {}
		for field in self.fields:
			result[field] = getattr(self, field)
		return result
	

class ActivitiesSerializer(object):
	
	def add_years(self, data):
		for row in data:
			if hasattr(self, row.year):
				year = getattr(self, row.year).add_company(row)
			else:
				setattr(self, row.year, YearSerializer(row))
				self.fields.append(row.year)

	def __init__(self, instance):
		self.fields = []
		self.add_years(instance)

	def __dict__(self):
		result = {}
		for field in self.fields:
			result[field] = getattr(self, field).__dict__
		return result

	@property
	def data(self):
		result = {}
		for field in self.fields:
			result[field] = getattr(self, field).data
		return result










	
	