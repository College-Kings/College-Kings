# SCENE 29: Your Room Sat Morning
# Locations: MC Wolves/Apes room
# Characters: MC (Underwear)
# Time: Sat Morning

label v9_your_room_satmorn:
    if mc.frat == Frat.WOLVES:
        scene v9smr1 # TPP. Show MC waking up on his Wolves bed in underwear.
        with fade

        pause 1

        scene v9smr2 # TPP. Show MC sat on the edge of his bed looking motivated.
        with dissolve

        u "(You've been working hard to get here. Everyone is counting on you, but above all you are counting on you. Go out there and fucking kill it today!)"

        scene v9smr2a # TPP. Show MC placing one hand on his stomach (As if you're hungry).
        with dissolve

        u "(Definitely won't be doing anything on an empty stomach. Breakfast is the most important meal and all that bullshit.)"

        jump v9_satmorn_gfb_walk

    else:
        scene v9smr3 # TPP. Show MC waking up on his Apes bed in underwear.
        with fade

        pause 1

        scene v9smr4 # TPP. Show MC sat on the edge of his bed looking motivated.
        with dissolve

        u "(You've been working hard to get here. Everyone is counting on you, but above all you are counting on you. Go out there and fucking kill it today!)"

        scene v9smr4a # TPP. Same camera as v9smr2, show MC placing one hand on his stomach (As if you're hungry).
        with dissolve

        u "(Definitely won't be doing anything on an empty stomach. Breakfast is the most important meal and all that bullshit.)"

        jump v9_satmorn_gfb_walk
