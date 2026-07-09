from django.contrib import admin

from inmobiliaria.models import Edificio, Departamento


class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'ciudad')
    list_filter = ('tipo', 'ciudad')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_propietario', 'costo', 'numero_cuartos', 'edificio')
    search_fields = ('nombre_propietario',)
    raw_id_fields = ('edificio',)


admin.site.register(Departamento, DepartamentoAdmin)
