# After protest with Autumn
# Location: Wolves Room, MC's College Dorm
# Outfits: MC outfit 3
# Time: Saturday Afternoon

# WOLVES ROOM
label after_prot_wolves:
    scene v8sprot22 # TPP. Show MC entering his wolves room.
    with fade
    play sound sound.door_open
    pause 0.5

    scene v8sprot23 # TPP. Show MC sitting at his desk with an open book.
    with dissolve

    u "(I suppose I can study for a bit.)"

    scene v8sprot23a # TPP. Same camera as v8sprot23, but MC has his head on desk.
    with dissolve

    pause 1

    scene v8sprot23b # TPP. Same camera as v8sprot23, but MC is now sat back up and looking fed up.
    with dissolve

    u "I'm never gonna get this shit."

    play sound sound.knock
    "*Knock knock knock*"

    scene v8sprot24 # FPP. Show the closed door of MC's room as Sebastian is knocking on the door.
    with dissolve

    u "(Just in time.)"
    u "Come in!"

    play sound sound.door_open

    scene v8sprot25 # TPP. Show Sebastian now in MC's room pointing at the books on his desk, Sebastian mouth open.
    with dissolve

    se "Looks like I showed up just in time."

    scene v8sprot26 # FPP. Close up Sebastian, Sebastian smile, mouth closed.
    with dissolve

    u "Totally. What's up?"

    scene v8sprot26a # FPP. Same camera as v8sprot26, Sebastian smile, mouth open.
    with dissolve

    se "I'm headed to the gym to workout. Figured I'd show you around."

    scene v8sprot27 # TPP. Show MC standing up out of his chair leaving his room with Sebastian. MC smile, mouth open.
    with dissolve

    u "Great! I need a break."

    jump wolves_gym_intro

# MC'S COLLEGE DORM
label after_prot_dorm:
    scene v8sprot28 # TPP. Show MC entering his college dorm.
    with fade
    play sound sound.door_open
    pause 0.5

    scene v8sprot29 # TPP. Show MC sitting on the edge of his bed. MC mouth open.
    with dissolve

    u "Might as well get ready for the ceremony."

    scene v8sprot30 # TPP. Show MC getting ready in his dorm for the Apes ceremony.
    with fade
    pause 0.5

    jump apes_join_ceremony
