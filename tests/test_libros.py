import pytest
from django.db import IntegrityError

from inventario.libros import (
    actualizar_libro,
    buscar_libros,
    consultar_libros,
    registrar_libro,
)
from inventario.forms import LibroForm
from inventario_app.models import Libro


@pytest.mark.django_db
def test_cp04_registra_y_almacena_libro():

    registrar_libro(
        codigo="LIB-001",
        titulo="Cien años de soledad",
        autor="Gabriel García Márquez",
        categoria="Novela",
        precio=15.00,
        stock=10,
    )

    libro_guardado = Libro.objects.get(
        codigo="LIB-001"
    )

    assert libro_guardado.titulo == "Cien años de soledad"
    assert libro_guardado.autor == "Gabriel García Márquez"
    assert libro_guardado.categoria == "Novela"
    assert libro_guardado.precio == 15.00
    assert libro_guardado.stock == 10


@pytest.mark.django_db
def test_rf02_consultar_inventario():

    registrar_libro(
        codigo="LIB-002",
        titulo="El principito",
        autor="Antoine de Saint-Exupéry",
        categoria="Literatura",
        precio=10.00,
        stock=5,
    )

    libros = consultar_libros()

    assert libros.count() == 1
    assert libros.first().codigo == "LIB-002"


@pytest.mark.django_db
def test_rf03_actualizar_libro():

    libro = registrar_libro(
        codigo="LIB-003",
        titulo="Don Quijote",
        autor="Miguel de Cervantes",
        categoria="Clásico",
        precio=20.00,
        stock=10,
    )

    actualizar_libro(
        libro_id=libro.id,
        codigo="LIB-003",
        titulo="Don Quijote de la Mancha",
        autor="Miguel de Cervantes",
        categoria="Clásico",
        precio=22.00,
        stock=15,
    )

    libro_actualizado = Libro.objects.get(
        id=libro.id
    )

    assert libro_actualizado.titulo == "Don Quijote de la Mancha"
    assert libro_actualizado.precio == 22.00
    assert libro_actualizado.stock == 15


@pytest.mark.django_db
def test_rf04_codigo_no_puede_repetirse():

    registrar_libro(
        codigo="LIB-004",
        titulo="Libro de prueba",
        autor="Autor de prueba",
        categoria="Prueba",
        precio=10.00,
        stock=5,
    )

    with pytest.raises(IntegrityError):
        registrar_libro(
            codigo="LIB-004",
            titulo="Otro libro",
            autor="Otro autor",
            categoria="Otra",
            precio=12.00,
            stock=3,
        )


@pytest.mark.django_db
def test_rf04_rechaza_campos_obligatorios_vacios():

    form = LibroForm(
        data={
            'codigo': '',
            'titulo': '',
            'autor': '',
            'categoria': '',
            'precio': '',
            'stock': '',
        }
    )

    assert form.is_valid() is False

    assert 'codigo' in form.errors
    assert 'titulo' in form.errors
    assert 'autor' in form.errors
    assert 'categoria' in form.errors
    assert 'precio' in form.errors
    assert 'stock' in form.errors


@pytest.mark.django_db
def test_rf10_buscar_por_titulo():

    registrar_libro(
        codigo="LIB-005",
        titulo="Cien años de soledad",
        autor="Gabriel García Márquez",
        categoria="Novela",
        precio=15.00,
        stock=10,
    )

    resultados = buscar_libros("Cien")

    assert resultados.count() == 1
    assert resultados.first().titulo == "Cien años de soledad"


@pytest.mark.django_db
def test_rf10_buscar_por_autor():

    registrar_libro(
        codigo="LIB-006",
        titulo="El amor en los tiempos del cólera",
        autor="Gabriel García Márquez",
        categoria="Novela",
        precio=18.00,
        stock=8,
    )

    resultados = buscar_libros("García")

    assert resultados.count() == 1
    assert resultados.first().autor == "Gabriel García Márquez"


@pytest.mark.django_db
def test_rf10_buscar_por_categoria():

    registrar_libro(
        codigo="LIB-007",
        titulo="Libro de ficción",
        autor="Autor",
        categoria="Fantasía",
        precio=12.00,
        stock=6,
    )

    resultados = buscar_libros("Fantasía")

    assert resultados.count() == 1
    assert resultados.first().categoria == "Fantasía"