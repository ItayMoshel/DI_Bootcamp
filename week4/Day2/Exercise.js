function infoAboutMe() {
    console.log("itay moshel, 27 from israel.");
}
infoAboutMe();


function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log("You'r name is: " + personName + ", you are " + personAge + " years old, and " + personFavoriteColor + " is you'r favorite color.")
}
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

// let userAge = Number(prompt("How old are you?"));


function checkDriverAge(age) {
    let userAge = age;
    if (userAge < 18)
        alert("Sorry, you are too young to drive this car. Powering off.")

    else if (userAge > 18)
        alert("You are old enough to drive, Powering On. Enjoy the ride!")

    else if (userAge === 18)
        alert("Congratulations on your first year of driving. Enjoy the ride!")
    else
        alert("Input Undifind.")
}

checkDriverAge(18);


function checkNumber() {
    for (i = 0; i <= 100; i++)
    if (i % 2 === 0)
        console.log(i + " Even number.")
    else
        console.log(i + " Odd number.")
}

checkNumber();


function isDivisible(divisor) {
    var sum = 0;
    for (i = 0; i <= 500; i++)
        if (i % 23 === 0)
            sum += i;
            console.log(sum);
}

isDivisible();


let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket() {
    let userItem = prompt("Choose an item.");
    for (key in amazonBasket) {
        if (amazonBasket[userItem])
        return alert(userItem + " is in the basket.");

    }
}

checkBasket();



var itemPrice = 0.4;
const quarters  = 0.25;
const dimes = 0.10;
const nickels = 0.05;
const pennies = 0.01;
let  sum = [quarters, dimes, nickels, pennies];

function changeEnough() {
    if (sum[0] + sum[1] + sum[2] + sum[3] < itemPrice)
        console.log(false);
    else
        console.log(true);
}

changeEnough();


// let words = prompt("Please wright several words seperated by comma.");
// var wordsList = words.split(",");
// console.log(wordsList);

