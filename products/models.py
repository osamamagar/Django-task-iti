from django.db import models
from django.urls import reverse




class Product(models.Model):
    name = models.CharField("Name", max_length=100, null=True)
    description = models.TextField("Description", null=True)
    price = models.DecimalField("Price", decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='products/images/' ,blank=True , null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)





    def __str__(self):
        return self.name
    
    def get_show_url(self):
        return reverse('products:product_detail', args=[self.id])
        
    def get_delete_url(self):
        return reverse('products:delete', args=[self.id])

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    

