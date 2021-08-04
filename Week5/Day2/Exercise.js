let body = document.body;
let article = document.getElementsByTagName('article')[0];

let submit = document.getElementsByTagName('input')[2];
let firstName = document.getElementsByTagName('input')[0];
let lastName = document.getElementsByTagName('input')[1];
submit.addEventListener('click', submitNameValue);


let div = document.getElementsByTagName('div')[0];
let table = document.createElement('table');
let tr = document.createElement('tr');
let tb = document.createElement('tb');
div.style.margin = "20px 0px"


let lastP = article.lastElementChild;
article.removeChild(lastP);


let button = document.createElement('button');
button.innerHTML = "Click me";
button.style.margin = "20px 1px";
article.appendChild(button);
button.addEventListener('click', makeTextBold);


let h1 = document.getElementsByTagName('h1')[0];
let randomNum = Math.floor(Math.random() * 101);
h1.style.fontSize = `${randomNum}px`;


let h2 = document.getElementsByTagName('h2')[0];
h2.addEventListener('click', changeH2);
h2.addEventListener('mouseover', changeCursor);


let h3 = document.getElementsByTagName('h3')[0];
h3.addEventListener('click', clickToHide);


let p2 = document.getElementsByTagName('p')[1];
p2.addEventListener('click', fadeEffect);
console.log(randomNum);


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


function submitNameValue(event) {
    tb.innerText = firstName.value + " " + lastName.value;
    tr.appendChild(tb);
    table.appendChild(tr);
    div.appendChild(table);
    event.preventDefault();
}










