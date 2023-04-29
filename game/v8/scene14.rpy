# Sunday Morning in MC's room
# Location: MC's Apes Room OR MC Wolves Room
# Outfits: MC Underwear
# Time: Sunday Morning

# -Sunday Morning in MC's room-

label mc_wolves_sun_morn:
    scene v8ssm1 # TPP. Show MC waking up in his bed in his Wolves room, MC yawning.
    with fade

    u "*Yawn*"

    scene v8ssm2 # TPP. Show MC sat on the edge of his bed, looking really tired.
    with dissolve
    pause 0.5

    $ MessengerService.new_message(penelope, _("[name] I'm really scared! I am in so much trouble! I need you! Please come over??"))
    $ MessengerService.add_reply(penelope, _("Ok try to stay calm. I'll be right over."))
    

    play sound "sounds/vibrate.mp3"

    scene v8ssm2a # TPP. Same camera as v8ssm2, but MC now has phone in hand.
    with dissolve
    pause 0.5

    jump v8_s14_pen_text

label mc_apes_sun_morn:
    scene v8ssm3 # TPP. Show MC waking up in his bed in his Apes room, MC yawning.
    with fade

    u "*Yawn*"

    scene v8ssm4 # TPP. Show MC sat on the edge of his bed, looking really tired.
    with dissolve

    pause 0.5

    $ MessengerService.new_message(penelope, _("[name] I'm really scared! I am in so much trouble! I need you! Please come over??"))
    $ MessengerService.add_reply(penelope, _("Ok try to stay calm. I'll be right over."))
    

    play sound "sounds/vibrate.mp3"

    scene v8ssm4a # TPP. Same camera as v8ssm4, but MC now has phone in hand.
    with dissolve
    pause 0.5

    jump v8_s14_pen_text

    while MessengerService.has_replies(penelope):
        call screen phone
        if MessengerService.has_replies(penelope):
            u "(I should reply to her.)"
        
    u "(That sounded serious. What got her all upset so sudden?)"
    jump penelope_dorm_hack
