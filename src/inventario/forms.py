from django import forms

from inventario_app.models import Libro


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = [
            'codigo',
            'titulo',
            'autor',
            'categoria',
            'precio',
            'stock',
        ]

        labels = {
            'codigo': 'Código',
            'titulo': 'Título',
            'autor': 'Autor',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'stock': 'Stock',
        }

        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'placeholder': 'Ej. LIB-001'
                }
            ),
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Título del libro'
                }
            ),
            'autor': forms.TextInput(
                attrs={
                    'placeholder': 'Autor'
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'placeholder': 'Categoría'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'step': '0.01',
                    'min': '0'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'min': '0'
                }
            ),
        }