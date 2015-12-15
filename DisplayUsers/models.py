from django.db import models
from django.utils import timezone

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.firstname+" "+self.lastname
