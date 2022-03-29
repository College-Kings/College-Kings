# SCENE 4: Mc goes to bed WOLVES OR APES room (both)
# Locations: Wolves and Apes room.
# Characters: MC (Outfit: 1), Ms. Rose (Outfit: 1)
# Time: Night

init python:
    def v16s4_reply1():
        naomi.messenger.newMessage("That look? It's called motivation. I was motivated to prove how into me you are, and it looks like I've done just that. Buh- bye! <3")
        
    def v16s4_reply2():
        setattr(store, "v16s4_dissnaomi", True)
        naomi.messenger.newMessage("Wtf??? You'll regret this, asshole.")

label v16s4:
    play sound "sounds/dooropen.mp3"

    if joinwolves:
        scene v16s4_1 # TPP. MC walking into his wolves room through the door, neutral face, mouth closed.
    else:
        scene v16s4_14 # TPP. MC walking into his apes room through the door, neutral face, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    if joinwolves:
        scene v16s4_2 # TPP. In wolves room, MC closing the door to his room neutral face, mouth closed.
    else:
        scene v16s4_15 # TPP. In apes room, MC closing the door to his room neutral face, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s4_3 # FPP. In wolves room, MC looking at his bed.
    else:
        scene v16s4_16 # FPP. In apes room, MC looking at his bed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s4_4 # TPP. In wolves room, Close up of just MC's face as he stands in his room, slight smile, mouth closed.
    else:
        scene v16s4_17 # TPP. In apes room, Close up of just MC's face as he stands in his room, slight smile, mouth closed.
    with dissolve

    u "(Finally... My bed! I've missed you so much.)"

    if joinwolves:
        scene v16s4_5 # TPP. In wolves room, Show MC taking off his pants, only in his underwear and shirt, neutral face, mouth closed.
    else:
        scene v16s4_18 # TPP. In apes room, Show MC taking off his pants, only in his underwear and shirt, neutral face, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s4_5a # TPP. In wolves room, Show MC taking off his shirt, only in his underwear, neutral face, mouth closed.
    else:
        scene v16s4_18a # TPP. In apes room, Show MC taking off his shirt, only in his underwear, neutral face, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s4_6 # TPP. In wolves room, Show MC getting into his bed, slight smile, mouth closed.
    else:
        scene v16s4_19 # TPP. In apes room, Show MC getting into his bed, slight smile, mouth closed.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s4_7 # TPP. In the wolves room, Show MC laying in bed with his eyes closed his phone nearby in view (not turned on), neutral face, mouth closed.
    else:
        scene v16s4_20 # TPP. In the apes room, Show MC laying in bed with his eyes closed his phone nearby in view (not turned on), neutral face, mouth closed.
    with fade

    pause 0.75
    
    play sound "sounds/vibrate.mp3"

    if joinwolves:
        scene v16s4_7a # TPP. Show MC laying in bed with his eyes now open his phone nearby in view illuminating the room, Tired, mouth closed.
    else:
        scene v16s4_20a # TPP. Show MC laying in bed in apes room with his eyes now open his phone nearby in view illuminating the room, Tired, mouth closed.
    with vpunch

    u "(For fuck's sake...)"

    if joinwolves:
        scene v16s4_8 # TPP. In wolves room, Show MC in bed reaching to grab his phone, tired, mouth closed.
    else:
        scene v16s4_21 # TPP. In apes room, Show MC in bed reaching to grab his phone, tired, mouth closed.
    with dissolve

    pause 0.75

    $ naomi.messenger.newMessage("Hey, [name]! This is Naomi. The one and only... Lol.", force_send=True)

    if "v15_naomi" in sceneList:
        $ naomi.messenger.newMessage("Just wanted to say, as much as I enjoyed our little bathroom break, don't read too much into it. I just wanted to piss off Aubrey and well... mission succeeded!")
        $ naomi.messenger.newMessage("Anyway, maybe I'll message you again...")
        $ naomi.messenger.newMessage("Maybe I won't ;)")

    else:
        $ naomi.messenger.newMessage("Just wanted to say, as much as I would've enjoyed getting closer with you at the wedding, don't read too much into it. I just wanted to piss off Aubrey, haha. Definitely not into you like that.")
        $ naomi.messenger.newMessage("Still can't believe you turned me down, though?? Things must be serious between you two... Gross.")
        $ naomi.messenger.newMessage("Either way, no second chances ;)")
    
    $ naomi.messenger.addReply("Aw, come on... I saw that look in your eyes all night, we can have some fun together I think? ;)", v16s4_reply1)
    $ naomi.messenger.addReply("Please don't text me again. Thanks.", v16s4_reply2)

    if joinwolves:
        scene v16s4_9 # TPP. In wolves room, Show MC in bed looking at his phone, tired, mouth closed.
    else:
        scene v16s4_22 # TPP. In apes room, Show MC in bed looking at his phone, tired, mouth closed.
    with dissolve

    pause 0.75

    label v16s4_phoneContinue:
        if naomi.messenger.replies:
            call screen phone
        if naomi.messenger.replies:
            u "(I should reply to Naomi.)"
            jump v16s4_phoneContinue
        
    if joinwolves:
        scene v16s4_9
    else:
        scene v16s4_22
    with dissolve

    u "(That girl loves playing games with your emotions... Can't imagine how hard it was growing up with her, ha.)"

    u "(It's finally time to sleep, phew.)"

    if joinwolves:
        scene v16s4_7
    else:
        scene v16s4_20
    with fade

    pause 0.75

    scene v16s4_23 # Black Screen (get from Photoshop or Mozzart)
    with dissolve

    pause 0.75

    if joinwolves and (ms_rose.relationship >= Relationship.FWB or v15_threaten_ms_rose):
        play sound "sounds/call.mp3"

        scene v16s4_7a
        with vpunch

        u "*Groans* (I'm about to throw this fucking phone out the window.)"

        scene v16s4_8
        with dissolve

        pause 0.75

        scene v16s4_9
        with dissolve

        pause 0.75
        
        stop sound

        scene v16s4_10 # TPP. In wolves room, Show MC holding the phone to his ear, tired, mouth open.
        with dissolve

        u "Hello?"

        scene v16s4_11 # TPP. Just Ms. Rose outside on her phone, slight smile, mouth open [DO NOT SHOW FRAT HOUSE].
        with dissolve

        ro "[name], it's Lorraine. I'm outside... Can you come down, please? I want to talk."

        scene v16s4_12 # TPP. Just Ms. Rose outside on her phone, slight smile, mouth closed [DO NOT SHOW FRAT HOUSE].
        with dissolve

        u "You're... outside?! Is everything okay?"

        scene v16s4_11
        with dissolve

        ro "Yes, I'm fine. Please hurry, it won't take long."

        scene v16s4_12
        with dissolve

        u "Okay, I'll be right down."

        play sound "sounds/rejectcall.mp3"

        scene v16s4_9a # TPP. In wolves room, MC laying in bed looking at his phone, slight smile, mouth closed.
        with dissolve

        u "(Am I dreaming? *laughs*)"

        scene v16s4_13 # TPP. In wolves room, shot from behind MC of him getting up.
        with dissolve

        pause 0.75

        jump v16s5

    else:
        jump v16s4a