from django.db import models

# Create your models here.
class crawlingData(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    link = models.URLField()
    company = models.TextField()
    tech = models.TextField()

    def __str__(self):
        return self.title