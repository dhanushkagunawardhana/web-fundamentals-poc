const output = document.querySelector("#output");
const saved = localStorage.getItem("preferredModel") || "Model 3";
output.textContent = saved;
document.querySelector("#action").addEventListener("click", () => {
  localStorage.setItem("preferredModel", "Performance");
  output.textContent = "Performance";
});
