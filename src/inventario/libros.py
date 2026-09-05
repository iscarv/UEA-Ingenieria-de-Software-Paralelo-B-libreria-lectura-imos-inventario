from inventario_app.models import Libro


def registrar_libro(codigo, titulo, autor, categoria, precio, stock):
    return Libro.objects.create(
        codigo=codigo,
        titulo=titulo,
        autor=autor,
        categoria=categoria,
        precio=precio,
        stock=stock,
    )