from django.db import models

# Create your models here.

class Todo (models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=18)
    obs = models.TextField(blank=True, null=True)
    cadastrado = models.DateTimeField(auto_now_add=True)
    finalizado_done = models.BooleanField(default=False)  