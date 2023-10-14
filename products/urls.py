from django.urls import path
from .views import Home ,contact_us ,about_us , product_detail ,delete ,search ,create_product ,edit_product
from django.contrib.auth.decorators import login_required


app_name = 'products'


urlpatterns = [
    path('home/', Home , name='home'),
    path('contact_us/', contact_us, name='contact_us'),
    path('about_us/', about_us, name='about_us'),
    path('products/product_detail/<int:id>/', product_detail, name='product_detail'),
    path('product/<int:id>/delete', delete, name='delete'),
    path('search/' , search ,name="search" ),
    path('create_product/',create_product,name="create_product"),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),




]