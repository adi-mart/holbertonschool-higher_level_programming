/*
 * Script de manipulation DOM - Ajout dynamique d'éléments
 * Ce script permet l'ajout dynamique d'éléments de liste (li)
 * à une liste existante. L'événement 'click' sur l'élément
 * 'add_item' crée un nouvel élément li avec le texte 'Item'
 * et l'ajoute à la liste ayant la classe 'my_list'.
 */
document.getElementById("add_item").addEventListener("click", function() {
	const Item = document.createElement('li');
  Item.textContent = 'Item';
  document.querySelector('.my_list').appendChild(Item);
});
