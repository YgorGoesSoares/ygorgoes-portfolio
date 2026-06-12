from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('painel-controle/', admin.site.urls),
    path('', include('core.urls')),
]
