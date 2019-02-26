from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'default_data': ''}
    return render(request, 'campus/index.html', context)