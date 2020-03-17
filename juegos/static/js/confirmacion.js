function confirmarElimninacion(id) {
    //alert(id);
    Swal.fire({
        title: 'Estas seguro de Eliminar Este Registro?',
        text: "No Podras Recuperar este Registro!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.value) {
            window.location.href = "/eliminar_usuarios/" + id + "/";

        }
    })
}
$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
    });
});