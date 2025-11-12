/*
 * Script de manipulation DOM - Gestionnaire d'événement
 * Ce script attache un gestionnaire d'événement 'click' à l'élément
 * ayant l'ID 'red_header'. Lors du clic, la couleur du premier
 * élément 'header' est modifiée pour devenir rouge (#FF0000).
 */
document.getElementById("red_header").addEventListener("click", function() {
    document.querySelector("header").style.color = "#FF0000";
});
