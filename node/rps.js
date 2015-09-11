// play until someome wins
process.stdin.resume();
process.stdin.setEncoding('utf8');

var choices = {
  // choice => beats
  'paper' : 'rock',
  'rock' : 'scissors',
  'scissors' : 'paper'
};

process.stdout.write("Your Move: ");
process.stdin.on('data', function (input) {
  // http://stackoverflow.com/questions/2532218/pick-random-property-from-a-javascript-object
  var computer_move = Object.keys(choices)[ Object.keys(choices).length * Math.random() << 0];
  var human_move = input.trim();

  if ( typeof choices[human_move] !== 'undefined' ) {
    if ( human_move == computer_move ) {
      console.log("Tie, Replay!");
    } else if ( choices[human_move] == computer_move ) {
      console.log("Human Wins!");
      process.exit();
    } else if ( choices[computer_move] == human_move ) {
      console.log("Computer Wins!");
      process.exit();
    }
  }

  process.stdout.write("Your Move: ");
});

