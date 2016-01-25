from __future__ import unicode_literals
from datetime import datetime, time
from django.db import models

class Manufacturer(models.Model):
	name = models.TextField(max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'manufacturers'

class Product(models.Model):
	name = models.TextField(max_length=100)
	price = models.FloatField()
	description = models.TextField(max_length=50)
	manufacturer = models.ForeignKey(Manufacturer)
	created_at = models.DateTimeField(default = datetime.now())
	updated_at = models.DateTimeField(default = datetime.now())
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'products'