from django.db import models

# Create your models here.
class Inventory(models.Model):

	name			= models.CharField(max_length=120)
	description		= models.TextField()
	quantity		= models.DecimalField(decimal_places=3, max_digits=20)
	unit			= models.CharField(max_length=20)
	place 			= models.CharField(max_length=20)