#!/usr/bin/node
const headerTag = document.getElementById('red_header');
headerTag.addEventListener("click", function() {
  document.getElementsByTagName('header')[0].style.color = '#FF0000';
});
