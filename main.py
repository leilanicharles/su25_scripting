'''

//text adventure game, python 
//leilani charles 
//july, 20th, 2025
//create a program in python that is a complete text adventure with atlest 10 diffrient choices


'''
### background info 

print (" you are on the road driving for a business trip when you suddenly find yourself in front of a grand circus tent ")
print( " you take note of the lack of guest and traffic around the grand tent")
print( " the sounds and smells coming from the tent seem to grab you and pull you in ")
print("the tent itself apeared to be almost breathing with the way its tarp would move in the air")
print( " DO YOU ENTER")
print("> yes")
print("> no")


### prompt for input choice wether to enter or not

enterChoice = input("> ")

### if our choice is yes this is our output

if(enterChoice == "yes"):
    print("___________________________________________________________________________")
    print("you allowed yourself to be pulled into the grand tent ")
    print("as you enter you are amazed by the large tents intirior noting the performers milling about ")
    print("as you enter you notice some atractions right at the entrance")
    print("while you take note of these you are noticed and welcomed by some of the performers")
  
    print("WHAT DO YOU WANT TO DO")
    print("> leave")
    print("> talk")
    print("> pick ")
    print("___________________________________________________________________________")
    
###if we chose to leave  this is our output
    startingChoice = input("> ")
    if (startingChoice == "leave"):
        print("___________________________________________________________________________")
        print ("you feel a building sense of dread from the grand circus and the performers attention around you ")
        print ("you decide to leave just as you enter")
        print ("on your way out you are given a baloon as a parting gift by a performer ")
        print (" the only thing you think of as you drive away was that maybe your feeling of unease was misplaced ")
        print("___________________________________________________________________________")
                                         ### this is an ending  ~~~~~~~~~~~
        
 ### if we chose pick this is our output  
    if (startingChoice == "pick"):
            print("___________________________________________________________________________")
            print("you decide to go and pick from some of the attractions at the entrance ")
            print ("while looking around some catch your eye")
            print ("you notice a large carousel over shadowing a closed tent  ")
       
            print ("WHERE DO YOU GO")
            print ("> carousel")
        
            print ("> tent ")
            print("___________________________________________________________________________")
            attractionChoice = input("> ")
        
        
         ### if we chose carousel
            if ( attractionChoice == "carousel"):
                print("___________________________________________________________________________")
                print("you make your way to the carousel and are let on by a nearby atendent ")
                print("you have a blast on the ancient machanical wonder ")
                print("you hop off and wonder what you should do next")
                print("WHAT DO YOU DO") 
                print("> leave")  
                print("> tent") 
                print("___________________________________________________________________________")
           
        
                
         ### if we chose the tent 
            if(attractionChoice == "tent"):
                    print("___________________________________________________________________________")
                    print("you go against your better judgment and investigate the suspicous tent. ")
                    print("up close you notice there are lights coming from the inside;")
                    print("as you enter you notice a large man in a coulorful suit, ")
                    print("he notices you and turns around; he looks down on you and greets you. ")
                    print("the large man wears a tense but kind smile he asks if you were here for the show and if you would be so kind to stay.
                    print("the large man walks you out of the tent and points you to where the show will be held and tells you it will be starting soon ")
                    print("aginst your better judgment you are instantly swayed by the man and make your way to wait for the show. ")
                    print("  . ")
                    print("  . . ")
                    print("  .  .  . ")
                    print("after a tense wait the show had begain you were amazed by the cacophony of sounds and sights that were soroundong you  ")
                    print("despite your erlier concerns you all had been wahsed awaywhen viewing the show ")
                    print("you were so entranced you had bearly noticed its end")
                    print("you dont know whether to wait and thank the performers or to leave as it was only getting later  ")
                    print("WHAT DO YOU DO ")
                    print("> wait")
                    print("> leave")
                    print("___________________________________________________________________________")
                    finalchoice = input ("> ")
                        if (finalchoice == "wait"):
                        print("despite everything in you telling you to leave you decide to stay and thank the performers as you wait you dont hear or see a single soul")
                        print(" after soome time the large man amerges from behind the curtain")
                        print(" he greets you and asks you if you like the show ")
                        print(" you tell him you did and how  amazed by it you were")
                        print(" the man leans down and looks at you with a too tight smile and asks you if you would like to join him ansd his little circus and make it even better")
                        print("you look to the man and fought to get the words out but the only words that spill from your lips were a resoulute yes")
                        print(" like that you sealed your fate the man laughed and took your had as he did so everything you saw went black")
                        ### this is an ending
                        
                        elif (finalchoice == "leave"):
                            print("you jump out of your seat deciding against staying here any longer as you rush to make your way to the exit you feel as if the very circus was folding around youalive and trying to keep you in")
                            print("your fears were realized when you finally steped out of the circuses entrance and bolted to your car")
                            print("as you reached for your keys you spared a glance back and find that the grand circus had vanished ")
                            print("the now desolate fild which once held a grand circus now was empty and still")
                           ### this is an ending
                        

### if we chose to talk this is our output
    if (startingChoice == "talk"):
        print("___________________________________________________________________________")
        print("you decide to try and tall to some of the performers milling about the entrance of the tent")
        print ("feeling overwhelmed you picked the kindest looking out of them")
        print ("you wave hello to the kind looking clown")
        print ("he greets you with a HONK and points in the direction of a large sign closer to the middle of the tent ")
     
        print ("WHAT DO YOU DO")
        print("> leave")
        print("> inspect")
      
        print("___________________________________________________________________________")
        clownChoice = input("> ")
        
        ### if we chose to leave
        if(clownChoice == "leave"):
         print("___________________________________________________________________________")
         print("you are unerved by the performers silence and the oddities of its atendents you decided  it best to leave")
         print("you quickly turn and make your way out of the tent deciding whatever was on that sign wasnt worth it ")
         print("as you step out a lone performer hands you a baloon and waves you off ")
         print(" you get in your car and feel conflicted maybe you were wrong? despite that you quickly pull away glad to be back on the road again")
         print("___________________________________________________________________________")
                              ###this is an ending~~~~~~~~~~~
        ##if we chose to inpsect
        
        elif (clownChoice == "inspect"):
            print("___________________________________________________________________________")
            print("you turn you head toward the large sign in the middle of the tent and give a thankful nod to the performer")
            print("you are sent off with another gleeful honk ")
            print("as you make your way to the large sign you notice that on it was a large countdown and above it read time till next show")
            print(" you wonder what you should do as the next show wasnt much longer from now")
      
            print("WHAT DO YOU DO")
            print("> wait")
            print("> leave")
            print("___________________________________________________________________________")
        timeChoice = input  ("> ")
             
        if(timeChoice == "wait"):
                print("___________________________________________________________________________")    
                print("you decide you have nothing to lose as you find a seat in the empty bleachers ")  
                print("you take a seat and wait with anticipation for the coming show")  
                print(".")  
                print("..")  
                print("...")  
                print("the show was well worth the wait as you were entranced by the sounds and acts being performed for you in the empty hall ") 
                print(" so much so that you found yourself dissapointed at the shows end ")
                print("despite this you debated wether or not you should bother the performers to thank them for the show")
                print("WHAT DO YOU DO ")
                print("> wait ")
                print("> leave")
                print("___________________________________________________________________________")               
                    lastchoiceG = input ("> ")
                    
                    if (lastchoiceG == "wait"):
                        print("you decided to wait for the performers as you had already decided to stay for the show it was only right to thank them")
                        print("as you waited you didnt see a single performer or atendedt leave behind the curtain")
                        print("you strted to worry untill slowly people started to filter out as you went to thank them  you noticed their faces light up ")
                        print(" although none spole you were glad you decided to stick around to thank them")
                        print("as you left youj were given a warm escort and a baloon by one of the atendants you were glad you made the stop ")
                        ##this is an end
                        
                    elif (lastchoiceG == "leave"):
                        print("you decided you had played around enough today and as you couldnt see a single performer or atendendt nearby you didnt want to be a bother ")
                        print("you got up and made youe way to the exit as you got into your car you decided to get one more good look at the grand circus")
                        print("however when you turned aroun nothing was there")
                        print("there was no trace of the grand circus ")
                        print("as you drove off confused and unerved you were glad that nothing bad had happend ")
                    ## this is an ending
        if(timeChoice == "leave"):
                print("___________________________________________________________________________")
                print("you decide you dont have enough time left to spare as you make your way out you make sure to apologize to the atendent at the front   ")  
                print(" they wave you off with a smile and hand you a baloon")  
                print("your a bit disapoonted in missing the show but are sure that such a large atraction will be here in the coming days")  
                              ###this is an ending ~~~~~~~~~
                    
                print("___________________________________________________________________________")
                
                
                
 
           
            


### if our choice is no  this is our output

elif(enterChoice == "no"):
    print("you decide not to enter afraid of running behind schedual  ")
    print("as you drive off you have a sense you made the right choice ") 
   
                                        ### this is an ending~~~~~~~~~~~~~~


 ### if neither of the choices are picked or are incorectly spelt
else:
     print("please chose from one of the options")