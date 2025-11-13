
const input = document.getElementById('inp')
const enabled = document.getElementById('enable')
const disabled = document.getElementById('disable')

enabled.addEventListener('click', () => {
    input.value = ''
    input.removeAttribute('disabled')
});

disabled.addEventListener('click', () => {
    input.value = ''
    input.setAttribute('disabled', true)
});