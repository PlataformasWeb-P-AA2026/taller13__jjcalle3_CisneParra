from django.shortcuts import render

from rest_framework import viewsets, permissions

from inmobiliaria.models import Edificio, Departamento
from inmobiliaria.serializers import EdificioSerializer, DepartamentoSerializer


# ---------------------------------------------------------
# Vistas normales (menú y listados en tabla)
# ---------------------------------------------------------

def menu(request):
    """
        Página principal: menú con acceso a los listados
        de Edificios y Departamentos.
    """
    return render(request, 'menu.html')


def lista_edificios(request):
    """
        Lista todos los Edificios registrados en una tabla.
    """
    edificios = Edificio.objects.all()
    contexto = {'edificios': edificios, 'numero_edificios': edificios.count()}
    return render(request, 'edificios.html', contexto)


def lista_departamentos(request):
    """
        Lista todos los Departamentos registrados en una tabla.
    """
    departamentos = Departamento.objects.all()
    contexto = {'departamentos': departamentos, 'numero_departamentos': departamentos.count()}
    return render(request, 'departamentos.html', contexto)


# ---------------------------------------------------------
# API REST (servicios web) - acceso protegido con Token
# ---------------------------------------------------------

class EdificioViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite listar, crear, actualizar y
    eliminar Edificios. Requiere autenticación (token).
    """
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite listar, crear, actualizar y
    eliminar Departamentos. Requiere autenticación (token).
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
