from django.db import models

# Create your models here.

class Piso(models.Model):
    num_piso=models.PositiveIntegerField()  
    class Meta:
        db_table='piso'

class Habitacion(models.Model):
    num_habitacion=models.PositiveIntegerField(unique=True)
    capacidad=models.PositiveIntegerField()
    piso=models.ForeignKey(Piso, on_delete=models.CASCADE,
                            null=False, blank=False, 
                            related_name='habitaciones')
        
    class Meta:
        db_table='habitacion'
    
class Paciente(models.Model):
    cc_paciente=models.PositiveIntegerField()
    nombre=models.CharField(max_length=20)
    habitacion = models.OneToOneField(Habitacion, on_delete=models.CASCADE, 
                                      null=False, blank=False, 
                                      related_name='pacientes')
    class Meta:
        db_table='paciente'

class Visitante(models.Model):
    cc_visitante=models.PositiveIntegerField()
    rostro=models.ImageField(null=True, blank=True)
    estado=models.CharField(max_length=20)
    habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE, 
                                 null=False, blank=False, related_name='visitantes')
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, 
                                null=True, blank=True, related_name='visitantes')
    class Meta:
        db_table='visitante'

