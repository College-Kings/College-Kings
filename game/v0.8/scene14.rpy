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

    # Phone buzzes #

    scene v8ssm2a # TPP. Same camera as v8ssm2, but MC now has phone in hand.
    with dissolve

    $ contact_Penelope.newMessage("[name] I'm really scared! I am in so much trouble! I need you! Please come over??")

    $ contact_Penelope.addReply("Ok try to stay calm. I'll be right over.")

    pause 0.5

    jump penelope_dorm_hack

label mc_apes_sun_morn:
    scene v8ssm3 # TPP. Show MC waking up in his bed in his Apes room, MC yawning.
    with fade

    u "*Yawn*"

    scene v8ssm4 # TPP. Show MC sat on the edge of his bed, looking really tired.
    with dissolve

    pause 0.5

    # Phone buzzes #

    scene v8ssm4 # TPP. Same camera as v8ssm4, but MC now has phone in hand.
    with dissolve

    $ contact_Penelope.newMessage("[name] I'm really scared! I am in so much trouble! I need you! Please come over??")

    $ contact_Penelope.addReply("Ok try to stay calm. I'll be right over.")

    pause 0.5

    jump penelope_dorm_hack
