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


def consultar_libros():
    return Libro.objects.all().order_by('titulo')


def obtener_libro(libro_id):
    return Libro.objects.get(id=libro_id)


def actualizar_libro(
    libro_id,
    codigo,
    titulo,
    autor,
    categoria,
    precio,
    stock
):
    libro = Libro.objects.get(id=libro_id)

    libro.codigo = codigo
    libro.titulo = titulo
    libro.autor = autor
    libro.categoria = categoria
    libro.precio = precio
    libro.stock = stock

    libro.save()

    return libro


def buscar_libros(termino):
    return Libro.objects.filter(
        titulo__icontains=termino
    ) | Libro.objects.filter(
        autor__icontains=termino
    ) | Libro.objects.filter(
        categoria__icontains=termino
    )