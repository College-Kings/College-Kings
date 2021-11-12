# SCENE 46: Mc walks (either to Lindsey or home)
# Locations: MC on the sidewalk; Lauren's room. 
# Characters: MC (Outfit: 1), LAUREN (Outfit: 1) Thursday
# Time: Afternoon

label v14s46: # -MC is walking along the sidewalk when he gets a call from Lauren-
    scene v14s46_1 # TPP. MC, neutral expression, mouth closed, walking from the left to the right (facing right) on the side walk.
    with dissolve

    play sound "sounds/call.mp3"

    pause 0.75

    scene v14s46_2 # FPP. MC, looking at his phone. (if Possible, have picture of Lauren show on the screen).
    with dissolve

    u "(I'm famous today...)"
   
    play sound "sounds/answercall.mp3"

    scene v14s46_3 # TPP. MC, smiling, mouth open, holding his phone to his ear,v facing right, head looking slghtly right with background 1.
    with dissolve
    
    u "Hello?"

    scene v14s46_4 # TPP. Lauren, smiling, excited, mouth open, holding her phone to her ear, facing left, head looking slightly left.
    with dissolve

    la "Hey, so... I just learned something really cool and I have to try it."

    scene v14s46_3a # TPP. Same as v14s46_3, but with MC's different epression (but smiling) and head position but still mostly looking/facing right with background 2 (so it looks like he's walking).
    with dissolve

    u "What is it?"

    scene v14s46_4a # TPP. Same as v14s46_4, but Lauren with a different expression but still facing/looking slightly left.
    with dissolve

    la "I learned the theory of hypnosis, and now I want to try and hypnotize someone... aka you."

    scene v14s46_3
    with dissolve

    u "Haha, okay. When?"

    scene v14s46_4a
    with dissolve

    la "Now?"

    if not v14_help_lindsey: # -If not helping Lindsey
        scene v14s46_3a
        with dissolve

        u "Oh wow, yeah I guess I can volunteer. Where are you?"

        scene v14s46_4
        with dissolve

        la "My place, do you remember where it is?"

        scene v14s46_3
        with dissolve

        u "Yeah of course. *Chuckles* I'll be there soon."

        play sound "sounds/rejectcall.mp3"
        
        scene v14s46_5 # TPP. MC, back to camera, slight angle, walking from left to right on sidewalk.
        with dissolve

        pause 0.75

        jump v14s46a

    else: # -If helping Lindsey
        scene v14s46_3a
        with dissolve

        u "Oh shoot. I can't now, already set something up."

        scene v14s46_4
        with dissolve

        la "Ahh okay, maybe another time?"

        scene v14s46_3
        with dissolve

        u "Sounds good, yeah."

        scene v14s46_4a
        with dissolve

        la "Okay, talk to you soon."

        scene v14s46_3a
        with dissolve

        u "Bye."

        play sound "sounds/rejectcall.mp3"

        scene v14s46_5
        with dissolve

        pause 0.75

        if v14_lindsey_sell: # Sell Car Scene 47 
            jump v14s47

        else: # Steal fund/distract Chloe Scene 49
            jump v14s49