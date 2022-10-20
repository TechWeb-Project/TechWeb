from django.db import models


# Create your models here.


class Tech(models.Model):
    name = models.CharField(max_lenght=50)

    def __str__(self):
        return self.name


class Comapny(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    tech = models.ManyToManyField(Tech, on_delete=models.CASCADE)
