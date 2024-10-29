-- Step 1: Create Choices Table
CREATE TABLE Choices (
    id INT PRIMARY KEY,
    name VARCHAR(10)
);

-- Insert choices into the Choices table
INSERT INTO Choices (id, name) VALUES
(1, 'rock'),
(2, 'paper'),
(3, 'scissors');

-- Step 2: Create Results Table
CREATE TABLE Results (
    user_choice INT,
    computer_choice INT,
    result VARCHAR(20),
    FOREIGN KEY (user_choice) REFERENCES Choices(id),
    FOREIGN KEY (computer_choice) REFERENCES Choices(id)
);

-- Step 3: Simulate a Game Round
DELIMITER //
CREATE PROCEDURE PlayRPS(IN user_choice INT)
BEGIN
    DECLARE computer_choice INT;
    DECLARE game_result VARCHAR(20);
    
    -- Simulate a random computer choice (1 to 3)
    SET computer_choice = FLOOR(1 + RAND() * 3);
    
    -- Determine the result
    SET game_result = CASE 
        WHEN user_choice = computer_choice THEN 'tie'
        WHEN (user_choice = 1 AND computer_choice = 3) OR
             (user_choice = 2 AND computer_choice = 1) OR
             (user_choice = 3 AND computer_choice = 2) THEN 'win'
        ELSE 'lose'
    END;
    
    -- Insert the game round results into the Results table
    INSERT INTO Results (user_choice, computer_choice, result)
    VALUES (user_choice, computer_choice, game_result);
END //
DELIMITER ;

-- Step 4: Play the Game (example with rock, which is id 1)
CALL PlayRPS(1);

-- Step 5: View the Results
SELECT 
    c1.name AS user_choice,
    c2.name AS computer_choice,
    r.result
FROM 
    Results r
JOIN 
    Choices c1 ON r.user_choice = c1.id
JOIN 
    Choices c2 ON r.computer_choice = c2.id;
