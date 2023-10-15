from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User



class CustomizedUserCreationForm(UserCreationForm):
    first_name = forms.CharField( required=True, help_text="Required. 30 characters or fewer.")
    last_name = forms.CharField( required=True, help_text="Required. 30 characters or fewer.")

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
