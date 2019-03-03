from django.db import models

class Register(models.Model):
	create_date = models.DateTimeField(auto_now_add=True)
	country =  models.CharField(max_length=250)
	year =  models.CharField(max_length=4)