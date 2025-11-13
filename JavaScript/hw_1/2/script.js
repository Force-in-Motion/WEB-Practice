const input = document.getElementById("inp");
const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
  btn.textContent = input.value;
  input.value = "";
});
