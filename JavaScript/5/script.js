const inputOne = document.getElementById("one");
const inputTwo = document.getElementById("two");
const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
    oneText = inputOne.value
    inputOne.value = inputTwo.value;
    inputTwo.value = oneText
});
