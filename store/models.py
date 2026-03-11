from django.db import models

# Create your models here.

# clave primaria personalizada
class Producto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True, default="c0000") # "c001"
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    



# Claves primarias compuestas

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Inscripciones(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('estudiante', 'curso') # el registro combinado de estudiante - curso -> será único

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre}"