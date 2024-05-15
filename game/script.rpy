# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narater")

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

    show eileen happy

    # These display lines of dialogue.

    N "Welcome to game"

    N "play the music"
    play sound "woof.mp3"

    show bg cheese

    N "cheese time"
    # This ends the game.

    return
