from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100, unique=True)
    publicado = models.DateTimeField(auto_now=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
