from django.db import models

from adoption.models import Person


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.name)


class Pet(models.Model):
    # folio = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    redemption_date = models.DateField()
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    vaccine = models.ManyToManyField(Vaccine, blank=True)
    
    def __str__(self):
         return '{}'.format(self.name)
