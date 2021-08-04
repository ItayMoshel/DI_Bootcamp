let button = document.getElementById('lib-button');

let noun = document.getElementsByTagName('input')[0];
let adjective = document.getElementsByTagName('input')[1];
let someOnesName = document.getElementsByTagName('input')[2];
let verb = document.getElementsByTagName('input')[3];
let aPlace = document.getElementsByTagName('input')[4];

let storyTell = document.getElementById('story');

button.addEventListener('click', getInputs);

function getInputs() {
    let nounValue = noun.value;
    let adjectiveValue = adjective.value;
    let someOneNameValue = someOnesName.value;
    let verbValue = verb.value;
    let aPlaceValue = aPlace.value;
    storyTell.innerHTML = `There once was a person called ${someOneNameValue}, and he/ she was very ${adjectiveValue}. That person wanted to travel to ${aPlaceValue}. so he/ she went ${verbValue} to do it. and he/ she grabbed a ${nounValue} and went there.`
}

// i'm sure that there is a way to make the code better, but i tried and don't know where to improve it.