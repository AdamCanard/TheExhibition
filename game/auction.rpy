define Auctioneer = Character("Auctioneer")

image auctioneer = "Auctioneer Neutral.png"
image auctioneer shock = "Auctioneer Shocked.png"
image auctioneer happy = "Auctioneer Happy.png"

label auction:
    hide screen convoCountdown
    scene bg auction
    show blink
    show auctioneer behind blink

    Auctioneer "STEP RIGHT UP FOLKS STEP RIGHT UP WHOSE GONNA TAKE HOME THE LEGENDARY PAINTING “DIRT JUNIOR”"

    Auctioneer "ALL BIDDERS AT THE READY THATS RIGHT FOLKS GET READY TO PLACE THOSE BIDS LETS MAKE HISTORY ALRIGHT GET READY"

    Auctioneer "ONE DOLLAR BID, ONE DOLLAR BID, ALRIGHT TWO, DO I HEAR TWO, ALRIGHT TWO, WHOSE ON THREE"

    $ time = 2
    $ timer_range = 2
    $ timer_jump = 'snooze' 
    show screen convoCountdown

    menu:

        "$3":
            hide screen convoCountdown
            Auctioneer "WHAT AN INSULT I SAY FOLKS THIS GUY HAS NO RESPECT FOR DIRT JUNIOR DID I HEAR A NO RESPECT, BAD TASTE BAD TASTE GET OUTTA HERE!"
            hide auctioneer
            jump right

        "$1000":
            hide screen convoCountdown
            Auctioneer "I HEAR $1000, ANYONE FOR $3000 DO I HEAR A"
            extend " YUP THERE IT IS $3000 HOW ABOUT $4000 "
            extend "OH YEAR DO I HEAR $5000"
            $ time = 1
            $ timer_range = 1
            $ timer_jump = 'snooze' 
            show screen convoCountdown
            menu:
                
                "$5000":
                    hide screen convoCountdown
                    Auctioneer "I HEAR $5000, ANYONE FOR $6000, "
                    extend "WHAT’S THAT $11 000, WHO WANTS DIRT JUNIOR FOR &12 000, THE LEGENDARY PAINTING FOR JUST $12 000?"
                    Auctioneer "DO I HEAR A TWELVE?? OR IS IT ELEVEN? GOING ONCE, GOING. TWICE…SOLD!!!"

                    hide auctioneer
                    jump right
                "$99999":
                    hide screen convoCountdown
                    Auctioneer "WELL WELL WELL LOOKS LIKE WE’VE GOT A CLEVER ONE FOLKS!!!"
                    Auctioneer "AS YOU ALL KNOW I’M LEGALLY REQUIRED TO SELL THIS PAINTING TO THE ONE WHO SAYS THE MAGIC NUMBER WHICH JUST HAPPENS TO BE 99999!!"
                    show auctioneer happy
                    Auctioneer "GOING ONCE AND ONLY ONCE TO THE ONE WITH THE MAGIC TOUCH! SOLD!!!!"

                    $ auctionFlag = True
                    "You receive “Legendary painting Dirt Junior.”"
                    hide auctioneer
                    jump right

        "$5 000 000 000":
            hide screen convoCountdown
            show auctioneer shock 
            Auctioneer "Wait wait wait, five billion? FIVE BILLION???? I was joking about the whole making history thing."

            Auctioneer "$5 000 000 000! GOING ONCE, GOING TWICE, SOLD!!!!!!!!"

            $ auctionFlag = True
            "You receive “Legendary painting Dirt Junior”."
            hide auctioneer
            jump right

label snooze:
    hide screen convoCountdown
    auctioneer "GOING ONCE. GOING TWICE... "
    extend "GOING THRICE!!!"

    auctioneer "SOOOOLD TO NOT YOU"
    hide auctioneer
    jump right