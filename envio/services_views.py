from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def costos_view(request):
    paquetes = request.data.get("paquetes", [])

    if not isinstance(paquetes, list) or len(paquetes) == 0:
        return Response(
            {"detail": "El campo 'paquetes' debe ser una lista no vacía."},
            status=status.HTTP_400_BAD_REQUEST
        )

    gran_total = 0
    detalle     = []

    for paquete in paquetes:
        ruta      = paquete.get("ruta", "")
        tipo      = paquete.get("tipo", "")
        peso =  float(paquete.get("peso", 0))

        # Determinar porcentaje de recargo según días de atraso
        if tipo == "normal":
            costo = 3.00
        elif tipo == "fragil":
            costo = 5.50
        elif tipo == "refrigerado":
            costo = 8.00

        if peso <= 5:
            recargo = 0
        elif peso <=10:
            recargo = 2
        else:
            recargo = 4


        recargo     = round(costo * recargo / 100, 2)
        cobro_paquete = round(costo + recargo, 2)
        gran_total = round(gran_total + cobro_paquete, 2)

        detalle.append({
            "ruta":      ruta,
            "recargo": recargo,
            "gran_cobro": cobro_paquete,
        })

    return Response({
        "total_paquetes": len(detalle),
        "total_cobro":  gran_total,
        "detalle":      detalle,
    })


