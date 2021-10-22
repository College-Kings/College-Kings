# SCENE 14a: Wake up Apes
# Locations: MC's Apes Bedroom
# Characters: MC (Outfit: just boxers and 9)
# Time: Morning


label v14s14a:

    play sound "sounds/vibrate.mp3"

    scene v14s14a_1 # TPP. MC wakes up to his phone vibrating, reaches one hand towards his phone on his night stand newt to his alarm clock, tired expression, mouth closed
    with dissolve

    pause 0.75

    play sound "sounds/vibrate.mp3"

    scene v14s14a_1a # TPP. same as v14s14a_1 MC no espression, picks up his phone
    with dissolve

    u "Mmm… Huh?"

    scene v14s14a_1b # TPP. same as v14s14a_1a mc checks his phone
    with dissolve

    u "(Who's blowing up my phone?)"

    scene v14s14a_1b
    with dissolve

    $ contact_Chloe.newMessage(_("You won't believe what I'm looking at right now!!!! "), queue=True)
    $ contact_Chloe.newMessage(_("Lindsey and I are NOT friends anymore. "), queue=True)
    $ contact_Chloe.newMessage(_("I'm gonna need your help with the president thing, big time "), queue=True)
    $ contact_Chloe.newMessage(_("[NAME]!!! "), queue=True)
    $ contact_Chloe.newMessage(_("Right, you're probably asleep. When you read this, just meet me in the hall near Ms. Rose's classroom at 10. "), queue=True)

    scene v14s14a_1c # TPP. same as v14s14a_1b MC puts his phone away
    with dissolve

    u "(Fuck… What time is it now?)"

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

    jump v14s15