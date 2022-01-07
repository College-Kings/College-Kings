# SCENE 48b: Leaving Nora's cabin
# Locations: Nora's Cabin
# Characters: NORA (Outfit: Naked/1), MC (Outfit: Naked/1)
# Time: Evening

label v15s48b:
    if "v15_nora" in sceneList: # Placeholder
        $ nora.relationship = Relationship.FWB
    
        scene v15s48b_1 # TPP. MC and Nora spooning, MC big spoon with his arm around her, Nora holding his hand, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_2 # TPP. Nora flips over and faces MC, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_3 # FPP. MC and Nora laying in bed, Nora looking at MC, MC looking at Nora, Nora smirking, mouth open.
        with dissolve

        no "That was... incredible, [name]."

        scene v15s48b_3a # FPP. Nora looking at MC, MC looking at Nora, Nora smirking, Mouth closed.
        with dissolve

        u "It really was. I hate to break it to you, but I don't think it'll be the last time either."

        scene v15s48b_3
        with dissolve

        no "*Laughs* Fine by me."

        scene v15s48b_4 # TPP. Show Nora grabbing her phone off the side of the bed, slight smile, mouth closed.
        with dissolve

        no "I guess it's time to switch this on."

        play sound "sounds/vibrate.mp3"

        scene v15s48b_5 # TPP. Shot from behind the phone illuminating Nora's face, Nora slight smile, mouth open.
        with dissolve

        no "Oh, God. So many messages."

        scene v15s48b_3a
        with dissolve

        u "See how many people care about you?"

        scene v15s48b_3
        with dissolve

        no "*Sighs* Yeah. Better get back to the Chicks house."

        scene v15s48b_5a # TPP. Show Nora tapping on her phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_3a
        with dissolve

        u "Are you sure?"

        scene v15s48b_3
        with dissolve

        no "Believe me, I could stay here all week and do what we just did. But I've got some explaining to do."

        no "I can't hide here forever."

        scene v15s48b_3a
        with dissolve

        u "You want to get a cab with me?"

        scene v15s48b_3
        with dissolve

        no "No, you go home. I just texted Lorraine to come pick me up."

        scene v15s48b_3a
        with dissolve

        u "Oh, okay. Yeah, probably best I leave you to talk through some stuff."

        scene v15s48b_3
        with dissolve

        no "Yeah. Thanks again, for everything. Tonight was... perfect."

        scene v15s48b_3a
        with dissolve

        u "You really don't have to thank me, Nora. I'd do it all over again a million times, you know that."

        scene v15s48b_6 # TPP. MC and Nora kissing as they lay down.
        with dissolve

        pause 0.75

        scene v15s48b_3a
        with dissolve

        u "I'd better go find my clothes first."

        scene v15s48b_3
        with dissolve

        no "Haha, good idea."

        scene v15s48b_7 # TPP. Show MC walking out of the bedroom naked, Nora watching him, both slight smile, mouth closed.
        with dissolve

        pause 0.75
        
        play sound "sounds/dooropen.mp3"
       
        scene v15s48b_8 # TPP. MC dressed and walking out the front door, Nora behind him watching him leave as her naked body is wrapped in a blanket, both slight smile, mouth closed.
        with dissolve

        pause 0.75

    else:
        $ nora.relationship = Relationship.FRIEND
    
        scene v15s48b_9 # TPP. Show Nora trying to open a bottle of wine in the kitchen.
        with fade

        pause 0.75

        scene v15s48b_10 # FPP. Show the bottle of wine on the counter in the Kitchen, MC looking at Nora, Nora looking at MC, Nora slight smile, mouth closed.
        with dissolve

        u "Nora, I think I'll head back now. Thanks for the wine."

        scene v15s48b_10a # FPP. MC looking at Nora, Nora looking at MC, Nora slight smile, mouth open.
        with dissolve

        no "Oh, okay... If you're sure."

        scene v15s48b_10
        with dissolve

        u "Yeah, it's getting late. I'll order a cab."

        scene v15s48b_11 # TPP. Show MC pulling out his phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_11a # TPP. MC looking at his phone and tapping on it, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_10
        with dissolve

        u "Shouldn't be long."

        scene v15s48b_10a
        with dissolve

        no "It's okay. I was about to text Lorraine to come pick me up soon anyway."

        scene v15s48b_10
        with dissolve

        u "Oh, okay."

        u "I'm glad I came out here. Maybe do it again sometime. You can show me around."

        scene v15s48b_10a
        with dissolve

        no "I'd like that. Thanks for always being the guy who listens to all my shit."

        scene v15s48b_10
        with dissolve

        menu:
            "It's not shit":
                $ add_point(KCT.BOYFRIEND)
                
                u "Haha, it's not shit. It's important to talk through your feelings with someone. Helps you figure things out."

            "You're welcome":
                $ add_point(KCT.TROUBLEMAKER)
                
                u "Haha, you're welcome. Any time, Nora."

        scene v15s48b_10a
        with dissolve

        no "Thanks, [name]."

        scene v15s48b_12 # TPP. Show Nora walking up to MC, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_13 # TPP. Nora and MC hugging, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48b_14 # FPP. Nora infront of MC, MC looking at Nora, Nora looking at MC, Nora slight smile, mouth open.
        with dissolve

        no "See you soon."

        scene v15s48b_14a # FPP. MC looking at Nora, Nora looking at MC, Nora slight smile, mouth closed.
        with dissolve

        u "Bye."

    play sound "sounds/revving.mp3"

    scene v15s48b_15 # TPP. MC standing outside as the cab arrives.
    with fade

    pause 0.75

    play sound "sounds/cardooropen.mp3"

    scene v15s48b_16 # TPP. MC getting in the cab
    with dissolve

    pause 0.75

    jump v15s49