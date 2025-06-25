
function printusersum()
    --variables
    local done = false
    local sum = 0
    local userNum = nil
    local userC = nil

    while done == false do -- add morefrom user 
        while (userNum == nil or userNum == "" or not tonumber(userNum)) do
            print("number to add to total : ")
            userNum = io.read()
        end
        -- add sum to user num
        sum = sum + userNum
        --reset usernum for new number
        userNum = nil
        --check wether or not to continue to add num
        print (" press Q to QUIT, any opther key to continue! ")
        userC = io.read()
        if  string.upper(userC) == "Q"  then
            print("your sum is :".. sum )
            done = true
            break
        
        end

        userC = nil
    end
end