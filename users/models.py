from django.db import models
from django.contrib.auth.models import AbstractUser

class utilisateur(AbstractUser):
    description = models.TextField(max_length=100, blank=True, null=True)
    categorie = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class photo(models.Model):
    id = models.AutoField(primary_key=True)
    photo=models.ImageField(upload_to='images',default='media/default.png')
    user = models.ForeignKey(utilisateur,on_delete=models.CASCADE)

