from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)
    external_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title