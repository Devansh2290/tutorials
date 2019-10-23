from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length=50)


class BasicInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
