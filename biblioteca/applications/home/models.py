from django.db import models

# Create your models here.
class Persona(models.Model):
    full_name = models.CharField(
        'nombres', 
        max_length=50
    )
    pais = models.CharField(
        'pais', 
        max_length=30
    )
    pasaporte = models.CharField(
        'pasaporte', 
        max_length=30
    )
    edad = models.IntegerField()
    apelativo = models.CharField(
        'Apelativo',
        max_length=10
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table='persona'
        unique_together=['apelativo']
        constraints=[
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayr_18')
        ]
        # abstract=True

    def __str__(self):
        return self.full_name

class Empleados(Persona):
    empleado = models.CharField(
        'Empleo', 
        max_length=50
    )

class Cliente(Persona):
    email = models.EmailField(
        'Cliente', 
        max_length=254
    )
    
    