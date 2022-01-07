# SCENE 53: MC goes to bed Riley's bed
# Locations: Hotel Corridor, Hotel Room
# Characters: MC (Outfit: 5), RILEY (Outfit: 5)
# Time: Night

label v13s53:
    scene v13s53_1 # TPP. Show MC walking through the hallway, neutral expression, mouth closed
    with dissolve

    u "(I wonder if Riley is up.)"

    play music "music/v13/Track Scene 52.mp3" fadein 2

    scene v13s53_2 # TPP. Show MC walking into the room, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s53_3 # FPP. MC in the room, looking at Riley, she's lying on her bed, holding a book, looking at MC, slight smile, mouth closed
    with dissolve

    u "What are you doing?"

    if v13s48_ryan_double_date:
        scene v13s53_3a # FPP. Same as v13s53_3, Riley mouth open
        with dissolve
        
        ri "Trying to recover from that failure of a date."

        scene v13s53_3
        with dissolve

        u "You and I both. *Chuckles*"

    else:
        scene v13s53_3a # FPP. Same as v13s53_3, Riley mouth open
        with dissolve

        ri "Just getting some reading in... *Chuckles*"

        scene v13s53_3
        with dissolve

        u "On vacation? Haven't we been over this already? *Laughs*"
    
    scene v13s53_3a
    with dissolve

    ri "I was actually just getting ready to turn out the light. How about you come snuggle up next to me after you do it."

    scene v13s53_3
    with dissolve

    u "*Chuckles* I'm sure I can handle that."

    scene v13s53_4 # TPP. Show MC removing his shirt (already in his boxers), slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s53_5 # TPP. Show MC turning off the lights
    with dissolve

    pause 0.75

    scene v13s53_6 # TPP. Show MC getting into bed with Riley, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s53_7 # TPP. Show MC and Riley snuggling in bed, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s53_8 # TPP. MC and Riley snuggling, show Riley's face, Riley slight smile, mouth open
    with dissolve

    ri "Mmmm... You're always so warm. *Chuckles*"

    scene v13s53_8a # TPP. Same as v13s53_8, Riley mouth closed
    with dissolve

    u "Am I making you hot?"

    scene v13s53_8
    with dissolve

    ri "No, no... You're making me comfortable, I always sleep best when you're next to me."

    scene v13s53_8a
    with dissolve

    u "I'll make sure that happens more often then."

    scene v13s53_8
    with dissolve

    ri "*Chuckles* Good."

    scene v13s53_9 # TPP. Show Riley and MC sleeping together
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s53a