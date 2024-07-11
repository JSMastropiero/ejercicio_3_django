from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import MinValueValidator

class Matriz(models.Model):
    filas = models.IntegerField(validators=[MinValueValidator(1)])
    columnas = models.IntegerField(validators=[MinValueValidator(1)])
    matriz_original = models.TextField()
    matriz_final = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Matriz {self.id} - {self.filas}x{self.columnas}"


