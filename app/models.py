from django.db import models


# Create your models here.
class Job(models.model):
    name = models.CharField(max_lenght=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_lenght=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    finish_date = models.DateTimeField()
    url = models.CharField()
