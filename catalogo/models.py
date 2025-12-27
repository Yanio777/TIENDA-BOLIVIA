from django.db import models
# Esta línea es la nueva herramienta para conectar con la nube
from cloudinary.models import CloudinaryField

class ProductoBoliviano(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Aquí es donde estaba el cambio: 
    # Antes decía models.ImageField, ahora usamos CloudinaryField
    imagen = CloudinaryField('imagen') 

    def __str__(self):
        return self.nombre