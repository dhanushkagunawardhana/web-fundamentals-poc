const output = document.querySelector("#output");
function makeCounter() {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
}
const next = makeCounter();
output.textContent = `${next()}, ${next()}`;
