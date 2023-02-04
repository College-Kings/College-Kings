# SCENE 49: Walking back with Aubrey
# Locations: Sidewalk, Hotel.
# Characters: AUBREY (Outfit: 4), MC (Outfit: 1) 
# Time: Evening

label v13s49:
    scene v13s49_1 # TPP. Show MC and Aubrey walking down the sidewalk, both slight smile, mouths closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 49.mp3" fadein 2

    scene v13s49_2 # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
    with dissolve

    au "Thanks for taking these pictures for me [name]. I'm gonna choose my favorite one and upload it right now."

    scene v13s49_2a # FPP. Same as v13s49_2, Aubrey looking at phone, Aubrey slight smile, mouth closed.
    with dissolve

    pause 0.75
    
    $ v13s49_kiwiiPost1 = KiwiiPost(aubrey, "phone/kiwii/Posts/v13/aubrey_beach.webp", _("Swimming up the ladder! #ScheveningenBeach"), number_likes=4218)
    $ v13s49_kiwiiPost1.newComment(imre, _("Hot as fuck Aubrey!!"), number_likes=renpy.random.randint(1800, 3600))
    $ v13s49_kiwiiPost1.newComment(chloe, _("This is the hottest pic I've ever seen of you!"), mentions=[aubrey], number_likes=renpy.random.randint(1800, 3600))
    $ v13s49_kiwiiPost1.addReply(_("Wow, they turned out great!"), number_likes=renpy.random.randint(1800, 3600))
    $ v13s49_kiwiiPost1.addReply(_("Ah, beautiful. But even better in person ;)"), mentions=[aubrey], number_likes=renpy.random.randint(1800, 3600))
    $ v13s49_kiwiiPost1.newComment(aubrey, _("Thank you! <3"), number_likes=renpy.random.randint(2400, 3800))
    $ v13s49_kiwiiPost1.newComment(naomi, _("OMG! You look just like me! <3"), number_likes=renpy.random.randint(3800, 6000))

    scene v13s49_2b # FPP. Same as v13s49_2, (Aubrey's phone off camera), Aubrey slight smile, mouth closed.
    with dissolve

    u "Of course, anytime."

    scene v13s49_1a # FPP. Same as v13s49_1, Different location on the sidewalk.
    with dissolve

    pause 0.75

    scene v13s49_3 # FPP. MC and Aubrey in the hotel lobby, Aubrey slight smile, mouth open.
    with fade

    au "I'm gonna go put some clothes on."

    scene v13s49_3a # FPP. Same as v13s49_3, Aubrey slight smile, mouth closed.
    with dissolve

    u "Haha, you do that."

    scene v13s49_3b # FPP. Same as v13s49_3a, Show Aubrey walking away from MC.
    with dissolve

    if v13s48_ryan_double_date:
        scene v13s49_4 # FPP. Show Ryan walking up to MC, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v13s49_4a # FPP. Same as v13s49_4, Ryan standing in front of MC.
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v13s50
  
    elif emily_europe:
        scene v13s49_5 # FPP. Show Emily walking up to MC, angry expression, mouth closed.
        with dissolve

        pause 0.75

        scene v13s49_5a # FPP. Same as v13s49_5, Emily standing in front of MC.
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v13s51_emily_fight

    else:
        stop music fadeout 3
        
        if chloe.relationship >= Relationship.GIRLFRIEND and not v11_riley_roomate:
            jump v13s52

        elif riley.relationship >= Relationship.FWB and v11_riley_roomate:
            jump v13s53

        else:
            jump v13s54