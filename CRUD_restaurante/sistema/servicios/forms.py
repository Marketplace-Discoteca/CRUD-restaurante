from django import forms
from .models import Rest

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Rest
        fields = [
            'nombre_comida',
            'categoria',
            'subcategoria',
            'descripcion',
            'peso',
            'insumos',
            'stock',
            'fecha_promocion_inicio',
            'fecha_promocion_final',
            'precio_anterior',
            'descuento',
            'precio_oferta',
            'video',
            'imagen_principal',     # Añadido
            'imagen_secundaria',     # Añadido
            'imagen_opcional1',      # Añadido
            'imagen_opcional2',      # Añadido
        ]
        widgets = {
            'fecha_promocion_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_promocion_final': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),  # Ajusta el tamaño del área de texto
        }
