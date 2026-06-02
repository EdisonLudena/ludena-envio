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
    class Tipo(models.TextChoices):
        NORMAL = "normal", "Normal"
        FRAGIL = "fragil", "Fragil"
        REFRIGERADO = "refrigerado", "Refrigerado"
    entregado = models.BooleanField(default=True)

    tipo = models.CharField(
        max_length=20,
        choices=Tipo.choices,
        default=Tipo.FRAGIL
    )

    def __str__(self):
        return f"{self.ruta.codigo} {self.codigo_rastreo} {self.destinatario} {self.peso} {self.tipo} {self.entregado}"