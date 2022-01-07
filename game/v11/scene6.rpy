# SCENE 06: MC in his room Thursday night
# Locations: MC bedroom,
# Characters: MC (smart outfit from scene 1)
# Time: Thursday night

label v11_thurs_night_room:
    play music "music/v11/Track Scene 6.mp3" fadein 2
    if joinwolves:
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

        $ riley.messenger.addReply("You wanna catch the indoor skydiving thing tomorrow before the trip?")
        $ riley.messenger.newMessage("I knew I was forgetting something... I actually made plans with Charli already. Sorry :(")
        $ riley.messenger.addReply("It's fine, gn.")
        $ riley.messenger.newMessage("Goodnight")

        label v11s6_PhoneContinue:
            if riley.messenger.replies:
                call screen phone
            if riley.messenger.replies:
                "(I should reply to Riley.)"
                jump v11s6_PhoneContinue

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

        $ riley.messenger.addReply("You wanna catch the indoor skydiving thing tomorrow before the trip?")
        $ riley.messenger.newMessage("I knew I was forgetting something... I actually made plans with Charli already. Sorry :(")
        $ riley.messenger.addReply("It's fine, gn.")
        $ riley.messenger.newMessage("Goodnight")

        scene v11seap2b
        with dissolve

        u "(Actually, I should text Riley real quick and see if she wants to go to that thing tomorrow.)"

        #-MC gets out his phone and text Riley-

        label v11s6_PhoneContinue1:
            if riley.messenger.replies:
                call screen phone
            if riley.messenger.replies:
                "(I should reply to Riley.)"
                jump v11s6_PhoneContinue1
                
        u "(This is kinda weird... First I have no idea who this guy is and now he's in my circle? *Sighs* I'm not gonna stress about it, I just need to relax. Getting some sleep will be nice.)"

        scene v11tnr6 # TPP. Show MC laying on his apes bed
        with dissolve

        pause 1
        stop music fadeout 3

        jump v11_room_aubrey_shopping