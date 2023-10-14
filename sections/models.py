from django.db import models
from django.shortcuts import  reverse


class Section(models.Model):
    name= models.CharField(max_length=100, unique=True)
    description=  models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_all_sections(cls):
        return  cls.objects.all()

    def get_image_url(self):
        return f"/media/{self.image}"
