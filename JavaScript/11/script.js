
const ol = document.getElementById('ol')
const btn = document.getElementById('btn')


btn.addEventListener('click', () => {
    ol.lastElementChild.remove()
});