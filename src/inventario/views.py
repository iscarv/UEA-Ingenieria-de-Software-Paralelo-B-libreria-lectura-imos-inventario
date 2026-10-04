from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from inventario_app.models import Libro

from .forms import LibroForm


def lista_libros(request):
    termino = request.GET.get('q', '').strip()

    if termino:
        libros = Libro.objects.filter(
            titulo__icontains=termino
        ) | Libro.objects.filter(
            autor__icontains=termino
        ) | Libro.objects.filter(
            categoria__icontains=termino
        )
    else:
        libros = Libro.objects.all()

    libros = libros.order_by('titulo')

    return render(
        request,
        'inventario/lista_libros.html',
        {
            'libros': libros,
            'termino': termino,
        }
    )


def registrar_libro_view(request):

    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Libro registrado correctamente.'
            )

            return redirect('lista_libros')

    else:
        form = LibroForm()

    return render(
        request,
        'inventario/formulario_libro.html',
        {
            'form': form,
            'titulo_pagina': 'Registrar libro',
        }
    )


def editar_libro(request, libro_id):

    libro = get_object_or_404(
        Libro,
        id=libro_id
    )

    if request.method == 'POST':
        form = LibroForm(
            request.POST,
            instance=libro
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Libro actualizado correctamente.'
            )

            return redirect('lista_libros')

    else:
        form = LibroForm(instance=libro)

    return render(
        request,
        'inventario/formulario_libro.html',
        {
            'form': form,
            'titulo_pagina': 'Actualizar libro',
            'libro': libro,
        }
    )


def eliminar_libro(request, libro_id):

    libro = get_object_or_404(
        Libro,
        id=libro_id
    )

    if request.method == 'POST':
        libro.delete()

        messages.success(
            request,
            'Libro eliminado correctamente.'
        )

        return redirect('lista_libros')

    return render(
        request,
        'inventario/confirmar_eliminacion.html',
        {
            'libro': libro,
        }
    )