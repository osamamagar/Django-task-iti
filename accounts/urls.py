from django.urls import path , include
from .views import CreateCustomUser, profile 
from accounts.views import profile_view ,edit_profile , delete_profile



urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/',profile,name="profile"),
    path('register/',CreateCustomUser.as_view(), name='accounts.create'),
    path('profile_view/', profile_view, name='profile_view'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/',delete_profile, name='delete_profile'),


]

