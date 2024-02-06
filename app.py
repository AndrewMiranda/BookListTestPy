from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de muestra
libros = [
    {'titulo': 'El Señor de los Anillos', 'autor': 'J.R.R. Tolkien', 'publicacion': 1954, 'imagen': 'static/images/señorAnillosBook.jpg'},
    {'titulo': '1984', 'autor': 'George Orwell', 'publicacion': 1949, 'imagen': 'static/images/1984Book.jpg'},
    {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'publicacion': 1967, 'imagen': 'static/images/cienAñosBook.jpg'},
]

@app.route('/')
def index():
    # Obtener parámetros de filtro y ordenación
    filtro_autor = request.args.get('filtro', '')
    ordenar_por = request.args.get('orden', 'titulo')

    # Aplicar filtro
    libros_filtrados = libros if not filtro_autor else [libro for libro in libros if libro['autor'] == filtro_autor]

    # Ordenar libros
    libros_ordenados = sorted(libros_filtrados, key=lambda x: x[ordenar_por])

    return render_template('index.html', libros=libros_ordenados, filtro_autor=filtro_autor)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)