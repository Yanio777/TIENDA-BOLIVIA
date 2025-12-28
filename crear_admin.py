import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings')
django.setup()

from django.contrib.auth.models import User

# Cambia 'admin' y 'tu_contraseña' por lo que quieras
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Bolivia2025*')
    print("Superusuario creado con éxito")
else:
    print("El superusuario ya existe")