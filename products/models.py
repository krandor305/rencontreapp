from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    nom=models.CharField(max_length=50)
    Description=models.TextField(max_length=200)
    Image=models.ImageField(upload_to='product_images',default='default.jpg')

    def __str__(self):
        return self.nom

class Productsinnovation(Products):
    innovateur=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class message(models.Model):
    nom=models.TextField(max_length=300)
    Produit=models.ForeignKey('Productsinnovation', on_delete=models.CASCADE)
    innovateur=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
