from django.shortcuts import render, get_object_or_404
from .models import Cliente

# Create your views here.

# Obtener desde la base de datos todos los clientes y enviarlos como respuesta
def listar_clientes(request):
    # consultas a la base de datos por medio del modelo
    clientes = Cliente.objects.all()
    total_clientes = Cliente.objects.count()

    # respuesta
    return render(request, 'clientes/listar_clientes.html', {
        'clientes': clientes,
        'total': total_clientes
    })

# Obtiene la lista de clientes activos y los envia como respuesta
def clientes_activos(request):
    # consultas a la base de datos por medio del modelo
    clientes_act = Cliente.objects.filter(activo=True)

    # respuesta
    return render(request, 'clientes/clientes_activos.html', {
        'clientes': clientes_act
    })

# Obtiene el detalle de un cliente lo envia como respuesta
def detalle_cliente(request, cliente_id):
    # consultas a la base de datos por medio del modelo
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if cliente:
        if cliente.tipo == "V0":
            cliente.tipo = "VIP"
        else:
            cliente.tipo = "regular"


    #respuesta
    return render(request, 'clientes/detalle_cliente.html',{
        'cliente': cliente
    })

