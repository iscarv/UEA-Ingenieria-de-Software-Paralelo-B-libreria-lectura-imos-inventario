import pytest

from inventario.libros import registrar_libro
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

    libro_guardado = Libro.objects.get(codigo="LIB-001")

    assert libro_guardado.titulo == "Cien años de soledad"
    assert libro_guardado.autor == "Gabriel García Márquez"
    assert libro_guardado.categoria == "Novela"
    assert libro_guardado.precio == 15.00
    assert libro_guardado.stock == 10