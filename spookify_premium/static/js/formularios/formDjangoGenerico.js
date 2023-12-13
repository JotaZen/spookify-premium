import { notificacionToast } from "../notificaciones/swalToast"

async function notificarMensaje(mensaje, redireccion) {
    await Swal.fire({
        icon: 'success',
        title: mensaje,
        toast: true,
        position: 'bottom',
        background: 'green',
        color: 'white',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
    })
    window.location.href = redireccion
}