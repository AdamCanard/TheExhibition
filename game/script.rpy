# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define WelcomeGuy = Character("Guy Who welcomes you to the game")
define GameOverGuy = Character("Guy Who tells you game over")

image bg cheese:
    "cheese one.png"
    pause 0.14
    "cheese two.png"
    pause 0.14
    "cheese three.png"
    pause 0.14
    "cheese four.png"
    pause 0.14
    repeat 

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bus

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "PlaceHolder Name" "PlaceHolder Text"

    $ _window_hide()

    show welcomeguy:
        xalign 0.0
        linear 1.5 xpos 0.70
        linear 0.2 xpos 0.10
    pause 2.0
    $ _window_show()

    # These display lines of dialogue.

    WelcomeGuy "Welcome to game"

    WelcomeGuy "play the music"
    play sound "woof.mp3"
    extend "Bark"

    menu:

        "Do you want cheese time?"

        "Yes":

            jump cheese

        "No":
            jump themenu



label cheese:
    scene bg cheese

    WelcomeGuy "cheese time"
    # This ends the game.
    return

label themenu:
    "fade to black"
    scene black
    with dissolve
    
    "Main Menu Time"
    scene bg themenu

    show gameoverguy
    GameOverGuy "Game Over"
    return

    
