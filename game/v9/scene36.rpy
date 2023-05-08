# SCENE 36: Run With Imre
# Locations: MC Wolves Room/Park
# Characters: MC (Outfit 3/Outfit 5), Imre (Outfit 3)
# Time: Saturday Afternoon

label v9_run_w_imre:
    scene v9rwi1 # TPP. Show Imre walking through MC's door into his room.
    with dissolve

    play music music.ck1.v9.Track_Scene_36 fadein 2

    pause 1

    scene v9rwi2 # FPP. Show Imre, smile, mouth open
    with dissolve
    
    imre "Hey man, let's get a good run in. I'm not a fan of afternoon runs, but I heard that's when all the chicks run, so I've been motivated."

    scene v9rwi2a # FPP. Same camera as v9rwi2, smile, mouth closed.
    with dissolve

    u "I'm sure you have..."

    scene v9rwi3 # TPP. Show MC and Imre jogging in the park. MC now wearing outfit 4.
    with fade

    pause 1

    scene v9rwi4 # TPP. Show Imre and MC stopping jogging and looking at eachother.
    with dissolve

    pause 1

    scene v9rwi5 # FPP. Show Imre, Imre slight worry, mouth closed.
    with dissolve

    u "Everything alright man?"

    scene v9rwi5a # FPP. Same camera as v9rwi5, slight worry, mouth open.
    with dissolve

    imre "Yeah, just thinking about the brawl."

    scene v9rwi5
    with dissolve

    u "What about it?"

    scene v9rwi5a
    with dissolve

    imre "There's just gonna be a lot of girls there man! What if I get the shit beat out of me!?"

    scene v9rwi5
    with dissolve

    u "Is that really what your worried about? I'm the one that's barely fought before."

    scene v9rwi5a
    with dissolve

    if winadam:
        imre "You fought Adam though, and you won."

    elif adamdmg > 0:
        imre "You fought Adam though, and well you did more damage than I did."

    scene v9rwi5
    with dissolve

    u "All luck."

    scene v9rwi5a
    with dissolve

    imre "Sure it was. But I'm not worried about you. If I get the shit beat out of me my pussy getting days are over."

    scene v9rwi5
    with dissolve

    u "Then don't get the shit beat out of you."

    scene v9rwi5a
    with dissolve

    imre "Easier said than done bro, easier said than done."

    scene v9rwi6 # TPP. Show Ryan in the distance walking towards Imre and MC.
    with dissolve

    u "(Oh shit, is that who I think it is?)"

    scene v9rwi7 # FPP. Show Ryan now closer to Imre and MC, Ryan agitated, Imre angry, mouths closed.
    with dissolve

    u "Hey..."

    scene v9rwi8 # TPP. Show MC, Ryan and Imre, Ryan and Imre starring eachother out, both angry, Ryan mouth open.
    with dissolve

    ry "Not in the mood for distractions today, so just leave me the fuck alone."

    scene v9rwi8a # TPP. Same camera as v9rwi8, Imre mouth open.
    with dissolve

    imre "Well [name], if I get to fight this piece of shit I got nothing to worry about."

    scene v9rwi8
    with dissolve

    ry "Watch your fucking mouth bro! I don't need a reason to whoop your ass. I'm not in the mood!"

    scene v9rwi8a
    with dissolve

    imre "Well, you better get in the mood cause the minute I get a chance to put my hands on you it's gonna be lights out."

    scene v9rwi8a
    with dissolve

    ry "You got the chance now!"

    scene v9rwi9 # TPP. Show Imre lunging towards Ryan, both angry.
    with dissolve

    pause 0.75

    scene v9rwi9a # TPP. Same camera as v9rwi9, Show MC pulling Imre back, Imre mouth open.
    with dissolve

    imre "See your ass at the brawl bitch!"

    scene v9rwi10 # FPP. Show Ryan walking away from camera, Ryan puts his middle finger up to the camera as walking away.
    with dissolve

    pause 1

    scene v9rwi5b # FPP. Same camera as v9rwi5, Imre angry, mouth closed.
    with dissolve
    
    u "Bro chill, we can't get caught fucking with him before the brawl. We'd get our asses chewed out!"

    scene v9rwi5c # FPP. Same camera as v9rwi5, Imre relaxing a bit, mouth open.
    with dissolve

    imre "Fuck! You're right, he just pisses me off. I hate the fucking Apes."

    scene v9rwi5d # FPP. Same camera as v9rwi5, Imre relaxing a bit, mouth closed.
    with dissolve

    u "Let's just head back."

    scene v9rwi11 # TPP. Show Imre and MC walking away to somewhere else in the park.
    with dissolve

    pause 1

    scene v9rwi12 # FPP. Show Imre, now elsewhere in the park, Imre neutral, mouth closed.
    with fade

    u "Feeling better?"

    scene v9rwi12a # FPP. Same camera as v9rwi12, mouth open.
    with dissolve

    imre "Not really man, I swear the Apes just always get to me."

    scene v9rwi12
    with dissolve

    u "Well, the brawl will be your chance to change all that."

    scene v9rwi12a
    with dissolve

    imre "Yeah I guess."

    scene v9rwi13 # FPP. Show Imre checking his phone.
    with dissolve

    pause 1

    scene v9rwi12b # FPP. Same camera as v9rwi12, smile, mouth open.
    with dissolve

    imre "Ahh, sorry bro. Gotta dip, duty calls!"

    scene v9rwi12c # FPP. Same camera as v9rwi12, smile, mouth closed.
    with dissolve

    u "Duty?"

    scene v9rwi12b
    with dissolve

    imre "Imre will always be in service to the ladies."

    scene v9rwi14 # TPP. Show Imre walking away on his own.
    with dissolve

    stop music fadeout 3

    pause 1

    jump v9_walk_li_txt