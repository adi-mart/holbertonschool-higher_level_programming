/*
 * Script de manipulation DOM - Récupération de données API
 * Ce script utilise l'API Fetch pour récupérer les données
 * du personnage numéro 5 depuis l'API Star Wars (SWAPI).
 * Le nom du personnage est ensuite affiché dans l'élément
 * ayant l'ID 'character' une fois les données reçues.
 */
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  });
