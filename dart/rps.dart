import "dart:math";
import "dart:io";


void main() {
    const turn_options = ['rock', 'paper', 'scissors'];

    while (true) {
        stdout.write("Your Move: ");

        String? player_turn = stdin.readLineSync();
        if (player_turn != null) {
            player_turn = player_turn.toLowerCase();
        } else {
            continue;
        }

        int randomChoice = Random().nextInt(turn_options.length);
        String opponent_turn = turn_options[randomChoice];

        if (turn_options.contains(player_turn)) {
            if (player_turn == opponent_turn) {
                print("Tie, Replay!");
            } else if (player_turn == "paper" && opponent_turn == "rock") {
                print("You Win!");
                break;
            } else if (player_turn == "scissors" && opponent_turn == "paper") {
                print("You Win!");
                break;
            } else if (player_turn == "rock" && opponent_turn == "scissors") {
                print("You Win!");
                break;
            } else {
                print("Computer Wins!");
                break;
            }
        }
    }
}