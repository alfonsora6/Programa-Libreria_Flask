# Programa-Libreria_Flask
Programa Librería - Flask (Lenguaje de Marcas)

https://libreria-flask-aroldan.herokuapp.com/
## Enunciado de la tarea

Debes crear una aplicación dinámica en python flask con las siguientes características:

1. Escoge una plantilla html5 gratuita y úsala para crear una plantilla base.html.

2. La aplicación nos va a permitir mostrar información de libros. Esa información está guardada en el fichero books.json.

3. La página principal debe mostrar una página donde ponga vuestro nombre, un título con la palabra "Biblioteca" y una lista de enlaces donde se vean los nombres de todos los libros y que nos lleve a una ruta del tipo /libro/<isbn> o /libro?isbn=xxxxxx. Es decir si el libro 1 tienes ISBN 1933988673 el enlace nos llevara a la ruta /libro/1933988673 o a la URL /libro?isbn=1933988673. **Elige la manera de enviar información (URL con parámetros o rutas dinámicas)**.

4. Página detalle del libro. La ruta será /libro/<isbn> o /libro, que mostrará un título con el nombre del libro, una imagen del libro (campo thumbnailUrl) y la siguiente información del libro: Número de páginas, descripción, autores y categorías.
    - Si el ISBN no existe se devolverá un error 404.
    - Si el valor del campo status es igual a MEAP mostraremos un mensaje que diga "ESTE LIBRO NO SE HA PUBLICADO" (usar un if dentro de la plantilla).
