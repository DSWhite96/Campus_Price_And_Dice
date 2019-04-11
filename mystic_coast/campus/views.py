from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Restaurant, Item, User
import json

def index(request):
    current_user = User.objects.get(username='root')
    context = {'user': current_user}

    return render(request, 'campus/index.html', context)

def restaurant_list(request):
    restaurant_list = Restaurant.objects.all()
    context = {'restaurant_list': restaurant_list}
    return render(request, 'campus/restaurant-list.html', context)

def delete_restaurant(request, restaurant_name):
    restaurant = Restaurant.objects.get(name=restaurant_name)
    restaurant.delete()
    context = {'restaurant_list': restaurant_list}
    return render(request, 'campus/restaurant-list.html', context)

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
    data = request.POST.get('serializedData', False)
    data = json.loads(data)

    name = data['restaurantName']
    location = data['location']
    phone_number = data['phoneNumber']
    item_list_dict = data['itemList']

    restaurant = Restaurant(name=name, location=location)
    restaurant.save()

    for item_index in item_list_dict:
        item = item_list_dict[item_index]
        item_name = item['name']
        item_price = item['price']
        item = Item(name=item_name, price=item_price)
        item.save()
        restaurant.item_list.add(item)

    return render(request, 'campus/add-restaurant.html', {})


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
