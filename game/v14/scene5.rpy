# SCENE 05: Going to bed - Chloe Roommate
# Locations: Hotel Room
# Characters: MC (Outfit: 3, Boxers), CHLOE (Outfit: 3)
# Time: Evening 

label v14s05:
    play music "music/v13/Track Scene 40_3.mp3" fadein 2

    play sound "sounds/dooropen.mp3"
    pause 0.51

    scene v14s05_1 # TPP. MC, mouth closed, worried, enters through his hotel room door.
    with dissolve

    pause 0.75

    scene v14s05_2 # TPP. MC, mouth closed, worried, walks towards his bed while Chloe sits on her bed.
    with dissolve

    pause 0.75

    scene v14s05_3 # FPP. Chloe, mouth closed, smiling at MC.
    with dissolve
    
    u "*Sighs*"

    scene v14s05_3b # FPP. Chloe, mouth closed, concerned.
    with dissolve

    cl "Everything okay?"

    scene v14s05_4 # TPP. MC, mouth closed, concerned, sits on the edge of the bed close to the pillow/wall feet on floor.
    with dissolve

    pause 0.75

    scene v14s05_4a # TPP. MC, mouth closed, concerned, sits on his bed, back slouched against the wall, knees bent, feet on the bed.
    with dissolve

    pause 0.75

    scene v14s05_4b # TPP. Same as v14s05_4a, but teeth clenched, frustrated, eyes looking up at the ceiling, hands folded behind his head.
    with dissolve

    pause 0.75

    scene v14s05_3a
    with dissolve

    u "It's Imre and Ryan again."

    scene v14s05_3b # FPP. Chloe, mouth open, concerned.
    with dissolve

    cl "Oh no... What happened?"

    scene v14s05_3a
    with dissolve

    u "Long story short, they were actually getting along when Ryan decided it'd be funny to set Imre up with a trans hooker."

    scene v14s05_3e # FPP. Chloe, mouth open, laughing hard, holding her stomach, head slightly tilted back.
    with dissolve

    cl "*Loud laugh*"

    scene v14s05_3f # FPP. Chloe, smiling, mouth open, hands covering her mouth.
    with dissolve

    pause 0.75
    
    scene v14s05_3d # FPP. Chloe, neutral expression, mouth open.
    with dissolve

    cl "Sorry! I shouldn't have laughed, it's just-"

    scene v14s05_3c # FPP. Chloe, neutral expression, mouth closed.
    with dissolve

    u "No, you're right..."

    scene v14s05_3 
    with dissolve

    u "I mean, it's funny and all, but I was done dealing with their pointless beef and now it's starting all over again."

    scene v14s05_3b
    with dissolve

    cl "Well, you can't help everything and everyone... You know?"

    scene v14s05_3a
    with dissolve

    u "Very true, and that's why I'm going to sleep. *Chuckles*"

    scene v14s05_5 # TPP. MC getting off the bed (transition from v14s05_4b).
    with dissolve

    pause 0.75

    scene v14s05_5a # TPP. MC standing next to his bed.
    with dissolve

    pause 0.75

    scene v14s05_5b # TPP. MC taking off his shirt.
    with dissolve

    pause 0.75

    scene v14s05_5c # TPP. MC taking oiff his pants, now wearing his boxers.
    with dissolve

    pause 0.75

    scene v14s05_5d # TPP. MC getting in bed, covers pulled back.
    with dissolve

    pause 0.75

    scene v14s05_5e # TPP. MC laying on his back, head on pillow, mouth closed, tired, looking at Chloe's (off camera).
    with dissolve

    pause 0.75

    scene v14s05_3d
    with dissolve

    cl "Haha, I'll let you get some rest..."

    scene v14s05_3g # FPP. Same as v14s05_3, but with mouth open.
    with dissolve

    cl "I have some campaign things I want to go over, I'll be back in a bit."

    if CharacterService.is_girlfriend(chloe):
        scene v14s05_6 # TPP. Chloe, smiling, mouth closed, getting up from her bed.
        with dissolve

        pause 0.75

        scene v14s05_6a # TPP. Chloe, smiling, mouth closed, walking towards MC's bed. MC in bed, under the covers, arms above the covers.
        with dissolve

        pause 0.75

        scene v14s05_6b # TPP. Same as v14s05_6a, but Chloe bending down, leaning in to give MC a kiss.
        with dissolve
        
        pause 0.75

        scene v14s05_7 # TPP. Close up (head shot), Chloe kissing MC while he is laying in bed.
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 0.75

        scene v14s05_6c # TPP. Same as v14s05_6a, but Chloe standing next to MC's bed, smiling, mouth closed, looking at MC.
        with dissolve
        
        pause 0.75
    
    scene v14s05_8 # FPP. Chloe standing next to MC's bed, smiling, mouth open.
    with dissolve

    cl "Have a good night, okay?"

    scene v14s05_8a # FPP. Same as v14s05_8, but Chloe mouth closed.
    with dissolve

    u "You too."

    scene v14s05_9 # TPP. Chloe walking towards the light switch.
    with dissolve

    pause 0.75

    scene v14s05_9a # TPP. Chloe touching the light switch (lights are on).
    with dissolve

    play sound "sounds/switch.mp3"

    pause 0.75

    scene v14s05_9b # TPP. Chloe walking towards the room door (lights off).
    with dissolve

    pause 0.75

    scene v14s05_9c # TPP. Chloe existing the room door (lights off).
    with dissolve

    pause 0.75

    scene v14s05_10 # TPP. MC laying in bed under the covers, arms above the covers, mouth closed, tired (lights off).
    with dissolve
    
    u "(And as quickly as it began, my day has concluded.)"

    stop music fadeout 3
    jump v14s06