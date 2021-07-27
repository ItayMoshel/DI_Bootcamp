// function playTheGame() {
//     let answer = confirm("Would you like to play the game?");
//     if (!answer) alert("No problem, Goodbye.");
//     else {
//       let num = parseInt(prompt("Please enter a number between 1~10."));
//       if (num > 10 || num < 0) alert("Sorry, it’s not a good number. Goodbye.");
//       else if (!num) alert("Sorry, not a number. Goodbye.");
//       else {
//         let computerNumber = Math.floor(Math.random() * 11);
//         alert(computerNumber);
//         test(num, computerNumber);
//       }
//     }
//   }

  

//   function test(num, computerNumber) {
//       if (num === computerNumber) {
//        alert("WINNER!");
//        return true;
//       }
//       else if (num > computerNumber) {
//           alert("You'r number is bigger them the computer's, Guess again.")
//           return;
//       }
//       else if (num < computerNumber) {
//           alert("You'r number is lower then the computer's, Guess again.")
//           return;
//       };
    
    
//   }

// test(num, computerNumber);  



function playTheGame() {
    if (!confirm("Would you like to play the game?")) {
      alert("No problem, Goodbye");
      return;
    }
    let computerNumber = Math.round(Math.floor(Math.random() * 11));
    let usersGuessNumber;
    for (var i = 0; i < 3; i++) {
      let usersGuessNumber = getUserGuessNumber();
      if (!usersGuessNumber) return;
      if (test(usersGuessNumber, computerNumber)) return;
    }
    alert("out of chances");
    return;
  }
  function getUserGuessNumber() {
    let userGuessNumber = parseInt(
      prompt("Please enter a number between 0 and 10")
    );
    if (!userGuessNumber) {
      alert("Sorry not a number, Goodbye");
      return;
    }
    if (userGuessNumber > 10 || userGuessNumber < 0) {
      alert("Sorry not a good number, Goodbye");
      return;
    }
    return userGuessNumber;
  }
  function test(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
      alert("WINNER");
      return true;
    }
    if (userNumber > computerNumber) {
      alert("Your number is bigger than the computer's, guess again");
      return false;
    }
    if (userNumber < computerNumber) {
      alert("Your number is smaller than the computer's, guess again");
      return false;
    }
  }