# Sunday Afternoon in in MC's room
# Location: MC's Apes Room OR MC Wolves Room
# Outfits: MC Outfit 2
# Time: Sunday Afternoon

init python:
    def v8s16_kiwiiReply1():
        v8s16_kiwiiPost2.newComment(lauren, _("Took a lot of work but Homecoming looks great"), numberLikes=renpy.random.randint(15, 35))

    def v8s16_kiwiiReply2():
        v8s16_kiwiiPost2.newComment(lauren, _("Thank you miss Rose also says thank you"), numberLikes=renpy.random.randint(15, 35))

    def v8s16_kiwiiReply3():
        v8s16_kiwiiPost3.newComment(riley, _("You will have to find out some times :)"), numberLikes=renpy.random.randint(15, 35))

    def v8s16_kiwiiReply4():
        v8s16_kiwiiPost3.newComment(riley, _("Not this time, but maybe next time you can join me ;)"), numberLikes=renpy.random.randint(15, 35))

label mc_wolves_sun_aft:
    scene v8smcrm1 # TPP. Show MC walking inside his Wolves room towards his bed.
    with fade

    pause 0.5

    play music "music/mindie1.mp3" fadein 2

    scene v8smcrm2 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    #scene v8smcrm2a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    #with dissolve

    $ v8s16_kiwiiPost1 = KiwiiPost(chloe, "phone/kiwii/Posts/v8/chlaubpost1.webp", _("Hanging with my best friend. Good times!"), numberLikes=346) # Chloe & Aubrey having fun at the beach.
    $ v8s16_kiwiiPost1.newComment(aubrey, _("Awww, I love hanging out with you <3"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost1.newComment(nora, _("Looking great Aubrey!"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost1.newComment(lindsey, _("Next time invite me along"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost1.addReply(_("Looking hot, ladies!"), numberLikes=321)
    $ v8s16_kiwiiPost1.addReply(_("This is such a great picture!"), numberLikes=334)

    if not hcGirl == "lauren":
        $ v8s16_kiwiiPost2 = KiwiiPost(lauren, "phone/kiwii/Posts/v8/laurosepost1.webp", _("Having fun with Ms. Rose at Hoco!"), numberLikes=328) # Lauren & Ms. Rose at Hoco.
        $ v8s16_kiwiiPost2.newComment(cameron, _("Teacher's pet!"), numberLikes=renpy.random.randint(15, 35))
        $ v8s16_kiwiiPost2.newComment(ryan, _("Booba"), numberLikes=renpy.random.randint(15, 35))        
        $ v8s16_kiwiiPost2.addReply(_("I'm glad you guys had fun"), v8s16_kiwiiReply1, numberLikes=320)
        $ v8s16_kiwiiPost2.addReply(_("Wow, you two look great!"), v8s16_kiwiiReply2, numberLikes=343)

    $ v8s16_kiwiiPost3 = KiwiiPost(riley, "phone/kiwii/Posts/v8/riclothpost1.webp", _("Nothing like a good day of shopping"), numberLikes=330) # Picture of Riley outside a clothing store.
    $ v8s16_kiwiiPost3.newComment(aubrey, _("Wish I could of been there to try things with you"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost3.newComment(imre, _("Looking good"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost3.addReply(_("How many bikinis did you buy? Haha."), v8s16_kiwiiReply3, numberLikes=350)
    $ v8s16_kiwiiPost3.addReply(_("Did you buy me anything?"), v8s16_kiwiiReply4, numberLikes=337)

    jump msrose_moving

label mc_apes_sun_aft:
    scene v8smcrm3 # TPP. Show MC walking inside his Apes room towards his bed.
    with fade

    pause 0.5

    play music "music/m11punk.mp3" fadein 2

    scene v8smcrm4 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    scene v8smcrm4a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    with dissolve

    $ v8s16_kiwiiPost1 = KiwiiPost(chloe, "phone/kiwii/Posts/v8/chlaubpost1.webp", _("Hanging with my best friend. Good times!"), numberLikes=346) # Chloe & Aubrey having fun at the beach.
    $ v8s16_kiwiiPost1.newComment(aubrey, _("Awww, I love hanging out with you <3"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost1.newComment(nora, _("Looking great Aubrey!"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost1.newComment(lindsey, _("Next time invite me along"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost1.addReply(_("Looking hot, ladies!"), numberLikes=321)
    $ v8s16_kiwiiPost1.addReply(_("This is such a great picture!"), numberLikes=334)

    if not hcGirl == "lauren":
        $ v8s16_kiwiiPost2 = KiwiiPost(lauren, "phone/kiwii/Posts/v8/laurosepost1.webp", _("Having fun with Ms. Rose at Hoco!"), numberLikes=328) # Lauren & Ms. Rose at Hoco.
        $ v8s16_kiwiiPost2.newComment(cameron, _("Teacher's pet!"), numberLikes=renpy.random.randint(15, 35))
        $ v8s16_kiwiiPost2.newComment(ryan, _("Booba"), numberLikes=renpy.random.randint(15, 35))        
        $ v8s16_kiwiiPost2.addReply(_("I'm glad you guys had fun"), v8s16_kiwiiReply1, numberLikes=320)
        $ v8s16_kiwiiPost2.addReply(_("Wow, you two look great!"), v8s16_kiwiiReply2, numberLikes=343)

    $ v8s16_kiwiiPost3 = KiwiiPost(riley, "phone/kiwii/Posts/v8/riclothpost1.webp", _("Nothing like a good day of shopping"), numberLikes=330) # Picture of Riley outside a clothing store.
    $ v8s16_kiwiiPost3.newComment(aubrey, _("Wish I could of been there to try things with you"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost3.newComment(imre, _("Looking good"), numberLikes=renpy.random.randint(15, 35))
    $ v8s16_kiwiiPost3.addReply(_("How many bikinis did you buy? Haha."), v8s16_kiwiiReply3, numberLikes=350)
    $ v8s16_kiwiiPost3.addReply(_("Did you buy me anything?"), v8s16_kiwiiReply4, numberLikes=337)

    jump sun_aft_apes_house
