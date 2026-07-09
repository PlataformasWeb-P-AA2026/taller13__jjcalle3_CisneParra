"""
    Manejo de urls para la aplicación inmobiliaria
"""
from django.urls import path, include
from rest_framework import routers

from inmobiliaria import views

router = routers.DefaultRouter()
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('', views.menu, name='menu'),
    path('edificios/', views.lista_edificios, name='lista_edificios'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),

    # API REST
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
