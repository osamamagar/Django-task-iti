from django.db import models

class Product(models.Model):
    name = models.CharField("Name", max_length=1024, null=True)
    description = models.TextField("Description", null=True)
    price = models.DecimalField("Price", decimal_places=2, max_digits=8)
    image = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
        
