from django.shortcuts import render

# Create your views here.

def home_section(request):
    return render(request, 'sections/home_section.html')