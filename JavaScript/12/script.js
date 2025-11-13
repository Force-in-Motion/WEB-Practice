
const ul = document.getElementById('ul')


ul.addEventListener('click', (event) => {
    if (event.target.tagName === 'LI') {
        event.target.remove()
    }
});