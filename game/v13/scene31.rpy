# SCENE 31: Lauren Hospital
# Locations: Hospital/Hotel Lobby/Hotel Corridor/Street
# Characters: AMBER (Outfit: 1), NURSE (Outfit: 1), MC (Outfit: 3), CAMERON (Outfit: 2), LAUREN (Outfit: 3)
# Time: Night

label v13s31:
    scene v13s31_1 # TPP. Show MC carrying Lauren, worried expression, mouth closed, Lauren, eyes closed, mouth closed, Amber ahead of them towards counter in hospital, worried expression mouth open
    with dissolve
   
    am "Hello, our friend here is having a negative reaction to marijuana... It was her first time and I-"

    play music "music/v13/Track Scene 31.mp3" fadein 2

    scene v13s31_2 # TPP. Show Amber looking at nurse, serious expression, mouth closed, MC looing at nurse, serious expression, mouth closed, nurse looking at amber, neutral look, mouth open
    with dissolve

    nurse "Okay, what's her name?"

    scene v13s31_3 # FPP. MC looking at Amber, Amber looking at nurse, neutral expression, mouth open 
    with dissolve

    am "Lauren."

    scene v13s31_99 # FPP. Same positioning as v13s31_3, Nurse looking at amber, Nurse slight smile, mouth open
    with dissolve

    nurse "Last name?"

    scene v13s31_3
    with dissolve

    am "Decker, Lauren Decker."

    scene v13s31_4 # TPP. Show MC looking at Amber, slight smile, mouth closed, Amber looking at MC, alitte surprised expression, mouth closed, Nurse looking at both, slight smile, mouth open  
    with dissolve

    nurse "Okay, I'm the only one here tonight... Our entire staff is out right now. But I can take her back. Except only one person is allowed to go with her."

    scene v13s31_5 # FPP. MC looking at Nurse, Nurse looking at MC, slight smile, mouth open
    with dissolve

    nurse "Based on her current state she'll need to stay the night."

