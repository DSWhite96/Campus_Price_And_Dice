from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Restaurant, Item, User

def index(request):
    current_user = User.objects.get(username='root')
    context = {'user': current_user}

    return render(request, 'campus/index.html', context)

def restaurant_list(request):
    restaurant_list = Restaurant.objects.all()
    context = {'restaurant_list': restaurant_list}
    return render(request, 'campus/restaurant-list.html', context)

def compare_restaurants(request):
    context = {'default_data': ''}
    return render(request, 'campus/compare-restaurants.html', context)

def compare_restaurants_action(request):
    first_restaurant = None
    second_restaurant = None

    context = {
        'first_restaurant': first_restaurant,
        'second_restaurant': second_restaurant
    }

    return render(request, 'campus/compare-restaurants.html', context)

def restaurant_detail(request, restaurant_id):
    try: 
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    return render(request, 'campus/restaurant-detail.html', {'restaurant': restaurant})

#3/26
def add_restaurant_form_submission(request):
   
    restaurant_name = request.POST.get('restaurant_name', False)
    restaurant_location = request.POST.get('restaurant_location', False)

    restaurant_reference = Restaurant(name=restaurant_name, location=restaurant_location)
    restaurant_reference.save()

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




