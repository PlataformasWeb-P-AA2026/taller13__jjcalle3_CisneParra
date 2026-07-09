from django.db import models


class Edificio(models.Model):
    """
        Representa un edificio (residencial o comercial)
        que puede contener varios departamentos.
    """
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='residencial')

    def __str__(self):
        return "%s (%s - %s)" % (self.nombre, self.ciudad, self.get_tipo_display())


class Departamento(models.Model):
    """
        Representa un departamento que pertenece
        a un único Edificio (relación 1 a muchos).
    """
    nombre_propietario = models.CharField(max_length=150)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuartos = models.PositiveIntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s - %s" % (self.nombre_propietario, self.edificio.nombre)