# -If didn't invite Sam
    if v11_invite_sam_europe and not v13_invite_samantha:
        scene v13s31_5a # FPP. Same position as v13s31_5, Nurse looking at MC, annoyed looking, mouth open
        with dissolve

        nurse "A young lady and her brother, him there, came in earlier tonight. You kids need to be more careful..."

        scene v13s31_5b # FPP. Same as v13s31_5, slight smile, mouth closed 
        with dissolve

        u "Oh god, Sam's here too. We should've kept an eye on her. What was I thinking..."

    scene v13s31_6 # FPP. MC looking at Amber, Amber neutral expression, mouth closed
    with dissolve

    u "I'll stay with Lauren."

    scene v13s31_6a # FPP. MC looking at Amber, Amber puts both her hands together, begging expression, mouth open
    with dissolve

    am "[name] please, let me. This is my fault."

    scene v13s31_6b # FPP. Same positioning as v13s31_6a, Amber hands back down to side, serious look, mouth open
    with dissolve

    am "I've been pushing her to do all these stupid things and I want to take responsibility."

    scene v13s31_6c # FPP. Same as v13s31_6b, Amber serious look, mouth closed
    with dissolve

    u "You can't blame yourself."

    scene v13s31_6d # FPP. MC looking at Amber, Amber has hand on foread, looking down, ashamed expression, mouth open
    with dissolve

    am "I can though, and I am. I need to be more aware of who people are and quit trying to make them someone else for my sake. Hand her to me."

    scene v13s31_5 
    with dissolve

    nurse "She'll be able to go home by morning, we just need to let her nerves calm and the drugs to leave her system."

    scene v13s31_7 # FPP. MC watches Amber take Lauren from him, Amber, serious face, mouth open
    with fade

    am "Let's keep this quiet. I don't want her feeling embarrassed."

    #scene v13s31_6
    #with dissolve

    #u "I agree."

    scene v13s31_8 # FPP. MC watches Amber walk off with Lauren, As Amber is walking off, MC thinks to himself
    with dissolve

    u "(Damn, this is crazy.)"

    if v11_invite_sam_europe and not v13_invite_samantha: #placeholder
        $ CharacterService.set_relationship(cameron, Relationship.BRO, mc)

        scene v13s31_100 # TPP. Show Cameron running towwards MC, angry, mouth closed
        with fade

        pause 0.75

        scene v13s31_9 # TPP. MC turning toward the Cameron, slight smile, mouth closed, Cameron slightly closer to MC (compared to v13s21_100), Angry expression, mouth open 
        with dissolve

        ca "Hey! [name]!"

        scene v13s31_10 # FPP. MC looking at Cameron, Cameron Angry expression, mouth open
        with dissolve

        ca "What the fuck is this shit I hear about you, and Samantha at a fucking weed tour?!"

        scene v13s31_10a # FPP. Same positioning as v13s31_10, Cameron Angry expression, mouth closed
        with dissolve

        u "The weed tour I didn't let her go on?"

        scene v13s31_10b # FPP. Same as v13s31_10, Cameron points at MC
        with dissolve

        ca "She said you basically called her a fiend, pissed her off to the point that she relapsed."

        scene v13s31_10c # FPP. Same positioning as v13s31_10, Cameron looking at MC, serious expression, mouth closed
        with dissolve

        u "*Sighs* You know, I actually care about your sister's well-being, Cam."

        scene v13s31_10c
        with dissolve

        u "When she asked to go with Amber and I, I simply said I didn't think it was a good idea due to her history. She took offense and ran off, but I still stand by my decision of not letting her come. I'm sorry."

        scene v13s31_10d # FPP. Same positioning as v13s31_10, Cameron slight smile, mouth open
        with dissolve

        ca "You really tried to stop her from getting high, huh?"

        scene v13s31_10e # FFP. Same as v13s31_10d, mouth closed
        with dissolve

        u "I did."

        scene v13s31_10g # FPP. Show MC looking at Cameron, Slight smile, mouth closed, Cameron looking to the side, slight sad expression, mouth open
        with dissolve

        ca "*Whispers* Fuck."

        scene v13s31_10f # FPP. Same position as v13s31_10, different pose, Cameron serious expression
        with dissolve

        $ grant_achievement("bro_moment")
        ca "I have a hard time trusting that people actually have pure intentions, man. It's obvious you do though..."

        scene v13s31_10d
        with dissolve

        ca "I'll stop tripping, like, whenever you try talking to her and everything. I don't know how you feel, but I'm pretty sure she likes you. And, I think you're a good person to be around her."

        scene v13s31_11 # TPP. MC and Cameron moved down the hallway to isolated area, both neutral expression, both mouth closed
        with dissolve

        pause 1.0
       
        scene v13s31_12 # TPP. MC puts hand on Camerons shoulder, slight smile, mouth open, Cameron looks at MCs hand, slight smile, mouth closed
        with dissolve

        u "Thanks Cam. How are you, man?"

        scene v13s31_13 # FPP. MC looking at Cameron, Cameron looking at MC, slightly sad expression, mouth open
        with dissolve

        ca "This is getting to me, but I'm... I'm holding it together, you know? For her."

        scene v13s31_13a # FPP. Same position as v13s31_13, Cameron tears up, sad expression, eyes looking away, mouth open
        with dissolve

        ca "*Whisper* Fuck."

        scene v13s31_13b # FPP. Same postition as v13s31_13, cameron slight smile, mouth closed
        with dissolve

        u "I'll head back to the hotel, man. Give you some space. Just know, I'm always around for you, bro. Both of you."

        scene v13s31_14 # TPP. Show MC and cameron hugging, MC slight smile, mouth closed, Cameron slight smile, mouth closed  
        with dissolve

        pause 0.75

        scene v13s31_13a
        with dissolve

        ca "Oh, shit. I'm sorry. Um, y-yeah, see you later."

        scene v13s31_13
        with dissolve

        u "(He must be going through some heavy shit.)"

        scene v13s31_13b
        with dissolve

        u "I'll catch up with you later Cameron."

        scene v13s31_15 # FPP. MC watches Cameron walk away, Camerons back toward MC
        with fade

        pause 1
 
        scene v13s31_16 # TPP. Show MC thinking to himself, puzzeled expression, mouth closed   
        with dissolve

        u "(We actually just had a bit of a moment... This must be serious to him. Letting someone get close.)"

    scene v13s31_17 # TPP. Show MC leaving the hospital, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s31_18 # TPP. Show MC walking on the street, neutral expression, mouth closed
    with fade

    pause 0.75

    scene v13s31_19 # TPP. Show MC walking into the hotel lobby, neutral expression, mouth closed
    with fade

    pause 0.75

    scene v13s31_20 # TPP. Show MC walking though hotel lobby, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s31_21 # TPP. Show MC walking in hotel corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s32