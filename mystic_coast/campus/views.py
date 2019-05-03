from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from .models import Restaurant, Item, User
from .verification import verify_restaurant, verify_item
from .verification import save_restaurant_log
from campus.forms import SaveRestaurantForm
import random
import json

def index(request):
    context = {}
    return get_five_restaurants(request)

def restaurant_list(request, context = {}):
    restaurant_list = Restaurant.objects.all()
    context['restaurant_list'] = restaurant_list
    return render(request, 'campus/restaurant-list.html', context)

def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant.delete()
    
    return HttpResponseRedirect(reverse('campus:restaurant_list'))


def delete_item(request, restaurant_id, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()

    return HttpResponseRedirect(reverse('campus:restaurant_detail', kwargs={'restaurant_id': restaurant_id}))


def average_restaurant_list(request):
    #average_restaurant_list = Restaurant.objects.all()
    #context = {'average_restaurant_list': average_restaurant_list}
    print("test")
    #return render(request, 'campus/restaurant-list.html', context)


def restaurant_detail(request, restaurant_id, context={}):
    
    try: 
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    context['restaurant'] = restaurant
    
    return render(request, 'campus/restaurant-detail.html', context)

'''
    Method to add a restaurant to the database. Takes in a 
    JSON-formatted string, parses it, and stores its individual
    attributes into a restaruant and saves it
'''
def add_restaurant_action(request, context = {}):
    context = {}

    if request.method == 'POST':
        preliminary_info_form = SaveRestaurantForm(request)

    else:
        preliminary_info_form = SaveRestaurantForm()
        
        context['preliminary_info_form'] = preliminary_info_form

        return render(request, 'campus/add-restaurant.html', context)
  

def edit_restaurant(request, restaurant_id):
    context = {}

    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        context['name'] = restaurant.name
        context['location'] = restaurant.location
        context['phone_number'] = restaurant.phone_number
        context['description'] = restaurant.description
       
        context['sunday'] = restaurant.sunday
        context['monday'] = restaurant.monday
        context['tuesday'] = restaurant.tuesday
        context['wednesday'] = restaurant.wednesday
        context['thursday'] = restaurant.thursday
        context['friday'] = restaurant.friday
        context['saturday'] = restaurant.saturday

        context['is_data_preloaded'] = True
        context['restaurant_id'] = restaurant.id

        return render(request, 'campus/add-restaurant.html', context)   

    except Restaurant.DoesNotExist:
        restaurant = None
        return restaurant_list(request)


def add_item(request):
    context = {}
    invalid_form = False

    restaurant_id = request.POST.get('restaurant_id')
    item_id = request.POST.get('item_id')
    
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        try:
            item = Item.objects.get(pk=item_id)
            is_save = True
        except Item.DoesNotExist:
            is_save = False

        item_name = request.POST.get('item_name', '')
        item_price = request.POST.get('item_price', 0)
        item_description = request.POST.get('item_description', '')

        context['item_name'] = item_name
        context['item_price'] = item_price
        context['item_description'] = item_description

        if is_save:
            context['item_id'] = item.id
            context['is_item_prefilled'] = True

        if item_price == '':
            item_price = 0

        form_status = verify_item.preliminary_info(item_name, item_price)

        if form_status == 'SUCCESS':
            if is_save:
                item.name = item_name
                item.price = item_price
                item.description = item_description
                item.save()
            else:
                item = Item(name=item_name, price=item_price, description=item_description)
                item.save()
                restaurant.item_list.add(item)
        else:
            invalid_form = True

            if form_status == 'NAME_LENGTH':
                context['form_error'] = """Oops! Your item's
                name needs to be larger than zero characters, and 
                no greater than 50 characters"""
            elif form_status == 'PRICE_VALUE':
                context['form_error'] = """Oops! Your item's price 
                price needs to be within the range: $0 - $1000"""

    except Restaurant.DoesNotExist:
        restaurant = None

    if invalid_form:
        return restaurant_detail(request, restaurant.id, context)
    else:
        return HttpResponseRedirect(reverse('campus:restaurant_detail',
            kwargs={'restaurant_id': restaurant_id}))
    

def load_item(request, item_id, restaurant_id):
    context = {}
    
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    item = Item.objects.get(pk=item_id)

    context['item_id'] = item.id
    context['item_name'] = item.name
    context['item_price'] = item.price
    context['item_description'] = item.description
    context['is_item_prefilled'] = True

    return restaurant_detail(request, restaurant.id, context=context)


def add_restaurant_page(request, context={}):
    context = {}

    if request.method == 'POST':
        preliminary_info_form = SaveRestaurantForm(request)

    else:
        preliminary_info_form = SaveRestaurantForm()
        
        context['preliminary_info_form'] = preliminary_info_form



'''def add_favorite_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        #'root' to be replaced by session username
        current_user = User.objects.get(username='root') 
        current_user.add_favorite_restaurant(restaurant)
        current_user.save()
        print("favorited")

    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    return render(request, 'campus/restaurant-list.html', {})'''


#4/2 Derrick
def user_profile(request):
    return render(request, 'campus/user_profile.html', {})

def get_five_restaurants(request):
    list = Restaurant.objects.all()
    unique_list = []
    largest_index = len(list) - 1
    context = {}

    if len(list) >= 3:
        for i in range(3):
            #uwu
            rand_index = random.randint(0, largest_index)
            
            while list[rand_index] in unique_list:
                rand_index = random.randint(0, largest_index)

            unique_list.append(list[rand_index])

        context['restaurant_list'] = unique_list

    return render(request, 'campus/index.html', context)

