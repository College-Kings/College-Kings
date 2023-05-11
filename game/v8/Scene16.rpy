# Sunday Afternoon in in MC's room
# Location: MC's Apes Room OR MC Wolves Room
# Outfits: MC Outfit 2
# Time: Sunday Afternoon
label mc_wolves_sun_aft:
    scene v8smcrm1 # TPP. Show MC walking inside his Wolves room towards his bed.
    with fade

    pause 0.5

    play music music.ck1.mindie1 fadein 2

    scene v8smcrm2 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    #scene v8smcrm2a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    #with dissolve

    $ kiwii_post = KiwiiService.new_post(chloe, "phone/kiwii/Posts/v8/chlaubpost1.webp", _("Hanging with my best friend. Good times!"), number_likes=346) # Chloe & Aubrey having fun at the beach.
    $ KiwiiService.new_comment(kiwii_post, aubrey, _("Awww, I love hanging out with you <3"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, nora, _("Looking great Aubrey!"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, lindsey, _("Next time invite me along"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.add_replies(kiwii_post,
        KiwiiReply(_("Looking hot, ladies!"), number_likes=321),
        KiwiiReply(_("This is such a great picture!"), number_likes=334)
    )

    if not hcGirl == "lauren":
        $ kiwii_post = KiwiiService.new_post(lauren, "phone/kiwii/Posts/v8/laurosepost1.webp", _("Having fun with Ms. Rose at Hoco!"), number_likes=328) # Lauren & Ms. Rose at Hoco.

        $ v8s16_kiwii_reply1 = KiwiiBuilder(kiwii_post)
        $ v8s16_kiwii_reply1.new_comment(lauren, _("Took a lot of work but Homecoming looks great"), number_likes=renpy.random.randint(15, 35))

        $ v8s16_kiwii_reply2 = KiwiiBuilder(kiwii_post)
        $ v8s16_kiwii_reply2.new_comment(lauren, _("Thank you miss Rose also says thank you"), number_likes=renpy.random.randint(15, 35))

        $ KiwiiService.new_comment(kiwii_post, cameron, _("Teacher's pet!"), number_likes=renpy.random.randint(15, 35))
        $ KiwiiService.new_comment(kiwii_post, ryan, _("Booba"), number_likes=renpy.random.randint(15, 35))
        $ KiwiiService.add_replies(kiwii_post,
            KiwiiReply(_("I'm glad you guys had fun"), number_likes=320, next_comment=v8s16_kiwii_reply1),
            KiwiiReply(_("Wow, you two look great!"), number_likes=343, next_comment=v8s16_kiwii_reply2)
        )

    $ kiwii_post = KiwiiService.new_post(riley, "phone/kiwii/Posts/v8/riclothpost1.webp", _("Nothing like a good day of shopping"), number_likes=330) # Picture of Riley outside a clothing store.
    
    $ v8s16_kiwii_reply3 = KiwiiBuilder(kiwii_post)
    $ v8s16_kiwii_reply3.new_comment(riley, _("You will have to find out some times :)"), number_likes=renpy.random.randint(15, 35))

    $ v8s16_kiwii_reply4 = KiwiiBuilder(kiwii_post)
    $ v8s16_kiwii_reply4.new_comment(riley, _("Not this time, but maybe next time you can join me ;)"), number_likes=renpy.random.randint(15, 35))

    $ KiwiiService.new_comment(kiwii_post, aubrey, _("Wish I could of been there to try things with you"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, imre, _("Looking good"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.add_replies(kiwii_post,
        KiwiiReply(_("How many bikinis did you buy? Haha."), number_likes=350, next_comment=v8s16_kiwii_reply3),
        KiwiiReply(_("Did you buy me anything?"), number_likes=337, next_comment=v8s16_kiwii_reply4)
    )

    jump msrose_moving

label mc_apes_sun_aft:
    scene v8smcrm3 # TPP. Show MC walking inside his Apes room towards his bed.
    with fade

    pause 0.5

    play music music.ck1.m11punk fadein 2

    scene v8smcrm4 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    scene v8smcrm4a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    with dissolve

    $ kiwii_post = KiwiiService.new_post(chloe, "phone/kiwii/Posts/v8/chlaubpost1.webp", _("Hanging with my best friend. Good times!"), number_likes=346) # Chloe & Aubrey having fun at the beach.
    $ KiwiiService.new_comment(kiwii_post, aubrey, _("Awww, I love hanging out with you <3"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, nora, _("Looking great Aubrey!"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, lindsey, _("Next time invite me along"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.add_replies(kiwii_post,
        KiwiiReply(_("Looking hot, ladies!"), number_likes=321),
        KiwiiReply(_("This is such a great picture!"), number_likes=334)
    )

    if not hcGirl == "lauren":
        $ kiwii_post = KiwiiService.new_post(lauren, "phone/kiwii/Posts/v8/laurosepost1.webp", _("Having fun with Ms. Rose at Hoco!"), number_likes=328) # Lauren & Ms. Rose at Hoco.

        $ v8s16_kiwii_reply1 = KiwiiBuilder(kiwii_post)
        $ v8s16_kiwii_reply1.new_comment(lauren, _("Took a lot of work but Homecoming looks great"), number_likes=renpy.random.randint(15, 35))

        $ v8s16_kiwii_reply2 = KiwiiBuilder(kiwii_post)
        $ v8s16_kiwii_reply2.new_comment(lauren, _("Thank you miss Rose also says thank you"), number_likes=renpy.random.randint(15, 35))

        $ KiwiiService.new_comment(kiwii_post, cameron, _("Teacher's pet!"), number_likes=renpy.random.randint(15, 35))
        $ KiwiiService.new_comment(kiwii_post, ryan, _("Booba"), number_likes=renpy.random.randint(15, 35))
        $ KiwiiService.add_replies(kiwii_post,
            KiwiiReply(_("I'm glad you guys had fun"), number_likes=320, next_comment=v8s16_kiwii_reply1),
            KiwiiReply(_("Wow, you two look great!"), number_likes=343, next_comment=v8s16_kiwii_reply2)
        )

    $ kiwii_post = KiwiiService.new_post(riley, "phone/kiwii/Posts/v8/riclothpost1.webp", _("Nothing like a good day of shopping"), number_likes=330) # Picture of Riley outside a clothing store.
    
    $ v8s16_kiwii_reply3 = KiwiiBuilder(kiwii_post)
    $ v8s16_kiwii_reply3.new_comment(riley, _("You will have to find out some times :)"), number_likes=renpy.random.randint(15, 35))

    $ v8s16_kiwii_reply4 = KiwiiBuilder(kiwii_post)
    $ v8s16_kiwii_reply4.new_comment(riley, _("Not this time, but maybe next time you can join me ;)"), number_likes=renpy.random.randint(15, 35))

    $ KiwiiService.new_comment(kiwii_post, aubrey, _("Wish I could of been there to try things with you"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, imre, _("Looking good"), number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.add_replies(kiwii_post,
        KiwiiReply(_("How many bikinis did you buy? Haha."), number_likes=350, next_comment=v8s16_kiwii_reply3),
        KiwiiReply(_("Did you buy me anything?"), number_likes=337, next_comment=v8s16_kiwii_reply4)
    )

    jump sun_aft_apes_house
