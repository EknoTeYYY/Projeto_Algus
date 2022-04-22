from cmath import log
from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name ='home'),
    path('Produtos/', views.prod, name ='produto'),
    path('Adicionar/' ,views.criar, name ='criar'),
    path('Relatório/', views.relatar, name ='rell'),
    path('Excluir/<int:id>', views.excluir, name='excluir'),
    path('Editar/<int:id>', views.editar, name='editar'),
    path('Diminuir/<int:id>', views.diminuir, name='diminuir'),
    path('Info/<int:id>', views.info, name='info')
]

