from django import forms
from .models import Product
from sections.models import Section

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','price', 'image']

# class ProductForm(forms.Form):
#     name=forms.CharField()
#     description = forms.CharField()
#     price = forms.DecimalField("Price", decimal_places=2, max_digits=8)
#     image = forms.ImageField(upload_to='products/images/' ,null=False , blank=False)
#     section = forms.ModelChoiceField(
#         Section.get_all_sections(),required=False
#     )
class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
