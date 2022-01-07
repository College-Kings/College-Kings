# SCENE 15: Imre GIRL IN HALLWAY
# Locations: College Campus (outside), Campus buildings entrances, Campus Hallway
# Characters: MC (Outfit: 9), IMRE (Outfit: 2)
# Time: Morning

label v14s15:
    play music "music/v13/Track Scene 1_2.mp3" fadein 2

    scene v14s15_1 # TPP. Outside, MC running between campus buildings. 
    with dissolve

    pause 0.75

    scene v14s15_2 # TPP. Outside, MC pushing open a door, entering a campus building.
    with dissolve

    pause 0.75

    scene v14s15_3 # FPP. MC looking down a hallway and seeing «Lindsey for President» posters down both walls.
    with dissolve

    u "(Holy... shit... This is serious!)"

    if v11_lindsey_slogan == 1: # 0 or 1, just in case someone fudges the variables
        scene v14s15_4 # FPP. MC looking at a banner with the campaign slogan «Lindsey, Returning The Promise».
        with dissolve
        
    else:
        scene v14s15_4a # FPP. MC looking at a banner with the campaign slogan «Lindsey, Say Bye To The Bullshit»
        with dissolve

    pause 1.25

    scene v14s15_5 # FPP. MC looking at a hallways intersection, seeing Lindsey posters on all the walls.
    with dissolve

    pause 1.25 

    scene v14s15_6 # FPP. MC looking at wall with several Lindsey posters. 
    with dissolve

    u "(I can see why Chloe was freaking out now... I don't see a single Chloe poster... She must feel like she can't compete or has already lost.)"

    scene v14s15_7 # FPP. MC looking down the hallway, seeing Imre marching up the hallway, with his hand cupped around his mouth, yelling, mouth open.
    with dissolve

    imre "WOLVES SAY, CHLOE FOR PRESIDENT!"

    scene v14s15_7a # FPP. Same as v14s15_7, but Imre getting closer and head yelling in the opposite direction, hand cupped around open mouth.
    with dissolve

    imre "RESPECT LOYALTY, RESPECT TRADITION!"

    scene v14s15_7b # FPP. Same as v14s15_7a, but Imre level with MC but yelling to the side opposite of MC, hand cupped around open mouth.
    with dissolve

    imre "DON'T BE A TRAITOR LIKE LINDSEY!"

    scene v14s15_7c # FPP. Same as v14s15_7b, but Imre less than an arms leght past MC, yelling, hand cupped around open mouth open.
    with dissolve
    
    imre "WOLVES SAY, VOTE FOR CHLOE!"

    scene v14s15_7d # FPP. Same as v14s15_7c, but MC grabbing Imre by the sholder. Imre slightly turning his head torward his shoulder, still yelling, but hand by his side.
    with dissolve

    pause 0.75

    scene v14s15_7e # FPP. Imre, smiling, mouth closed.
    with dissolve

    u "Hey man, what the hell is going on?"

    scene v14s15_7f # FPP Same as v14s15_7d, but mouth open.
    with dissolve

    imre "Isn't it obvious? Lindsey is running for President, dude."

    scene v14s15_7e
    with dissolve

    u "Yeah, so? What are you doing out here?"

    scene v14s15_7f
    with dissolve

    imre "Supporting Chloe..."

    scene v14s15_7e
    with dissolve

    u "I didn't know you and Chloe were that close."

    scene v14s15_7f
    with dissolve

    imre "We're not, but the Chicks President should be the hottest girl and Chloe is the hottest."

    scene v14s15_7e
    with dissolve

    u "Wait, that's how you're deciding? *Chuckles*"

    scene v14s15_7g # FPP. Same as v14s15_7f, but bigger smile and slight different body position.
    with dissolve

    imre "That's how I decide everything. It's a very fair and balanced scale."

    scene v14s15_7e
    with dissolve

    menu:
        "It's genius":
            $ add_point(KCT.BRO)
            u "Not gonna lie, that seems like a genius way to decide things, haha."

            scene v14s15_7f
            with dissolve

            imre "Many call me the Einstein of decision making."

        "It's idiotic":
            $ add_point(KCT.TROUBLEMAKER)

            scene v14s15_7e
            #with dissolve
            
            u "Not gonna lie, that is a ridiculously stupid way to make decisions, haha."

            scene v14s15_7f
            with dissolve

            imre "I'm just ahead of my time."

    scene v14s15_7e
    with dissolve

    u "Why are you saying the Wolves are supporting Chloe, though?"

    scene v14s15_7f
    with dissolve

    imre "Oh, 'cause that part is true. Chris and Chloe have always been tight, and they get along well as Presidents."

    imre "There's no doubt in my mind that this is what Chris would want me to be doing... So, if you'll excuse me, I'll be getting back to impressing the pretty woma-"

    scene v14s15_7g
    with dissolve

    imre "Er, I mean, Chloe..."

    scene v14s15_7h # FPP. MC watching Imre walking down the hall, hand cupped around his mouth, yelling. Imre is several feet down the hall past MC, so his back is to MC.
    with dissolve

    imre "VOTE FOR CHLOE, LOOK AT THAT RACK!"

    scene v14s15_8 # TPP. MC, smiling and thinking to himself.
    with dissolve

    u "(That man is a whole ass character... But I think he has more than one reason why he's on Chloe's side. *Laughs*)"

    stop music fadeout 3
    jump v14s16