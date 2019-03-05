from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'default_data': ''}
    return render(request, 'campus/index.html', context)

def restaurant_list(request):
    conext = {'default_data': ''}
    return render(request, 'campus/restaurant-list.html', context)

    