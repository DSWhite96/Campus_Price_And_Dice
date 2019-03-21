from django.http import HttpResponse
from django.shortcuts import render
from .models import Restaurant, Item

def index(request):
    context = {'default_data': ''}
    return render(request, 'campus/index.html', context)

def restaurant_list(request):
    context = {'default_data': ''}
    return render(request, 'campus/restaurant-list.html', context)

def compare_restaurants(request):
    context = {'default_data': ''}
    return render(request, 'campus/compare-restaurants.html', context)

def add_restaurant(request):
    context = {'default_data': ''}
    pass

def restaurant_detail(request, restaurant_id):
    try: 
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    return render(request, 'campus/restaurant-detail.html', {'restaurant': restaurant})

def add_restaurant_page(request):
    return render(request, 'campus/add-restaurant.html', {})





