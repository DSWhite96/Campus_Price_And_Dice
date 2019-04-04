from django.urls import path
from . import views

app_name = 'campus'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_restaurant_action/', views.add_restaurant_action, name='add_restaurant_action'),
    path('add_restaurant/', views.add_restaurant_page, name='add_restaurant'),
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('compare_restaurants/', views.compare_restaurants, name='compare_restaurants'),
    path('compare_restaurants_action/', views.compare_restaurants_action, name='compare_restaurants_action'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('user_profile/', views.user_profile, name='user_profile' )
]