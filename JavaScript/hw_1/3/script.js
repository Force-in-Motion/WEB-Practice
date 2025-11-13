const items = document.querySelectorAll(".item");
const redBtn = document.getElementById("red");
const greenBtn = document.getElementById("green");
const item_id = document.getElementById('item')

const originalText = item_id.textContent

redBtn.addEventListener("click", () => {
  items.forEach((item) => {
    item.textContent = originalText
    item.style.color = "red";
    item.textContent += " Красный";
  });
});

greenBtn.addEventListener("click", () => {
  items.forEach((item) => {
    item.textContent = originalText
    item.style.color = "green";
    item.textContent += " Зеленый";
  });
});
