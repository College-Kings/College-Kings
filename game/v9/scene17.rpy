# SCENE 17: Your Room Fri Morning
# Locations: MC Wolves/Apes room
# Characters: MC (Underwear), Chris (Outfit 1), Grayson (Outfit 2)
# Time: Friday Morning

label v9_room_fri_morn:
    if joinwolves:
        scene v9fmr1 # FPP. Show Chris looking into camera as if Chris is looking at MC whilst MC is in bed. Chris letter in hand. Camera looking up at Chris , Chris mouth open. (MC Wolves Room)
        with fade

        ch "Wake up [name], Wolves aren't nocturnal. Go be productive. And someone sent you some mail Mr. Popular."

        scene v9fmr1a # FPP. Same camera as v9fmr1, Chris mouth closed.
        with dissolve

        u "Early bird gets the worm and yada yada yada."

        scene v9fmr2 # TPP. Show Chris placing the letter on MC's bed, Chris mouth open. Ensure MC's phone is visible on his bed near his pillow.
        with dissolve

        ch "Right!"

        scene v9fmr3 # TPP. Show Chris leaving MC's room.
        with dissolve

        pause 0.8

        scene v9fmr4 # TPP. Show MC sat up on the edge of the bed, grabbing the letter, looking tired.
        with dissolve

        pause 0.8
        scene v9fmr4a # TPP. Same camera as v9fmr4, MC now has the letter in hand and is reading it.
        with dissolve

        u "(Over the semester you've been way more than a student, a true confidant. I hope I'll have the opportunity to return the favor. With gratitude, Miss Rose.)"

        scene v9fmr4b # TPP. Same camera as v9fmr4, MC places the letter back on his bed, slight confused expression.
        with dissolve

        u "(Ms. Rose, did she get a divorce? And what does she mean return the favor? Guess I'll find out soon.)"

        scene v9fmr4c # TPP. Same camera as v9fmr4, show MC checking his phone.
        with dissolve

        play sound sound.vibrate

        $ MessengerService.new_message(lauren, _("Hey, would yould you like to come over to my dorm and help me? I need help with my Deer initiation. They want me to help with the annual charity day event they have."))
        $ MessengerService.add_reply(lauren, _("Sure, OMW!"))
        $ MessengerService.new_message(lauren, _("Ok :) See you soon!"))
        
        while MessengerService.has_replies(lauren):
            call screen phone
            if MessengerService.has_replies(lauren):
                u "(I should text Lauren.)"

        u "(I better get ready and head over there. Hope it's not too much work.)"

        jump v9_lau_dorm

    else:
        scene v9fmr5 # FPP. Show Grayson looking into camera as ikf Grayson is looking at MC whilst MC is in bed. Stern Grayson expression, Camera looking up at Grayson, Grayson mouth open. (MC Apes Room)
        with fade

        gr "Wake up, [name], Apes aren't lazy assholes. Get up. Go be productive. Oh, and I'd avoid the toilet. Cameron backed it up again."

        scene v9fmr5a # FPP. Same camera as v9fmr5, Grayson mouth closed.
        with dissolve

        u "*Drowsy* Uhh, yeah ok. I'm up, and ewww."

        scene v9fmr5
        with dissolve

        gr "Good."

        scene v9fmr6 # TPP. Show MC sitting on the edge of his bed looking tired.
        with dissolve

        u "(Is this guy my fucking dad? Jesus.)"

        scene v9fmr7 # TPP. Same camera as v9fmr6, show MC checking his phone.
        with dissolve

        play sound sound.vibrate

        $ MessengerService.new_message(lauren, _("Hey, would yould you like to come over to my dorm and help me? I need help with my Deer initiation. They want me to help with the annual charity day event they have."))
        $ MessengerService.add_reply(lauren, _("Sure, OMW!"))
        $ MessengerService.new_message(lauren, _("Ok :) See you soon!"))
        
        while MessengerService.has_replies(lauren):
            call screen phone
            if MessengerService.has_replies(lauren):
                u "(I should text Lauren.)"

        u "(I better get ready and head over there. Hope it's not too much work.)"

        jump v9_lau_dorm