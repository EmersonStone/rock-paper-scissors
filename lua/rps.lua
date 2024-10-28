math.randomseed(os.time())

function rock_paper_scissors()
    local turn_options = {'rock', 'paper', 'scissors'}

    while true do
        io.write("Your Move: ")
        local player_turn = io.read():lower()

        local opponent_turn = turn_options[math.random(1, #turn_options)]

        if player_turn == 'rock' or player_turn == 'paper' or player_turn == 'scissors' then
            
            if player_turn == opponent_turn then
                print("Tie, Replay!")
            
            elseif (player_turn == 'paper' and opponent_turn == 'rock') or
                   (player_turn == 'scissors' and opponent_turn == 'paper') or
                   (player_turn == 'rock' and opponent_turn == 'scissors') then
                print("You Win!")
                break
            
            else
                print("Computer Wins!")
                break
            end
        else
            print("Invalid input, please choose rock, paper, or scissors.")
        end
    end
end

rock_paper_scissors()
