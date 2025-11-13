
const square = document.getElementById('square');

square.addEventListener('mouseover', () => {
  square.textContent = 'Наведено';
});

square.addEventListener('mouseout', () => {
  square.textContent = '';
});Наведено