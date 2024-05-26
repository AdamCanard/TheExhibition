# All splash screens can be defined here.

label splashscreen:
    scene black
    with Pause(1)

    show text "{font=DejaVuSans.ttf}{color=#ff0000}WARNING{/color}\n\nThis game was made for the 'Worst Visual Novel Ever' game jam on itch.io.\nIt was created to be {i}purposely{/i} TERRIBLE!\nPlay at your own risk...{/font}" with dissolve
    with Pause(10)

    hide text with dissolve
    with Pause(1)

    return