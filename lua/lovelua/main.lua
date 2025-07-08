--REMEMBER WITH OUR DEBUGGER F5 for debug, SHIFT F5 for non-debug
--This is your debug code. It goes at the very top of main.
if arg[2] == "debug" then
    require("lldebugger").start()
end

-- Game where multiple images fall from sky
-- User clicks to send them back to top 
-- Click images before they hit the bottom or game over 

--should have title screen, level 1, game over
function titleLoad()
    slimeFire = love.graphics.newImage("fish_orange.png")
    titleText = "chicken Drop"
    --Update the window to be titled the titleText
    love.window.setTitle(titleText) 
    
end
-----------------------------------------------------------------
-- LOAD ALL

function love.load()
    --by default, Love sets your window to 800x600
    success = love.window.updateMode(1024, 768)    
    --load title stuff
    titleLoad()

    -- 0 = title screen
    -- 1 = game screen
    -- 2 = game over screen
    scene = 1

    --Set up slime variables
    fishO = love.graphics.newImage("fish_orange.png")
    fishnum = 5 -- how many
    fishX = {} -- where at (x)
    fishY = {} -- where at (y)
    fishSpeed = {} -- how fast 
    minSpeed = 10
    maxSpeed = 20
    speedMod = 1
    count = fishNums

    --Randomization
    math.randomseed(os.time())
    math.random(); math.random(); math.random()

    --initially populate the slimes
    while count > 0 do
        --get an x value between 0 and width of screen minus width of slime 
        fishX[#fishX+1] = math.random(0, love.graphics.getWidth() - fishO:getWidth())
        -- get a random y value between 1 and 2 slimes above window
        fishY[#fishY+1] = 0 -- math.random(slimeF:getHeight(), slimeF:getHeight()*2)
        -- get a random speed between min and max 
        fishSpeed[#fishSpeed+1] = math.random(minSpeed, maxSpeed)
        count = count - 1 --count down
    end

end
-----------------------------------------------------------------
-- CLICK ALL 

function love.mousepressed(x, y, button, istouch)
    --if it's left click
    if button == 1 then
        --if on title screen
        if scene == 0 then
            --if title screen
        end
        --in  the game
        if scene == 1 then
           --check image and see if it has collided with the mouseclick 
           for i, value in ipairs(fishX) do
                if x >= fishX[i] and x <= fishX[i] + fishO:getWidth() and y >= fishY[i] and y <= fishY[i] + fishO:getHeight() then
                    --print ("hit in the thing")
                    --randomize
                    math.randomseed(os.time())
                    math.random(); math.random(); math.random()
                    --send back to top and change speed
                    speedMod = speedMod + 1
                    maxSpeed = maxSpeed + speedMod
                    fishX[i] = math.random(0, love.graphics.getWidth() - fishO:getWidth())
                    fishY[i] = 0 - math.random(fishO:getHeight(), fishO:getHeight() * 2)
                   fishSpeed[i] = math.random(fishSpeed[i], maxSpeed) --can only get faster
                    break --so that it only clicks ONE thing and not overlapping things
                end
           end
        end
    end
end

-----------------------------------------------------------------
-- UPDATE ALL 



function love.update(dt)
    --if gameplay scene
    if scene == 1 then
        for i, value in ipairs(slimeX) do
            if slimeY[i] + slimeF:getHeight() >= love.graphics.getHeight() then
                --print ("Over the Edge")
                love.event.quit() --having "restart" will restart the thing
            end
            --Move slime 
            slimeY[i] = slimeY[i] + slimeSpeed[i] * dt
        end
    end

end

-----------------------------------------------------------------
-- DRAW ALL 

function love.draw()
    --TITLE SCREEN
    if scene == 0 then
        --draw the title screen
    end
    --GAMEPLAY
    if scene == 1 then
        for i, value in ipairs(slimeX) do
            love.graphics.draw(slimeF, slimeX[i], slimeY[i])
        end
    end
    --GAMEOVER
    if scene == 2 then
        --draw the game over screen
    end

end




-- highlighting  error issues allong with breakpoints
local love_errorhandler = love.errorhandler

function love.errorhandler(msg)
    if lldebugger then
        error(msg, 2)
    else
        return love_errorhandler(msg)
    end
end