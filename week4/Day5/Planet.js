let planets = ["Earth", "venus", "Jupiter", "Uranus", "Neptune"];

for (let i = 0; i < planets.length; i++) {
    let planetName = planets[i];
    let div = document.createElement('div');
    div.classList.add('planet', planetName);
    let planetNode = document.createTextNode(planetName);
    div.appendChild(planetNode);
    let section = document.querySelector('.listPlanets');
    section.appendChild(div);
    div.style.color = "pink";
    div.style.display = "flex";
    div.style.alignItems = "center";
    div.style.justifyContent = "center";
}

let divs = document.getElementsByTagName('div');
console.log(divs);

let earth = document.getElementsByTagName('div')[0];
let venus = document.getElementsByTagName('div')[1];
let Jupiter = document.getElementsByTagName('div')[2];
let Uranus = document.getElementsByTagName('div')[3];
let Neptune = document.getElementsByTagName('div')[4];

earth.style.backgroundColor = "red";
venus.style.backgroundColor = "orange";
Jupiter.style.backgroundColor = "yellow";
Uranus.style.backgroundColor = "green";
Neptune.style.backgroundColor = "blue";