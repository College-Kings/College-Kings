# Hallway with Nora
# Location: College Hallways
# Outfits: MC Outfit 2, Nora Outfit
# Time: Tuesday Morning

label hallway_w_nora:
    scene v8shal1 # TPP. Show MC walking down the college hallways, Nora walking towards MC in the distance with brochures in hand.
    with fade

    pause 0.5

    play music "music/mchill2.mp3"
    queue music "music/mindie4.mp3"

    scene v8shal2 # TPP. Show MC continuing to walk down the hallway, MC notices Nora and Nora notices MC.
    with dissolve

    if CharacterService.is_mad(nora):
        $ nora.relationship = Relationship.FRIEND
        scene v8shal3 # FPP. Close up Nora, Nora neutral expression, mouth open.
        with dissolve
        no "Hey, [name]... uh... got a sec?"

        scene v8shal3a # FPP. Same camera as v8shal3, Nora neutral expression, mouth closed.
        with dissolve
        u "Sure."

        scene v8shal3
        with dissolve
        no "We got off to a rough start, but can we just get past that?"

        scene v8shal3a
        with dissolve
        u "Sure, I'm not upset. I'd like to be friends."

        scene v8shal3
        with dissolve
        no "Good because..."

        jump cont_nora_hall

    else:
        scene v8shal3d # FPP. Same camera as v8shal3, Nora smile, mouth open.
        with dissolve
        no "Hey! [name] I'd like to speak with you."

        scene v8shal3c # FPP. Same camera as v8shal3, Nora smile, mouth closed.
        with dissolve
        u "Sure! What's up?"

        $ nora.relationship = Relationship.LIKES

        jump cont_nora_hall

label cont_nora_hall:
    scene v8shal3d
    with dissolve

    no "I'm signing people up for the annual school trip to Europe."

    scene v8shal3c
    with dissolve

    menu:
        "Act excited":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            jump nora_trip_exc

        "Act nervous":
            jump nora_trip_nerv


label nora_trip_exc:
    u "Wow that sounds awesome!"

    scene v8shal3
    with dissolve

    no "That's why I'm doing this. I wouldn't work on a project that was doomed to fail."

    scene v8shal3a
    with dissolve

    u "Of course you wouldn't."

    jump cont_nora_hall_2

label nora_trip_nerv:
    u "Wow that sounds awesome...ly expensive."

    scene v8shal3
    with dissolve

    no "If you can afford to come here, you can afford the trip."

    scene v8shal3a
    with dissolve

    u "Some of us are on scholarship."

    scene v8shal3d # FPP. Same camera as v8shal3, Nora shocked, mouth open.
    with dissolve

    no "You're a scholarship kid?"

    scene v8shal3e # FPP. Same camera as v8shal3, Nora shocked, mouth closed.
    with dissolve

    u "No, I'm just saying, Europe is the other side of the world. Not everyone has that kind of money."

    jump cont_nora_hall_2

label cont_nora_hall_2:
    scene v8shal3
    with dissolve

    no "It's a great opportunity since the school is covering up to half the price."

    scene v8shal3a
    with dissolve

    u "Half? That helps a lot."

    scene v8shal3
    with dissolve

    no "...IF I can get at least ten signups."

    scene v8shal3a
    with dissolve

    u "It's a big school. I'm sure you can find ten people who..."

    scene v8shal3f # FPP. Same camera as v8shal3, Nora excitable expression, mouth open.
    with dissolve

    no "I think it's something everyone should do if they can. Traveling is very important."

    scene v8shal3c
    with dissolve

    u "(I've never seen Nora excited about anything.)"

    scene v8shal3d
    with dissolve

    no "So you gonna come?"

    scene v8shal3c
    with dissolve

    menu:
        "Accept invitation":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            jump nora_hall_eu_go
        "Consider it":
            jump nora_hall_eu_no


label nora_hall_eu_go:
    u "Sure! Don't know when I'd get another opportunity like this!"

    jump cont_nora_hall_3

label nora_hall_eu_no:
    u "(Hmm, it's still a lot of money but I don't want to upset Nora.)"

    jump cont_nora_hall_3

label cont_nora_hall_3:
    scene v8shal4 # TPP. Show Nora handing MC a flyer, nora mouth open, smile.
    with dissolve

    no "Here!"

    scene v8shal3d
    with dissolve

    no "If you know any friends who would be interested, tell them to come find me. Remember, I need ten people. Ten!"

    scene v8shal3c
    with dissolve

    u "Ten! Gotcha."

    scene v8shal3
    with dissolve

    no "Wanna help me pass out flyers before your next class?"

    scene v8shal3c
    with dissolve

    menu:
        "Help Nora":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ helpedNora = True
            jump hallway_help_nora
        
        "Don't help Nora":
            jump hallway_no_help_nora

label hallway_help_nora:

    $ grant_achievement("helping_hand")
    u "(I kinda like this nicer Nora.)"

    scene v8shal3c
    with dissolve

    u "Yeah, I got a sec."

    scene v8shal5 # TPP. Show Nora handing MC a bunch of flyers, Nora neutral expression, mouth open.
    with dissolve

    pause 0.5

    scene v8shal7 # TPP. Show MC and Nora handing out some flyers to random people.
    with dissolve

    pause 0.5

    scene v8shal8 # TPP. Show MC and Nora handing out some flyers to another set of random people.
    with dissolve

    pause 0.5

    scene v8shal9 # FPP. Show Nora, Nora smile, mouth open.
    with dissolve

    no "Thanks for your help [name]!"

    scene v8shal9a # FPP. Same camera as v8shal9, Nora smile, mouth closed.
    with dissolve

    u "No problem. I've got some stuff to do so I've got to go."

    scene v8shal9
    with dissolve

    no "No problem, see you soon."

    scene v8shal9a
    with dissolve

    u "See ya."

    scene v8shal6 # TPP. Show MC walking away in the opposite direction to Nora after having handed out the flyers Nora gave him.
    with dissolve
    pause 0.5

    jump v8_tues_noon

label hallway_no_help_nora:
    u "(I'm already late.)"

    u "I would but I don't have much time."

    scene v8shal3e # FPP. Same camera as v8shal3, Nora visibly irritated, mouth closed.
    with dissolve

    u "Here, give me a couple flyers and I'll pass them out on my way."

    scene v8shal5
    with dissolve

    no "Don't throw them away! I'm counting on you to help."

    scene v8shal3a
    with dissolve

    u "I'll help. Promise. But I gotta go."

    scene v8shal6a # TPP. Same camera as v8shal6, MC now walking away in the opposite direction to Nora, MC holding some flyers.
    with dissolve
    pause 0.5

    jump v8_tues_noon
