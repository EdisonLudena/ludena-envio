from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Ruta(models.Model):
    codigo = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(120)])

    def __str__(self):
        return self.codigo

class Paquete(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name="paquetes")
    codigo_rastreo = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(120)])
    destinatario = models.CharField(max_length=120)
    peso = models.FloatField(default=0)
    tipo = models.CharField(max_length=120)
    entregado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ruta.codigo} {self.codigo_rastreo} {self.destinatario} {self.peso} {self.tipo} {self.entregado}"