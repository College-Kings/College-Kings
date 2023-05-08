# SCENE 38: Walking Home Lindsey Text
# Locations: Park
# Characters: MC (Outfit 5)
# Time: Saturday Afternoon

label v9_walk_li_txt:
    scene v9wlt1 # TPP. Show MC walking through the park on his own, looking stressed.
    with fade

    u "(Ugh, this is such a mess. How did I get stuck in the middle of those two?)"

    u "(I may need some help if they run into each other again)"

    play music "music/v9/Track Scene 8_3.mp3" fadein 2

    scene v9wlt1a # TPP. Same camera as v9wlt1, MC checking his phone.
    with dissolve
    
    play sound sound.vibrate

    u "(Please no more drama)"

    python:
        v9s38_reply1 = MessageBuilder(lindsey)
        v9s38_reply1.new_message(_("Great. See ya soon"))
        v9s38_reply1.set_variable("hangOutWithLindsey", True)

        v9s38_reply2 = MessageBuilder(lindsey)
        v9s38_reply2.new_message(_(":("))
        v9s38_reply2.add_reply(_("Please don't hate me. You know I want to. I really, really want to."))
        v9s38_reply2.new_message(_("No hard feelings. Bye"))
        v9s38_reply2.add_reply(_("Maybe after the fight?"))

        MessengerService.new_message(lindsey, _("Hey Freshmeat! How's it hangin?"))
        MessengerService.add_reply(lindsey, _("Hey Linds ;)"))
        MessengerService.new_message(lindsey, _("I've decided to allow the nickname under one condition"))
        MessengerService.add_reply(lindsey, _("Really? And what's that?"))
        MessengerService.new_message(lindsey, _("Come hang out with me"))
        MessengerService.add_replies(lindsey,
            Reply(_("Hell yeah! Be right there, Linds!"), v9s38_reply1),
            Reply(_("Aww, I wish I could, but I gotta get ready for the brawl"), v9s38_reply2)
        )
    
    while MessengerService.has_replies(lindsey):
        call screen phone
        if MessengerService.has_replies(lindsey):
            u "(I should reply to Lindsey.)"

    scene v9wlt2 # TPP. Show MC putting his phone away and continue to walk on.
    with dissolve

    if hangOutWithLindsey:
        u "(I suppose I should head to see Lindsey.)"

        stop music fadeout 3

        jump v9_hang_w_linds
    
    else:
        u "(Shit.)"

        if mc.frat == Frat.WOLVES:
            stop music fadeout 3
            jump v9_wolves_pre_fight

        else:
            stop music fadeout 3
            jump v9_apes_pre_fight
