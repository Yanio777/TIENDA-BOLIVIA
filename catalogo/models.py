from django.db import models

class ProductoBoliviano(models.Model):
    CATEGORIAS = [
        ('TEXTIL', 'Chompas y Textiles'),
        ('PIEDRA', 'Piedras y Minerales (Bolivianita, etc.)'),
        ('UTENSILIO', 'Urupé y Utensilios Tradicionales'),
        ('CULINARIA', 'Gastronomía Típica'),
    ]

    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True) # Para tus fotos
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"