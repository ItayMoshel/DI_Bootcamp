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

function isDivisible() {
    for (i = 0; i <= 500; i++)
    if (i % 23 === 0)
        console.log(i);
}

isDivisible();

// let words = prompt("Please wright several words seperated by comma.");
// var wordsList = words.split(",");
// console.log(wordsList);

