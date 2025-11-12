/*
 * Script de manipulation DOM - Gestion des classes CSS
 * Ce script attache un gestionnaire d'événement 'click' à l'élément
 * ayant l'ID 'red_header'. Lors du clic, la classe 'red' est ajoutée
 * au premier élément 'header' du document via classList.
 */
document.getElementById("red_header").addEventListener("click", function() {
	document.querySelector('header').classList.add('red');
});
