# SCENE 20: Charli Room Free Roam
# Locations: Hotel Room, Hotel Bathroom, Hotel Room Corridor
# Characters: MC (Outfit: 9), RILEY (Outfit: 2)
# Time: Morning

label v13s20:
    scene v13s20_1 # TPP. Show MC walking into Charli's room, smirking, mouth closed
    with dissolve

    play music music.ck1.v13.Track_Scene_20 fadein 2

    play sound sound.door_close

    u "(Ohhhh shit... I'm gonna fuck some shit up.) *Laughs*"

    call screen v13s20_room

label v13s20_closet:
    $ freeroam10.add("closet")

    scene v13s20clo_1 # TPP. Show MC walking towards the closet, mouth closed, smirking
    #with dissolve

    pause 0.75

    scene v13s20clo_2 # TPP. Show MC opening the closet, mouth closed, smirking
    with dissolve

    pause 0.75

    scene v13s20clo_3 # FPP. MC looking into the closet, some clothes inside
    with dissolve

    u "(Damn, he's got some ugly ass clothes...)"

    u "(They low-key smell good, though. It'd be a shame if someone pissed on his shit...)"

    menu:
        "Soak that shit":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            u "(Guess I gotta be that someone...)"

            scene v13s20clo_4 # TPP. Show MC pissing on Charli's clothes, smirking, mouth closed
            with dissolve

            pause

            scene v13s20clo_3a # FPP. Same as v13s20clo_3, clothes wet
            with dissolve

            u "Ahhh... Call it a stream of revenge. *Chuckles*"

            u "(Ugh... Oh, fuck) *Gags*"

            scene v13s20clo_5 # TPP. Show MC smirking, looking at the wet clothes, smirking, mouth open
            with dissolve

            u "*Laughs* Shit, man... He pisses so many people off, it's only fair he smells like it too. Haha!"

        "That's too far":
            u "*Chuckles* I can't do that nasty shit."
        
    scene v13s20clo_6 # TPP. Show MC walking away from the closet, smirking, mouth closed
    with dissolve

    pause 0.75

    call screen v13s20_room

label v13s20_bleach:
    $ freeroam10.add("bleach")

    scene v13s20bleach_1 # TPP. Show MC bending over, opening the cabinet underneath the sink, slight smile, mouth open, bottle of bleach inside
    #with dissolve

    u "Hmm, what do we have here? Ah! A nice bottle of bleach..."

    scene v13s20bleach_2 # FPP. MC looking into the cabinet underneath the sink, focus on the bottle of bleach
    with dissolve

    u "What can we do with this?"

    menu:
        "Bleach his suitcase":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ v13s20_bleach_suitcase = True
            u "(Riley said this suitcase is special to him, and that bleach would be a good addition to it... Let's find out.) *Laughs*"

            scene v13s20bleach_3 # TPP. Show MC grabbing the bottle of bleach, smirking, mouth closed
            with dissolve

            pause 0.75

            scene v13s20bleach_4 # TPP. Show MC walking out of the bathroom, smirking, mouth closed, holding the bottle of bleach
            with dissolve

            pause 0.75
            
            scene v13s20bleach_5 # TPP. Show MC in front of Charli's suitcase, smirking, mouth closed
            with dissolve

            pause 0.75

            scene v13s20bleach_6 # FPP. MC watching himself pour the bleach over the suitcase
            with dissolve

            u "Damn, that's potent! *Chuckles* This is so fucked up... But, well deserved, right?"

            scene v13s20bleach_5a # TPP. Same as v13s20bleach_5, Charli's suitcase bleached out
            with dissolve

            u "(He's gonna need therapy after today.) *Laughs*"

            scene v13s20bleach_4a # TPP. Same as v13s20bleach_4, MC walking back into the bathroom
            with dissolve

            pause 0.75

            scene v13s20bleach_3a # TPP. Same as v13s20bleach_3, MC putting the bleach back
            with dissolve

            pause 0.75

            scene v13s20bleach_1a # TPP. Same as v13s20bleach_1, MC closing the cabinet
            with dissolve

            pause 0.75

        "That's too far":
            u "Damn, that's potent! *Chuckles* This is so fucked up..."

            scene v13s20bleach_1a
            with dissolve

            pause 0.75
    
    call screen v13s20_bathroom

