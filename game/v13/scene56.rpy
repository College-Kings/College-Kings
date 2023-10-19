# SCENE 56: Nora and MC Gift Shop
# Locations: Gift Shop, Street, Hotel Lobby
# Characters: MC (Outfit: 3), NORA (Outfit: 1)
# Time: Morning

label v13s56:
    scene v13s56_1 # TPP. show MC and nora walking down the sidewalk to the gift shop, slight smiles, mouths closed
    with dissolve

    pause 0.75

    play music music.ck1.v13.Track_Scene_56 fadein 2

    scene v13s56_1a # TPP. Same as v13s56_1, different place on sidewalk
    with dissolve

    pause 0.75

    scene v13s56_2 # FPP. show just nora, slight smile, mouth closed, looking at MC
    with dissolve

    u "Finding a gift at a gift shop should be easy, right?"

    scene v13s56_2a # FPP. Same as v13s56_2, nora mouth open
    with dissolve

    no "It better be. *Chuckles* I don't have all day."

    scene v13s56_2
    with dissolve

    u "*Laughs* Do you have other plans?"

    scene v13s56_2a
    with dissolve

    no "Well, no, but I don't wanna be out here shopping all day."

    scene v13s56_2
    with dissolve

    u "I definitely feel that. *Chuckles*"

    if CharacterService.is_fwb(nora):
        scene v13s56_2
        with dissolve

        u "I'll have to get you a gift someday."

        scene v13s56_2a
        with dissolve

        no "*Chuckles* Why?"

        scene v13s56_2
        with dissolve

        u "After the gift you gave me the other night, I need to return the favor."

        scene v13s56_2b # FPP. same as v13s56_2a nora slightly embarrassed
        with dissolve

        no "Oh my god... Don't bring that up... In public."

        scene v13s56_2
        with dissolve

        u "*Chuckles*"

    scene v13s56_2a
    with dissolve

    no "So, what are we getting them?"

    scene v13s56_2
    with dissolve

    u "What? I thought you'd at least have an idea. You are the one that came up with this idea. I'm just the piggy bank."

    scene v13s56_2a
    with dissolve

    no "Lorraine likes basic lady stuff and Mr. Lee is all about weird history things, so keep those things in mind."

    scene v13s56_3 # TPP. Nora and MC walk into the gift shop from the sidewalk their backs are turned to the camera
    with dissolve

    pause 1

    scene v13s56_4 # TPP. Inside the gift shop, MC and Nora start looking around the store and they are looking at different things
    with dissolve

    pause 1

    scene v13s56_5 # FPP when Nora sees something and bends over with her ass toward MC
    with dissolve

    no "Hmm, these are actually kinda nice..."

    scene v13s56_5
    with dissolve

    menu:
        "*Accidently* bump against her":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v13s56_98 # TPP. MC grinds up against Nora's ass, Nora looks back slightly shocked, mouth open
            with dissolve

            u "Oh, my bad."

            scene v13s56_5b # FPP. same as v13s56_5a, nora stands straight, body facing towards mc, no expression, mouth closed, and looks left
            with dissolve

            pause 0.75

            scene v13s56_5c # FPP. same as v13s56_5b nora looks right
            with dissolve

            pause 0.75

            scene v13s56_5d # FPP. same as v13s56_5c nora looks at MC, slightly annoyed, mouth open
            with dissolve

            no "All that space and you had to bump into me?"

            scene v13s56_5e # FPP. same as v13s56_5d nora mouth closed
            with dissolve

            u "I said my bad. *Chuckles*"

            if CharacterService.is_fwb(nora):
                scene v13s56_5f # FPP. same as v13s56_5d nora slight smile
                with dissolve

                no "Yeah... I heard you."

            else:
                scene v13s56_5d
                with dissolve

                no "Yeah... I heard you."

        "Be respectful":
            $ reputation.add_point(RepComponent.BRO)
            scene v13s56_99 # FPP. same as v13s56_5 MC looks down at his crotch
            with dissolve

            grant achievement("calm_down_big_fella", "Respect Nora")
            u "(Calm down big fella.)"

    scene v13s56_5f
    with dissolve

    no "What do you think about this?"

    scene v13s56_5h # FPP. same as v13s56_5f nora mouth closed
    with dissolve

    u "What is it?"

    scene v13s56_5i # FPP. same as v13s56_5h Nora holds up a perfume
    with dissolve

    u "For Ms. Rose?" 

    scene v13s56_5j # FPP. same as v13s56_5i nora slightly annoyed, mouth open
    with dissolve

    no "*Sarcasm* No, for Mr. Lee..."

    scene v13s56_5k # FPP. same as v13s56_5i nora slight smile, mouth open
    with dissolve

    no "Obviously it's for her. *Chuckles*"

    scene v13s56_5i
    with dissolve

    u "Haha. You think she'll like it? It's kinda... basic."

    scene v13s56_5k
    with dissolve

    no "That's exactly how I know she'll like it. *Chuckles*"

    scene v13s56_5i
    with dissolve

    u "*Laughs* Perfect. One down and one to go."

    scene v13s56_4
    with dissolve

    pause 0.75

    scene v13s56_4a # FPP same as v13s56_4 MC and nora have switched positions
    with dissolve

    pause 0.75

    scene v13s56_6 # FPP nora holds up a bonsai tree, slight smile, mouth open, looking at mc
    with dissolve

    no "Mr. Lee has one of these plants as his wallpaper on his phone."

    scene v13s56_6a # FPP. same as v13s56_6 nora mouth closed
    with dissolve

    u "*Chuckles* I don't doubt it."

    scene v13s56_6
    with dissolve

    no "Let's just get him one then."

    scene v13s56_6a
    with dissolve

    u "If it's his phone wallpaper I'm sure he already has one, don't you think?"

    scene v13s56_6b # same as v13s56_6 nora slightly annoyed
    with dissolve

    no "Would you tell a woman who likes flowers that she has enough?"

    scene v13s56_6a
    with dissolve

    u "Haha... Good point."

    scene v13s56_6c # FPP. same as v13s56_6a nora is holding both the perfume and the bonsai tree, full smile
    with dissolve

    no "Alright, so we're good?"

    scene v13s56_6d # FPP. same as v13s56_6c nora is slightly concerned
    with dissolve

    u "Depends, how much are those?"

    scene v13s56_6e # FPP. same as v13s56_6d MC grabs the perfume and Bonsai from nora, and looks down at them in his hands
    with dissolve

    u "I can't afford both of these, Nora. *Chuckles*"

    scene v13s56_6f # FPP. same as v13s56_6e nora slightly sad, mouth open, mc looks back up at nora
    with dissolve

    no "What? Damn... You're not even a good piggy bank."

    scene v13s56_6g # FPP. same as v13s56_6f nora mouth closed
    with dissolve

    u "Hey! I'm not rich."

    scene v13s56_6h # FPP. same as v13s56_6f nora slight smile
    with dissolve

    no "*Chuckles* I'm just messing with you."

    scene v13s56_6h
    with dissolve

    no "Just choose one and I'll figure out something else for the person we don't buy a gift for."

    scene v13s56_6i # FPP. same as v13s56_6h nora mouth closed
    with dissolve

    u "Hmm, okay..."

    scene v13s56_6e
    with dissolve

    menu:
        "Perfume":
            $ v13_perfume = True

            u "Let's go with the perfume."

            scene v13s56_6j # FPP. same as v13s56_6h mc hands nora the Perfume
            with dissolve

        "Bonsai":
            scene v13s56_6e
            #with dissolve

            u "Let's go with the Bonsai."

            scene v13s56_6k # FPP. same as v13s56_6h mc hands nora the Bonsai
            with dissolve

    pause 0.75
        
    scene v13s56_7 # FPP. show nora slight smile mouth open looking at mc
    with dissolve

    no "Alrighty, sounds good. Go ahead and put the other one back and I'll meet you out front."

    scene v13s56_7a # FPP. same as v13s56_7 nora mouth closed
    with dissolve

    u "Don't you need the money?"

    scene v13s56_7
    with dissolve

    no "Oh, duh... *Laughs*"

    scene v13s56_7a
    with dissolve

    u "You'd be lost without me today. *Chuckles*"

    scene v13s56_7
    with dissolve

    no "*Chuckles* Kinda true, yeah."

    scene v13s56_7b # FPP. same as v13s56_7a MC hands Nora some money
    with dissolve

    pause 0.75

    scene v13s56_7c # FPP. same as v13s56_7b nora turns her back to MC, MC grabs her wrist
    with dissolve

    pause 0.75

    scene v13s56_7b
    with dissolve

    u "Get yourself something nice."

    scene v13s56_7d # FPP. same as v13s56_7b noras smile increases
    with dissolve

    no "Okay hot shot... *Chuckles*"

    scene v13s56_7e # FPP. same as v13s56_7c MC doesn't grab her wrist
    with dissolve

    u "(She really is a great person deep down.)"

    if v13_perfume:
        scene v13s56_8 # FPP. MC puts perfume back on shelf
        with dissolve

        pause 0.75

    else:
        scene v13s56_8a # FPP. same as v13s56_8 MC puts bonsai back on shelf instead
        with dissolve

        pause 0.75

    scene v13s56_3a # TPP. same as v13s56_3 MC no expression, mouth closed, is waiting outside the gift shop alone
    with dissolve

    pause 0.75

    scene v13s56_3b # TPP. same as v13s56_3a MC different position
    with dissolve

    pause 0.75

    scene v13s56_3c # TPP. same as v13s56_3b MC different position
    with dissolve

    pause 0.75

    scene v13s56_3d # TPP. same as v13s56_3c MC standing at front door and looks at nora as she walks out of the gift shop slightly angry, mouth, closed
    with dissolve

    pause 0.75

    scene v13s56_9 # FPP. MC and Nora standing outside the gift shop, nora slightly angry, mouth closed, looking at MC
    with dissolve

    u "What took so long?"

    scene v13s56_9a # FPP. same as v13s56_9 nora mouth open
    with dissolve

    no "The cashier guy was threatening to call the police because he thought the money was fake!"

    scene v13s56_9
    with dissolve

    u "The fuck?"

    scene v13s56_9a
    with dissolve

    no "I was defending it, but then for a minute I was like, did [name] give me fake money?"

    scene v13s56_9
    with dissolve

    u "*Laughs* Why would I do that?"

    scene v13s56_9b # FPP. same as v13s56_9a nora slight smile
    with dissolve

    no "I don't know... I was getting nervous. *Chuckles*"

    scene v13s56_9c # FPP. same as v13s56_9b nora mouth closed
    with dissolve

    u "Well, good thing that's all over. Let's go gift giving."

    if v13_perfume:
        scene v13s56_1b_b # TPP. same as v13s56_1a nora and MC's backs are turned
        with dissolve

    else:
        scene v13s56_1b_a # TPP. same as v13s56_1a nora and MC's backs are turned
        with dissolve

    pause 0.75

    if v13_perfume:
        scene v13s56_1c_a # TPP. same as v13s56_1 nora and MC's backs are turned
        with dissolve

    else:
        scene v13s56_1c_b # TPP. same as v13s56_1 nora and MC's backs are turned
        with dissolve

    pause 0.75

    if v13_perfume:
        scene v13s56_10a # TPP. MC and nora arrive at the hotel front door and walk in, both slight smiles, mouths closed, street perspective
        with dissolve

    else:
        scene v13s56_10 # TPP. MC and nora arrive at the hotel front door and walk in, both slight smiles, mouths closed, street perspective
        with dissolve
    
    pause 0.75

    if v13_perfume:
        scene v13s56_11b # TPP. MC and nora walk into the lobby, slight smiles, mouths closed, lobby perspective facing hotel front door
        with dissolve

    else:
        scene v13s56_11a # TPP. MC and nora walk into the lobby, slight smiles, mouths closed, lobby perspective facing hotel front door
        with dissolve

    pause 0.75

    stop music fadeout 3

    if v13_perfume:
        jump v13s57

    else:
        jump v13s57a