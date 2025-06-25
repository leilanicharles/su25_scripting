
--give 10 random numbers and see if they are even or odd
zeroCount = 0
evenCount = 0
oddCount = 0
counter = 0
checkNum = nil

--seed random num gen
 math.randomseed(os.time())-- randomizes
 math.random() math.random() math.random()-- gets rid of any values

    while counter < 10  do
    checkNum = math.random (0,100)

  --check for zeros  
if checkNum == 0 then 
   zeroCount = zeroCount+1
   print(checkNum .. " is a zero")

else 
    --check if odd
    if math.fmod(checkNum,2)== 1 then 
    oddCount = oddCount +1
    print(checkNum.." is odd")

    else 
        evenCount = evenCount + 1
        print(checkNum .." is even")
    end

    counter = counter + 1 
    end
end
print("zeros: " ..zeroCount)
print("left: "  ..oddCount)
print("right: " ..evenCount)



