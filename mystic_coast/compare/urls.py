from django.urls import path
from . import views

app_name = 'compare'
urlpatterns = [
    path('', views.index, name='index'),
    path('compare_restaurants/', views.compare_restaurants, name='compare_restaurants'),
]