from django.shortcuts import render

def catalogo_motos(request):
    return render(request, 'motos/catalogo.html')

def login_view(request):
    return render(request, 'motos/login.html')

def registro_view(request):
    return render(request, 'motos/registro.html')

def dashboard_view(request):
    return render(request, 'motos/dashboard.html')

def pedidos_cliente_view(request):
    return render(request, 'motos/pedidos.html')