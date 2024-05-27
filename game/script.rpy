﻿define WelcomeGuy = Character("Guy Who welcomes you to the game")
define GameOverGuy = Character("Guy Who tells you game over")
define Guide = Character("Guide")
define hatman = Character("HatMan")
define sm = Character("Survey Man")

image SurveyMan = "SurveyMan.png"
image guide = "Guide Neutral.png"
image guide happy = "Guide Happy.png"
image guide mad = "Guide Mad.png"
image guide sad = "Guide Sad.png"
image main = "bg main.png"
image main green = "bg main green.png"
image main red = "bg main red.png"
image main negative = "bg main negative.png"
image main forest = "bg main forest.png"
image main fish = "bg main fish.png"

#On screen countdown for decision

#init for timer vars
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
    $ loseFlag = False
    $ hatFlag = False
    $ surveyFlag = False

init python:
    def question():

        if loseFlag == True:
            renpy.jump("themenu")
        elif hatFlag and surveyFlag:
            renpy.jump("win")
        

        num = renpy.random.randint(1,10)

        if num == 1 and not hatFlag:
            renpy.jump("hat")

        userinput = renpy.input("Where do you want to go?", length=16)
        userinput = userinput.strip()

        if userinput == "guide":
            renpy.call("guide")
        elif userinput == "survey":
            renpy.jump("survey_intro")
        else:
            renpy.jump("wrong")
        
    def randomizeBackground():
        return (renpy.random.choice(["main", "main green", "main red", "main forest", "main fish", "main negative"]))

    def countdown(st, at, length=0.0):

        remaining = length - st
        minutes = (int) (length - st) / 60
        seconds = (int) (length - st) % 60

        if remaining > 0.0:
            return Text("%02d:" % minutes + "%02d" % seconds, color="#f00", size=200), .1
        else:
            global loseFlag
            loseFlag = True
            return Text("%02d:" % minutes + "%02d" % seconds, color="#000", size=200), .1

