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
    #initial null list of items 
    items = []
    def get_average_price(self, items):
        num_items =  0
        total_price = 0
        for i in items:
            num_items += 1
            total_price += i.price
        return float(total_price / num_items)

    def get_min_price(self, items):
        if not items:
            return 'There are no items at this restaurant'#case for empty list of items
        else:
            min_price = items[0].price
            for i in items:
                if i.price < min_price:
                    min_price = i.price
            return min_price

    def get_max_price(self, items):
        if not items:
            return 'There are no items at this restaurant' #case for empty list of items
        else:
            max_price = items[0].price
            for i in items:
                if i.price > max_price:
                    max_price = i.price
            return max_price

    def get_median_price(self, items):
        if not items:
            return 'There are no items at the restaurant' #case for empty list of items
        else:
            prices = [] #creates list of item prices
            for i in items:
                prices.append(i.price)
            prices.sort()#sorts list of items
            num_items = len(prices)
            index = int(num_items / 2)
            return prices[index]



class Item(models.Model):
    price = models.FloatField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    is_admin = models.BooleanField()
    favorite_restaurants = models.ManyToManyField(Restaurant)
    