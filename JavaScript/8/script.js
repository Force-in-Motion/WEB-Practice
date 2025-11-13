
const square = document.getElementById('square')
const btn = document.getElementById('btn')

const pathBlackTea = "url('./Black Tea Cup.png')";
const pathEspresso = "url('./Espresso Cup by Mugs.co.png')";

let blackTea = true;

btn.addEventListener('click', () => {
    square.style.backgroundImage = blackTea ? pathEspresso : pathBlackTea;
    blackTea = !blackTea

});