screen convoCountdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('convoCountdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

screen countdown(cd_time):
    zorder 2
    frame:
        #xalign 1.0
        xpos 500
        yalign 0.1
        background None
        add DynamicDisplayable(countdown, length=cd_time)

# The game starts here.

label start:

    jump main

    #every scene should show blink right under it
    scene bg bus

    "PlaceHolder Name" "PlaceHolder Text"

    $ _window_hide()

    show welcomeguy behind blink:
        xalign 0.0
        linear 1.5 xpos 0.70
        linear 0.2 xpos 0.50
    pause 2.0
    $ _window_show()


    WelcomeGuy "Welcome to game"

    WelcomeGuy "Your eyes look a little red. Don't forget to blink while you are here!"
    #for blink to work correctly, every new show must be behing blink
    show blink

    WelcomeGuy "I am so happy you were able to make it to the Exhibition today!"

    WelcomeGuy "Unfortunately, the Exhibition closes in 5 minutes :("

    show screen countdown(300)

    WelcomeGuy "But enough with the sappy stuff, Lets get that music going!"
    
    play music "theme.mp3"
    show welcomeguy at sprial
    $ renpy.pause (10.0, hard=True)
    
    WelcomeGuy "Pretty killer toon huh"

    jump main

label main:   
    scene bg main
    show blink 
    show guide happy behind blink at Gright

    $ loseFlag = False

    Guide "Hi, i am so happy to see you"

    show guide -happy at Gleft
    Guide "We have a wonderful Exhibiton for you today"

    Guide "I will be here to whole time to guide you! Thats why they gave me the name"

    Guide "So, \n"
    show guide happy at Gright
    extend "Where do you want to go?"
        
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'slow' 
    show screen convoCountdown
    $ question()
    hide screen convoCountdown

    label wrong:
        $ num = renpy.random.randint(1,2)
        if num == 1:
            show guide mad at Gleft
        else:
            show guide mad at Gright

        $ background = randomizeBackground()
        $ renpy.show(background, behind=["guide"])
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'slow' 
        show screen convoCountdown
        show blink 
        
        Guide "WRONG"
        show guide happy
        $ question()
        hide screen convoCountdown


    label right:

        $ num = renpy.random.randint(1,2)
        if num == 1:
            show guide happy at Gleft
        else:
            show guide happy at Gright

        $ background = randomizeBackground()
        $ renpy.show(background, behind=["guide"])
        show blink 
        
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'slow' 
        show screen convoCountdown
        Guide "That was a great time!"
        $ question()
        hide screen convoCountdown

    label slow:
        
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'slow' 

        $ num = renpy.random.randint(1,2)
        if num == 1:
            show guide sad at Gleft
        else:
            show guide sad at Gright

        $ background = randomizeBackground()
        $ renpy.show(background, behind=["guide"])
 
        show screen convoCountdown
        Guide "You are taking sooo long"
        $ question()
        hide screen convoCountdown

label missedHat:
    show hatman
    hatman "waste of my time"
    
    jump right

label hat:
    hide screen convoCountdown
    "Unknown Voice" "Hey "
    extend "psst..."
    extend " over here"

    "Unknown Voice but louder" "HEY! "
    extend "LOOK AT ME !"

    show hatman at creepIn
    $ renpy.pause (2.0, hard=True)
    hatman "come here, check this out"
    label choose:
        $ time = 2
        $ timer_range = 2
        $ timer_jump = 'missedHat' 
        show screen convoCountdown
        menu:
            "Limited Time Response"

            "sure i guess":
                $ hatFlag = True
                hide screen convoCountdown
                show hatman happy
                hatman "eeheehee hee…"
                $ randSnack = renpy.random.choice(['worms', 'juice', 'lint'])

                if (randSnack == 'worms'):
                    hatman "this is my favourite snack... enjoy..."

                    "Receive a handful of worms from HatMan."
                    jump right

                elif (randSnack == 'juice'):
                    hatman "i juiced this myself…"

                    "Receive freshly squeezed ‘juice?’."
                    jump right

                elif (randSnack == 'lint'):
                    hatman "i found this in my pocket… good for the Gums…"

                    "Receive damp and weird smelling pocket lint."
                    jump right
                    
            "uhhhh, no thanks":
                hide screen convoCountdown
                show hatman mad
                hatman "“hrhhghhhhrhhhhrhhhghghhrhhhhhhghhehhrhghhhrhhghhhhhh”"
                jump right
            "...":
                hide screen convoCountdown
                hatman "heyheyheyheyhey come onnnn…. "
                extend "psssst… just take a peek… pleaaaaaaaasesseaseeee…"
                jump choose


label guide:
    hide screen convoCountdown
    scene bg cheese:
        xalign 0.5
        yalign 0.5

    show cycle guide at Gright
    Guide "I am the guide, I will have dialog soon"

    jump right

label survey_intro:
    hide screen convoCountdown
    show SurveyMan behind blink

    $ surveyFlag = True

    sm "Hola."

    jump survey_choice

label survey_choice:

    # Asking if the player wants to do a survey.
    # Will continue to ask until the player says yes.
    menu:

        "Quieres hacer una survey?"

        "Si":

            jump survey_start

        "No":
            sm "Necesitas hacerlo."

            jump survey_choice

label survey_start:

    # Asking the player if they are having fun.
    menu:

        "Tengo divertido?"

        "Si":
            
            sm "Bueno."

        "No":

            sm "Interesante..."
    
    # Asking the player what their favorite exhibition is.
    # Feel free to add all of the exhibits as options, I just don't know how many we're going to have yet.
    menu:

        "Que es tu exhibit favorito?"

        "Cheese":

            sm "Delicioso..."

        "Teeth Garden":

            sm "Muy Bien."

    # Asking the player if they would come back to the exhibition
    menu:

        "Vanga un otra vez?"

        "Si":

            sm "Excelente."

        "No":

            sm "No bueno..."
    
    # Asking who the player's favorite character is.
    # Feel free to add options for all relevant characters.
    menu:

        "Que es tu persona favorito?"

        "Hat Man":

            sm "Misterioso..."

        "Tour Guide":

            sm "No me gusta..."

        "Tu":

            sm "..."

            sm "Gracias"

    # Telling the player the survey is done and to enjoy the exhibition.

    sm "El survey estas terminado."

    sm "Gracias por tu opinion."

    sm "Disfruta de The Exhibition."

    jump right

label themenu:
    "fade to black"
    scene black
    with dissolve
    
    "Main Menu Time"
    scene bg themenu

    show gameoverguy
    GameOverGuy "Game Over"
    $ renpy.full_restart()

label win:
    "you win"
    $ renpy.full_restart()

transform creepIn:
    xalign -2.0
    linear 2 xpos -1.3

transform Gright:
    xalign 3.0
    yalign 0.5 
    linear 0.5 xpos 2.4


transform Gleft:
    xalign -2.0
    yalign 0.5 
    linear 0.5 xpos -1.3

transform sprial:
    anchor (10,0)
    linear 1 yalign 0.0 clockwise circles 1
    linear 1 rotate 30 
    linear 1 yalign 0.0 clockwise circles 1
    linear 1 rotate 60
    linear 1 yalign 0.0 clockwise circles 1
    linear 1 rotate 90
    linear 1 yalign 0.0 clockwise circles 1
    linear 1 rotate 120
    linear 1 yalign 0.0 clockwise circles 1
    linear 1 rotate 0

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

image blink:
    "blink1.png"
    pause 4.0
    "blink2.png"
    pause 0.14
    "blink3.png"
    pause 0.14
    "blink4.png"
    pause 0.14
    "blink5.png"
    pause 0.14
    "blink4.png"
    pause 0.14
    "blink3.png"
    pause 0.14
    "blink2.png"
    pause 0.14
    repeat

image bg cheese:
    "cheese (1).png"
    pause 0.14
    "cheese (2).png"
    pause 0.14
    "cheese (3).png"
    pause 0.14
    "cheese (4).png"
    pause 0.14
    "cheese (5).png"
    pause 0.14
    "cheese (6).png"
    pause 0.14
    "cheese (7).png"
    pause 0.14
    "cheese (8).png"
    pause 0.14
    "cheese (9).png"
    pause 0.14
    "cheese (10).png"
    pause 0.14
    "cheese (11).png"
    pause 0.14
    "cheese (12).png"
    pause 0.14
    "cheese (13).png"
    pause 0.14
    "cheese (14).png"
    pause 0.14
    "cheese (15).png"
    pause 0.14
    "cheese (16).png"
    pause 0.14
    "cheese (17).png"
    pause 0.14
    "cheese (18).png"
    pause 0.14
    "cheese (19).png"
    pause 0.14
    "cheese (20).png"
    pause 0.14
    "cheese (21).png"
    pause 0.14
    "cheese (22).png"
    pause 0.14
    "cheese (23).png"
    pause 0.14
    "cheese (24).png"
    pause 0.14
    "cheese (25).png"
    pause 0.14
    "cheese (26).png"
    pause 0.14
    "cheese (27).png"
    pause 0.14
    "cheese (28).png"
    pause 0.14
    "cheese (29).png"
    pause 0.14
    "cheese (30).png"
    pause 0.14
    "cheese (31).png"
    pause 0.14
    "cheese (32).png"
    pause 0.14
    "cheese (33).png"
    pause 0.14
    "cheese (34).png"
    pause 0.14
    "cheese (35).png"
    pause 0.14
    "cheese (36).png"
    pause 0.14
    "cheese (37).png"
    pause 0.14
    "cheese (38).png"
    pause 0.14
    "cheese (39).png"
    pause 0.14
    repeat 

image cycle guide:
    "Guide Neutral.png"
    pause 0.14
    "Guide Happy.png"
    pause 0.14
    "Guide Mad.png"
    pause 0.14
    "Guide Sad.png"
    pause 0.14
    repeat
    
