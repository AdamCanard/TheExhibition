# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define WelcomeGuy = Character("Guy Who welcomes you to the game")
define GameOverGuy = Character("Guy Who tells you game over")
define Guide = Character("Guide")
define hatman = Character("HatMan")

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

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

# The game starts here.

label start:

    scene bg bus

    "PlaceHolder Name" "PlaceHolder Text"

    $ _window_hide()

    show welcomeguy:
        xalign 0.0
        linear 1.5 xpos 0.70
        linear 0.2 xpos 0.50
    pause 2.0
    $ _window_show()


    WelcomeGuy "Welcome to game"

    WelcomeGuy "Turn on the music!"
    play music "theme.mp3"
    show welcomeguy at sprial
    
    $ renpy.pause (10.0, hard=True)
    
    extend "\n\n This i can get down to"

    jump decide

label decide:   
    scene bg bus 
    show welcomeguy

    menu:

        "Where would you like to visit"

        "Guide":

            jump guide

        "Hat Man":
            jump hat

        "End me":
            jump themenu

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

label missedHat:
    show hatman
    hatman "waste of my time"
    jump decide

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
                    jump decide

                elif (randSnack == 'juice'):
                    hatman "i juiced this myself…"

                    "Receive freshly squeezed ‘juice?’."
                    jump decide

                elif (randSnack == 'lint'):
                    hatman "i found this in my pocket… good for the Gums…"

                    "Receive damp and weird smelling pocket lint."
                    jump decide
                    
            "uhhhh, no thanks":
                hide screen countdown
                show hatman mad
                hatman "“hrhhghhhhrhhhhrhhhghghhrhhhhhhghhehhrhghhhrhhghhhhhh”"
                jump decide
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

    jump decide

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

transform Gleft:
    xalign 3.0
    linear 0.5 xpos 2.4

transform Gright:
    xalign -2.0
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


    
