let body = document.body;
let article = document.getElementsByTagName('article')[0];
let lastP = article.lastElementChild;
let p2 = document.getElementsByTagName('p')[1];
article.removeChild(lastP);

let button = document.createElement('button');
button.innerHTML = "Click me";
button.style.margin = "20px 1px";
article.appendChild(button);
button.addEventListener('click', makeTextBold);

let h2 = document.getElementsByTagName('h2')[0];
let h1 = document.getElementsByTagName('h1')[0];
let h3 = document.getElementsByTagName('h3')[0];
h3.addEventListener('click', clickToHide);
h2.addEventListener('click', changeH2);
h2.addEventListener('mouseover', changeCursor);
p2.addEventListener('click', fadeEffect);
let randomNum = Math.floor(Math.random() * 101);
console.log(randomNum);
h1.style.fontSize = `${randomNum}px`;

function changeCursor() {
    h2.style.cursor = "pointer"
}

function changeH2() {
    h2.style.backgroundColor = '#'+Math.floor(Math.random()*16777215).toString(16);
}

function clickToHide() {
    h3.style.display = "none"
}

function makeTextBold() {
    body.style.fontWeight = "bold"
}

function fadeEffect(){
    p2.classList.add("w3-animate-fading");
    p2.style.border = "2px solid black"
}
console.log(p2);