# Scene 6
# MC arrives back at his room and lays down on his bed. He gets on his phone and opens the Kiwii app. MC scrolls through homecoming photos.
# Note to renderers, MC wearing outfit 3.
label aft_amb_night:
    if joinwolves:
        scene scaf1 # TPP. Show MC lay on his bed on his phone in his wolves bedroom.
        with fade

        pause 1

        play music music.ck1.mchill1

        scene scaf1a # TPP. As above but show MC sat on the edge of his bed, mouth open.
        with dissolve

        u "Man, I'm hungry. I need something to eat."

        scene scaf2 # TPP. Show MC leaving his room, camera from behind.
        with dissolve
        pause 0.7

        jump caf_w_aub

    else:
        scene scaf3 # TPP. Show MC lay on his bed on his phone in his college dorm.
        with fade

        pause 1

        play music music.ck1.mchill1

        scene scaf3a # TPP. Show MC sat on the edge of his bed, mouth open.
        with dissolve

        u "Man, I'm hungry. I need something to eat."

        scene scaf4 # TPP. Show MC leaving his dorm, camera from behind.
        with dissolve
        pause 0.7

        jump caf_w_aub
