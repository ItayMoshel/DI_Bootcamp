let me = ["My" , "favorite" , "color" , "is" , "Blue."];
let display = me[0] + " " + me[1] + " " + me[2] + " " + me[3] + " " + me[4];
console.log(display);



let str1 = "mix";
let str2 = "pod";

str1Slice = str1.slice(0,2);
str2Sclice = str2.slice(0,2);

console.log(str1Slice);
console.log(str2Sclice);
console.log(str1);
console.log(str2);

let str3 = str1Slice.concat("d " + str2Sclice + "x")

console.log(str3);



let num1 = prompt("choose a number.");
let num2 = prompt("choose anthoer that you would like to calculate.");
let sum = Number(num1) + Number(num2);
console.log(sum);
alert("This is you'r sum: " + sum);

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