$(document).ready(function() {
    $('#myTable').DataTable();

    $('#listar_post').click(function () {
        $('form').submit(); // Envía el formulario
    });

    document.addEventListener("DOMContentLoaded", function() {
        const postearBtn = document.getElementById("postearBtn");
      
        postearBtn.addEventListener("click", function(event) {
          event.preventDefault(); // Prevent the form from submitting normally
      
          // Your custom logic here, e.g., validation, AJAX request, etc.
      
          // Example: Display a success message
          alert("Post submitted successfully!");
        });
      });
});
/* var createPostUrl = "{% url 'create_Post' %}";

console.log("URL generada:", createPostUrl);

$(document).ready(function () {
    $('#myTable').DataTable();
    $(document).ready(function() {
        $('#postearBtn').click(function() {
            // Obtén los datos del formulario
            var formData = new FormData($('#createPostForm')[0]);
            

            // Realiza la solicitud AJAX
            $.ajax({
                url:  createPostUrl,
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    // Maneja la respuesta del servidor
                    console.log(response);
                    // Cierra el modal si es necesario
                    $('#postearB').modal('hide');
                    // Recarga la lista de posts o realiza alguna acción adicional
                    // (puedes hacer esto según la lógica de tu aplicación)
                    // window.location.reload(); // Descomenta esto si quieres recargar la página
                },
                error: function(error) {
                    // Maneja el error
                    console.error(error);
                }
            });
        });
        
    });
}); */
/* document.addEventListener('DOMContentLoaded', function () {
    var editarModal = new bootstrap.Modal(document.getElementById('editar'));
    var formulario = document.getElementById('formulario');

    document.getElementById('modificar').addEventListener('click', function () {
        var postId = this.getAttribute('data-post-id');

        // Puedes hacer una solicitud AJAX aquí para obtener los datos del post y llenar el formulario
        // o puedes simplemente abrir el modal y llenar el formulario cuando el usuario hace clic en "Guardar Cambios".

        // Ejemplo de solicitud AJAX:
        // ...

        // Ejemplo de llenado del formulario (simulado):
        document.querySelector('textarea[name="titulo"]').value = "Título del post";
        document.querySelector('textarea[name="extracto"]').value = "Extracto del post";
        document.querySelector('textarea[name="contenido"]').value = "Contenido del post";

        // Abrir el modal de edición
        editarModal.show();
    });

    // Agregar evento de envío del formulario (puedes ajustar según tus necesidades)
    formulario.addEventListener('submit', function (event) {
        event.preventDefault();

        // Aquí puedes hacer una solicitud AJAX para enviar los datos actualizados al servidor
        // y luego cerrar el modal o manejar la respuesta según tus necesidades.

        // Ejemplo de solicitud AJAX para enviar datos al servidor:
        // ...

        // Cerrar el modal (simulado)
        editarModal.hide();
    });
}); */




/*     // Función para crear  post

$('#postForm').on('submit', function(event) {
    event.preventDefault();
    $.ajax({
        url: '{% url "create_post" %}',
        method: 'POST',
        data: new FormData(this),
        contentType: false,
        processData: false,
        success: function(data) {
            if (data.success) {
                alert('¡Post creado con éxito!');
                cargarLista();  // Recargar la lista después de agregar un nuevo post
            } else {
                alert('Error al crear el post. Revise los datos.');
            }
        },
        error: function() {
            alert('Error al realizar la solicitud POST.');
        }
    });
}); */



/* $(document).ready(function() {
    // Función para cargar la lista de elementos mediante AJAX
    function cargarLista() {
        $.ajax({
            url: '/listar_post/',  // URL de tu vista en Django que devuelve la lista en formato JSON
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                // Manipular la respuesta de la vista y actualizar la lista en la página
                var listaPost = $('#listar_post tbody');
                listaPost.empty(); // Limpiar la lista antes de actualizar

                $.each(data.post, function(index, elemento) {
                    // Agregar cada elemento a la tabla
                    listaPost.append('<tr id="fila_id_' + elemento.id_post + '"><td>' + elemento.id_post + '</td><td>' + elemento.titulo + '</td><td>' + elemento.fecha + '</td></tr>');
                });
            },
            error: function(error) {
                console.log('Error en la solicitud AJAX:', error);
            }
        });
    }

    // Llama a la función cargarLista al cargar la página
    cargarLista();

});
//************************script_modificar_post.js*************************
$(document).ready(function() {
    $('#editar').submit(function(event) {
        event.preventDefault();

        $.ajax({
            url: '/editar_post/{{ post.id }}/',  // Ajusta la URL según tu configuración
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function(data) {
                if (data.success) {
                    alert('Post actualizado correctamente');
                    // Puedes realizar más acciones después de la actualización
                } else {
                    alert('Error al actualizar el post. Verifica los datos e inténtalo de nuevo.');
                }
            },
            error: function(error) {
                console.log('Error en la solicitud AJAX:', error);
            }
        });
    });
}); */