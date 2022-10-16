# SCENE 6: At the docks
# Location: Docks
# Characters: MC (Outfit 1), Riley (Outfit 3), Mr. Lee (Outfit 1)
# Time: Morning

label v12_docks:
    scene v12dock1 # TPP. Show the shuttle parking at the dock
    with dissolve

    pause 1

    play music "music/v12/Track Scene 6.mp3" fadein 2

    scene v12dock2 # TPP. Show MC walking out of the shuttle, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12dock3 # TPP. Show MC walking in the docks with Riley, slight smiles, mouths closed
    with dissolve

    pause 1.25

    scene v12dock4 # FPP. Show Mr Lee waving at MC and Riley, slight smile, mouth open (Mr Lee pretty far away)
    with dissolve

    lee "Riley, [name], may I speak with you?"

    scene v12dock5 # FPP. Same positioning as v12dock4, MC now closer to Mr Lee, Mr Lee smiling, mouth closed, not waving anymore
    with dissolve

    pause 0.75

    scene v12dock6 # FPP. Same positioning as v12dock5, MC and Riley now talking distance to Mr Lee, MC looking at Riley, Riley looking at Mr Lee's direction, Riley smiling, mouth open (Riley standing next to MC, Mr Lee in front of both of them)
    with dissolve

    ri "Yes?"

    scene v12dock7 # FPP. Same positioning as v12dock6, MC looking at Mr Lee, Mr Lee looking at Riley's direction, Mr Lee smiling, mouth open
    with dissolve

    lee "Well, how's it going? I know you can't move on to the next part without completing the first, so how did it go?"

    scene v12dock6
    with dissolve

    ri "It was fun, I have to admit."

    scene v12dock7a # FPP. Same as v12dock7, Mr Lee looking at MC, Mr Lee smiling, mouth closed
    with dissolve

    u "As long as there's extra credit at the end, I won't be too mad."

    scene v12dock7
    with dissolve

    lee "*Laughs* Just keep going with it. I only wanted to make sure the venture didn't end in London."

    scene v12dock6
    with dissolve

    ri "Nope, we're ready to tackle Paris."

    scene v12dock7
    with dissolve

    lee "Good to hear."

    scene v12dock7b # FPP. Show Mr Lee walking away, smiling, mouth closed
    with dissolve

    pause 0.75

    scene v12dock6a # FPP. Same as v12dock6, Riley looking at MC, slight smile, mouth open
    with dissolve

    ri "He's so giggly about this little treasure hunt."

    scene v12dock6b # FPP. Same as v12dock6a, Riley slight smile, mouth closed
    with dissolve

    u "Suspiciously giggly if you ask me."

    scene v12dock6c # FPP. Same as v12dock6a, Riley slightly worried, avoiding eye contact, mouth open
    with dissolve

    ri "Speaking of asking you things, and please just keep this between me and you, but I saw you walking with Amber. Did she say anything about me?"

    scene v12dock6d # FPP. Same as v12dock6c, Riley avoiding eye contact, slightly worried, mouth closed
    with dissolve

    menu:
        "Not much":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            scene v12dock6e # FPP. Same as v12dock6d, Riley looking at MC, slightly worried, mouth closed, different pose
            with dissolve

            u "Not much, we didn't really talk. What's going on?"

        "No":
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v12dock6e
            with dissolve

            u "No, what's going on?"

    scene v12dock6f # FPP. Same as v12dock6d, Riley slightly worried, mouth open
    with dissolve

    ri "Well, I said something and I don't know how she took it."

    scene v12dock6e
    with dissolve

    u "What'd you say?"

    scene v12dock6f
    with dissolve

    ri "I kinda told her I liked her, liked her."

    scene v12dock6d
    with dissolve

    u "Oh. And she said...?"

    scene v12dock6c
    with dissolve

    ri "Well, that's the thing. She didn't say anything. She kinda just brushed it off and left real fast."

    scene v12dock6e
    with dissolve

    u "Oh..."

    scene v12dock6f
    with dissolve

    ri "I just wanted to know if she said anything, I'm not gonna let it bother me though."

    scene v12dock6a
    with dissolve
    
    ri "Aubrey and I talked about this little slumber party idea I had and she's been keeping me company."

    scene v12dock6b
    with dissolve

    u "Well, that's good. You and Aubrey were already really close I thought."

    scene v12dock6a
    with dissolve

    ri "We are, I'd just been spending a lot of time with Amber and blowing off pretty much everyone else."

    scene v12dock6b
    with dissolve

    u "Ohh, haha."

    scene v12dock6a
    with dissolve

    ri "Well, thanks. And don't pretend like you don't enjoy doing the treasure hunt... You know you like spending time with me."

    scene v12dock6b
    with dissolve

    u "Haha. Yeah, you're right. I do."

    scene v12dock6g # FPP. Same as v12dock6, show Riley walking away
    with dissolve

    u "(Hmmm, this must be what Amber was saying she wanted to talk about. I knew them two were getting close, but not like this.)"

    stop music fadeout 3

    jump v12s7fr #scene 7