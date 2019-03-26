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
    
    '''

        DERRICK:

        Hey Derrick, thanks for the work! There is a slight correction that 
        should be made, but it won't require changing much of your code. 
        (Just some slight additions)
        
        Replace the initialization of the 'items' list with the commented
        code to the right of it. This creates a list-type object called a 
        'ManyToManyField'. Think of it as a data type mapped to the database.

        
        And then before accessing each item of the list, follow the steps in the 
        comment block below! 

    '''

    #initial null list of items 
    items = [] # DERRICK: items = models.ManyToManyField(Item)

    '''
        DERRICK:

        To create and access an list from a ManyToManyField, you'll do the following:
            my_list = items.all() #This returns an iterable object of all items
            for item in my_list: 
                etc.
    '''

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


