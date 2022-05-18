const splash = document.querySelector('.splash');

document.addEventListener('DOMContentLoaded', (e)=>{
    setTimeout(()=>{
        splash.classList.add('display-none')
    }, 3000);
})

function mostrar_res() {
    $(".deteccion").attr('src', 'static/img/foto_detectada.jpg');
}