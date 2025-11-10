document.getElementById("add_item").addEventListener("click", function() {
	const Item = document.createElement('li');
  Item.textContent = 'Item';
  document.querySelector('.my_list').appendChild(Item);
});
