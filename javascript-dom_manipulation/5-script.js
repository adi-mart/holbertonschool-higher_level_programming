/*
 * Script de manipulation DOM - Modification de contenu textuel
 * Ce script attache un gestionnaire d'événement 'click' à l'élément
 * ayant l'ID 'update_header'. Lors du clic, le contenu textuel
 * du premier élément 'header' est remplacé par 'New Header!!!'.
 */
document.getElementById('update_header').addEventListener('click', function() {
  document.querySelector('header').textContent = 'New Header!!!';
});
