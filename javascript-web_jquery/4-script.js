#!/usr/bin/node
const headerTag = document.getElementById('toggle_header');
const tagName = document.getElementsByTagName('header')[0];
headerTag.addEventListener("click", function() {
  if ('red' in tagName.classList) {
    tagName.classList.toggle('green');
  } else {
    tagName.classList.toggle('red');
  }
});
