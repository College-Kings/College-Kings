# SCENE 38: Walking Home Lindsey Text
# Locations: Park
# Characters: MC (Outfit 5)
# Time: Saturday Afternoon

init python:
    def v9s38_reply1():
        lindsey.messenger.newMessage(_("Great. See ya soon"))
        setattr(store, "hangOutWithLindsey", True)

    def v9s38_reply2():
        lindsey.messenger.newMessage(_(":("))
        lindsey.messenger.addReply(_("Please don't hate me. You know I want to. I really, really want to."))
        lindsey.messenger.newMessage(_("No hard feelings. Bye"))
        lindsey.messenger.addReply(_("Maybe after the fight?"))

label v9_walk_li_txt:
    scene v9wlt1 # TPP. Show MC walking through the park on his own, looking stressed.
    with fade

    u "(Ugh, this is such a mess. How did I get stuck in the middle of those two?)"

    u "(I may need some help if they run into each other again)"

    play music "music/v9/Track Scene 8_3.mp3" fadein 2

    scene v9wlt1a # TPP. Same camera as v9wlt1, MC checking his phone.
    with dissolve
    
    play sound "sounds/vibrate.mp3"

    u "(Please no more drama)"

    $ lindsey.messenger.newMessage(_("Hey Freshmeat! How's it hangin?"), force_send=True)
    $ lindsey.messenger.addReply(_("Hey Linds ;)"))
    $ lindsey.messenger.newMessage(_("I've decided to allow the nickname under one condition"))
    $ lindsey.messenger.addReply(_("Really? And what's that?"))
    $ lindsey.messenger.newMessage(_("Come hang out with me"))
    $ lindsey.messenger.addReply(_("Hell yeah! Be right there, Linds!"), v9s38_reply1)
    $ lindsey.messenger.addReply(_("Aww, I wish I could, but I gotta get ready for the brawl"), v9s38_reply2)
    
    label s38_PhoneContinue:
        if lindsey.messenger.replies:
            call screen phone
        if lindsey.messenger.replies:
            u "(I should reply to Lindsey.)"
            jump s38_PhoneContinue 
    
    scene v9wlt2 # TPP. Show MC putting his phone away and continue to walk on.
    with dissolve

    if hangOutWithLindsey:
        u "(I suppose I should head to see Lindsey.)"

        stop music fadeout 3

        jump v9_hang_w_linds
    
    else:
        u "(Shit.)"

        if joinwolves:
            stop music fadeout 3
            jump v9_wolves_pre_fight

        else:
            stop music fadeout 3
            jump v9_apes_pre_fight
