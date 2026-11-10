from django.shortcuts import render, redirect

# Lista global en memoria para simular base de datos interactiva editable
if 'MOTOS_DB' not in globals():
    MOTOS_DB = [
        {
            "id": 1,
            "nombre": "Boxer 150 Tech",
            "categoria": "Urbana / Sport",
            "precio": "$6,500,000 COP",
            "stock": 12,
            "imagen": "/static/motos/images/boxer150.jpg",
            "descripcion": "Diseñada para trabajo duro en ciudad y carretera con mínimo consumo de combustible.",
            "cilindraje": "144.8 cc",
            "potencia": "12 HP @ 7500 RPM"
        },
        {
            "id": 2,
            "nombre": "Pulsar NS 200 FI",
            "categoria": "Naked / Alta Gama",
            "precio": "$11,200,000 COP",
            "stock": 8,
            "imagen": "/static/motos/images/ns200.jpg",
            "descripcion": "Potencia naked con inyección electrónica, triple chispa y sistema de frenado ABS.",
            "cilindraje": "199.5 cc",
            "potencia": "24.13 HP @ 9750 RPM"
        },
        {
            "id": 3,
            "nombre": "Apache RTR 200 4V",
            "categoria": "Racing / Sport",
            "precio": "$10,500,000 COP",
            "stock": 5,
            "imagen": "/static/motos/images/apachertr.jpg",
            "descripcion": "Tecnología de pista adaptada para dominar las calles con modos de manejo.",
            "cilindraje": "197.75 cc",
            "potencia": "20.5 HP @ 9000 RPM"
        }
    ]

def catalogo_motos(request):
    usuario = request.session.get('usuario')
    return render(request, 'motos/catalogo.html', {'motos': MOTOS_DB, 'usuario': usuario})

def detalle_moto(request, moto_id):
    usuario = request.session.get('usuario')
    moto = next((m for m in MOTOS_DB if m['id'] == moto_id), None)
    if moto is None:
        moto = {
            "id": 0,
            "nombre": "Moto no encontrada",
            "categoria": "Sin categoría",
            "precio": "$0 COP",
            "stock": 0,
            "imagen": "/static/motos/images/boxer150.jpg",
            "descripcion": "No encontramos esta motocicleta en el catálogo actual.",
            "cilindraje": "N/A",
            "potencia": "N/A"
        }
    return render(request, 'motos/detalle.html', {'moto': moto, 'usuario': usuario})


def login_view(request):
    if request.method == 'POST':
        email = (request.POST.get('email', '') or '').strip()
        if not email:
            return render(request, 'motos/login.html')

        email_lower = email.lower()
        if 'admin' in email_lower or email_lower == 'admin@techgear.com':
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
    global MOTOS_DB  # Declarado correctamente al inicio de la vista

    usuario = request.session.get('usuario')
    if not usuario or usuario.get('rol') != 'admin':
        return redirect('login')

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'crear' or accion == 'editar':
            moto_id = request.POST.get('moto_id')
            nombre = request.POST.get('nombre')
            categoria = request.POST.get('categoria', 'Urbana')
            precio = request.POST.get('precio')
            stock = int(request.POST.get('stock', 0))
            descripcion = request.POST.get('descripcion', 'Moto TechGear de alto rendimiento.')

            if moto_id:  # Editar existente
                for m in MOTOS_DB:
                    if m['id'] == int(moto_id):
                        m['nombre'] = nombre
                        m['precio'] = precio
                        m['stock'] = stock
                        m['categoria'] = categoria
            else:  # Crear nueva
                nuevo_id = max([m['id'] for m in MOTOS_DB], default=0) + 1
                MOTOS_DB.append({
                    "id": nuevo_id,
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": precio,
                    "stock": stock,
                    "imagen": "/static/motos/images/boxer150.jpg",
                    "descripcion": descripcion,
                    "cilindraje": "150 cc",
                    "potencia": "14 HP"
                })

        elif accion == 'eliminar':
            moto_id = int(request.POST.get('moto_id', 0))
            MOTOS_DB = [m for m in MOTOS_DB if m['id'] != moto_id]

        return redirect('dashboard')

    return render(request, 'motos/dashboard.html', {'motos': MOTOS_DB, 'usuario': usuario})