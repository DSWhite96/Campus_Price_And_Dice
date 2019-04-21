from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from campus.models import Restaurant, Item, User
from .verification import verify_compare

def index(request, context = {}):
    return render(request, 'compare/index.html', context)

def compare_restaurants(request, context = {}):
    name_error_list = []
    restaurant_compare_list = []
    invalid_form = False

    first_restaurant_name = request.POST.get('first_restaurant')
    second_restaurant_name = request.POST.get('second_restaurant')
    
    try:
        first_restaurant = Restaurant.objects.get(name=first_restaurant_name)
        restaurant_compare_list.append(first_restaurant)
    except Restaurant.DoesNotExist:
        invalid_form = True
        name_error_list.append(first_restaurant_name)

    try:
        second_restaurant = Restaurant.objects.get(name=second_restaurant_name)
        restaurant_compare_list.append(second_restaurant)
    except Restaurant.DoesNotExist:
        invalid_form = True
        name_error_list.append(second_restaurant_name)

    if invalid_form:
        context['name_error_list'] = name_error_list
    else:
        context['restaurant_compare_list'] = restaurant_compare_list

    return index(request, context)
    
