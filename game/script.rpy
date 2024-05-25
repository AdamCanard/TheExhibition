define WelcomeGuy = Character("Guy Who welcomes you to the game")
define GameOverGuy = Character("Guy Who tells you game over")
define Guide = Character("Guide")
define hatman = Character("HatMan")

image guide = "Guide Neutral.png"
image guide happy = "Guide Happy.png"
image guide mad = "Guide Mad.png"

#On screen countdown for decision
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

#init for timer vars
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

init python:
    def question():
        userinput = renpy.input("Where do you want to go?", length=16)
        userinput = userinput.strip()

        if userinput == "guide":
            renpy.call("guide")
        elif userinput == "hat":
            renpy.call("hat")
        else:
            renpy.jump("wrong")
        

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

    #DISPLAY 5:00 Timer

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

    Guide "Hi, i am so happy to see you"

    show guide -happy at Gleft
    Guide "We have a wonderful Exhibiton for you today"

    Guide "I will be here to whole time to guide you! Thats why they gave me the name"

    Guide "So, \n"
    show guide happy at Gright
    extend "Where do you want to go?"
        
    $ question()

    label wrong:
        show guide mad
        Guide "WRONG"
        show guide happy
        $ question()


    label right:
        scene bg main
        show blink 
        show guide happy behind blink at Gleft
        Guide "That was a great time!"
        Guide "Where to next?"
        $ question()
        

    menu:

        "Where would you like to visit"

        "Guide":

            jump guide

        "Hat Man":
            jump hat

        "End me":
            jump themenu

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

label missedHat:
    show hatman
    hatman "waste of my time"
    jump right

label hat:

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
        show screen countdown
        menu:
            "Limited Time Response"

            "sure i guess":
                hide screen countdown
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
                hide screen countdown
                show hatman mad
                hatman "“hrhhghhhhrhhhhrhhhghghhrhhhhhhghhehhrhghhhrhhghhhhhh”"
                jump right
            "...":
                hide screen countdown
                hatman "heyheyheyheyhey come onnnn…. "
                extend "psssst… just take a peek… pleaaaaaaaasesseaseeee…"
                jump choose


label guide:

    scene bg cheese:
        xalign 0.5
        yalign 0.5

    show cycle guide at Gright

    Guide "I am the guide, I will have dialog soon"

    jump right

label themenu:
    "fade to black"
    scene black
    with dissolve
    
    "Main Menu Time"
    scene bg themenu

    show gameoverguy
    GameOverGuy "Game Over"
    return

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
    
