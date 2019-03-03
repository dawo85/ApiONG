from django.db import models

class AidMonetary(models.Model):
	company = models.CharField(max_length=250)
	budget = models.FloatField()
	year = models.CharField(max_length=4)
	country = models.ForeignKey('CallsRegisters.Country', related_name='aids', on_delete=models.CASCADE)

	class Meta:
		ordering = ('year', '-budget',)

	def add_budget(self, value):
		self.budget += value
		self.save()