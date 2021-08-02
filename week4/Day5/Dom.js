let pId = document.getElementById('text');

pId.style.width = "auto";
pId.style.height = "auto";
pId.style.backgroundColor = "orange";
pId.style.color = "tomato";
pId.style.borderRadius = "5px";
pId.style.border = "2px solid red";
pId.style.fontSize = "3em";

let div = document.body.firstElementChild;
div.removeAttribute('id');
div.setAttribute('id', 'socialNetworkNavigation');
console.log(div.getAttribute('id'));

let ul = document.getElementsByTagName('ul')[0];

let newLi = document.createElement('li');
newLi.innerHTML = "Logout";
ul.appendChild(newLi);

newLi.innerHTML = "<a href = '#'>Logout</a>";




let pete = document.getElementById('container').nextElementSibling.lastElementChild;
console.log(pete);

pete.textContent = "Richard";

let uls = document.getElementsByClassName('list');



for (i of uls) 
    i.children[0].innerHTML = "itay";

for (i = 0; i < 2; i++){
    let newLi = document.createElement('li');
    newLi.innerHTML = "Hey students!";
    for (i of uls) {
        i.appendChild(newLi);
    }
}

// Can't understand why the last ul is the only on that added the li.


for (i of uls)
    i.classList.add('student_list');

uls[0].classList.add('university', 'attendance');

console.log(uls);

let exerciseThreeDiv = document.getElementsByTagName('div')[2];
exerciseThreeDiv.style.backgroundColor = "lightblue";

let exersiceThreeUl = document.getElementsByTagName('ul')[3];
// Do not display, as for erase the name? or delete the first li?
exersiceThreeUl.firstElementChild.innerHTML = "";

let exerciseThreePete = exersiceThreeUl.lastElementChild;
console.log(exerciseThreePete);

exerciseThreePete.style.border = "2px solid black";
exerciseThreePete.style.borderRadius = "3px";

// Made to whole exercises in one file hope it's fine.

document.getElementsByTagName('section')[0].style.fontSize = "2em";



