from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    """Avatar for users."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True, default='default.png')

    def __str__(self) -> str:
        return f"{self.user}"

class Mensajes(models.Model):

    envia = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Envia")
    recibe = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Recibe")
    mensaje = models.TextField()
    enviado = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return f"{self.mensaje[:50]}[...]"