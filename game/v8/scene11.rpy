# Gym With Sebastian
# Location: Wolves Gym, MC's Wolves Room
# Outfits: MC Outfit 3, Sebastian Outfit 1
# Time: Saturday Night

label work_with_seb:
    scene v8sgym4 # TPP. Show MC and Sebastian walking over to a punching bag in the gym.
    with dissolve

    pause 0.5

    scene v8sgym5 # FPP. Show Sebastian punching the punching bag. Sebastian mouth open.
    with hpunch

    se "This is every teacher who flunked me!"

    scene v8sgym6 # TPP. Show MC punching the punching bag. MC mouth open.
    with hpunch

    u "And this is every guy who stole my girl!"

    scene v8sgym7 # FPP. Close up Sebastian, Sebastian smile, mouth open.
    with dissolve

    se "You got some fight in you after all! Come on."

    scene v8sgym8 # FPP. Show Sebastian stood next to some lifting equipment, Sebastian pointing at the equipment, mouth open.
    with dissolve

    se "This is where I spend most of my time. Ladies love muscles."

    scene v8sgym9 # TPP. Show Sebastian and MC lifting weights, MC tense expression, mouth closed, Sebastian mouth open.
    with fade

    se "Twenty-eight... Twenty-nine... Thirty..."

    scene v8sgym9a # TPP. Same camera as v8sgym9, MC mouth open, Sebastian mouth closed.
    with dissolve

    u "Wow, impressive."

    scene v8sgym9
    with dissolve

    se "Thanks. I wasn't this good when I started last year."

    # -MC looks down at his arms-
    scene v8sgym9b # TPP. Same camera as v8sgym9, MC mouth open, looking down at his arm, Sebastian looking at MC, mouth closed.
    with dissolve

    u "I think I need you to train me."

    scene v8sgym10 # FPP. Close up Sebastian, Sebastian smile, mouth open.
    with dissolve

    se "No problem, man. We Wolves stick together."

    scene v8sgym10a # FPP. Close up Sebastian, Sebastian smile, mouth closed.
    with dissolve

    menu:
        "Open up to Sebastian":
            $ add_point(KCT.BRO)
            jump wolves_gym_conf

        "Play it cool":
            jump wolves_gym_cool

label wolves_gym_conf:

    u "It's nice to have that, especially being new around here."

    scene v8sgym10b # FPP. Same camera as v8sgym10, Sebastian neutral expression, mouth open.
    with dissolve

    se "Yeah, I remember how rough it was the first few months."

    scene v8sgym10d # FPP. Same camera as v8sgym10, Sebastian looking around, neutral expression, mouth open.
    with dissolve

    se "I almost went home. Until the Wolves took me in."

    scene v8sgym10c # FPP. Same camera as v8sgym10, Sebatian neutral expression, mouth closed.
    with dissolve

    u "I totally get that. I've almost called my step-mom to come get me a couple times. It can get lonely."

    scene v8sgym10
    with dissolve

    se "Well, you're not totally alone. I've seen all the chicks dripping off you."

    scene v8sgym10a
    with dissolve

    u "I'm doing alright."

    scene v8sgym10
    with dissolve

    se "Alright? I didn't have near that many girls my freshman year!"

    scene v8sgym11 # TPP. Show MC placing his hand on MC's back, MC starts excersing again, MC mouth open.
    with dissolve

    u "One... Two... Three..."

    jump wolves_gym_end

label wolves_gym_cool:
    scene v8sgym10a
    with dissolve

    u "Seems to be working out great. Can you spot me?"

    scene v8sgym10
    with dissolve

    se "Sure. Gotta get those reps up if you want to be a contender."

    scene v8sgym9a
    with dissolve

    u "Not sure I'll ever be that. But the girls seem to like the muscles."

    scene v8sgym9c # TPP. Same camera as v8sgym9, MC mouth closed, Sebastian laugh, mouth open.
    with dissolve

    se "I can tell! You're one lucky bastard!"

    scene v8sgym9a
    with dissolve

    u "Maybe I'll show you some of my tricks after this."

    scene v8sgym9c
    with dissolve

    se "Yeah! I can teach you how to kick ass and you can teach me how to pull some!"

    scene v8sgym9a
    with dissolve

    u "Deal."

    jump wolves_gym_end

label wolves_gym_end:
    scene v8sgym12 # FPP. Show Sebastian, slightly worried, mouth open.
    with Fade(0.75, 0.25, 0.75)

    se "Shit, it's late. I never finished my chem homework."

    scene v8sgym12a # FPP. Same camera as v8sgym12, neutral expression, mouth closed.
    with dissolve

    u "Fuck. I was supposed to be studying."

    scene v8sgym12b # FPP. Same camera as v8sgym12, neutral expression, mouth open.
    with dissolve

    se "I better get back to work."

    scene v8sgym12a
    with dissolve

    u "Me too. Thanks for the workout. I'm gonna be sore tomorrow!"

    scene v8sgym12c # FPP. Same camera as v8sgym12, Sebastian slightly winking, mouth open.
    with dissolve

    se "Don't forget our deal, man."

    scene v8sgym12d # FPP. Same camera as v8sgym12, Sebastian smile, mouth closed.
    with dissolve

    u "I won't. G'night."

    stop music fadeout 3

    scene black
    with fade
    pause 0.5

    jump mc_wolves_sun_morn