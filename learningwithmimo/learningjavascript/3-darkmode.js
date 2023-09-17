// Dark Mode - Sept 17, 2023

let mode = "ninja";
let color = "ghostWhite";
let image = "/img/light-icon.png";
let label = "Light Mode";

if (mode === "dark") {
  color = "darkSlateBlue";
  image = "/img/dark-icon.png";
  label = "DarkMode";
}

else if (mode === "light") {
  color = "ghostWhite";
  image = "/img/light-icon.png";
  label = "LightMode";
}

else {
  color = "dimGray";
  image = "/img/ninja-icon.png";
  label = "NinjaMode";
}

console.log(label);