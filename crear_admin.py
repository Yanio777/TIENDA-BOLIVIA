import os
import django

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin_yanio'
email = 'tu_correo@ejemplo.com'
password = 'Bolivia2025*'

if not User.objects.filter(username=username).exists():
    print(f"Creando superusuario {username}...")
    User.objects.create_superuser(username, email, password)
    print("Superusuario creado con éxito.")
else:
    print(f"El usuario {username} ya existe.")