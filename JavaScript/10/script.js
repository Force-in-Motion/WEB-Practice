
const ol = document.getElementById('ol')
const btn = document.getElementById('btn')


btn.addEventListener('click', () => {
    const li = document.createElement('li')
    const input = document.createElement('input')

    li.classList.add('item');
    input.classList.add('inp');
    input.placeholder = 'Введите текст'

    li.appendChild(input)
    ol.appendChild(li)
});