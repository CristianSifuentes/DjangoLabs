from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()

