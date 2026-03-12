from django.db import models
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    edad = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    

class Curso(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    cupo = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Inscripciones(models.Model): # RECORDAR NO COMETER EL ERROR DEL PROF --- > LO MODELOS VAN EN SINGULAR
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='activa')

    class Meta:
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre}"



try:
 estudiante = Estudiante.objects.get(correo="email@email.com")
 print(estudiante)
except ObjectDoesNotExist:
 print("Estudiante no existe")