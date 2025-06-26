    function printguessGame()
    --variables
    guess = nil
    compNum = nil
     try = 0
    playAgain="Y"
    attemptsLeft= 7


    --seed random num gen
    math.randomseed(os.time())-- randomizes
    math.random() math.random() math.random()

    while try ~= 7 or try > 7 do 
    
if (string.upper(guess) ~= compNum )then
                try = try + 1
attemptsLeft= attemptsLeft - try
            print("wrong guess you have".. attemptsLeft "atempts left")
            

            else 
                print("you guessed corectly want to try again? press Y to continue any other key to QUIT")
                playAgain = io.read()
            compNum = nil
            guess = nil
                if (string.upper(playAgain) ~="Y" )then
                break
                

            else playAgain = "Y"
            
        --ask for user input
        while (guess == nil or guess == " " or not tonumber(guess)) do
            print("please enter a guess: ")
            guess = io.read() -- keep asking untill valid 

        end 

            --print the random number
            compNum = math.random(1,100)
            print("the computer picked the random number: ".. compNum )
    
        
        
            
            
            if (attemptsLeft == 0 or attemptsLeft < 1) then 
            
            print("you have ran out of trys you lose :( press Y to try again any other key to QUIT)")
            playAgain= io.read()
       
            end
            if (string.upper(playAgain) ~="Y" )then
            compNum = nil
            guess = nil
                break
            else  playAgain= "Y"
            

            end
        end
    end
    end
end 
        









