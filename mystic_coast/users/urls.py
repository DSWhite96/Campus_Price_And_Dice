from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.register, name='index'),
    path('load_profile/', views.load_profile, name='load_profile'),
]