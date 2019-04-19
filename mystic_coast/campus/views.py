from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Restaurant, Item, User
from .verification.add_restaruant import VerifyRestaurant
from .verification.add_item import VerifyItem
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

def add_restaurant_action(request):
    data = request.POST
    invalid_form = False
    error_message = ''
    context = {}

    '''
    is_prelim_info_correct = Verify.preliminary_info(name, location, phone_number)
    
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

        context['error_message'] = error_message
    '''
    restaurant_id = data.get('restaurant_id', None)

    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        is_save = True
    except Restaurant.DoesNotExist:
        is_save = False

    if is_save:
        restaurant.name = data['restaurant_name']
        restaurant.location = data['restaurant_location']
        restaurant.phone_number = data['phone_number']

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

        sunday = data['sunday']
        monday = data['monday']
        tuesday = data['tuesday']
        wednesday = data['wednesday']
        thursday = data['thursday']
        friday = data['friday']
        saturday = data['saturday']

    if invalid_form:
        return render(request, 'campus/add-restaurant.html', {})
    else:
        
        if not is_save:
            restaurant = Restaurant(name=name, 
                location=location, phone_number=phone_number, sunday=sunday, 
                monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday,
                friday=friday, saturday=saturday)

        restaurant.save()

        '''DERRICK'''
        return HttpResponseRedirect(reverse('campus:restaurant_detail', 
        kwargs={'restaurant_id': restaurant.id}))



def edit_restaurant(request, restaurant_id):
    context = {}

    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)

        context['name'] = restaurant.name
        context['location'] = restaurant.location
        context['phone_number'] = restaurant.phone_number
       
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

        if item_price == '':
            item_price = 0

        form_status = VerifyItem.preliminary_info(item_name, item_price)

        if form_status == 'SUCCESS':
            if is_save:
                item.name = item_name
                item.price = item_price
                item.save()
            else:
                item = Item(name=item_name, price=item_price)
                item.save()
                restaurant.item_list.add(item)
        else:
            if form_status == 'NAME_LENGTH':
                context['item_error'] = """Oops! Your item's
                name needs to larger than zero characters, and 
                no greater than 50 characters"""
            elif form_status == 'PRICE_VALUE':
                context['item_error'] = """Oops! Your item's price 
                price needs to be within the range: $0 - $1000"""

    except Restaurant.DoesNotExist:
        restaurant = None

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
