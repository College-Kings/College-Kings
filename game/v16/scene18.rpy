# SCENE 18: Transition MC walks home alone or with Imre
# Locations: MC's Room
# Characters: MC (Outfit: 5)
# Time: Tuesday night


label v16s18: # MC goes home
    scene v16s18_1 # TPP Show MC walking into his bedroom
    with dissolve

    pause 1


    scene v16s18_2 # TPP Show MC flopped onto his bed as if exhausted
    with dissolve

    u "(Is there ever going to be a day without drama? *Sighs* Maybe now I can finally get some rest.)"


    # MC's phone vibrates
    play sound "sounds/vibrate.mp3"

    scene v16s18_2
    with dissolve

    u "(Spoke too soon.)"


    scene v16s18_2a # TPP Same angle as 2, MC sitting up on his bed and looking at his phone
    with dissolve

    pause 1


    $ contact_amber.newMessage("Hey. You know how much you love me? ;) I'm at work all night tonight and forgot my phone charger at home! Grab it for me please? Key is under the mat.")
    $ contact_amber.addReply("Yeah, I guess I can help you out this one time :P")
    $ contact_amber.addReply("Ughhhhh")
    $ contact_amber.newMessage("Hurry, please. Battery's almost dead!!!!!!!")


    scene v16s18_2b # TPP Same angle as 2, MC putting his phone back into his pocket
    with dissolve

    u "(A hero's work is never done!)"


    scene v16s18_1a # TPP Same angle as 1, MC leaving his room
    with dissolve

    pause 1


    jump v16s19 # -Transition to Scene 19-