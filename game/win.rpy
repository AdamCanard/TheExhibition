# This file contains the script for the winning screen.

# This is intended to be spoken by the tour guide.
# Survey Man is being used as a placeholder, feel free to replace him once the tour guide is created.

label win_intro:
    hide screen convoCountdown
    show SurveyMan

    sm "Congrats."

    sm "You have seen everything in the museum."

    sm "Just in time for closing."

    # Feel free to have the tour guide interrupt this choice.
    # Interrupt dialogue: "I don't care."
    menu:

        "Did you have fun?"

        "yes":

            sm "I don't care."

        "no":

            sm "I don't care."

    sm "It's time to leave now."

    scene bg bus

    jump win_bus


label win_bus:

    # Feel free to have the tour guide interrupt this choice.
    # Interrupt dialogue: "GET IN THE BUS!"
    menu:
        "Get in the bus."

        "OK":

            sm "Bye."

        "Fine.":

            sm "You don't have to get snippy with me."

        "No":

            sm "GET IN THE BUS!"

            jump win_bus

    "You are now leaving The Exhibiton."

    "Come again!"

    $ renpy.full_restart()