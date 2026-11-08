const models = [
  { id: "standard", name: "Model 3", range: 321 },
  { id: "performance", name: "Model 3 Performance", range: 300 },
];
const title = document.querySelector("#title");
const details = document.querySelector("#details");
const choices = document.querySelector("#choices");
const saved = localStorage.getItem("preferredModel");
function showModel(id) {
  const model = models.find(({ id: modelId }) => modelId === id) || models[0];
  title.textContent = model.name;
  details.textContent = `${model.range} miles of range`;
  localStorage.setItem("preferredModel", model.id);
}
models
  .map(({ id, name }) => ({ id, name }))
  .forEach(({ id, name }) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = name;
    button.addEventListener("click", () => showModel(id));
    choices.append(button);
  });
showModel(saved);
