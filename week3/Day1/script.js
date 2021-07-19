// this is a comment

/* this is a commet
and this 
and this 
and this */

console.log("before alert1;")
alert("this is alert1");
console.log("alert1 run successfully");

let addressNumber = "Six";
let addressStreet = "Rambam";
let country = "Israel";

let global_address = addressStreet + " " + addressNumber + ", " + country;

console.log(global_address)

let birth = 1994;
let future = 2032;
let age = future - birth;
console.log("i will be " + age + " in " + future)

let pets = ['cat' , 'dog' , 'fish' , 'rabbit' , 'cow'];
console.log(pets[1])

pets.splice(3 , 1 , 'horse');
console.log(pets);

console.log(pets.length);

let age_prom = prompt('How old are you?',['Please fill here.']);

let howAreYou = confirm('How are you?');
alert(howAreYou);