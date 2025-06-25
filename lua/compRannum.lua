--get num
--print random num between 0 and usernum
function printRandomnum()
    --variables
    maxNum = nil
    compNum = nil
    playAgain = "Y"

    --seed random num gen
    math.randomseed(os.time())-- randomizes
    math.random() math.random() math.random()

    while playAgain == "Y" do 

        --ask for user input
    while (maxNum == nil or maxNum == " " or not tonumber(maxNum)) do
        print("please enter a maximum number: ")
        maxNum = io.read() -- keep asking untill valid 

    end 

        --print the random number
        compNum = math.random(1,maxNum)
        print("the computer picked the random number: ".. compNum )
    maxNum = nil
    compNum = nil
        --ask if they want to play again
        print("press Y for another number any other key to EXIT ")
        playAgain = io.read()
        
        if (string.upper(playAgain) ~="Y" )then
            break
        else playAgain = "Y"
        end


    
        
    end



end




