from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    hours_of_operation = {
        'sunday': models.CharField(max_length=20),
        'monday': models.CharField(max_length=20),
        'tuesday': models.CharField(max_length=20),
        'wednesday': models.CharField(max_length=20),
        'thursday': models.CharField(max_length=20),
        'friday': models.CharField(max_length=20)
    }


class Item(models.Model):
    price = models.FloatField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_lenth=200)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    is_admin = models.BooleanField()

    