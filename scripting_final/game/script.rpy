##this is my renpy game i did not have enpught ime to really flesh this out like the other assighnemnt so it is much shorter 
##and i also didnt have the time to create every sprite to my standards so some of the are a bit slopp(most of them are a bit sloppy)
##anyway i hope you all enjoy
##leilani charles
##python july 30th 2025
#renpy


define e = Character(" ")


# The game starts here.

label start:


    scene black
    scene drive
    with fade
    play sound radio volume 0.4

##introduction to our story

    e " you are on the road driving for a business trip when you suddenly find yourself in front of a grand circus tent" 
   
##wide shot of our tent
    scene wide_tent
    with fade
    e "you pull in and investigate the grand tent noticing the lack of trafic and people around,"

##close looming shot of the tent maybe animated? start choices
##also mute the radio sound
    play sound radio volume 0.0
    scene tent
    with fade
    "the sounds and smells coming from the tent seem to grab you and pull you in ; 
    the tent itself apeared to be almost breathing with the way its tarp moved in the air"
#labels it 
    label startchoices:
        e "( YOU THINK ABOUT ENTERING )" 
##alows us to chose with a pop up menu
    menu:

        "leave":
            jump start_choicea
   
        "enter":
            jump start_choiceb

## choice to leave
    label start_choicea:
##create background like intro but flipped
##leave0 is using the one without the balloon
        scene leave0
        with fade

        e "you decide not to enter afraid of running behind schedule "
        e "as you drive off you have a sense you made the right choice" 
### this is an ending
        scene black
        with fade
        return


## choice to stay
    label start_choiceb:
##enter background where you enter and see the people inside
        scene backgroundpeople
        with fade
        ##lower volume
        play music "background.mp3" volume 0.7
        e "you allowed yourself to be pulled into the grand tent" 
        e "as you enter you are amazed by the large tents interior, noting the performers milling about"
        e "you also notice some attractions scatered through filling the space"
       
        
  
    label attractionchaoice:
        e"(WHAT DO YOU WANT TO DO)"
    menu:
        "go up and talk to one of the  performers":
            jump  talk_choice


        "leave":
            jump  leave_1

##if we choose to talk to one of the performers and are given two choices
    label talk_choice:
##see if we can add walk like movement if not just add the clown sprite
        scene background
        with  fade
        e"you decide to try talking to one of the performers"
        e"you decide to try and strike up conversation with the nicest looking clown"
##adding in our sprites
##adding in our sounds as well for our clown
        play sound "honk.mp3"
        show honk_clown 
        e "honk!"
        e "the clown while mute joyfully honks at you"
##will hide our clown till we need to call him or we call for the next scene then it will wipe it
        hide honk_clown
        show happy clown
        e"you notice him pointing"
        e"you look where they are pointing and notice a large sign in the middle of the tent"
       
##our choices for wether or not we investigate or leave  i cut the other options
        label clown_choice:
            "(YOU WONDER WHAT TO DO)"
        menu:
            "go investigate the sign":
                jump investigate_sign

            "leave":
                jump leave_2

##if we choose to leave after entering
    label leave_1:
        play music "background.mp3" volume 0.0
        scene black
        with fade
        e"you feel a building sense of dread from the grand circus and the performers attention around you 
        you decide to leave just as you enter"
        ##this one has the balloon
        scene leave1
        e "on your way out you are given a balloon as a parting gift by a performer the only thing you think of as you drive away was that maybe your feeling of unease was misplaced"

##enter background same as before with you driving off but add a balloon in the rear veiw
        
        scene black
        with fade
        return


##this is an ending
    label leave_2:
##easiest way i found to turn off the volume on the quiet scenes
        play music "background.mp3" volume 0.0
        
        scene black
        with fade
       
        e"as you look upon the small clown you feel as if many eyes are looking down on you. "
        e"you cant handle this place and leave quickly."
        scene leave1
        with fade
        e"as you leave a performer hands you a red balloon and waves you off; despite the gesture your not sure if staying would have been the right choice."
        return


