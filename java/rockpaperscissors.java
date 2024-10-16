import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.HashMap;

    public class rockpaperscissors {
        public static void main(String[] args) {

            HashMap<String, String> dictionary = new HashMap<>();
            dictionary.put("rock", "scissors");
            dictionary.put("paper", "rock");
            dictionary.put("scissors", "paper");


            // List of words for the "computer"
            ArrayList<String> computerchoice = new ArrayList<>();
            computerchoice.add("rock");
            computerchoice.add("paper");
            computerchoice.add("scissors");

            // Chooses a random word
            Random wordpicked = new Random();
            int randomIndex = wordpicked.nextInt(computerchoice.size());
            String computermove = computerchoice.get(randomIndex);

            // Allows user input
            Scanner scanner = new Scanner(System.in);

            System.out.println("Do you want to play rock, paper, scissors? (Y/N)");
            String i = scanner.nextLine();

            // Starts the game
            if (i.equalsIgnoreCase("Y")) {
                System.out.println("Your Move (choose 'rock', 'paper' or 'scissors'): ");
                String playermove = scanner.nextLine();

                String playercheck = playermove;

                String playerMoveBeats = dictionary.get(playercheck);
                String computerMoveBeats = dictionary.get(computermove);

                    // Checks for a valid input
                    if (computerMoveBeats.equalsIgnoreCase(playercheck)) {
                        System.out.println("You choose: " + playermove);
                        System.out.println("Computer choose: " + computermove);
                        
                        // Compares computer and player moves
                        if (computerMoveBeats.equalsIgnoreCase(playercheck)) {
                            System.out.println("Paper beats rock. You lose!");
                        }
                        else if (playerMoveBeats.equalsIgnoreCase(computermove)) {
                            System.out.println("Rock beats Scissors. You win!");
                        }
                        else if (playerMoveBeats.equalsIgnoreCase(computerMoveBeats)){
                            System.out.println("Its a tie!");
                        }
                    }
                    else {
                        System.out.println("Invalid Input...");
                    }
            }

            // If N/n is put in, ends the game
            else if (i.equalsIgnoreCase("N")) {
                System.out.println("Okay, Goodbye! :)");
            }

            // If something other than Y/N is put in, ends the game
            else {
                System.out.println("Invalid Input...");
            }
        }
    }
