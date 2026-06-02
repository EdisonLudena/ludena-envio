from rest_framework import serializers
from .models import Ruta, Paquete

class RutaSerializer(serializers.ModelSerializer):
    total_paquetes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = Ruta
        fields = ["id", "codigo"]

    def get_total_paquetes(self, obj):
        return obj.socios.filter(activo=True).count()

class PaqueteSerializer(serializers.ModelSerializer):
    ruta_codigo = serializers.CharField(source="ruta.codigo", read_only=True)

    class Meta:
        model  = Paquete
        fields = ["id", "ruta", "codigo_rastreo", "destinatario", "peso", "tipo", "estado"]