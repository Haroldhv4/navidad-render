from django.db import models

# Create your models here.
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    cedula=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    direccion=models.TextField()
    fecha_nacimiento=models.DateField()
    correo=models.EmailField()


    def __str__(self):
        fila="{0}: {1} {2}"
        return fila.format(self.cedula,self.apellido,self.nombre)
