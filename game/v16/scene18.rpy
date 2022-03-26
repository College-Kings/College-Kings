# SCENE 18: Transition MC walks home alone or with Imre
# Locations: MC's Room
# Characters: MC (Outfit: 5)
# Time: Tuesday night

label v16s18: # MC goes home
    if joinwolves:
        scene v16s18_3 # TPP Show MC walking into his bedroom [WOLF ROOM].
    else:
        scene v16s18_1 # TPP Show MC walking into his bedroom [APE ROOM].
    with dissolve
        
    pause 0.75

    if joinwolves:
        scene v16s18_4 # TPP Show MC flopped onto his bed as if exhausted [WOLF ROOM].
    else:
        scene v16s18_2 # TPP Show MC flopped onto his bed as if exhausted [APE ROOM].
    with dissolve

    u "(Is there ever going to be a day without drama? *Sighs* Maybe now I can finally get some rest.)"

    # MC's phone vibrates
    play sound "sounds/vibrate.mp3"

    if joinwolves:
        scene v16s18_4
    else:
        scene v16s18_2
    with dissolve

    u "(Spoke too soon.)"

    if joinwolves:
        scene v16s18_4a # TPP Same angle as 4, MC sitting up on his bed and looking at his phone [WOLF ROOM].
    else:
        scene v16s18_2a # TPP Same angle as 2, MC sitting up on his bed and looking at his phone [APE ROOM].
    with dissolve

    pause 0.75

    ### check queue and force check phone

    $ amber.messenger.newMessage("Hey. You know how much you love me? ;) I'm at work all night tonight and forgot my phone charger at home! Grab it for me please? Key is under the mat.", force_send=True)
    $ amber.messenger.addReply("Yeah, I guess I can help you out this one time :P")
    $ amber.messenger.addReply("Ughhhhh")
    $ amber.messenger.newMessage("Hurry, please. Battery's almost dead!!!!!!!")

    label v16s18_phoneContinue:
        if amber.messenger.replies:
            call screen phone
        if amber.messenger.replies:
            u "(I should reply to Amber.)"
            jump v16s18_phoneContinue

    if joinwolves:
        scene v16s18_4b # TPP Same angle as 4, MC putting his phone back into his pocket [WOLF ROOM].
    else:
        scene v16s18_2b # TPP Same angle as 2, MC putting his phone back into his pocket [APE ROOM].
    with dissolve

    u "(A hero's work is never done!)"

    if joinwolves:
        scene v16s18_3a # TPP Same angle as 3, MC leaving his room [WOLF ROOM].
    else:
        scene v16s18_1a # TPP Same angle as 1, MC leaving his room [APE ROOM].
    with dissolve

    pause 0.75

    jump v16s19 # -Transition to Scene 19-