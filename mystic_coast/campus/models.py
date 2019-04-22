from django.db import models
import logging

DEFAULT_HOURS = '8AM - 10PM'

class Item(models.Model):
    price = models.FloatField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default='No description')
  
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, default='(xxx) xxx-xxxx')
    description = models.CharField(max_length=300, default='No description added')

    #Ideally, should convert this to JSONField
    #Only a temporary solution for the time being
    sunday = models.CharField(max_length=20, default=DEFAULT_HOURS)
    monday = models.CharField(max_length=20, default=DEFAULT_HOURS)
    tuesday = models.CharField(max_length=20, default=DEFAULT_HOURS)
    wednesday = models.CharField(max_length=20, default=DEFAULT_HOURS)
    thursday = models.CharField(max_length=20, default=DEFAULT_HOURS)
    friday = models.CharField(max_length=20, default=DEFAULT_HOURS)
    saturday = models.CharField(max_length=20, default=DEFAULT_HOURS)

    #initial null list of item_list 
    item_list = models.ManyToManyField(Item)

    #returns the average price of an item at a restaruant 
    def get_average_price(self):
        #creates iterable list of item_list
        item_list = self.item_list.all()
        if not item_list:
            #case for empty list of item_list
            return 'N/A'
        else:
            num_item_list =  0
            total_price = 0
            #obtains iterable list of item_list
            for i in item_list:
                num_item_list += 1
                total_price += i.price
            return float(total_price / num_item_list)

    def get_min_price(self):
        #obtains iterable list of item_list
        item_list = self.item_list.all()
        if not item_list:
            #case for empty list of item_list
            return 'N/A'
        else:
            min_price = item_list[0].price
            for i in item_list:
                if i.price < min_price:
                    min_price = i.price
            return min_price

    def get_max_price(self):
        #obtains iterable list of item_list
        item_list = self.item_list.all()
        if not item_list:
            #case for empty list of item_list
            return 'N/A' 
        else:
            max_price = item_list[0].price
            for i in item_list:
                if i.price > max_price:
                    max_price = i.price
            return max_price

    def get_median_price(self):
        #obtains iterable list of item_list
        item_list = self.item_list.all()
        if not item_list:
            #case for empty list of item_list
            return 'N/A' 
        else:
            #creates list of item prices
            prices = [] 
            for i in item_list:
                prices.append(i.price)
            #sorts list of item_list
            prices.sort()
            num_item_list = len(prices)
            index = int(num_item_list / 2)
            return prices[index]

    def get_cheapest_item(self):
        item_list = self.item_list.all()
        if not item_list:
            return 'N/A'
        else:
            cheap_price = self.get_min_price()
            cheap_item = None
            for i in item_list:
                if i.price == cheap_price:
                    cheap_item = i.name
                    break
        return cheap_item

    def get_most_expensive(self):
        item_list = self.item_list.all()
        if not item_list:
            return 'N/A'
        else:
            high_price = self.get_max_price()
            expensive_item = None
            for i in item_list:
                if i.price == high_price:
                    expensive_item = i.name
                    break
        return expensive_item

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


