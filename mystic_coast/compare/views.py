from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from campus.models import Restaurant, Item, User
from .verification import verify_compare
from django.contrib import messages
from django.contrib.messages import get_messages

ERROR = 50 

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

        try:
            second_restaurant = Restaurant.objects.get(name=second_restaurant_name)
            restaurant_compare_list.append(second_restaurant)
        except Restaurant.DoesNotExist:
            invalid_form = True
            form_error = "Oops! %s is not a restaurant" % (second_restaurant_name)

    except Restaurant.DoesNotExist:
        invalid_form = True
        form_error = "Oops! %s is not a restaurant" % (first_restaurant_name)

    name_status = verify_compare.restaurant_names(first_restaurant_name, second_restaurant_name)

    if name_status != 'SUCCESS':
        invalid_form = True
        if name_status == 'DUPLICATE_NAME':
            form_error = "Oops! You can't enter the same restaurant twice"
        elif name_status == 'EMPTY_NAME':
            form_error = "Oops! You can't leave a name blank"
            
    if invalid_form:
        messages.add_message(request, messages.ERROR, form_error, fail_silently=True)
        return HttpResponseRedirect(reverse('compare:index'))

    else:
        context['request_forwarded'] = True
        context['restaurant_compare_list'] = restaurant_compare_list
        return index(request, context)
    
