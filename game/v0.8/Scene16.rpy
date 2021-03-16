# Sunday Afternoon in in MC's room
# Location: MC's Apes Room OR MC Wolves Room
# Outfits: MC Outfit 2
# Time: Sunday Afternoon

label mc_wolves_sun_aft:
    scene v8smcrm1 # TPP. Show MC walking inside his Wolves room towards his bed.
    with fade

    pause 0.5

    scene v8smcrm2 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    scene v8smcrm2a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    with dissolve

    $ newKiwiiPost = KiwiiPost("Chloe", "images/chlaubpost1", "Hanging with my best friend. Good times!", numberLikes=346) # Chloe & Aubrey having fun at the beach.

    $ newKiwiiPost.addReply("Looking hot, ladies!", "replyLabel", numberLikes=321)
    $ newKiwiiPost.addReply("This is such a great picture!", "replyLabel", numberLikes=334)

    $ newKiwiiPost = KiwiiPost("Lauren", "images/laurosepost1", "Having fun with Ms. Rose at Hoco!", numberLikes=328) # Lauren & Ms. Rose at Hoco.

    $ newKiwiiPost.addReply("I'm glad you guys had fun", "replyLabel", numberLikes=320)
    $ newKiwiiPost.addReply("Wow, you two look great!", "replyLabel", numberLikes=343)

    $ newKiwiiPost = KiwiiPost("Riley", "images/riclothpost1", "Nothing like a good day of shopping", numberLikes=330) # Picture of Riley outside a clothing store.

    $ newKiwiiPost.addReply("How many bikinis did you buy? Haha.", "replyLabel", numberLikes=350)
    $ newKiwiiPost.addReply("Did you buy me anything?", "replyLabel", numberLikes=337)
    jump msrose_moving

label mc_apes_sun_aft:
    scene v8smcrm3 # TPP. Show MC walking inside his Apes room towards his bed.
    with fade

    pause 0.5

    scene v8smcrm4 # TPP. Show MC sitting on the edge of his bed.
    with dissolve

    u "(Guess I'll chill out for a bit.)"

    scene v8smcrm4a # TPP. Show MC sitting on the edge of his bed, phone in hand.
    with dissolve

    $ newKiwiiPost = KiwiiPost("Chloe", "images/chlaubpost1", "Hanging with my best friend. Good times!", numberLikes=312) # Chloe & Aubrey having fun at the beach.

    $ newKiwiiPost.addReply("Looking hot, ladies!", "replyLabel", numberLikes=302)
    $ newKiwiiPost.addReply("This is such a great picture!", "replyLabel", numberLikes=316)

    $ newKiwiiPost = KiwiiPost("Lauren", "images/laurosepost1", "Having fun with Ms. Rose at Hoco!", numberLikes=344) # Lauren & Ms. Rose at Hoco.

    $ newKiwiiPost.addReply("I'm glad you guys had fun", "replyLabel", numberLikes=301)
    $ newKiwiiPost.addReply("Wow, you two look great!", "replyLabel", numberLikes=322)

    $ newKiwiiPost = KiwiiPost("Riley", "images/riclothpost1", "Nothing like a good day of shopping", numberLikes=343) # Picture of Riley outside a clothing store.

    $ newKiwiiPost.addReply("How many bikinis did you buy? Haha.", "replyLabel", numberLikes=319)
    $ newKiwiiPost.addReply("Did you buy me anything?", "replyLabel", numberLikes=349)
    jump sun_aft_apes_house
