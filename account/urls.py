from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-room/', views.create_room, name='create_room'),
    path('profile/', views.profile, name='profile'),
    path('add-staff/', views.add_staff, name='add_staff')
]
