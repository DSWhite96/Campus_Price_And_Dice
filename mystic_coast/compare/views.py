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

    first_restaurant_name = request.POST.get('first_restaurant', '')
    second_restaurant_name = request.POST.get('second_restaurant', '')
    
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

    first_name = first_restaurant.name
    second_name = second_restaurant.name

    name_status = verify_compare.restaurant_names(first_name, second_name)

    if name_status != 'SUCCESS':
        invalid_form = False
        if name_status == 'DUPLICATE_NAME':
            form_error = "Oops! You can't enter the same restaurant twice"
        elif name_status == 'EMPTY_NAME':
            form_error = "Oops! You can't leave a name blank"
            
        context['form_error'] = form_error

    if invalid_form:
        context['name_error_list'] = name_error_list
    else:
        context['restaurant_compare_list'] = restaurant_compare_list

    return index(request, context)
    
