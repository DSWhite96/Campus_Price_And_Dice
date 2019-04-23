from django.urls import path
from . import views

app_name = 'campus'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_restaurant_action/', views.add_restaurant_action, name='add_restaurant_action'),
    #path('favorite_restaurant_<int:restaurant_id>', views.add_favorite_restaurant, name='add_favorite_restaurant'),
    path('add_restaurant/', views.add_restaurant_page, name='add_restaurant'),
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('delete_restaurant_<int:restaurant_id>/', views.delete_restaurant, name='delete_restaurant'),
    path('add_item/', views.add_item, name='add_item'),
    path('load_item/<int:item_id>/<int:restaurant_id>', views.load_item, name='load_item'),
    path('edit_restaurant/<int:restaurant_id>', views.edit_restaurant, name='edit_restaurant'),
    path('user_profile/', views.user_profile, name='user_profile' ),
    path('delete_item_<int:restaurant_id>_<int:item_id>/', views.delete_item, name='delete_item')
]