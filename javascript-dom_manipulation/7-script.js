/*
 * Script de manipulation DOM - Affichage de liste depuis API
 * Ce script récupère la liste complète des films Star Wars
 * via l'API SWAPI. Pour chaque film retourné, un élément
 * de liste (li) est créé avec le titre du film et ajouté
 * à l'élément ayant l'ID 'list_movies'. Gestion d'erreur incluse.
 */
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.getElementById('list_movies');

    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
