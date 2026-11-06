from django.shortcuts import render, redirect

# Lista de motos global para simular catálogo dinámico con imágenes y detalles
MOTOS_DATA = [
    {
        "id": 1,
        "nombre": "Boxer 150 Tech",
        "categoria": "Urbana / Sport",
        "precio": "$6,500,000 COP",
        "precio_num": 6500000,
        "stock": 12,
        "imagen": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=500&auto=format&fit=crop",
        "descripcion": "Diseñada para trabajo duro en ciudad y carretera con mínimo consumo de combustible.",
        "cilindraje": "144.8 cc",
        "potencia": "12 HP @ 7500 RPM"
    },
    {
        "id": 2,
        "nombre": "Pulsar NS 200 FI",
        "categoria": "Naked / Alta Gama",
        "precio": "$11,200,000 COP",
        "precio_num": 11200000,
        "stock": 8,
        "imagen": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop",
        "descripcion": "Potencia naked con inyección electrónica, triple chispa y sistema de frenado ABS.",
        "cilindraje": "199.5 cc",
        "potencia": "24.13 HP @ 9750 RPM"
    },
    {
        "id": 3,
        "nombre": "Apache RTR 200 4V",
        "categoria": "Racing / Sport",
        "precio": "$10,500,000 COP",
        "precio_num": 10500000,
        "stock": 5,
        "imagen": "https://images.unsplash.com/photo-1591637333184-19aa84b3e01f?w=500&auto=format&fit=crop",
        "descripcion": "Tecnología de pista adaptada para dominar las calles con modos de manejo.",
        "cilindraje": "197.75 cc",
        "potencia": "20.5 HP @ 9000 RPM"
    }
]

def catalogo_motos(request):
    usuario = request.session.get('usuario')
    return render(request, 'motos/catalogo.html', {'motos': MOTOS_DATA, 'usuario': usuario})

def detalle_moto(request, moto_id):
    usuario = request.session.get('usuario')
    moto = next((m for m in MOTOS_DATA if m['id'] == moto_id), None)
    return render(request, 'motos/detalle.html', {'moto': moto, 'usuario': usuario})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        # Si el correo contiene 'admin', entra como Administrador
        if 'admin' in email.lower():
            request.session['usuario'] = {'nombre': 'Alejandro (Admin)', 'rol': 'admin', 'email': email}
            return redirect('dashboard')
        else:
            nombre = email.split('@')[0].capitalize()
            request.session['usuario'] = {'nombre': nombre, 'rol': 'cliente', 'email': email}
            return redirect('catalogo')
    return render(request, 'motos/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('catalogo')

def registro_view(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'motos/registro.html')

def dashboard_view(request):
    usuario = request.session.get('usuario')
    return render(request, 'motos/dashboard.html', {'motos': MOTOS_DATA, 'usuario': usuario})