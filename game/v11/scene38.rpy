# SCENE 38: Amber at the bar
# Location: Hotel Lobby, Hotel Bar, Road
# Characters: MC (Outfit 9), Amber (Outfit 1). Bartender (Outfit ask lew)
# Time: Afternoon

init python:
    def v11s38_kiwiiReply1():
        reputation.add_point(RepComponent.BOYFRIEND)
        v11s38_kiwiiPost1.newComment(amber, _("Haha, thank you [name]"), number_likes=138, mentions=[mc])
        v11s38_kiwiiPost1.newComment(cameron, _("Fucking simp"), number_likes=126, mentions=[mc])
    
    def v11s38_kiwiiReply2():
        reputation.add_point(RepComponent.BRO)
        v11s38_kiwiiPost1.newComment(amber, _("You were busy somewhere else... ;)"), number_likes=173)

label v11_amber_bar:

    $ v11s38_kiwiiPost1 = KiwiiPost(amber, "phone/kiwii/Posts/v11/v11s38_amber_kiwii.webp", _("Living the London life"), number_likes=312) # Amber sitting at the bar with a drink in her hand, smiling at the camera, hers legs are crossed, sexy pose
    $ v11s38_kiwiiPost1.newComment(lauren, _("So that's where you've been this entire trip! Beautiful as always"), number_likes=renpy.random.randint(150,300))
    $ v11s38_kiwiiPost1.newComment(riley, _("Hotttt! We need a girls night soon ;)"), number_likes=renpy.random.randint(150,300))
    $ v11s38_kiwiiPost1.newComment(caleb, _("Damn... looking good"), number_likes=renpy.random.randint(150,300))
    $ v11s38_kiwiiPost1.newComment(charli, _("I told you that outfit was made for you... absolutely stunning."), number_likes=renpy.random.randint(150,300))
    $ v11s38_kiwiiPost1.addReply(_("Woah! Hot as always"), v11s38_kiwiiReply1, number_likes=renpy.random.randint(260, 340))
    $ v11s38_kiwiiPost1.addReply(_("Thanks for the invite... lol"), v11s38_kiwiiReply2, number_likes=renpy.random.randint(250, 330))
    play music music.ck1.v11.Track_Scene_3 fadein 2
    scene v11amb1 # TPP. Show MC walking in the lobby, he has a slight smile, mouth closed
    with dissolve

    pause 1

    scene v11amb2 # TPP. Show MC walking into the bar, MC slight smile, show the bartender and Amber talking at the counter in the background, everyone smiling (Amber has her back to MC and the camera)
    with dissolve

    pause 1

    scene v11amb3 # FPP. MC standing relatively far from Amber and the bartender, MC looking at Amber (bartender out of shot), Amber mouth open, smiling seductively, looking at Bartender
    with dissolve

    am "I kissed a girl recently so I've had some experience..."

    scene v11amb4 # FPP. Same positioning as v11amb3, MC looking at Bartender, Bartender looking at Amber (out of shot), Bartender smiling, mouth open
    with dissolve

    bartender "*Chuckles* A skilled partner is always helpful."

    scene v11amb3
    with dissolve

    am "But you can never have enough practice, right? Maybe you could help me out Miss Bartender..."

    scene v11amb3a # FPP. Same as v11amb3, Amber holding her hand in front of her mouth as if she was holding a microphone, mouth open, smiling
    with dissolve
    
    am "*Singing* \"I like the Bartender, if you're lookin' for me I'm at the bar-r with her\". *Laughs*"

    scene v11amb4
    with dissolve

    bartender "Classic song right there."

    scene v11amb3b # FPP. Same as v11amb3, Amber smiling, mouth open, different pose
    with dissolve

    am "*Chuckles* Surprised you know it."

    scene v11amb4
    with dissolve

    bartender "It's literally called Bartender, of course I know it. *Laughs*"

    scene v11amb5 # TPP. Show MC walking in the bar towards a seat at the counter (Amber and Bartender talking in the background), MC smiling, mouth closed
    with dissolve

    pause 0.75

    scene v11amb6 # TPP. Show MC sitting next to Amber (Only MC in shot), MC mouth closed, slight smile
    with dissolve

    pause 0.75

    scene v11amb7 # FPP. MC looking at Amber who is sitting in the seat next to him, Amber looking at MC, Amber smiling, mouth closed
    with dissolve

    u "What? Don't stop flirting because of me. Please, continue."

    scene v11amb7a # FPP. Same as v11amb7, Amber smiling, mouth open
    with dissolve

    am "*Laughs* Where have you been? You've been ignoring me."

    scene v11amb7
    with dissolve

    u "What? No I haven't."

    scene v11amb7b # FPP. Same as v11amb7a, different pose
    with dissolve

    am "Then why haven't we done anything stupid together yet?"

    scene v11amb7c # FPP. Same as v11amb7b, Amber mouth closed, smiling
    with dissolve

    u "*Chuckles* I don't know, I haven't even seen you. I just got done dealing with Imre and Ryan."

    scene v11amb7b
    with dissolve

    am "Sure... You were probably busy with one of your girl friends."

    scene v11amb7
    with dissolve

    u "Really, Amber?"

    scene v11amb7a
    with dissolve

    am "What? Don't tell me you don't like being teased. I thought that was so much fun for you and Aubrey. *Laughs* Anyway, there is something I've been wanting to do."

    scene v11amb7c
    with dissolve

    u "What's that?"

    scene v11amb7b
    with dissolve

    am "I want to go go-kart racing."

    scene v11amb7c
    with dissolve

    u "Isn't that for little kids?"

    scene v11amb7a
    with dissolve

    am "What? No... Do you not know what go-karts are? *Chuckles*"

    scene v11amb7
    with dissolve

    u "Yes, Amber, I know what go-karts are. *Chuckles* I just thought they were more for little kids."

    scene v11amb7a
    with dissolve

    am "Well, the place I found only lets adults use the karts, so that should answer your question. Wanna come race me?"

    scene v11amb7
    with dissolve

    u "Haha, yeah. I'll race you."

    scene v11amb7d # FPP. Same as v11amb7, different pose, Amber now looking at Bartender's direction (bartender is in front of Amber, on the other side of the counter), Amber mouth open, smiling
    with dissolve

    am "Miss Bartender, how do we get to the go-kart place?"

    scene v11amb8 # FPP. MC now looking at the bartender, bartender mouth open, slight smile, Bartender looking at Amber's direction (Amber in same position as v11amb7)
    with dissolve

    bartender "It's literally right around the corner. Just turn right when you walk outside and keep walking until you bump into it."

    scene v11amb7d
    with dissolve

    am "Good, thanks."

    scene v11amb7b
    with dissolve
    
    am "Let's go, [name]."

    scene v11amb9 # TPP. Show Amber and MC getting up from their chairs, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11amb10 # TPP. Show MC and Amber leaving the bar, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11amb11 # TPP. Show MC and Amber walking in the hotel lobby, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11amb12 # TPP. Show MC and Amber walking out the hotel lobby into the street, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11amb13 # TPP. Show MC and Amber walking on the sidewalk, both smiling, mouths closed
    with fade

    pause 0.75
    stop music fadeout 3
    jump v11_mc_amber_gokart