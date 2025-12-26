from django.db import models

# Aquí guardamos la información de los artesanos bolivianos
class Artesano(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100) # Ej: La Paz, Tarija, etc.
    historia = models.TextField() # Aquí cuentas su vida y técnica

    def __str__(self):
        return self.nombre

# Aquí guardamos los productos que enviaremos a EE.UU.
class Producto(models.Model):
    artesano = models.ForeignKey(Artesano, on_delete=models.CASCADE) # Conecta el producto con su creador
    nombre_producto = models.CharField(max_length=200)
    precio_dolares = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_ingles = models.TextField() # Para que el gringo entienda qué compra

    def __str__(self):
        return self.nombre_producto