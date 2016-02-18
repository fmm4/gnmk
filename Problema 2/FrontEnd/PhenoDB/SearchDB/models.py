
from django.db import models


class PhenoDB(models.Model):
	phenogene = models.CharField(max_length=20)
	phenoilln = models.CharField(max_length=150)
	def __str__(self):
		return self.phenogene