from django.db import models

class Rest(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremental
    nombre_comida = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    subcategoria = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    peso = models.CharField(max_length=50, blank=True, null=True)
    insumos = models.CharField(max_length=255, blank=True, null=True)
    stock = models.IntegerField()
    fecha_promocion_inicio = models.DateField(blank=True, null=True)
    fecha_promocion_final = models.DateField(blank=True, null=True)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    
    imagen_principal = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    imagen_secundaria = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    imagen_opcional1 = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    imagen_opcional2 = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre_comida
