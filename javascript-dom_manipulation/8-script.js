/*
 * Script de manipulation DOM - Traduction via API externe
 * Ce script attend le chargement complet du DOM avant d'exécuter
 * une requête fetch vers une API de traduction. La traduction
 * française du mot "hello" est récupérée et affichée dans
 * l'élément ayant l'ID 'hello'. Gestion d'erreur asynchrone incluse.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Récupérer la traduction française de "hello"
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Obtenir l'élément avec l'id 'hello'
      const Element_hello = document.getElementById('hello');
      // Afficher la traduction
      Element_hello.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});
