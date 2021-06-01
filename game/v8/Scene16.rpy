# Sunday Afternoon in in MC's room
# Location: MC's Apes Room OR MC Wolves Room
# Outfits: MC Outfit 2
# Time: Sunday Afternoon

init python:
    def v8s16_kiwiiReply1():
        v8s16_kiwiiPost3.newComment("Riley", _("You will have to find out some times :)"))

    def v8s16_kiwiiReply2():
        v8s16_kiwiiPost3.newComment("Riley", _("Not this time but maybe you should come some time ;)"))

label mc_wolves_sun_aft:
    scene v8smcrm1 # TPP. Show MC walking inside his Wolves room towards his bed.
    with fade

    pause 0.5

    play music "music/mindie1.mp3" fadein 1

    scene v8smcrm2 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    scene v8smcrm2a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    with dissolve

    $ v8s16_kiwiiPost1 = KiwiiPost("Chloe", "v8/chlaubpost1.webp", _("Hanging with my best friend. Good times!"), numberLikes=346) # Chloe & Aubrey having fun at the beach.
    $ v8s16_kiwiiPost1.newComment("Aubrey", _("Awww, I love hanging out with you <3"), queue=False)
    $ v8s16_kiwiiPost1.newComment("Nora", _("Ugh, stop being so fake"), queue=False)
    $ v8s16_kiwiiPost1.addReply(_("Looking hot, ladies!"), numberLikes=321)
    $ v8s16_kiwiiPost1.addReply(_("This is such a great picture!"), numberLikes=334)

    $ v8s16_kiwiiPost2 = KiwiiPost("Lauren", "v8/laurosepost1.webp", _("Having fun with Ms. Rose at Hoco!"), numberLikes=328) # Lauren & Ms. Rose at Hoco.
    $ v8s16_kiwiiPost2.newComment("Camreon", _("Teacher's pet!"), queue=False)
    $ v8s16_kiwiiPost2.addReply(_("I'm glad you guys had fun"), numberLikes=320)
    $ v8s16_kiwiiPost2.addReply(_("Wow, you two look great!"), numberLikes=343)

    $ v8s16_kiwiiPost3 = KiwiiPost("Riley", "v8/riclothpost1.webp", _("Nothing like a good day of shopping"), numberLikes=330) # Picture of Riley outside a clothing store.
    $ v8s16_kiwiiPost3.newComment("Aubrey", _("Wish I could of been there to try things with you"), queue=False)
    $ v8s16_kiwiiPost3.newComment("Imre", _("Looking good"), queue=False)
    $ v8s16_kiwiiPost3.addReply(_("How many bikinis did you buy? Haha."), v8s16_kiwiiReply1, numberLikes=350)
    $ v8s16_kiwiiPost3.addReply(_("Did you buy me anything?"), v8s16_kiwiiReply2, numberLikes=337)

    jump msrose_moving

label mc_apes_sun_aft:
    scene v8smcrm3 # TPP. Show MC walking inside his Apes room towards his bed.
    with fade

    pause 0.5

    play music "music/m11punk.mp3" fadein 1

    scene v8smcrm4 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    scene v8smcrm4a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    with dissolve

    $ v8s16_kiwiiPost1 = KiwiiPost("Chloe", "images/chlaubpost1", "Hanging with my best friend. Good times!", numberLikes=312) # Chloe & Aubrey having fun at the beach.
    $ newKiwiiPost1.addReply("Looking hot, ladies!", "replyLabel", numberLikes=302)
    $ newKiwiiPost1.addReply("This is such a great picture!", "replyLabel", numberLikes=316)

    $ v8s16_kiwiiPost2 = KiwiiPost("Lauren", "images/laurosepost1", "Having fun with Ms. Rose at Hoco!", numberLikes=344) # Lauren & Ms. Rose at Hoco.
    $ newKiwiiPost2.addReply("I'm glad you guys had fun", "replyLabel", numberLikes=301)
    $ newKiwiiPost2.addReply("Wow, you two look great!", "replyLabel", numberLikes=322)

    $ v8s16_kiwiiPost3 = KiwiiPost("Riley", "images/riclothpost1", "Nothing like a good day of shopping", numberLikes=343) # Picture of Riley outside a clothing store.
    $ newKiwiiPost3.addReply("How many bikinis did you buy? Haha.", "replyLabel", numberLikes=319)
    $ newKiwiiPost3.addReply("Did you buy me anything?", "replyLabel", numberLikes=349)

    jump sun_aft_apes_house
