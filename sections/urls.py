from django.urls import path
from .views import home_section

urlpatterns = [
    path('home_section/', home_section , name="home_section"),
]
