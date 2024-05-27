# This file contains the script for the survey scene

define sm = Character("Survey Man")

image SurveyMan = "SurveyMan.png"

label survey_intro:

    show SurveyMan

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

    return