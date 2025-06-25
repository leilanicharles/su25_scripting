--talke two numbers add  together and print the sum

function printTwonumsum()
    --variables
    local numOne = nil
    local numTwo = nil
    local sum = 0

    -- getting first number
    while numOne == nil or numOne == "" or not tonumber(numOne) do

    print("please enter your first number: ")
    numOne = io.read()

    end

    while numTwo == nil or numTwo == "" or not tonumber(numTwo) do

    print("please enter your second number: ")
    numTwo = io.read()

    end
    sum = numOne + numTwo

  print ("ypur sum is : ")  print (sum)
    end
end