from django.db import models
from django.contrib.auth.models import User

class Produtos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.IntegerField()
    descricao = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = ('Produtos')

class Vendidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.IntegerField()
    descricao = models.TextField(blank=True)
    data = models.CharField(max_length=8)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = ('Vendidos')

