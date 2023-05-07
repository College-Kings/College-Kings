# Sebastian in Room
# Location: MC Wolves Room
# Outfits: MC Outfit 2, Sebastian Outfit 1
# Time: Tuesday Night
    # -Tuesday night in MC's room if he joined Wolves-
    # -MC is at his desk, getting up to go sit on his bed and check his phone-
    # -There is a knock at his door-

label seb_in_room:
    scene v8ssir1 # FPP. Show MC sat on his bed checking his phone.
    with fade

    pause 0.5

    play sound sound.knock

    scene v8ssir2 # FPP. Show the closed door of MCs room.
    with dissolve

    u "(Wonder who that is.)"

    play music music.ck1.punk15
    queue music ["music/m16punk.mp3", "music/m7punk.mp3"]

    scene v8ssir3 # TPP. Show MC going to the door and opening it, show Sebastian stood on the other side, Sebastian smile, mouth open.
    with dissolve

    se "Hey, bro! What's shaking? You got a minute?"

    scene v8ssir3a # TPP. Same camera as v8ssir3, Show MC gesturing Sebastian to come in, MC mouth open, Sebastian mouth closed.
    with dissolve

    u "Yeah, of course, come on in."

    scene v8ssir4 # FPP. Show Sebastian walking to the middle of MC's room, MC closing the door, Sebastian looking around.
    with dissolve

    pause 0.5

    scene v8ssir5 # FPP. Close up Sebastian, Sebastian neutral expression, mouth open.
    with dissolve

    se "How you settling in? You cool with being here?"

    scene v8ssir5a # FPP. Same camera as v8ssir5, Sebastian mouth closed.
    with dissolve

    u "Yeah! It's great. Can't think of anything I'm missing."

    scene v8ssir5b # FPP. Same camera as v8ssir5, Sebastian chuckle, mouth open.
    with dissolve

    se "Except some deco on the walls eh? Hahaha!"

    scene v8ssir5c # FPP. Same camera as v8ssir5, Sebastian smile, mouth closed.
    with dissolve

    u "Ahh, yeah maybe. I haven't really had time to add a personal touch. I'll get there eventually."

    scene v8ssir5b
    with dissolve

    se "Ah yeah, I hear that. Took me almost a month to finally get my cave looking sexy and shit haha."

    scene v8ssir5c
    with dissolve

    u "I'm not that great at decorating. Maybe you could give me some pointers some time?"

    scene v8ssir5
    with dissolve

    se "I'd be happy to, bro. Which reminds me, I came here to ask you something."

    scene v8ssir6 # TPP. Show MC beckoning Sebastian to take a seat at his desk, MC goes to sit on the edge of his bed.
    with dissolve

    pause 0.5

    scene v8ssir7 # TPP. Show MC now sat on his bed, Sebastian sat in MC's chair backwards, his arms on the seat's back. MC looking at Sebastian, MC mouth open.
    with dissolve

    u "Yeah shoot. What's up?"

    scene v8ssir8 # FPP. Show Sebastian sat in MC's chair backwards, his arms on the seat's back, Sebastian neutral expression, mouth open.
    with dissolve

    se "Nothing major, man. Just wanted to ask a small favor."

    scene v8ssir8a # FPP. Same camera as v8ssir8, Sebastian mouth closed.
    with dissolve

    u "If I can, I will. What's going on man?"

    scene v8ssir8
    with dissolve

    se "Well, me and Marcus usually do this together, but he's unavailable at the moment. Something came up and he had to split. Something about his father. I didn't press."

    scene v8ssir8b # FPP. Same camera as v8ssir8, Sebastian looking to his side, stalling, mouth closed.
    with dissolve

    # -Sebastian looks like he's stalling-

    u "You have a hard time asking a favor, don't you?"

    scene v8ssir8c # FPP. Same camera as v8ssir8, Sebastian now looking back at camera, laugh, mouth open.
    with dissolve

    se "Fuck man, do I! Haha. I've always just been a \"Do It Yourself\" kind of guy, even for stupid and small things."

    scene v8ssir8d # FPP. Same cabera as v8ssir8, Sebastian smile, mouth closed.
    with dissolve

    u "Like I said, Wolves stick together, you need a hand, I'll do whatever I can."

    scene v8ssir8e # FPP. Same camera as v8ssir8, Sebastian smile, mouth open.
    with dissolve

    se "Thanks [name]. Ok well, like I was saying, Marcus usually does this but he can't tonight. I was wondering if you want to climb the hospital with me?"

    scene v8ssir9 # FPP. Show Sebastian and MC looking at eachother, MC looking confused, MC mouth open.
    with dissolve

    u "Umm, hospital? Climb? I'm not following."

    scene v8ssir8c
    with dissolve

    se "Haha, I'm not surprised. Me and Marcus climb the hospital, from the ground to roof, no equipment, just pure balls and stupidity haha."
    se "It's also a great workout bro. Really gets those muscles working and that blood pumping. You in?"

    scene v8ssir8d
    with dissolve

    u "Damn, that sounds dangerous. What if we fall?"

    scene v8ssir8e
    with dissolve

    se "Trust me [name], we have the perfect route up. If you want, you can always use a safety hook. I'll show you how to use it."

    scene v8ssir8d
    with dissolve

    u "Yeah sure, fuck it. Why not?"

    scene v8ssir8f # FPP. Same camera as v8ssir8, Sebastian fist pumping, looking happy, mouth open.
    with dissolve

    se "WOOO! Awesome! Thanks, buddy! I knew I could count on you!"

    scene v8ssir8d
    with dissolve

    u "Hahaha! No problem, man."

    scene v8ssir10 # FPP. Show Sebastian standing up from the chair, mouth open.
    with dissolve

    se "Alright well, we gotta get moving. We'll go together. It's a nice easy jog to warm up."

    scene v8ssir11 # TPP. Show MC standing up from his bed, MC smile, mouth open.
    with dissolve

    u "Way ahead of you, let's rock."

    scene v8ssir12 # TPP. Show Sebastian clapping MC on the back, Sebastian smile, MC smile, Sebastian mouth open.
    with dissolve

    se "This is gonna be so fuckin great, you'll see!"

    scene v8ssir13 # TPP. Show MC and Sebastian leaving MC's Wolves room.
    with dissolve
    pause 0.5

    jump hosp_climb_seb
