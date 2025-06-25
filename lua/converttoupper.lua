--take string from user and return as a capital

function printuppercase()
    --variable

    local userInput = nil
    upperUserinput = nil

    while (userInput == nil or userInput == "" or userInput == string.upper(userInput) or tonumber(userInput)) do 
        print("please input what you would like to capitalize: " )
        userInput = io.read()
    end
    --once valid uppercase
    upperUserinput = string.upper(userInput)
    --print capital string--final string
    
    print (upperUserinput)


end

function changeToupper()
    --variable

    local userInput = nil
    upperUserinput = nil

    while userInput == nil or userInput == "" or userInput == string.upper(userInput) or tonumber(userInput) do 
    
        userInput = io.read()
    end
    --once valid uppercase
    upperUserinput = string.upper(userInput)
    --print capital string--final string
    
    return (upperUserinput)


end





