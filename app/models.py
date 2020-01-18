from django.db import models


# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    yoe = models.IntegerField()
    has_certification = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Job(models.Model):
    EMPLOYMENT_TYPE = [("FULL-TIME", "FULL TIME"),
                       ("PART-TIME", "PART TIME"),
                       ("SELF-EMPLOYED", "SELF-EMPLOYED"),
                       ("FREELANCE", "FREELANCE")]

    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    url_company = models.URLField(max_length=200, null=True)
    project = models.CharField(max_length=50, null=True)
    url_project = models.URLField(max_length=200, null=True)
    location = models.CharField(max_length=50)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=70)
    image = models.ImageField(blank=True, null=True, default=None, upload_to='media/images/')
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    current = models.BooleanField(default=False)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title

    def get_description(self):
        return self.description.split('-')


class Certification(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    issuing_organization = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    finish_date = models.DateTimeField()
    url = models.URLField(max_length=200)
    identifier = models.CharField(max_length=50)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='media/images/')
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name


class Note(models.Model):
    Note = models.TextField(null=True, blank=True)
    lang = models.CharField(max_length=50)


class Reading(models.Model):
    name = models.CharField(max_length=50)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)
    url = models.URLField(max_length=200)
    finish_date = models.DateTimeField()
    author = models.CharField(max_length=50)
    url_image = models.URLField(max_length=200)
