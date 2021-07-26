// let isApproved = true; 
// let selectedColors = null;
// console.log(name);


// let firstName = undefined;
// let lastName = "moshel";

// let interestRate = 0.3;
// interestRate = 1;
// console.log(interestRate)

// const interestRate = 0.3; 
// interestRate = 1;
// console.log(interestRate);

// use const if you don't need to reasign constant is the best choice.
// but if you need to reasign, use let.

// let person = {
//     name: 'itay',
//     age: 30
// };

// dot notation (default choice).
// person.name = 'john';

// bracket notation ()
// let selection = 'name';
// person[selection] = 'mary';

// console.log(person);

// let selectedColors = ['red', 'blue'];
// adding an item in array (to the end of the array).
// selectedColors[2] = 'green';
// replacing an item in an array.
// selectedColors[0] = 2;
// console.log(selectedColors)
// console.log(selectedColors[0])
// console.log(selectedColors.length)
// array is an data stracture that we use to represent a list of items.


// preforming a task.
// function greet(name, lastName) {
//     console.log("hello " + name + " " + lastName);
// }

// greet('John', 'smith');


// calculating a value.
// function square (number) {
//     return number * number;
// }

// let number = square(2);
// console.log(number);
// console.log(square(2));


// let addressNumber = 6;
// let AddrressStreet = "Rambam";
// let country = "israel";

// let global_address = "i live in " + AddrressStreet + " " + addressNumber + ", in " + country + ".";
// console.log(global_address)


// let birthYear = 1994;
// let futureYear = 2054;

// let futureAge = futureYear - birthYear;

// console.log("i will be " + futureAge + " in " + futureYear + ".");



// let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];
// console.log(pets[1]);

// //(listName)[#]; ADDS AN ITEM TO THE LIST IN A SPECIFIC PLACE.
// pets[5] = 'horse';
// console.log(pets);

// //(listName).splice(#, #, ***); WITH *SPLICE* YOU CAN REMOVE AN ITEM FORM A SPECIFIC PLACE IN THE ARRAY. AND ALSO YOU CAN PUSH AN ITEM
// //IN A SPECIFIC PLACE
// pets.splice(3,1);
// console.log(pets);

// console.log(pets.length);

// let list = ['tiger', 'cat', 'bear', 'bird'];
// console.log(list);

// list.shift; "SHIFTS" THE LIST ONE PLACE AHEAD TO THE RIGHT SO THE FIRST ITEM ON THE LIST DISAPPEARS.
// list.shift();
// console.log(list);

// list.pop; "POPS" THE LAST ITEM ON THE LIST (REMOVES THE LAST ITEM). 
// list.pop();
// console.log(list);

//list.push("***"); PUSHES ANOTHER ITEM TO THE END OF THE LIST.


//list.concat; WITH THIS ACTION YOU CAN ADD ANOTHER ARRAY WITH THE FIRST ARRAY.
// let newList = list.concat(['bee', 'deer']);
// console.log(newList);

//list.sort(); SORTS THE LIST FROM 'A' - 'Z'.
// list.sort();
// console.log(list);

// let hour = 13;
// if (hour >= 6 && hour < 12) 
//     console.log("good morning.");


// else if (hour >= 12 && hour < 18) 
//     console.log("good afternoon.");

// else 
//     console.log("good evening.");

// let role = 'Moderator';

// switch (role) {
//     case 'Guest':
//         console.log("guest user");
//     break;

//     case 'Moderator':
//         console.log("Moderator user");
//     break;

//     default:
//         console.log("Unknown user");
// };

// if (role === 'guest') console.log("Guest");
// else if (role === 'Moderator') console.log("Moderator");
// else console.log("Unknown");


// for loop:



// let i = 0;
// while loop:
// while (i <= 15) {
//     if (i % 2 !==0) console.log(i + " is an odd number.")
//     else console.log(i + " is an even number.")
//     i++;
// }


// do while loop:
// let i = 16;

// do {
//     if (i % 2 !==0) console.log(i + " is an odd number.")
//     else console.log(i + " is an even number.")
//     i++;
// } while (i <= 15);

// let firstNumber = Number(prompt("Choose a number."));
// let secondNumber = Number(prompt("Choose another number."));

// if (firstNumber > secondNumber) 
// alert("This is the highest number. " + firstNumber)
// else if (secondNumber > firstNumber) alert ("This is the highest number. " + secondNumber);


// let number = max(1, 2);

// console.log(number)

// function max (a, b) {
    // if (a > b) return a;
    // else return b;

//     return (a > b) ? a : b;
// }

let userNumber = Number(prompt("pleasse insert a number."));

console.log(typeof(userNumber));

if (userNumber < 2)
    console.log("Boom");
else if ((userNumber % 2 === 0) && (userNumber % 5 === 0))
    console.log("B" + "O".repeat(userNumber) + "M!");    
else if (userNumber % 5 === 0)
    console.log("B" + "O".repeat(userNumber) + "M");    
else if (userNumber % 2 === 0)
    console.log("B" + "o".repeat(userNumber) + "m!")
else if (userNumber > 2)
    console.log("B" + "o".repeat(userNumber) + "m");



















