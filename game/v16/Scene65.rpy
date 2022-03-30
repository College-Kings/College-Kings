# SCENE 65: Designing the cover with Chloe in her room
# Locations: Chloe's Room
# Characters: CHLOE (Outfit: 1), MC (Outfit: 2)
# Time: Thursday Evening

label v16s65:
    scene v16s65_1 # TPP. Show MC (slight smile, mouth closed, looking atr the door) knocking on the front door of the chicks sorority house
    with dissolve

    pause 0.75

    scene v16s65_2 # FPP. Show Chloe (slight smile, mouth open, looking at MC) in the open doorway of the Chicks Sorority house
    with dissolve

    cl "Hey, I just finished getting the photos all ready. Perfect timing!"

    scene v16s65_2a # FPP. Show Chloe (slight smile, mouth closed, looking at MC) in the open doorway of the Chicks Sorority house
    with dissolve

    u "It's my amazing intuition at work. I just know exactly when you need me, haha."

    scene v16s65_2
    with dissolve

    cl "Haha, right... Come on, silly. Sit!"

    scene v16s65_3 # TPP. Chloe (slight smile, mouth is closed, looking at her laptop) leads MC (slight smile, mouth is closed, looking at Chloe) into her bedroom. She has an open laptop on her bed. The laptop has a black screen.
    with dissolve

    pause 0.75

    scene v16s65_4 # FPP. Chloe (slight smile, mouth open, looking at MC) sitting on her bed with her laptop in front of her, the back of the laptop facing MC
    with dissolve

    cl "So, these are the best photos we got. I tried to come up with some interesting options."

    cl "And there's a couple of choices for the headline, too."

    scene v16s65_4a # FPP. Chloe (slight smile, mouth closed, looking at MC) sitting on her bed with her laptop in front of her, the back of the laptop facing MC
    with dissolve

    u "Okay, let me get my brain into gear..."

    scene v16s65_4
    with dissolve

    cl "We haven't got that long. *Laughs*"

    scene v16s65_4a
    with dissolve

    u "Funny. I walked right into that one..."

    # player already made a subtask choice in s12
    ### The UI pops up for the player to choose the cover design
    ### -We exit the UI when the player has made their choices-
    
    if v16_chloe_on_cover : # -if MC chose Promote Chloe on the cover
        # -(Photo one: mid-shot of Chloe smiling and waving a "Vote for Chloe flag", wearing a Chicks t-shirt. Photo two: Chloe in a white bikini with white toenails, posing by Jenny's lagoon from v14, hand on hip. Headline one: Great leadership starts with a beautiful smile! Headline two: I'm ready to dive in, I just need your vote!)

        scene v16s65_4
        with dissolve

        cl "Aw, yay! I was hoping you'd choose that photo, it's my favorite..."

        scene v16s65_4a
        with dissolve

        u "Why didn't you just choose it, then? *Laughs*"

        scene v16s65_4
        with dissolve

        cl "Because I wanted to see what you chose, haha."

        scene v16s65_4a
        with dissolve

        u "And the headline?"

        scene v16s65_4
        with dissolve

        cl "Perfect! I mean, it's me on the cover of the first ever edition of the SVC Times... How else do you describe this?"

        scene v16s65_4a
        with dissolve

        u "Ha, yeah. What an honor, actually! Congrats, Chloe."

        scene v16s65_4
        with dissolve

        cl "It's the SVC Times that should be honored. *Giggles*"

        scene v16s65_4a
        with dissolve

        u "Oookay... And the ego has landed."

        scene v16s65_4
        with dissolve

        cl "Haha, I'm just joking... Still though, who wouldn't want to pick up a newspaper with me on the cover?"

        scene v16s65_4a
        with dissolve

        u "(I can probably think of a few people...)"

    else: # -if MC chose Embarrass Lindsey on the cover

        # -(Photo one: Lindsey on her knees vomiting into the chicks bathroom toilet, in a party dress, old photo. Photo two: Lindsey's first driver's license picture when she was 16 with an awkward smile, wearing no make-up, a big zit on her forehead, and she has one eyelid half-closed. Headline one: #NotMyPresident Headline two: Lindsey WHO???

        scene v16s65_4
        with dissolve

        cl "Haha, nice choice!"

        scene v16s65_4a
        with dissolve

        u "Thanks, that photo really speaks to me."

        scene v16s65_4
        with dissolve

        cl "Oh yeah, and what is it saying?"

        scene v16s65_4a
        with dissolve

        u "\"Yikes.\""

        scene v16s65_4
        with dissolve

        cl "*Laughs* Yikes is right! Hopefully everyone reacts the same way."

        cl "And the headline fits perfectly. With a cover like this, people won't even want to look at Lindsey, let alone vote for her."

        scene v16s65_4a
        with dissolve

        u "Ha. It's going to be a landslide, no doubt."

        scene v16s65_4
        with dissolve

        cl "Damn straight! I'm gonna destroy that bitch..."

        scene v16s65_4a
        with dissolve

        u "Oh-"

    # -Regardless-

    scene v16s65_4
    with dissolve

    cl "Let me email our final decision to Elijah really quick."
    
    menu:

        "Mention their kiss":

            $ add_point(KCT.TROUBLEMAKER)

            scene v16s65_4a
            with dissolve

            u "Are you still recovering from your magical kiss with him? *Laughs*"

            scene v16s65_4b # FPP. Chloe (full smile, mouth open, looking at MC) sitting on her bed with her laptop in front of her, the back of the laptop facing MC
            with dissolve

            cl "Eww, no! Stop it, ugh... I'd actually forgotten about it until now."

            scene v16s65_4
            with dissolve

            cl "Thanks for reminding me, dickhead."

            scene v16s65_4a
            with dissolve

            u "Oops..."

            scene v16s65_4b
            with dissolve

            cl "Ha, now I need to scrub my mouth again."

            scene v16s65_4a
            with dissolve

            u "Come on, it couldn't have been that bad."

            scene v16s65_4
            with dissolve

            cl "Then why don't you do it? Huh?"

            scene v16s65_4a
            with dissolve

            u "Fair point, moving on..."

        "Don't bring it up":
            scene v16s65_4a
            with dissolve

            u "(Why the fuck would I want to remind her of that trauma?)"

    # -Regardless of Elijah choice-

    scene v16s65_4c # # FPP. Chloe (slight smile smile, mouth closed, looking at MC), typing on her laptop, sitting on her bed with her laptop in front of her, the back of the laptop facing MC
    with dissolve

    cl "Sent."

    if chloe.relationship == Relationship.GIRLFRIEND: # -if ChloeGF
        scene v16s65_4b
        with dissolve

        cl "Thanks for all your help again, baby."

        scene v16s65_5 # TPP. Show MC (slight smile, kissing, eyes closed) passionately kissing Chloe (slight smile, kissing, eyes closed)
        with dissolve

        pause 0.75

        scene v16s65_4a
        with dissolve

        u "Mmm, it's always a pleasure."

    else: # -if not chloegf
        scene v16s65_4
        with dissolve

        cl "Thanks for your help, [name]."


    # -end if

    scene v16s65_4b
    with dissolve

    cl "Now get out of here. I'm a busy woman."

    scene v16s65_4a
    with dissolve

    u "Pfft, always kicking me out as soon as it gets good... *Groans*"

    scene v16s65_4
    with dissolve

    cl "Hehe, I appreciate you!"

    scene v16s65_4a
    with dissolve

    u "Thanks. I appreciate you too."

    scene v16s65_4
    with dissolve

    cl "Obviously, haha."

    scene v16s65_4a
    with dissolve

    u "Haha, see you later ego- I mean Chloe."

    scene v16s65_4
    with dissolve

    cl "*Chuckles* Bye!"

    scene v16s65_6 # TPP. Chloe (slight smile, mouth closed) watches MC (slight smile, mouth closed) exit the room.
    with dissolve

    pause 0.75

    jump v16s66 # -Transition to Scene 66-