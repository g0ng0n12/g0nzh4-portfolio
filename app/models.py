from django.db import models


# Create your models here.
class Job(models.model):
    EMPLOYMENT_TYPE = [("FULL-TIME", "FULL TIME"),
                       ("PART-TIME", "PART TIME"),
                       ("SELF-EMPLOYED", "SELF-EMPLOYED"),
                       ("FREELANCE", "FREELANCE")]

    title = models.CharField(max_lenght=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_lenght=50)
    image = models.ImageField(upload_to='images/')
    issuing_organization = models.CharField(max_lenght=50)
    description = models.CharField(max_length=200)
    finish_date = models.DateTimeField()
    url = models.URLField(max_length=200)
    certification_id = models.CharField(max_lenght=50)

    def __str__(self):
        return self.name