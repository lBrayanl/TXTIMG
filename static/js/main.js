$(document).ready(function() {
    $('#file-input').on('change', function() {
      uploadImage();
    });
  });

function uploadImage() {
    var formData = new FormData($('#upload-form')[0]);
    console.log(formData);
    $.ajax({
        url: '/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            $('#image').attr('src', '/static/img/' + data);
            $('#image').css('display', 'block');
            $('#eliminar').css('display', 'block');
        }
    });
    return false;
}

function eliminarImagen(){
    var imagen = document.getElementById("file-input").files[0];
    $('#image').attr('src', '');
    $('#image').css('display', 'none');
    document.getElementById("file-input").value = "";

    $('#eliminar').css('display', 'none');
}

function procesarImg(){
    var imagen = document.getElementById("file-input").files[0];
    
    var formData = new FormData();
    formData.append("imagen", imagen);
    
    fetch("/procesarImagen", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        $('#resultadoImg').css('display', 'block');
        document.getElementById("texto-procesado").innerText = data.texto;
        document.getElementById("idiomas-texto-procesado").innerText = data.idiomas_detectados;
    })
    .catch(error => console.error(error));
}
