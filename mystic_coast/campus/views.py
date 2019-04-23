from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Restaurant, Item, User
from .verification import verify_restaurant, verify_item
import random
import json


def index(request):
    context = {}

    return get_five(request)


def restaurant_list(request):
    restaurant_list = Restaurant.objects.all()
    context = {'restaurant_list': restaurant_list}
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
    data = request.POST
    invalid_form = False
    error_message = ''

    restaurant_id = data.get('restaurant_id', None)

    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        is_save = True
    except Restaurant.DoesNotExist:
        is_save = False

    name = data.get('restaurant_name', '')
    location = data.get('restaurant_location', '')
    phone_number = data.get('phone_number', '')
    description = data.get('restaurant_description', '')
    picture = data.get('document', '')
    
    sunday = data.get('sunday', '')
    monday = data.get('monday', '')
    tuesday = data.get('tuesday', '')
    wednesday = data.get('wednesday', '')
    thursday = data.get('thursday', '')
    friday = data.get('friday', '')
    saturday = data.get('saturday', '')
    
    #Info to send back to the page in-case server-side verification
    #fails
    context['name'] = name
    context['location'] = location
    context['phone_number'] = phone_number
    context['restaurant_description'] = description
    context['sunday'] = sunday
    context['monday'] = monday
    context['tuesday'] = tuesday
    context['wednesday'] = wednesday
    context['thursday'] = thursday
    context['friday'] = friday
    context['saturday'] = saturday

    is_prelim_info_correct = verify_restaurant.preliminary_info(name, location, phone_number)
    
    if not (is_prelim_info_correct == 'SUCCESS'):
        invalid_form = True

        if (is_prelim_info_correct == 'PHONE_LENGTH'):
            error_message = "Your phone number is too large or too small"
        elif (is_prelim_info_correct == 'NAME_LENGTH'):
            error_message = "Your name's length is too large or too small"
        elif (is_prelim_info_correct == 'LOCATION_LENGTH'):
            error_message = "Your location's length is too large or too small"
        else:
            error_message = "Something went wrong!"

        context['form_error'] = error_message
    else:
        if is_save:
            restaurant.name = name
            restaurant.location = location
            restaurant.phone_number = phone_number
            restaurant.description = description
            restaurant.picture = picture

            restaurant.sunday = data['sunday']
            restaurant.monday = data['monday']
            restaurant.tuesday = data['tuesday']
            restaurant.wednesday = data['wednesday']
            restaurant.thursday = data['thursday']
            restaurant.friday = data['friday']
            restaurant.saturday = data['saturday']
        else:
            name = data['restaurant_name']
            location = data['restaurant_location']
            phone_number = data['phone_number']
            description = data['restaurant_description']

            sunday = data['sunday']
            monday = data['monday']
            tuesday = data['tuesday']
            wednesday = data['wednesday']
            thursday = data['thursday']
            friday = data['friday']
            saturday = data['saturday']

    if invalid_form:
        return add_restaurant_page(request, context)
    else:
        
        if not is_save:
            restaurant = Restaurant(name=name, 
                location=location, phone_number=phone_number, description=description, picture=picture, sunday=sunday,
                monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday,
                friday=friday, saturday=saturday)

        restaurant.save()

        return HttpResponseRedirect(reverse('campus:restaurant_detail', 
        kwargs={'restaurant_id': restaurant.id}))


def edit_restaurant(request, restaurant_id):
    context = {}

    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        context['name'] = restaurant.name
        context['location'] = restaurant.location
        context['phone_number'] = restaurant.phone_number
        context['restaurant_description'] = restaurant.description
       
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
    context['is_item_prefilled'] = True

    return restaurant_detail(request, restaurant.id, context=context)


def add_restaurant_page(request, context={}):
    return render(request, 'campus/add-restaurant.html', context)


def add_favorite_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        #'root' to be replaced by session username
        current_user = User.objects.get(username='root') 
        current_user.add_favorite_restaurant(restaurant)
        current_user.save()
        print("favorited")

    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    return render(request, 'campus/restaurant-list.html', {})


#4/2 Derrick
def user_profile(request):
    return render(request, 'campus/user_profile.html', {})

def get_five(request):
    list = Restaurant.objects.all()
    unique_list = []
    largest_index = len(list) - 1
    for i in range(3):
        #uwu
        rand_index = random.randint(0, largest_index)

        while list[rand_index] not in unique_list:
            rand_index = random.randint(0, largest_index)

        unique_list.append(list[rand_index])
    context = {'restaurant_list': unique_list}
    return render(request, 'campus/index.html', context)

