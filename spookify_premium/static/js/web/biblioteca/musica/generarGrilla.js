import { notificacionToast } from "../../../notificaciones/swalToast.js";
import { tarjeta } from "./tarjetaCancion.js";

export const generarGrid = async (sortFunction = null) => {
    const grilla = $("#songs-grid")[0];
    let contenido = ""

    let arrayCanciones
    await $.ajax({
        url: "/biblioteca/musica/todo",
        method: "GET",
        dataType: "json",
        success: function (response) {
            console.log(response.canciones)
            arrayCanciones = response.canciones
        },
        error: function (error) {
            notificacionToast('error', 'Error', 'No se pudieron cargar las canciones')
        }
    });
    console.log(arrayCanciones)

    if (arrayCanciones.length === 0) {
        contenido += `
        <div class="col-12">
            <h3 class="text-center">No hay canciones</h3>
        </div>
        `
    }


    sortFunction && arrayCanciones.sort(sortFunction2);

    arrayCanciones.forEach(cancion => {
        contenido += `
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-4 col-xl-2 pb-4">
                    ${tarjeta(cancion, cancion.id)}
                    </div> 
                `
    })
    grilla.innerHTML = contenido;

    $('.play-button').on('click', function (e) {
        e.stopPropagation();
        e.preventDefault();
        const idCancion = e.currentTarget.id.split("-")[1];
        const audio = $(`#audio-${idCancion}`)[0];
        if (audio.paused) {
            audio.play();
            this.classList.add("pause-btn");
            this.classList.remove("play-btn");
        } else {
            audio.pause();
            this.classList.add("play-btn");
            this.classList.remove("pause-btn");
        }
    });

    // Ver como juntar con el de abajo
    // const botonFavorito = document.querySelectorAll("#favorite-button")
    // botonFavorito.forEach((boton) => {
    //     boton.addEventListener("click", async (e) => {
    //         e.stopPropagation();
    //         e.preventDefault();
    //         const idCancion = e.currentTarget.dataset.id;
    //         if (e.currentTarget.classList.contains("favorite-button-true")) {
    //             e.currentTarget.classList.remove("favorite-button-true")
    //             e.currentTarget.classList.add("favorite-button-false")
    //             await editarFavorito(idCancion, false)
    //         } else {
    //             e.currentTarget.classList.remove("favorite-button-false")
    //             e.currentTarget.classList.add("favorite-button-true")
    //             await editarFavorito(idCancion, true)
    //         }
    //     })
    // })
    // //

}