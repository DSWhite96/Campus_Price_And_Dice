from django.urls import path
from . import views

app_name = 'campus'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_restaurant', views.add_restaurant, name='add_restaurant')
]