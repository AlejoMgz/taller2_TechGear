from django.shortcuts import render, redirect

def catalogo_motos(request):
    return render(request, 'motos/catalogo.html')

def login_view(request):
    if request.method == 'POST':
        # Al enviar el formulario de login, redirige automáticamente al Dashboard
        return redirect('dashboard')
    return render(request, 'motos/login.html')

def registro_view(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'motos/registro.html')

def dashboard_view(request):
    return render(request, 'motos/dashboard.html')

def pedidos_cliente_view(request):
    return render(request, 'motos/pedidos.html')