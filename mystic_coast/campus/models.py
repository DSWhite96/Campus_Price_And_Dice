from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from address.models import AddressField
import logging
import gettext

_ = gettext.gettext
DEFAULT_HOURS = '8:00AM - 10:00PM'

WEEKDAYS = [
    (1, _("Sunday")),
    (2, _("Monday")),
    (3, _("Tuesday")),
    (4, _("Wednesday")),
    (5, _("Thursday")),
    (6, _("Friday")),
    (7, _("Saturday"))
]

class Item(models.Model):
    price = models.FloatField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default='No description')
  
class Restaurant(models.Model):
    
    name = models.CharField(
        verbose_name='Restaurant Name',
        max_length=200
    )

    location = AddressField(
        verbose_name='Location',
        max_length=200,
        on_delete=models.CASCADE
    )

    phone_number = models.CharField(
        verbose_name='(Primary) Phone Number',
        max_length=20, 
        default='(xxx) xxx-xxxx'
    )

    description = models.CharField(
        verbose_name='Tell us abbout your restaurant!',
        max_length=300, 
        default='No description added'
    )

    #User that owns the restaurant
    maintainer = models.ForeignKey( 
        default=None,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
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


class BusinessHours(models.Model):
    restaurant = models.ForeignKey(
        to=Restaurant, 
        on_delete=models.CASCADE
    )

    opening_time = models.TimeField()
    closing_time = models.TimeField()