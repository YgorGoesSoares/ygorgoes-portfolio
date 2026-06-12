from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('network/', views.network, name='network'),
    path('certificacoes/', views.certificacoes, name='certificacoes'),
    path('contato/', views.contato, name='contato'),
    path('cliente/', views.client_login, name='client_login'),
]
