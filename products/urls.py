from django.urls import path
from .views import Home ,contact_us ,about_us , product_detail ,delete ,search


app_name = 'products'

urlpatterns = [
    path('home/', Home , name='home'),
    path('contact_us/', contact_us, name='contact_us'),
    path('about_us/', about_us, name='about_us'),
    path('product_detail/<int:id>', product_detail, name='product_detail'),
    path('product/<int:id>/delete', delete, name='delete'),
    path('search/' , search ,name="search" ),


]
