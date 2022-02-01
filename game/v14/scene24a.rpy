# SCENE 24a: Gas station pickup
# Locations: Gas Station 
# Characters: MC (Outfit:9), GRAYSON (Gas Station Outfit)
# Time: Evening (Tuesday)

label v14s24a:
    play music "music/v12/Track Scene 33_5.mp3" fadein 2

    scene v14s24a_1 # TPP. MC, smiling, walking towards the door of the gas station.
    with dissolve

    pause 0.75

    scene v14s24a_2 # TPP. MC opening the door to enter the gas station.
    with dissolve

    pause 0.75

    scene v14s24a_3 # TPP. MC walking down an aisle looking for soemthing to buy.
    with dissolve
    
    u "What to buy, what to buy..."

    scene v14s24a_4 # TPP. MC walking down a different aisle looking for something to buy.
    with dissolve

    pause 0.75

    scene v14s24a_5 # TPP. MC walking down the candy aisle looking for something to buy.
    with dissolve

    pause 0.75

    scene v14s24a_6 # TPP. MC stops in the middle of the candy aisle and looks at candy.
    with dissolve

    u "Hmm... (What candy would Amber like best?)"

    scene v14s24a_7 # FPP. Close up on the candy MC has to choose from Twezzlers or Gummy Fish?
    with dissolve

    menu:
        "Twezzlers":
            $ add_point(KCT.BOYFRIEND)
            scene v14s24a_8 # TPP. MC, smiling, grabs Twezzlers from the shelf.
            with dissolve

        "Gummy Fish":
            $ add_point(KCT.BRO)
            $ v14s24a_gummyfish = True
            scene v14s24a_8a # Same as v14s24a but MC grabs Gummy Fish from the shelf.
            with dissolve
    
    pause 0.75

    if v14s24a_gummyfish:
        scene v14s24a_9 # TPP. MC, smiling, walks with the gummy fish towards the cash register (do not show the cashier).
        with dissolve
    
    else:
        scene v14s24a_9a # # TPP. MC, smiling, walks with the Twezzlers towards the cash register (do not show the cashier).
        with dissolve

    pause 0.75

    scene v14s24a_10 # TPP. Camera behind MC, standing at the front counter looking at the clerk who has their back to MC.
    with dissolve

    pause 0.75

    scene v14s24a_11 # FPP. MC looking at the clerk, who has his back to MC. 
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 34_2.mp3" fadein 2

    scene v14s24a_11a # FPP. Same as v14s24a_11 but with Grayson (clerk), facing MC, slightly angry, mouth closed.
    with dissolve

    u "No fucking way... *Laughs*"

    scene v14s24a_11b # FPP. Same as a v14s24a_11a but with Grayson, mouth open.
    with dissolve

    gr "Is something funny, [name]?"

    scene v14s24a_11a
    with dissolve

    u "Ha, no... Nothing. I'm just shocked to find you working here."

    scene v14s24a_11b
    with dissolve

    gr "Well, I need money like everyone else."

    scene v14s24a_11a
    with dissolve

    u "Clearly, yeah, but I just never saw you doing something like this."

    scene v14s24a_11c # FPP. Same as v14s24a_11b, but Grayson mad, mouth open.
    with dissolve

    gr "Well I do. Make a big deal of it and it'll be lights out all over again."

    scene v14s24a_11a
    with dissolve

    u "Chill bro, just ring me up."

    scene v14s24a_11d # Grayson, mad, mouth closed, standing by cash register with his hand out towards MC (waiting for money).
    with dissolve

    pause 0.75

    scene v14s24a_11e # Same as v14s24a_11d, but with MC handing some bills to Grayson.
    with dissolve
    
    pause 0.75

    scene v14s24a_11c
    with dissolve

    gr "Now get the fuck out so I can get back to watching my shows."

    scene v14s24a_11a
    with dissolve

    u "Cartoons?"

    scene v14s24a_11b
    with dissolve

    gr "You got jokes today or somethin'?"

    scene v14s24a_11a
    with dissolve

    u "Haha, later man."

    scene v14s24a_12 # TPP. MC, big smile, mouth closed, pushing on the door to leave the store. Candy is either in pocket (not visible) or you need a bag. 
    with dissolve

    pause 0.75

    scene v14s24a_13 # TPP. MC,laughing, mouth open, walking past the front of the store, walking towards Amber's house. Candy is either in pocket or in a bag. 
    with dissolve

    pause 0.75
    
    scene v14s24a_14 # TPP. MC, smiling, walking down the side walk toward Amber's house. Candy is either in pocket or in a bag. 
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s25