# SCENE 38: Walking Home Lindsey Text
# Locations: Park
# Characters: MC (Outfit 5)
# Time: Saturday Afternoon

default hangOutWithLindsey = False

label v9_walk_li_txt:
    scene v9wlt1 # TPP. Show MC walking through the park on his own, looking stressed.
    with fade

    u "(Ugh, this is such a mess. How did I get stuck in the middle of those two?)"

    u "(I may need some help if they run into each other again)"

    play music "music/v09/Scene 38/Track Scene 38.mp3" fadein 2

    scene v9wlt1a # TPP. Same camera as v9wlt1, MC checking his phone.
    with dissolve
    
    play sound "sounds/vibrate.mp3"

    u "(Please no more drama)"

    $ phoneexit = "s38_PhoneContinue"

    $ contact_Lindsey.newMessage("Hey Freshmeat! How's it hangin?")
    $ contact_Lindsey.addReply("Hey Linds ;)", "s38_LinReply1")
    $ showphone = True
    call screen phone
    
    label s38_LinReply1:
        $ contact_Lindsey.newMessage("I've decided to allow the nickname under one condition")
        $ contact_Lindsey.addReply("Really? And what's that?", "s38_LinReply2")

        call screen messager(contact_Lindsey)

    label s38_LinReply2:
        $ contact_Lindsey.newMessage("Come hang out with me")
        $ contact_Lindsey.addReply("Hell yeah! Be right there, Linds!", "s38_LinReplyGood1")
        $ contact_Lindsey.addReply("Aww, I wish I could, but I gotta get ready for the brawl", "s38_LinReplyBad1")

        call screen messager(contact_Lindsey)

    label s38_LinReplyGood1:
        $ contact_Lindsey.newMessage("Great. See ya soon")
        $ hangOutWithLindsey = True
        call screen messager(contact_Lindsey)

    label s38_LinReplyBad1:
        $ contact_Lindsey.newMessage(":(")
        $ contact_Lindsey.addReply("Please don't hate me. You know I want to. I really, really want to.", "s38_LinReplyBad2")

        call screen messager(contact_Lindsey)

    label s38_LinReplyBad2:
        $ contact_Lindsey.newMessage("No hard feelings. Bye")
        $ contact_Lindsey.addReply("Maybe after the fight?")

        call screen messager(contact_Lindsey)

    label s38_PhoneContinue:
        if contact_Lindsey.messages[-1].replies:
            "(I should reply to Lindsey.)"
            jump s38_PhoneContinue

    scene v9wlt2 # TPP. Show MC putting his phone away and continue to walk on.
    with dissolve

    if hangOutWithLindsey:
        u "(I suppose I should head to see Lindsey)"

        stop music fadeout 3

        jump v9_hang_w_linds
    
    else:
        u "(Shit)"

        if joinwolves:
            stop music fadeout 3
            jump v9_wolves_pre_fight

        else:
            stop music fadeout 3
            jump v9_apes_pre_fight
