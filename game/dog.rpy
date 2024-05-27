
define Dog = Character("Dog")

image dog = "dog neutral.png"
image dog mad = "dog angry.png"

label dog:
    hide screen convoCountdown
    $ dogFlag = True
    scene bg sculpture garden
    show blink
    show dog behind blink at topLeft

    Dog "Woof! Bark bark bark bark bark"

    menu:

        "Woof?":
            jump woofbow

        "Bark bark arf":
            jump arf


label woofbow:

    Dog "Woof! Woof woof woof! Bow wow wow bow wow!"
    menu:

        "Woof woof! Woof woof!":
            jump bow

        "Woof.":
            jump arf

label bow:

    Dog "Bow wow wow!"
    hide dog
    jump right

label woof:
    show dog angry
    Dog "RRRRRRRRRR BARK BARK BARK!!!!"
    hide dog
    jump right

label arf:
    show dog angry
    Dog "ARF??? Bark bark bark bark grrrrrrrrrr! GRRRRRRR!!!"
    hide dog
    jump right

transform topLeft:
    xalign 0.5