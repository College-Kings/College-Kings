# SCENE 30: Going for Breakfast
# Locations: The sidewalk
# Characters: MC (Outfit 3), Nora (Outfit 1)
# Time: Saturday Morning

label v9_satmorn_gfb_walk:
    scene v9gfb1 # FPP. MC on sidewalk, looking at the horizon, sun barely risen
    with fade

    play music music.ck1.v9.Track_Scene_30 fadein 2

    pause 1

    scene v9gfb2 # FPP. Nora very close to mc, Surprised look, mouth open
    with dissolve
    no "Oh wow, I'm sorry."

    scene v9gfb3 # FPP. Nora a little further away from , Surprised look, mouth closed
    with dissolve
    u "*Laugh* You're sorry? I'm the one that was staring into the sun. Are you okay?"

    scene v9gfb3a # FPP. Same camera as v9gfb3, Nora a little further away from , Surprised look, mouth open
    with dissolve
    no "Wow..."

    scene v9gfb3
    with dissolve
    u "Wow what?"

    scene v9gfb3a
    with dissolve
    no "I'm just realizing it's been so long since someone's actually asked me that."

    scene v9gfb3
    with dissolve
    u "Well, we all need to hear it now and again."

    if v8_nora_likes_mc:
        scene v9gfb3b # FPP. Same camera as v9gfb3, Nora hand on hip, Neutral look, mouth open
        with dissolve
        no "What are you doing out this early? Shouldn't you be getting some extra rest, today's a big day for you."

        scene v9gfb3c # FPP. Same camera as v9gfb3, Nora hand on hip, Neutral look, mouth closed
        with dissolve
        u "Thought I'd get a real breakfast for once. My mom and I would always eat breakfast together, but since college started I realize most people barely get up in time for lunch."

        scene v9gfb3a
        with dissolve
        no "Hahaha. You can say that again. I may not be as good of company as your mom, but I'll join you for breakfast."

        scene v9gfb3
        with dissolve
        u "Sounds great! I know a cafe right around the corner."
        
        stop music fadeout 3

        jump v9_sat_cafe_w_nora
    else:
        scene v9gfb3b
        with dissolve
        no "That's true. Anyway, I gotta go. See you around."

        scene v9gfb3c
        with dissolve
        u "Yeah, of course."

        stop music fadeout 3

        jump v9_sat_cafe