# SCENE 06: MC in his room Thursday night
# Locations: MC bedroom,
# Characters: MC (smart outfit from scene 1)
# Time: Thursday night

label v11_thurs_night_room:
    play music "music/v11/Track Scene 6.mp3" fadein 2
    if mc.frat == Frat.WOLVES:
        scene v11tnr1 # TPP. Show MC walking into his wolves bedroom.
        with fade
        
        pause 0.75

        scene v11tnr2 # TPP. Show MC near his wolves bed
        with dissolve

        if "v11_candy" in sceneList:
            u "(That was crazy, but worth it! I'm tired as hell though... I'll pack tomorrow.)"

        else:
            u "(I'm tired as hell... I'll pack tomorrow.)"

        u "(Actually, I should text Riley real quick and see if she wants to go to that thing tomorrow.)"

        #-MC gets out his phone and text Riley-

        $ MessengerService.add_reply(riley, "You wanna catch the indoor skydiving thing tomorrow before the trip?")
        $ MessengerService.new_message(riley, "I knew I was forgetting something... I actually made plans with Charli already. Sorry :(")
        $ MessengerService.add_reply(riley, "It's fine, gn.")
        $ MessengerService.new_message(riley, "Goodnight")

        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "(I should reply to Riley.)"

        u "(This is kinda weird... First I have no idea who this guy is and now he's in my circle? *Sighs* I'm not gonna stress about it, I just need to relax. Getting some sleep will be nice.)"

        scene v11tnr3 # TPP. Show MC laying on his wolves bed
        with dissolve
        pause 1
        stop music fadeout 3

#-Non dialog images of MC getting into bed and sleeping-
        jump v11_room_aubrey_shopping
    else:
        scene v11tnr4 # TPP. Show MC walking into his apes bedroom.
        with fade
        
        pause 0.75

        scene v11tnr5 # TPP. Show MC near his apes bed
        with dissolve

        if "v11_candy" in sceneList:
            u "(That was crazy, but worth it! I'm tired as hell though... I'll pack tomorrow.)"

        else:
            u "(I'm tired as hell... I'll pack tomorrow.)"

        $ MessengerService.add_reply(riley, "You wanna catch the indoor skydiving thing tomorrow before the trip?")
        $ MessengerService.new_message(riley, "I knew I was forgetting something... I actually made plans with Charli already. Sorry :(")
        $ MessengerService.add_reply(riley, "It's fine, gn.")
        $ MessengerService.new_message(riley, "Goodnight")

        scene v11seap2b
        with dissolve

        u "(Actually, I should text Riley real quick and see if she wants to go to that thing tomorrow.)"

        #-MC gets out his phone and text Riley-

        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "(I should reply to Riley.)"
                
        u "(This is kinda weird... First I have no idea who this guy is and now he's in my circle? *Sighs* I'm not gonna stress about it, I just need to relax. Getting some sleep will be nice.)"

        scene v11tnr6 # TPP. Show MC laying on his apes bed
        with dissolve

        pause 1
        stop music fadeout 3

        jump v11_room_aubrey_shopping