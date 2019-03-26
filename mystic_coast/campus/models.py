from django.db import models
import logging

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
    items = models.ManyToManyField(Item) # WASSIM: I get an error because Item is called before it has been assigned

    #returns the average price of an item at a restaruant 
    def get_average_price(self, items):
        #creates iterable list of items
        items_list = items.all()
        if not items_list:
            #case for empty list of items
            return 'There are no items at this restaurant'
        else:
            num_items =  0
            total_price = 0
            #obtains iterable list of items
            for i in items_list:
                num_items += 1
                total_price += i.price
            return float(total_price / num_items)

    def get_min_price(self, items):
        #obtains iterable list of items
        items_list = items.all()
        if not items_list:
            #case for empty list of items
            return 'There are no items at this restaurant'
        else:
            min_price = items_list[0].price
            for i in items_list:
                if i.price < min_price:
                    min_price = i.price
            return min_price

    def get_max_price(self, items):
        #obtains iterable list of items
        items_list = items.all()
        if not items_list:
            #case for empty list of items
            return 'There are no items at this restaurant' 
        else:
            max_price = items_list[0].price
            for i in items_list:
                if i.price > max_price:
                    max_price = i.price
            return max_price

    def get_median_price(self, items):
        #obtains iterable list of items
        items_list = items.all()
        if not items_list:
            #case for empty list of items
            return 'There are no items at the restaurant' 
        else:
            #creates list of item prices
            prices = [] 
            for i in items_list:
                prices.append(i.price)
            #sorts list of items
            prices.sort()
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
    favorite_restaurant_list = models.ManyToManyField(Restaurant)
    
    def add_favorite_restaurant(self, restaurant):
        self.favorite_restaurant_list.add(restaurant)

    '''
    
    DERRICK: For Reference on how to create an iterable 
    from a ManyToManyField

    '''
    def test(self):
        my_list = self.favorite_restaurant_list.all()
        print('Restaurant Name: %s' % my_list[0].name)


