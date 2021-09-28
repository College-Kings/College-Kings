# SCENE 14: Wake up Wolves
# Locations: MC's room in Wolves house.
# Characters: MC (Outfit: 9)
# Time: Morning


label v14s14:

    $ contact_Chloe.newMessage(_("You won't believe what I'm looking at right now!!!!"))
    play sound "sounds/vibrate.mp3"

    scene v14s14_1 # FPP. MC looking at his room as he is waking up. 
    with fade

    $ contact_Chloe.newMessage(_("Lindsey and I are NOT friends anymore."))
    play sound "sounds/vibrate.mp3"

    u "Mmm… Huh?"

    scene v14s14_2 # TPP. MC sitting up on his bed, confused face, mouth closed.
    with dissolve

    $ contact_Chloe.newMessage(_("I'm gonna need your help with the president thing, big time"))
    play sound "sounds/vibrate.mp3"

    pause 0.75

    scene v14s14_2a # TPP. Same as v14s14_2, MC looking at his phone which he is now holding, confused face, mouth closed.
    with dissolve

    $ contact_Chloe.newMessage(_("[name]!!!"))
    play sound "sounds/vibrate.mp3"

    u "(Who's blowing up my phone?)"

    $ contact_Chloe.newMessage(_("Right, you're probably asleep. When you read this, just meet me in the hall near Ms. Rose's classroom at 10."))

    label v14s14_PhoneContinueChloe:
        if contact_Chloe.getReplies():
            call screen phone
        if contact_Chloe.getReplies():
            u "(I should check my phone.)"
            jump v14s14_PhoneContinueChloe

    scene v14s14_2b # TPP. Same as v14s14_2a, MC putting his phone aways, slight smile, mouth closed.
    with dissolve

    u "(Fuck… What time is it now?)"

    scene v14s14_3 # FPP. MC looking at the clock on his nightstand, Time shows 9:59.
    with dissolve


    u "Nine fifty ni- OH, SHIT!"

    scene v14s14_4 # TPP. Show MC bolting for the door, worried face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s14_5 # TPP. MC throwing his door open in a hurry and running out, worried face, mouth closed.
    with dissolve

    jump v14s15

