const output = document.querySelector("#output");
const models = [
  { name: "Model 3", range: 321 },
  { name: "Performance", range: 300 },
];
const names = models.filter(({ range }) => range > 300).map(({ name }) => name);
output.textContent = names.join(", ");
