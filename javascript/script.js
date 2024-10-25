var choices = {
  // choice => beats
  paper: "rock",
  rock: "scissors",
  scissors: "paper",
};

var notifier = document.getElementById("notifier");
var moveNotifier = document.getElementById("computer-move");
var input = document.getElementById("human-move");

const submitMove = () => {
  // calculate computer move
  // source; http://stackoverflow.com/questions/2532218/pick-random-property-from-a-javascript-object
  var computerMove =
    Object.keys(choices)[(Object.keys(choices).length * Math.random()) << 0];
  var humanMove = input.value.toLowerCase().trim();

  if (typeof choices[humanMove] !== "undefined") {
    if (humanMove == computerMove) {
      // play until someome wins
      notifier.innerText = "Tie, Replay!";
      moveNotifier.innerText = `Computer chose ${computerMove} as well!`;
      updateCSS("tie");
    } else if (choices[humanMove] == computerMove) {
      notifier.innerText = "You Win!";
      moveNotifier.innerText = `Computer chose ${computerMove} which is defeated by ${humanMove}`;
      updateCSS("win");
    } else if (choices[computerMove] == humanMove) {
      notifier.innerText = "Computer Wins!";
      moveNotifier.innerText = `Computer chose ${computerMove} which defeats ${humanMove}`;
      updateCSS("lose");
    }
  } else {
    notifier.innerText = `${humanMove} is not an option!`;
  }

  input.value = "";
  input.focus();

  return false;
};

const updateCSS = (result) => {
  switch (result) {
    case "win":
      notifier.classList.add("winner");
      notifier.classList.remove("loser");
      break;
    case "lose":
      notifier.classList.remove("winner");
      notifier.classList.add("loser");
      break;
    case "tie":
      notifier.classList.remove("winner");
      notifier.classList.remove("loser");
      break;
  }
};
