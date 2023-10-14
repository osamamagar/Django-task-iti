from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import  User
from accounts.forms import  CustomizedUserCreationForm
from django.urls import reverse_lazy

# Create your views here.

def profile(request):
    return redirect('/products/home')



class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/registeration.html'
    form_class = CustomizedUserCreationForm
    success_url = reverse_lazy("login")
