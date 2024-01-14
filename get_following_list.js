function extractNames() {
  const nameElements = document.querySelectorAll("div.css-1rynq56.r-bcqeeo.r-qvutc0");
  const names = Array.from(nameElements).map(el => el.textContent.trim());
  const validNames = names.filter(name => name !== '').filter(name => name[0] == "@");
  const givenNames = validNames.map(name => name.slice(1)).slice(1)
  return givenNames;
}

const names = extractNames();
console.log(names);

