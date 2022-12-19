#!/usr/bin/node
const elementDiv = document.getElementById('add_item');
const listElement = document.getElementsByTagName('list')[0];
elementDiv.addEventListener("click", function() {
  listElement.innerHTML += '<li>Item</li>';
});