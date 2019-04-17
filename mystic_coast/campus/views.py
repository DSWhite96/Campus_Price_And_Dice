from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Restaurant, Item, User
from .verification.add_restaruant import Verify
import json

def index(request):
    current_user = User.objects.get(username='root')
    context = {'user': current_user}

    return render(request, 'campus/index.html', context)

def restaurant_list(request):
    restaurant_list = Restaurant.objects.all()
    context = {'restaurant_list': restaurant_list}
    return render(request, 'campus/restaurant-list.html', context)

def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant.delete()

    '''
        DERRICK: I recommend using 
        return HttpResponseRedirect(request.path_info)
        This redirects the user to the restaurant-list page,
        and if the user refreshes the page, it'll take them back
        to the same page (Try refreshing the page after deleting an item
        with the current code)
    '''
    return restaurant_list(request)

def average_restaurant_list(request):
    #average_restaurant_list = Restaurant.objects.all()
    #context = {'average_restaurant_list': average_restaurant_list}
    print("test")
    #return render(request, 'campus/restaurant-list.html', context)

def compare_restaurants(request, context = None):
    
    if not context:
        context = {'default_data': ''}

    return render(request, 'campus/compare-restaurants.html', context)

def compare_restaurants_action(request):
    name_error_list = []

    first_restaurant_name = request.GET.get('first_restaurant')
    second_restaurant_name = request.GET.get('second_restaurant')
    
    try:
        first_restaurant = Restaurant.objects.get(name=first_restaurant_name)
    except Restaurant.DoesNotExist:
        first_restaurant = None
        name_error_list.append(second_restaurant_name)

    try:
        second_restaurant = Restaurant.objects.get(name=second_restaurant_name)
    except Restaurant.DoesNotExist:
        second_restaurant = None
        name_error_list.append(first_restaurant_name)
        

    context = {
        'first_restaurant': first_restaurant,
        'second_restaurant': second_restaurant,
        'name_error_list': name_error_list
    }
    
    return render(request, 'campus/compare-restaurants.html', context)

def restaurant_detail(request, restaurant_id):
    try: 
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    return render(request, 'campus/restaurant-detail.html', {'restaurant': restaurant})

'''
    Method to add a restaurant to the database. Takes in a 
    JSON-formatted string, parses it, and stores its individual
    attributes into a restaruant and saves it
'''

def add_restaurant_action(request):
    data = request.POST
    invalid_form = False
    error_message = ''
    context = {}

    name = data['restaurant_name']
    location = data['restaurant_location']
    phone_number = data['phone_number']
    
    '''is_prelim_info_correct = Verify.preliminary_info(name, location, phone_number)

    if not (is_prelim_info_correct == 'SUCCESS'):
        invalid_form = True

        if (is_prelim_info_correct == 'PHONE_NUMBER'):
            error_message = "Your phone number is formatted incorrectly"
        elif (is_prelim_info_correct == 'NAME_LENGTH'):
            error_message = "Your name's length is too large or too small"
        elif (is_prelim_info_correct == 'LOCATION_LENGTH'):
            error_message = "Your location's length is too large or too small"
        else:
            error_message = "Something went wrong!"

        context['error_message'] = error_message'''
    
    restaurant = Restaurant(name=name, location=location)
    restaurant.save()

    '''
    for item_index in item_list_dict:
        item = item_list_dict[item_index]
        item_name = item['name']
        item_price = item['price']
        item = Item(name=item_name, price=item_price)
        item.save()
        restaurant.item_list.add(item)
    '''

    if invalid_form:
        return render(request, 'campus/add-restaurant.html', {})
    else:
        return render(request, 'campus/restaurant-detail.html', {'restaurant': restaurant})


def add_restaurant_page(request):
    return render(request, 'campus/add-restaurant.html', {})

def add_favorite_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        #'root' to be replaced by session username
        current_user = User.objects.get(username='root') 
        current_user.add_favorite_restaurant(restaurant)
        current_user.save()

    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    
    return HttpResponseRedirect(request.path_info)

#4/2 Derrick
def user_profile(request):
    return render(request, 'campus/user_profile.html', {})
