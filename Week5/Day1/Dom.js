let button = document.querySelector('#pinkButton');
button.addEventListener("mouseover", inform);
button.addEventListener("mouseout", informOut);


function inform(event) {
    event.target.innerHTML = "Hello";
    event.target.style.backgroundColor = "white";
    event.target.style.color = "black";
}

function informOut(event) {
    event.target.innerHTML = "Bye";
    event.target.style.backgroundColor = "black";
    event.target.style.color = "white";
    
}

let h1 = document.getElementById('green');
h1.addEventListener("mouseover", inform);
h1.addEventListener("mouseout", informOut);


h1.style.border = "2px solid black"

