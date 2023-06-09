from django.urls import path
from .views import cadastrar_presenca, listar_presenca

urlpatterns = [
    path('', cadastrar_presenca, name='cadastrar_presenca'),
    path('listar/', listar_presenca, name='listar_presenca'),
]