label v13s20_toothbrush:
    $ freeroam10.add("brush")

    scene v13s20brush_1 # TPP. MC grabbing the toothbrush, smirking, mouth closed
    #with dissolve

    pause 0.75

    scene v13s20brush_2 # TPP. Show MC standing in front of the toilet, holding the toothbrush, smirking, mouth closed
    with dissolve

    pause 0.75

    scene v13s20brush_3 # FPP. MC looking down at the toilet, holding the toothbrush
    with dissolve

    u "Ha... The classic \"toothbrush in the toilet\" trick, shall we?"

    menu:
        "Flush, flush, motherfucker!":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v13s20brush_4 # TPP. Show MC bending over the toilet, sticking the toothbrush in the toilet, smirking, mouth closed
            with dissolve

            pause 0.75

            scene v13s20brush_5 # FPP. Same positioning as v13s20brush_4, MC sticking the toothbrush in the toilet
            with dissolve

            grant Achievement("flush_flush", "Flush Charli's toothbrush")
            u "TASTE SHIT BITCH! *Chuckles*"

            scene v13s20brush_5a # FPP. Same as v13s20brush_5, MC moved the toothbrush a bit
            with dissolve

            u "This is why you shouldn't be a trashy human being, pal..."

        "Too much":
            u "(Nah... I won't do that. I'd have to kill someone if they did that to me.)"
    
    scene v13s20brush_1a # TPP. Same as v13s20brush_1, MC putting the toothbrush back, smirking, mouth closed
    with dissolve

    pause 0.75

    call screen v13s20_bathroom

label v13s20_end:
    scene v13s20end_1 # TPP. Show MC walking over to the laptop, smirking, mouth closed
    #with dissolve

    pause 0.75

    scene v13s20end_2 # TPP. MC sitting, using the laptop, clicking on it (don't show the screen), MC smirking, mouth open
    with dissolve

    u "What do we have here?"

    scene v13s20end_3 # TPP. Same as v13s20end_2, different angle
    with dissolve

    u "*Whispers* Is this man doing homework on the trip? *Chuckles*"

    scene v13s20end_2a # TPP. Same as v13s20end_2, MC slightly shocked
    with dissolve

    u "Hmm... Oh, shit. This is Mr. Lee's test..."

    scene v13s20end_3a # TPP. Same as v13s20end_3, MC very shocked
    with dissolve

    u "He's doing tests for people in Mr. Lee's class!? This is..."

    scene v13s20end_2a
    with dissolve

    u "\"The final turned out great, I can't thank you enough, Charli. Academic honors scholarship, here I come!\""

    scene v13s20end_2
    with dissolve

    u "Haha! This is too fucking good... He's helping students cheat their way to the top..."

    scene v13s20end_4 # TPP. Same as v13s20_3, different angle, MC different pose, mouth closed
    with dissolve

    u "(I could put an end to him with this... He's getting paid big bucks... I mean, this is a whole damn business! I should expose his ass, right? Look at all of these fucking emails, I could get him expelled...)"

    menu:
        "Expose him":
            $ v13_charli_exposed = True
            scene v13s20end_5 # TPP. Same as v13s20end_4, different angle
            with dissolve

            u "(Bye, bye Charli! You had a nice run. *Chuckles*)"

            scene v13s20end_4
            with dissolve

            u "(Let's send all of this over to Mr. Lee and see what he thinks.)"

            scene v13s20end_2
            with dissolve

            u "Alright... Forward email... MrLee@CK.com... and sent! Just in case, I'll send it to myself too.)"

        "Confront him":
            scene v13s20end_5
            with dissolve

            u "(I'll just wait to see what Charli has to say about all of this...)"

            scene v13s20end_2
            with dissolve

            u "Either way though, this man won't be fucking with me anymore. That, I'm sure of."

    scene v13s20_6 # TPP. Show MC closing the laptop, smirking, mouth closed
    with dissolve

    u "(Time to unleash some hell.)"

    scene v13s20_7 # TPP. Show MC leaving the hotel room, smirking, mouth closed, Riley standing outside, looking at him, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s20_8 # FPP. MC and Riley standing outside the hotel room, looking at each other, Riley slight smile, mouth open
    with dissolve

    ri "Hey! How'd it go? Spill the tea..."

    scene v13s20_8a # FPP. Same as v13s20end_8, Riley mouth closed
    with dissolve

    u "Better than you'd expect... Follow me."

    scene v13s20_9 # TPP. Show MC and Riley walking through the hotel corridor, MC in front of Riley, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    if v13_charli_exposed:
        jump v13s21a 
    else:
        jump v13s21