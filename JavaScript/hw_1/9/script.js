
const ol = document.getElementById('ol')
const btn = document.getElementById('btn')


btn.addEventListener('click', () => {
    const li = document.createElement('li')

    li.classList.add('item');
    li.textContent = 'Элемент нумерованного списка'

    ol.appendChild(li)
});