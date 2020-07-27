from django.db import models

class Pet(models.Model):
    folio = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    redemption_date = models.DateField()
