from django.db import models

# Create your models here.


class Novels(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    year = models.IntegerField()

    # def __str__(self):
    #     return id