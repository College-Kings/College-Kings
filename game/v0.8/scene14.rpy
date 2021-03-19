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

    $ contact_Penelope.newMessage("[name] I'm really scared! I am in so much trouble! I need you! Please come over??")
    $ contact_Penelope.addReply("Ok try to stay calm. I'll be right over.")
    call screen messager(contact_Penelope)

    $ phoneexit = "v8_s14_pen_text"
    $ showphone = True

    play sound "sounds/vibrate.mp3"

    scene v8ssm2a # TPP. Same camera as v8ssm2, but MC now has phone in hand.
    with dissolve
    pause 0.5

    call screen messager(contact_Penelope)

label mc_apes_sun_morn:
    scene v8ssm3 # TPP. Show MC waking up in his bed in his Apes room, MC yawning.
    with fade

    u "*Yawn*"

    scene v8ssm4 # TPP. Show MC sat on the edge of his bed, looking really tired.
    with dissolve

    pause 0.5

    $ contact_Penelope.newMessage("[name] I'm really scared! I am in so much trouble! I need you! Please come over??")
    $ contact_Penelope.addReply("Ok try to stay calm. I'll be right over.")
    $ phoneexit = "v8_s14_pen_text"
    $ showphone = True

    play sound "sounds/vibrate.mp3"

    scene v8ssm4a # TPP. Same camera as v8ssm4, but MC now has phone in hand.
    with dissolve
    pause 0.5

    call screen messager(contact_Penelope)


label v8_s14_pen_text:
if contact_Penelope.replies:
    u "(I should reply to her.)"
    jump v8_s14_pen_text
else:
    $ showphone = False
    u "(That sounded serious. What got her all upset so sudden?)"
    jump penelope_dorm_hack
