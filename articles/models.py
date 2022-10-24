from django.db import models

# Create your models here.

# 이걸 어떻게 연결 시켜야지?!
class Tech(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Article(models.Model):
    

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    link = models.URLField()
    company = models.TextField()
    tech = models.TextField()
    thumbnail = models.ImageField(null=True)



