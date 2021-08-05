// let body = document.body;
// function banner() {
//     let div = document.createElement('div');
//     let textnode = document.createTextNode("The sales end in ")
//     div.appendChild(textnode);
//     body.appendChild(div);
//     div.style.width = "300px";
//     div.style.height = "450px";
//     div.style.border = "2px solid black";
//     div.style.backgroundColor = "yellow";
//     div.style.color = "orange";
//     div.style.fontSize = "1.3em"
//     div.style.textShadow = "-1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000";
// } 

// setTimeout(banner, 5000);

// Exercise 1
///////////////////////////////////////////////////////////////////

let div = document.createElement('div');
document.body.appendChild(div);
let interval;

function timer() {
    let sec = 10;
    interval = setInterval(function(){
        div.innerHTML = `The sales end in ${sec}`;
        sec--;
        if (sec < 0) {
            clearInterval(interval);
            div.innerHTML = "Sale ended."
        }
    }, 1000)
}

setTimeout(timer, 2000);
