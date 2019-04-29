from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.register, name='index'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]