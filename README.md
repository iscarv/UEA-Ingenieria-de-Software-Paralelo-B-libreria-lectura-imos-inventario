# UEA-Ingeniería-de-Software-Paralelo-B-librería-lectura-imos-inventario

# Librería Lectura IMOS

## Información del proyecto

**Sistema:** Librería Lectura IMOS

**Módulo:** Gestión de Inventario

**Stack tecnológico:** Python + Django

**Integrante:** Isca Madaí Ortiz Sabando

**Asignatura:** Ingeniería de Software

**Docente:** Ing. Hermes Darío Sánchez Bermeo, Mg.

## Descripción

El proyecto corresponde al desarrollo de un sistema de gestión para la Librería Lectura IMOS. El módulo seleccionado para la implementación es **Gestión de Inventario**, el cual permitirá registrar, consultar y actualizar los libros del inventario, validar los campos obligatorios y buscar libros por título, autor o categoría.

## Flujo de ramas

Se utilizará un flujo de trabajo basado en **GitHub Flow**:

* **`main`**: contiene la versión estable del proyecto.
* **`feature/...`**: ramas utilizadas para desarrollar cambios o funcionalidades específicas.
* Cada cambio se desarrolla en una rama `feature/registrar-libro`, se realiza un commit y posteriormente se crea un **Pull Request** para revisar y fusionar los cambios hacia `main`.

## Estructura inicial

```text
lectura-imos-inventario/
├── README.md
├── .gitignore
├── src/
    └──.gitkeep
└── .github/
    └── workflows/
        └── ci.yml
```

## Estructura actual
``` text
lectura-imos-inventario/
├── README.md
├── .gitignore
├── pytest.ini
├── requirements.txt
├── src/
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── inventario/
│   │   └── libros.py
│   └── inventario_app/
│       ├── migrations/
│       │   └── 0001_initial.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── tests/
│   └── test_libros.py
└── .github/
    └── workflows/
        └── ci.yml
```
