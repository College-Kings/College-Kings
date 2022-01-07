# SCENE 14a: Wake up Apes
# Locations: MC's Apes Bedroom
# Characters: MC (Outfit: just boxers and 9)
# Time: Morning

label v14s14a:
    play music "music/v12/Track Scene 13.mp3" fadein 2

    scene black
    with fade
    
    pause 2

    $ chloe.messenger.newMessage(_("You won't believe what I'm looking at right now!!!!"), force_send=True)
    play sound "sounds/vibrate.mp3"

    u "*Phone vibrates*"

    scene v14s14a_1 # FPP. MC looking at his room as he is waking up. 
    with fade

    $ chloe.messenger.newMessage(_("Lindsey and I are NOT friends anymore."), force_send=True)
    play sound "sounds/vibrate.mp3"

    u "*Phone vibrates*"

    u "Mmm... Huh?"

    scene v14s14a_1a # TPP. MC sitting up on his bed, confused face, mouth closed.
    with dissolve

    $ chloe.messenger.newMessage(_("I'm gonna need your help with the President thing, big time"), force_send=True)
    play sound "sounds/vibrate.mp3"

    u "*Phone vibrates*"

    scene v14s14a_1b # TPP. Same as v14s14_2, MC looking at his phone which he is now holding, confused face, mouth closed.
    with dissolve

    $ chloe.messenger.newMessage(_("[name]!!!"), force_send=True)
    play sound "sounds/vibrate.mp3"

    u "*Phone vibrates*"

    u "(Who's blowing up my phone?)"

    $ chloe.messenger.newMessage(_("Right, you're probably asleep. When you read this, just meet me in the hall near Ms. Rose's classroom at 10."), force_send=True)

    call screen phone
    
    scene v14s14a_1c # TPP. same as v14s14a_1b MC puts his phone away
    with dissolve

    u "(Fuck... What time is it now?)"

    scene v14s14a_1d # TPP. same as v14s14a_1c Mc looks at his clock on his night stand
    with dissolve

    u "Nine fifty ni- OH, SHIT!"

    scene v14s14a_2 # TPP. MC jumps up out of bed, slightly shocked expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s14a_3 # TPP. MC puts on his shirt and pants, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s14a_4 # TPP. MC runs out of the room, mc's back is turned, face is not visible
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s15