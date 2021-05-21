# SCENE 32: MC at Home Tuesday Night 
# Locations: MC NEW Wolves/Apes Room
# Characters: MC (Outfit 9/underwear/Outfit 10), Lauren (Topless)
# Time: Tuesday Night/Wednesday Morning

label v10_tues_room_night:
    play music "music/v10/Scene 32/Track Scene 32_1.mp3" fadein 3
    if joinwolves:
        scene v10strn1 # TPP. Show MC tired and stressed, plopping down on his Wolves bed.
        with fade

        u "(What a long fucking day. Fuck, everyday is like this and things just get more and more complicated.)"

        scene v10strn2 # TPP. Show MC now lying on his back, looking tired.
        with dissolve

        if laurenrs or v1_laurenKiss or laurenkissb:
            pause 0.75

            scene v10strn2a # TPP. Same as 2, MC now browsing his phone.
            with dissolve

            u "(And it continues.)"

            python:
                contact_Lauren.newImgMessage("images/v10/scene 32/v9lauText.webp", queue=False)
                contact_Lauren.newMessage("Sweet Dreams ;)", queue=False)
                contact_Lauren.addReply("They will be now.")

            label v10s32_phoneCheckW:
                if contact_Lauren.getReplies():
                    call screen phone
                if contact_Lauren.getReplies():
                    u "(I should reply to Lauren)"
                    jump v10s32_phoneCheckW

            scene v10strn2b # TPP. Same as 2, MC no longer on his phone, subtle smile.
            with dissolve

            u "(Not everything is all that bad, haha. Time to go to sleep.)"

        else:
            u "(I'm going to sleep.)"

        scene v10strn3 # TPP. Show MC going to sleep.
        with dissolve

        pause 0.75

        scene black
        with fade

        pause 0.75

        scene v10strn4 # TPP. Show MC waking up and stretching, now wearing underwear, now daylight.
        with dissolve

        u "(Bright and fucking early! I'm so excited for this charity event. I need to get ready.)"

        scene v10strn5 # TPP. Show MC leaving his Wolves room, now wearing outfit 10
        with fade

        pause 0.75

        jump v10_charity_freeroam

    else:
        scene v10strn6 # TPP. Show MC tired and stressed, plopping down on his Apes bed.
        with fade

        u "(What a long fucking day. Fuck, everyday is like this and things just get more and more complicated.)"

        scene v10strn7 # TPP. Show MC now lying on his back, looking tired.
        with dissolve

        if laurenrs or v1_laurenKiss or laurenkissb:
            pause 0.75

            scene v10strn7a # TPP. Same as 2, MC now browsing his phone.
            with dissolve

            u "(And it continues.)"

            python:
                contact_Lauren.newImgMessage("images/v10/scene 32/v9lauText.webp", queue=False)
                contact_Lauren.newMessage("Sweet Dreams ;)", queue=False)
                contact_Lauren.addReply("They will be now.")

            label v10s32_phoneCheckA:
                if contact_Lauren.getReplies():
                    call screen phone
                if contact_Lauren.getReplies():
                    u "(I should reply to Lauren)"
                    jump v10s32_phoneCheckA

            scene v10strn7b # TPP. Same as 2, MC no longer on his phone, subtle smile.
            with dissolve

            u "(Not everything is all that bad, haha. Time to go to sleep.)"

        else:
            u "(I'm going to sleep.)"

        scene v10strn8 # TPP. Show MC going to sleep.
        with dissolve

        pause 0.75

        scene black
        with fade

        pause 0.75

        scene v10strn9 # TPP. Show MC waking up and stretching, now wearing underwear, now daylight.
        with dissolve

        u "(Bright and fucking early! I'm so excited for this charity event. I need to get ready.)"

        scene v10strn10 # TPP. Show MC leaving his Wolves room, now wearing outfit 10
        with fade

        pause 0.75
        stop music fadeout 3
        jump v10_charity_freeroam
