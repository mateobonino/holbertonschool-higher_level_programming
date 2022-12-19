#!/usr/bin/node
const updateHeader = document.getElementById('update_header');
const header = document.getElementsByTagName('header')[0];
updateHeader.addEventListener("click", function() {
  header.innerHTML = 'New Header!!!';
});
