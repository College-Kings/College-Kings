# SCENE 25a: Sam in Ape's Kitchen
# Locations: Apes House
# Characters: MC (Outfit 1), Samantha, cameron
# Time: Monday Evening
label v10_sam_kitchen:
    scene v10skt1 # FPP. Show the open front door of the apes house looking inside
    with fade
    u "Samantha???"

    play music music.ck1.v10.Track_Scene_25a fadein 2

    pause 0.5

    scene v10skt2 # FPP. Show Samantha Stood in the kitchen of the apes House. Big smile on face, mouth closed.
    with fade

    u "What... what's going on? Everything okay? I came as fast as I could!"

    scene v10skt2a # FPP. same camera as v10skt2, Big smile on face, mouth open.
    with dissolve

    sa "Could you make me a Sex on The Beach?"

    scene v10skt2 
    with dissolve

    u "What?"

    scene v10skt2a
    with dissolve

    sa "Could you make me a Sex on The Beach?"

    menu:
        "Make her a cocktail" (samantha=1.0):
            $ makeSamCock = True
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ samantha.points += 1
            scene v10skt2 
            with dissolve
            u "*Sighs* You're something else you know that? *Chuckles* I rushed all the way over here worried."

            scene v10skt2a
            with dissolve

            scene v10skt3 # TPP. Show MC Stood infront of kitchen counter with a empty cocktail glass.
            with dissolve

            pause 0.5

            scene v10skt3a # TPP. Same camera as v10skt3, Cocktail glass now full.
            with dissolve

            pause 0.5

            scene v10skt4 # FPP. Show samantha, mouth open, MC's arm held out in shot with cocktail in hand.
            with dissolve

            sa "Aww, were you worried about me?"

            scene v10skt4a # FPP. same camera as v10skt4, Samantha now holding cocktail, mouth closed. (Mc's arm no longer in shot)
            with dissolve

            u "I didn't burst in calling after you for no reason. You acted like it was urgent and serious."

            scene v10skt4b # FPP. same camera as v10skt4, Samantha now holding cocktail, mouth open. (Mc's arm no longer in shot)
            with dissolve

            sa "It is \"urgent and serious\"."

            scene v10skt4a 
            with dissolve

            u "What's so serious about me making you a cocktail?"

            scene v10skt4b
            with dissolve

            sa "Well, my brother isn't here and I needed a drink. I also didn't want to drink by myself. That's where you come in."

            scene v10skt4a 
            with dissolve

            u "So now I have to drink too?"

            scene v10skt4b
            with dissolve

            sa "Scared of a little drink? You're not gonna make me drink all by myself are you?"

            menu:
                "Drink with her" (samantha=1.0):
                    $ drinkWsam = True
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    $ samantha.points += 1
                    scene v10skt4a 
                    with dissolve
                    u "Scared? I'd never pass on a drink."

                    scene v10skt4b
                    with dissolve

                    sa "See! That's why I called you."

                "Pass" (samantha=-1.0):
                    $ samantha.points -= 1
                    scene v10skt4a 
                    with dissolve

                    u "I'm alright, it's already late."

                    scene v10skt4b
                    with dissolve

                    sa "Aww, you're no fun."

                    scene v10skt4a
                    with dissolve

        "Get mad" (samantha=-1.0):
            $ samantha.points -= 1
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v10skt2
            with dissolve

            u "You had me rush all the way here for this shit? That's pretty fucking ridiculous. I was worried."

            scene v10skt2a
            with dissolve

            sa "Oh my God, it was just a joke. It's not that serious."

            scene v10skt3b # TPP. Same camera as v10skt3, Show Samantha Stood infront of kitchen counter with a empty cocktail glass.
            with dissolve

            pause 0.5

            scene v10skt3c # TPP. Same camera as v10skt3, Show Samantha Stood infront of kitchen counter with a full cocktail glass.
            with dissolve

            pause 0.5

            scene v10skt4a
            with dissolve
            u "Also, you're not supposed to drink. Aren't you trying to be sober???"

            scene v10skt4b
            with dissolve

            sa "Yeah from hard drugs. But I'm not gonna stop drinking a little cocktail once in a while. I've never had an alcohol problem."

            scene v10skt4a
            with dissolve

            u "Are you sure this is a good idea?"

            scene v10skt4b
            with dissolve

            sa "Jeez, yeah. It's not that big of a deal. Just keep it on the low. Cameron isn't home anyways."

            scene v10skt4a
            with dissolve

            u "*Sighs* Fine."


    scene v10skt4b
    with dissolve

    sa "So what were you doing out? Were you with one of your little girlfriends?"

    menu:
        "Tease her" (samantha=1.0):
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ samantha.points += 1
            scene v10skt4a
            with dissolve

            u "And if I was?"

            scene v10skt4b
            with dissolve

            sa "I mean you're free to do what you want... As long as when I call you come running. *Chuckles*"
        "No" (samantha=-1.0):
            $ samantha.points -= 1
            scene v10skt4a
            with dissolve
            u "No, I was uhm... doing things, you know. Not girl related things."

            scene v10skt4b
            with dissolve

            sa "*Laughs* Uh-huh."

    scene v10skt4c # FPP. same camera as v10skt4, Samantha now holding cocktail, mouth closed. (Mc's arm no longer in shot), samantha looking up slightly
    with dissolve

    pause 0.5

    scene v10skt4d # FPP. same camera as v10skt4, Samantha now holding cocktail, mouth closed. (Mc's arm no longer in shot), samantha looking down slightly
    with dissolve

    pause 0.5

    scene v10skt4a
    with dissolve

    u "What was that about?"

    scene v10skt4e # FPP. same camera as v10skt4, Samantha now holding cocktail, mouth open. (Mc's arm no longer in shot), samantha looking down slightly
    with dissolve

    sa "*Tipsy* Hmmm..."

    scene v10skt4a
    with dissolve

    u "What?"

    scene v10skt4b
    with dissolve

    sa "*Tipsy* If you were an animal, what do you think you would be?"

    scene v10skt4a
    with dissolve

    u "*Chuckles* That was random? Why? Don't tell me you're drunk already."

    scene v10skt4b
    with dissolve

    sa "*Tipsy* I'm not drunk, just answer the question."

    menu:
        "Lion" (samantha=1.0):
            $ samantha.points += 1
            scene v10skt4a
            with dissolve

            u "Haha, okay. Let's see... I'd be a lion."
        "Eagle":
            scene v10skt4a
            with dissolve

            u "Haha, okay. Let's see... I'd be an eagle."


    scene v10skt4b
    with dissolve
    sa "*Tipsy* No no no, you'd be a bunny. *Laughs*"

    scene v10skt4a
    with dissolve

    u "*Laughs* A bunny?"

    scene v10skt4b
    with dissolve

    sa "*Drunk* Cause you like to hang out, like right now, we're hanging out. That means I'm a bunny too."

    scene v10skt5 # FPP. Show close up of Samantha, slight smile, mouth open
    with dissolve

    sa "*Drunk whisper* Let's make bunny babies."

    scene v10skt5a # FPP. Same Camera as v10skt5, Show close up of Samantha, slight smile, mouth closed
    with dissolve

    u "(Oh shit, she's fucked up.)"

    u "Oh god, alright... let's get you to sit down. You're clearly super drunk."

    scene v10skt5
    with dissolve

    sa "*Drunk* No sir, I'm Samantha! *Laughs*"

    scene v10skt6 # FPP. Show Livingroom, sofa in view
    with fade

    pause 0.75

    scene v10skt7 # FPP. MC and samantha now sat on sofa. Show Samantha slight smile, eyes closed, mouth closed
    with dissolve

    if makeSamCock:
        u "(Fuck, I put way too much alcohol in her cocktail...)"

    else:
        u "(Fuck, how much alcohol did she put in her cocktail?)"

    u "I guess me coming was an emergency, I definitely wouldn't want you drinking by yourself."

    sa "*Snoring*"

    u "(*Laughs* Wow, never have I seen more of a lightweight.)"

    scene v10skt8 # FPP. Show The empty apes kitchen,
    with fade

    u "(Huh?)"

    ca "Sam? Why are you sleeping on the couch?"

    if drinkWsam:
        scene v10skt8a # FPP. same camera as v10skt8, Show Cameron in the kitchen, angry look mouth open
        with dissolve

        ca "What the fuck! Were you drinking with my sister? I thought I told you to leave her alone!"

        scene v10skt8b # FPP. same camera as v10skt8, Show Cameron in the kitchen, angry look mouth closed
        with dissolve

        u "Chill out man, I got home and she was already drinking and I didn't want her to drink alone so I got a glass. It's not a big deal."

        scene v10skt8a
        with dissolve

        ca "Then why the fuck is she passed out?"

        scene v10skt8b
        with dissolve

        ca "Did you mess with my sister's drink?!"

        scene v10skt8a
        with dissolve

        u "Chill! Your sister's just a lightweight, she didn't even finish her drink."

        scene v10skt8b
        with dissolve

        ca "She shouldn't be drinking in the first place. Don't encourage her!"

        scene v10skt8a
        with dissolve

        u "Look man, I'm not her dad. I can't control what she does. And neither can you."

        scene v10skt8b
        with dissolve

        ca "Someone needs to!"

    else:
        scene v10skt8b
        with dissolve
        ca "What are you doing?"

        scene v10skt8a
        with dissolve

        u "Cleaning up?"

        scene v10skt8b
        with dissolve

        ca "Wait, were you drinking with my sister?"

        scene v10skt8a
        with dissolve

        u "What? No, I literally just walked in and she was passed out on the couch. It does look like she had a drink though."

        scene v10skt8b
        with dissolve

        ca "I swear!"

    scene v10skt8c # FPP. same camera as v10skt8, Show Cameron leaving the kitchen
    with dissolve

    stop music fadeout 3

    jump v10_amber_skatepark
