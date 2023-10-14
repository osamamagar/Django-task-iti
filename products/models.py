from django.db import models
from django.urls import reverse
from sections.models import Section



class Product(models.Model):
    name = models.CharField("Name", max_length=100, null=True)
    description = models.TextField("Description", null=True)
    price = models.DecimalField("Price", decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='products/images/' ,null=False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)





    def __str__(self):
        return self.name
    
    def get_show_url(self):
        return reverse('products:product_detail', args=[self.id])
        
    def get_delete_url(self):
        return reverse('products:delete', args=[self.id])
    
    def get_image_url(self):
        return f"../media/{self.image}"


    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    

