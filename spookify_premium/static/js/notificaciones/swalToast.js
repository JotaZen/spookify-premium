export const notificacionToast = (icono, titulo, mensaje = null) => {
    const backgroundColors = {
        'success': 'green',
        'error': '#cc0000',
        'warning': '#FF9800',
        'info': '#2196F3',
    }

    if (backgroundColors[icono] === undefined) {
        console.error('El tipo de notificación no es válido')
        return
    }

    Swal.fire({
        icon: icono,
        title: titulo,
        text: mensaje,
        toast: true,
        position: 'bottom',
        background: backgroundColors[icono],
        color: 'white',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
    })
}