from django.shortcuts import render , redirect

# Create your views here.

def profile(request):
    return redirect('/products/home')
