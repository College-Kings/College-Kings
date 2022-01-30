# TIME: FRIDAY NIGHT
# LOCATION: AMBER'S HOUSE
# OUTFITS: SAME AS AMBER HOCO ENDING

label hoco_amb_night:
    $ sceneList.add("v8_amber")
    stop music fadeout 3
    if config_censored:
        call screen censored_popup("v8s5_nsfwSkipLabel1")

    show screen v8s5_amberSexOverlay

    scene v8samb1 # TPP. Show Amber & MC laying on the floor in the living room. Amber begins to remove MC's pants. Amber mouth open, smile.
    with dissolve

    am "This will feel amazing."

    scene v8samb2 # FPP. Show Amber taking off her shirt, Amber smile, mouth closed.
    with dissolve

    pause 0.5

    play music "music/msexy.mp3"

label v8s5_amberBlowjob:
    scene v8samb3 # FPP. Show Amber starting to give MC a blowjob. MC legs spread enough for Amber to fit in-between, Amber looking at MC (Camera). (If needed, place the camera slightly above MC's head to give a clear view, so need not be technically FPP. Just should look first person)
    with dissolve
    pause 1

    image v8am1bj1 = Movie(play="images/v8/Scene 5/v8am1bj1.webm", loop=True, image="images/v8/Scene 5/ambj000.webp", start_image="images/v8/Scene 5/ambj000.webp") # BJ FPP
    image v8am1bj1f = Movie(play="images/v8/Scene 5/v8am1bj1f.webm", loop=True, image="images/v8/Scene 5/ambj000.webp", start_image="images/v8/Scene 5/ambj000.webp")

    image v8am1miss1 = Movie(play="images/v8/Scene 5/v8am1miss1.webm", loop=True, image="images/v8/Scene 5/am3_00.webp", start_image="images/v8/Scene 5/am3_00.webp") # Missionary (?) TPP 1
    image v8am1miss1f = Movie(play="images/v8/Scene 5/v8am1miss1f.webm", loop=True, image="images/v8/Scene 5/am3_00.webp", start_image="images/v8/Scene 5/am3_00.webp")

    image v8am1miss2 = Movie(play="images/v8/Scene 5/v8am1miss2.webm", loop=True, image="images/v8/Scene 5/am4_00.webp", start_image="images/v8/Scene 5/am4_00.webp") # Missionary (?) TPP 2
    image v8am1miss2f = Movie(play="images/v8/Scene 5/v8am1miss2f.webm", loop=True, image="images/v8/Scene 5/am4_00.webp", start_image="images/v8/Scene 5/am4_00.webp")

    image v8am1dt1 = Movie(play="images/v8/Scene 5/v8am1dt1.webm", loop=True, image="images/v8/Scene 5/amff00.webp", start_image="images/v8/Scene 5/amff00.webp") # Deep throat TPP
    image v8am1dt1f = Movie(play="images/v8/Scene 5/v8am1dt1f.webm", loop=True, image="images/v8/Scene 5/amff00.webp", start_image="images/v8/Scene 5/amff00.webp")

    scene v8am1bj1
    with dissolve

    u "Ah fuck. Ahhhh."

    scene v8am1bj1f
    with dissolve
    pause

    scene v8samb4 # FPP. Show MC and Amber standing up, MC begins to remove Amber's underwear. Amber removing MC's shirt so they are now both naked. Both smiling.
    with dissolve

    pause 1

    scene v8samb5 # FPP. Show Amber lying down on the sofa without underwear. Amber looking at the camera, smiling.
    with dissolve

    pause 1

label v8s5_amberMissonary:
    scene v8samb6 # TPP. Show Amber with one leg on MC, MC begins to bang Amber whilst holding her leg with one hand. Amber's eyes roll back in her head. Amber mouth open. Camera from the side.
    with dissolve

    am "Ah that feels... ah so good. Ah.. Fuck me."

    scene v8samb6a # TPP. Same camera as v8samb6, MC mouth open, Amber mouth closed.
    with dissolve

    u "Ahh. Fuck. Ahhh."

    scene v8samb6b # TPP. Same camera as v8samb6, MC mouth closed, Amber mouth open, smile.
    with dissolve

    am "Ahh ah ahhh."

    scene v8am1miss1
    with dissolve
    pause
    am "*Moans*"

    scene v8am1miss2
    with dissolve
    pause

    scene v8am1miss2f
    with dissolve
    pause 2
    u "Ahh fuck!"

    scene v8am1miss1f
    with dissolve
    pause
    am "You want me to finish you off?"
    u "With pleasure!"

    scene v8samb7 # FPP. Amber begins to stand up from the sofa. Amber flirty expression.
    with dissolve

    pause 1

    scene v8samb8 # TPP. Show MC sitting on the edge of the Sofa, Amber sits on thje floor against the sofa with hands on it for support.
    with dissolve

    pause 0.5

