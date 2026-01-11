from django.shortcuts import render

def home(request):
    # Esta es la "fuente de datos" manual (Pythonic way sin DB por ahora)
    datos_servicios = [
        {"id": 1, "nombre": "Contenedor Django", "estado": "Activo", "uso_cpu": "12%"},
        {"id": 2, "nombre": "PostgreSQL DB", "estado": "Activo", "uso_cpu": "5%"},
        {"id": 3, "nombre": "Redis Cache", "estado": "Inactivo", "uso_cpu": "0%"},
        {"id": 4, "nombre": "Nginx Proxy", "estado": "Error", "uso_cpu": "98%"},
        {"id": 5, "nombre": "Celery Worker", "estado": "Activo", "uso_cpu": "15%"},
    ]
    
    # El tercer argumento {'servicios': datos_servicios} es el "contexto"
    # que viaja hacia el HTML
    return render(request, 'inicio.html', {'servicios': datos_servicios})