/*
 * Script de manipulation DOM - Basculement de classes
 * Ce script implémente un système de basculement (toggle) entre
 * les classes CSS 'red' et 'green' sur l'élément header.
 * L'événement 'click' sur l'élément 'toggle_header' déclenche
 * l'alternance des classes selon l'état actuel.
 */
document.getElementById("toggle_header").addEventListener("click", function() {
	const header = document.querySelector('header');

		if (header.classList.contains("red")) 
			{
			  header.classList.remove('red');
				header.classList.add('green');
			} 
		else 
			{
				header.classList.remove('green');
				header.classList.add('red');
			}
});