label v8s5_amberFacefuck:
    scene v8samb9 # TPP. Show a closeup of Amber putting her mouth on MC's penis. MC places his hands on Amber's head to start banging her mouth.
    with dissolve

    pause 0.5

    scene v8am1dt1
    with dissolve
    pause

    scene v8am1dt1f
    with dissolve
    pause
    u "I'm gonna-"

    scene amff00
    with hpunch
    u "Ahh!"

    scene v8samb10 # FPP. Closeup of Amber still sat on the floor looking at the camera, smile.
    with dissolve

    u "That felt... way better than it usually does."

    scene v8samb10a # FPP. Same camera as v8samb10, Amber mouth open, smile.
    with dissolve

    am "Haha. It's the ecstasy."

    scene v8samb10
    with dissolve

    u "Damn. That was fucking good."
    
    hide screen v8s5_amberSexOverlay
    $ renpy.end_replay()

    scene v8samb10b # FPP. Same camera as v8samb10, Amber mouth open, slight laugh.
    with dissolve

    am "Haha yeah. Better than homecoming?"

    scene v8samb10
    with dissolve

    u "Way fucking better than homecoming."

    scene v8samb10b
    with dissolve

    am "Haha."

    stop music fadeout 3

    scene v8samb11 # TPP. Show Amber lying back down on the floor, MC joins her, they both look tired.
    with dissolve

    pause 0.5

    scene v8samb12 # TPP. Show Amber and MC lying on the floor, both asleep, camera overhead.
    with dissolve

    pause 0.8

    jump hoco_amb_morning

# TIME IS NOW SATURDAY MORNING

label hoco_amb_morning:
    scene v8samb13 # TPP. Same camera as v8samb12, it is now the next morning, MC sits up looking tired, mouth open, Amber still asleep.
    with Fade(0.75, 0.5, 0.75)

    u "Uhh..."

    scene v8samb14 # TPP. Show MC getting dressed, Amber now wakes up and sits up, Amber mouth open, both looking tired.
    with dissolve

    am "Oh shit. Must've passed out on the floor last night."

    scene v8samb15 # FPP. Show Amber starting to get dressed, Amber look tired, mouth closed.
    with dissolve

    u "Haha. Yeah."

    play music "music/mfunk.mp3"

    scene v8samb16 # FPP. Close up of Amber, Amber mouth open, tired expression.
    with dissolve

    am "Breakfast?"

    scene v8samb16a # FPP. Same camera as v8samb16, Amber mouth closed, tired expression.
    with dissolve

    u "Sure."

label v8s5_nsfwSkipLabel1:

    scene v8samb16
    with dissolve

    am "Okay."

    scene v8samb17 # FPP. Show Amber walking off to the kitchen.
    with dissolve

    pause 0.5

    scene v8samb18 # FPP. Now sat at a table in Amber's kitchen. Show MC's plate and him playing around with the food on the plate.
    with dissolve

    u "So where are your parents? I mean you have this whole house to yourself."

    scene v8samb19 # FPP. Close up of Amber sat opposite MC at the table, Amber neutral expression, mouth open.
    with dissolve

    am "Oh yeah... My parents moved away to Europe."

    scene v8samb19a # FPP. Same camera as v8samb19, Amber neutral expression, mouth closed.
    with dissolve

    u "Europe?"

    scene v8samb19
    with dissolve

    am "Yeah, I refused to go. So they left me here, let me keep the house."

    scene v8samb19a
    with dissolve

    u "Well that's a nice setup."

    scene v8samb19b # FPP. Same camera as v8samb19, Amber laugh, mouth open.
    with dissolve

    am "Yeah and who would want to live in Europe anyway. And Germany of all places! Haha."

    scene v8samb19c # FPP. Same camera as v8samb19, Amber smile, mouth closed.
    with dissolve

    u "Germany sounds pretty dope."

    scene v8samb19
    with dissolve

    am "Yeah I know. But I'd rather be here. Much more my vibe."

    scene v8samb19a
    with dissolve

    u "Yeah, I get it."

    scene v8samb19
    with dissolve

    am "I still talk to them all the time, it's not like we're estranged haha. But at least I have the house."

    scene v8samb19a
    with dissolve

    u "Yeah... Well, I'm gonna head out. Probably gonna try to sleep more. I still feel pretty exhausted."

    scene v8samb19
    with dissolve

    am "Yeah, you'll need extra rest."

    scene v8samb19a
    with dissolve

    u "Thanks for the invite."

    scene v8samb19d # FPP. Same camera as v8samb19, Amber smile, mouth open.
    with dissolve

    am "Of course. Anytime."

    stop music fadeout 3

    scene v8samb20 # TPP. Show MC leaving Amber's kitchen, Camera from behind MC.
    with dissolve
    pause 1

    scene black
    with Dissolve(1)
    pause 0.5

    # - CONTINUE at dorm/Wolves house -
    jump aft_amb_night
