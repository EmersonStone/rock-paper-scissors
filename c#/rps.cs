using System;

class RockPaperScissors
{
    // Choices for Rock, Paper, Scissors
    const string Rock = "rock";
    const string Paper = "paper";
    const string Scissors = "scissors";

    // Get the player's choice with validation
    static string GetPlayerChoice()
    {
        while (true)
        {
            Console.Write("Your Move: ");
            string input = Console.ReadLine()?.Trim().ToLower();

            if (input == Rock || input == Paper || input == Scissors)
                return input;

            Console.WriteLine("Invalid choice. Please enter Rock, Paper, or Scissors.");
        }
    }

    // Get the computer's choice randomly
    static string GetComputerChoice()
    {
        string[] choices = { Rock, Paper, Scissors };
        Random rand = new Random();
        return choices[rand.Next(choices.Length)];
    }

    // Determine the winner
    static string DetermineWinner(string player, string computer)
    {
        if (player == computer)
            return "tie";
        else if ((player == Rock && computer == Scissors) ||
                 (player == Paper && computer == Rock) ||
                 (player == Scissors && computer == Paper))
            return "player";
        else
            return "computer";
    }

    static void Main()
    {
        // Main game loop
        while (true)
        {
            string playerChoice = GetPlayerChoice();
            string computerChoice = GetComputerChoice();

            string result = DetermineWinner(playerChoice, computerChoice);

            if (result == "tie")
            {
                Console.WriteLine("Tie, Replay!");
            }
            else if (result == "player")
            {
                Console.WriteLine("You Win!");
                break;
            }
            else
            {
                Console.WriteLine("Computer Wins!");
                break;
            }
        }
    }
}