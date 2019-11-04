from django.db import models
from users.models import utilisateur

class message(models.Model):
    utilfrom = models.ForeignKey(utilisateur, on_delete=models.CASCADE,related_name='fromuser')
    utilto = models.ForeignKey(utilisateur, on_delete=models.CASCADE,related_name='touser')
    texte=models.TextField(max_length=300)

    def __str__(self):
        return self.texte