##if we choose to interact with the sign  
    label investigate_sign:
        scene sign
        e"you decide to go and investigate the sign, the kind clown waves you off"
        e"you walk up to the large sigh to see a time posted onto it and notice its not that far from now"
        e"you wonder what to do."

        label show_choice:
            menu:
                "stay and wait for the show":
                    jump staying

           
                "you dont have enough time":
                    jump leave_good
           


            
###if we chose to stay
    label staying:

        scene background
        with fade
        
        e"you decide to stay and wait for the show."
        e"after all you have already wasted some time a little longer should be fine"
        e"as you wait the performers around you start to dwindle untill there are none left around"
        ##will bring up a background instead of a sprite ran out of tiime to make a completely new sprite for the owner
        scene show
        with fade
        play music "background.mp3" volume 0.4
        e"when all of a sudden the lights are turned off and the show starts.theres a man who leads it all in the center of the tent grabing your attention"
        e"it seems like you cant look away"
        scene black
        with fade
        show background
        with fade
        e"and before you know it its over."
        e"amazed by the show you wonder what to do now"
        label final_choice:
            menu:
                "leave":
                    jump leave_final
                
                "wait to thank everybody":
                    jump choice_wait



                
    label choice_wait:
        scene background 
        with fade
        e"you decide to wait to give the man and the performers your thanks"
        show nutural owner
        e"after a while of waiting you finaly see the man walk out from behind a curtain he smiles at you strangely and asks if you enjoyed the show"
        e"you tell the man you loved the show and wanted to thank them"
        e"the mans expresion is steady as he asks an odd question, he asks if you would like to say here at the circus"
        e"what do you say"
        label yes_no:
            menu:
                "yes":
                    jump bad_end
                "no":
                    jump end
           
                
##bad ending its bad end 
        label bad_end:
            scene black
            with fade
            show nutural owner 
            play music background volume 0.75
            
            "you look to the man and fight to get the words out but the only words that spill from your lips were a resoulute yes"
            "like that you sealed your fate the man took your had, and as he did so everything around you went black"
            hide nutural owner
            scene black

            with fade
            "the mans expression never changed"
            return

##this is an end
##the oficial ending
        label end:
            
            e"you laugh off the mans request thinking nothing of it and once again thank them for letting you see their wonderfull show"
            e"the man is still smiling when he stands straight up and thanks you for coming."
            scene black
            with fade
            play music background volume 0.0
            e"you make your way out thanking the performers you encounter along the way."  
            e"as you leave a performer hands you a balloon and waves you off."
            scene leave1
            with fade
##this will play our radio sound affect
##may cut down clip
            play sound radio volume 0.3
            e"as you hop in your car your glad that you decided to take this stop and see such an amazing show"
            scene black
            with fade
            return




##this is an ending and is the last one labeled leave 
    label leave_final:
##this will play our backgroun circus music but the volume comand will mute it for this scene
        play music "background.mp3" volume 0.0
        scene black
        with fade
        e"you decide that you dont have enough time and make your way out of the circus tent at a leasurely pace."
        e"on the way out you are handed a balloon by a kind performer and waved off"
        scene leave1
        with fade
        e"as you drive off you hope youll be able to stop by again to see the show again"
        scene black 
        with fade 
        return






##if we chose to leave
##this is the last ending you can get
    label leave_good:
        ##this will play our backgroun circus music but the volume comand will mute it for this scene
        play music "background.mp3" volume 0.0
        scene black
        with fade
        e"you decide you dont have enough time and make your way out of the circus tent at a leasurely pace."
        e"on the way out you are handed a balloon by a kind performer and waved off"
        scene leave1
        with fade
        e"as you drive off you hope youll be able to stop by again to see that show"
        scene black 
        with fade 
        return


       