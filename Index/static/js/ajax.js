$(document).ready(function() {
    $('#btn-postear').click(function() {
      var formData = new FormData($('#formulario')[0]);

      $.ajax({
        type: 'POST',
        url: '/ruta-de-tu-api/',  // Reemplaza con la ruta de tu vista para la operación POST
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          console.log(response);
          $('#exampleModal').modal('hide');
          // Puedes realizar otras acciones, como recargar la lista de moderadores
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });