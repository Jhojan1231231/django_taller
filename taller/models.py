from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class reparacion(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_ingreso = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Reparación de {self.cliente.nombre} {self.cliente.apellido} - {self.estado}"
