from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('campus/', include('campus.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
]