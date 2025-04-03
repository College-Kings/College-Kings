# SCENE 14: Samantha At The Apes
# Locations: MC - Apes Living Room
# Characters: Sam (Outfit 2), MC (Outfit 1), Cameron (Outfit 3)
# Time: Sunday Morning

label v10_apes_samantha:
    scene v10ssap1 # TPP. Show MC in the Ape's living room. He's sitting on the couch, appearing exhausted, mouth closed.
    with fade

    play music music.ck1.v10.Track_Scene_14 fadein 2

    u "(Shit I'm tired.)"

    scene v10ssap1a # TPP. Same camera as v10ssap1. MC's sitting on the couch, appearing exhausted, mouth closed. He reaches forward to grab the remote.
    with dissolve
    
    pause 0.5

    scene v10ssap1b # TPP. Same camera as v10ssap1. MC's sitting on the couch, appearing exhausted, mouth closed. He's holding the remote. Show Samantha come into the living room.
    with dissolve
    
    pause 0.5

    scene v10ssap1c # TPP. Same camera as v10ssap1. MC's sitting on the couch, appearing exhausted, mouth closed. He's holding the remote. Samantha sits down on the couch next to him, smiling, mouth open.
    with dissolve

    sa "Hey hey!"

    scene v10ssap2 # FPP. Perspective is from MC, who is sitting on the couch in Ape's living room. Show Sam (who is sitting beside him), normal/slightly curious expresison, mouth closed.
    with dissolve

    u "Hey..."

    scene v10ssap2a # FPP. Same camera as v10ssap2. Show Sam, normal/slightly curious expresison, mouth open.
    with dissolve

    sa "Something wrong?"

    scene v10ssap2
    with dissolve

    u "Uhm... no, I'm good. I'm just tired."

    scene v10ssap2a
    with dissolve

    sa "Oh okay. I got a question for you."

    scene v10ssap2
    with dissolve

    u "What's up?"

    scene v10ssap2a
    with dissolve

    sa "I've been thinking a lot about the frats and the fighting. My brother has been a hothead his entire life-"

    scene v10ssap2
    with dissolve

    u "*Chuckles* Really? I didn't notice."

    scene v10ssap2b # FPP. Same camera as v10ssap2. Show Sam, smiling, mouth open.
    with dissolve

    sa "*Laughs* Yeah, it's very subtle. But yeah, he's always been a hothead so it makes sense to me for a guy like him to fight and be in a frat like this, but you're not like him and yet you're in this frat too."

    scene v10ssap2c # FPP. Same camera as v10ssap2. Show Sam, smiling, mouth closed.
    with dissolve

    u "And your question is..."

    scene v10ssap2a
    with dissolve

    sa "Well, I guess I really just wanna know why. It's kinda weird, don't you think? You don't really fit in with everyone else here."

    scene v10ssap2
    with dissolve

    menu:
        "I can be a hothead" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v10ssap2c
            with dissolve

            u "I can be a hot head at least when I need to be, *chuckles* sometimes when I wanna be."

            scene v10ssap2b
            with dissolve

            sa "So you have a dangerous side... I never knew"

            scene v10ssap2c
            with dissolve

            u "I may not have gotten into fights before college, but I never let people disrespect me and I definitely wasn't afraid to speak my mind."

            scene v10ssap2b
            with dissolve

            sa "That we have in common."

            scene v10ssap2
            with dissolve

            u "I just think sometimes there's better ways to make someone pay than violence."

            scene v10ssap2a
            with dissolve

            sa "What do you mean?"

            scene v10ssap2a
            with dissolve

            u "Back in high school I had a teacher that was just always out to get me."

            u "People were doing all kinds of shit, they were throwing paper planes at him during class, cheating on his tests and just making fun of him even with him in the room."

            u "But they never got into any trouble. I did anything remotely questionable, there I go, straight to detention."

            u "Well at some point I got really fed up and I wanted to piss him off you know, get him really good."

            scene v10ssap2b
            with dissolve

            sa "Please tell me this is leading to something really juicy like a senior prank or sugar in a gas tank?"

            scene v10ssap2c
            with dissolve

            u "Not quite. He announced that he was gonna be one of the chaperones for our senior prom and I knew his daughter just happened to be going to our school and graduating with me."

            u "Sooo... long story short, I asked his daughter to prom and - after some very painful back and forth - she said yes."

            u "We danced all night and I tried to give him as much eye contact as I possibly could, it was so funny."

            u "To be honest, the girl really wasn't keen on it once she found out why I had asked her, but... totally worth it. *Laughs*"

            scene v10ssap2b
            with dissolve

            sa "*Laughs* Remind me to never be a part of your revenge plans."

            scene v10ssap2c
            with dissolve

            u "Haha, I'll remember that."
       
        "What's that supposed to mean?" (bro=1.0):
            $ reputation.add_point(RepComponent.BRO)
            
            scene v10ssap2c
            with dissolve

            u "*Chuckles* What's that supposed to mean?"

            scene v10ssap2b
            with dissolve

            sa "You know.. Just that you're not really the strong macho type."

            scene v10ssap2c
            with dissolve

            u "I'll have you know that I can be quite a dangerous thumb-wrestler. Also, I still like doing dumb shit, I'm just trying to be smart about the dumb shit I do"

            scene v10ssap2b
            with dissolve

            sa "*Laughs* Was that your senior quote or something?"

            scene v10ssap2c
            with dissolve

            u "No, but it definitely could've been. My senior quote was way better. It went something like *chuckles* \"Cheaters never win, but I just did.\""

            scene v10ssap2b
            with dissolve

            sa "*Laughs* So you were the \"can I copy off of you\" kinda guy?"

            scene v10ssap2c
            with dissolve

            u "Hey, who's smarter, the guy that studies all night so he can get the right answers or the guy that doesn't study and then gets the answers from the guy that studies the next morning."

            scene v10ssap2b
            with dissolve

            sa "What's that saying? \"Don't hate the player, hate the game.\""

            scene v10ssap2c
            with dissolve

            u "Exactly."

    scene v10ssap1d # TPP. Same camera as v10ssap1. MC and Samantha are sitting on the couch, smiling, mouths closed. Camera walks into the living room with an aggressive look on his face, mouth closed.
    with fade
    
    pause 0.5

    scene v10ssap3 # FPP. Perspective is from MC, who is sitting on the couch in Ape's living room. He is looking up at Cameron who is standing nearby. Show Cameron with an angry expression, mouth open.
    with dissolve
    
    ca "The fuck you guys doing? [name] you trying to hit on my sister?!"

    scene v10ssap3a # FPP. Same camera as v10ssap3. Show Cameron with an angry expression, mouth closed.
    with dissolve

    menu:
        "Maybe" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            
            scene v10ssap3a
            with dissolve

            u "Maybe I am, maybe I'm not. Why do you care?"

            scene v10ssap2d # FPP. Same camera as v10ssap2. Show Sam, with a smile that displays a bit of interest, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap3
            with dissolve

            ca "I don't need a reason, just don't be hitting on my sister!"

            scene v10ssap3a
            with dissolve

            u "My bad, I didn't realize you had called dibs already."

            scene v10ssap3
            with dissolve

            ca "What the fuck, no! I just..."

            scene v10ssap1e # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is standing nearby, angry expression, mouth closed. Sam is smiling, mouth open. MC is smiling, mouth closed.
            with dissolve

            sa "*Laughs*"

            scene v10ssap1f # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is standing nearby, angry expression, mouth open. Sam looks pissed, mouth closed. MC has a normal expression, mouth closed.
            with dissolve

            ca "I don't see what's so funny, you shouldn't be-"

            scene v10ssap1g # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is standing nearby, angry expression, mouth closed. Sam looks pissed, mouth open. MC has a normal expression, mouth closed.
            with dissolve

            sa "YOU SHOULDN'T BE TELLING ME WHAT I SHOULD OR SHOULDN'T BE DOING! Just leave us alone Cameron."

            scene v10ssap1f 
            with dissolve

            ca "*Grunts*"

            scene v10ssap1h # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is walking away, angry expression, mouth closed. Sam looks annoyed, mouth closed. MC has a normal expression, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap2c
            with fade

            u "That was fun."

            scene v10ssap2b
            with dissolve

            sa "*Chuckles* Oh shut up. And just so we're clear no one is calling dibs on me. I'm not some leftover lasagna."

            scene v10ssap2c
            with dissolve

            u "Oh, guess I need to tell the guys to forget I called dibs then."

            scene v10ssap2d
            with dissolve

            sa "So you called dibs huh?"

            scene v10ssap2c
            with dissolve

            u "Uhm... there may have been dibs called at some point in the past."

            scene v10ssap2b
            with dissolve

            sa "*Laughs*"

            scene v10ssap1i # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Sam starts to stand up from the couch. Mouths closed, normal expressions.
            with dissolve
            
            pause 0.5

            scene v10ssap3b # FPP. Same camera as v10ssap3. Show Sam standing nearby, normal expression, mouth open.
            with dissolve

            sa "Alright, I have some stuff I need to take care of, I'll see you later."

            scene v10ssap3c # FPP. Same camera as v10ssap3. Show Sam standing nearby, normal expression, mouth closed.
            with dissolve

            u "What kinda stuff?"

            scene v10ssap3b
            with dissolve

            sa "Uhm... you know? Stuff."

            scene v10ssap1j # TPP. Same camera as v10ssap1. Show MC sitting on the couch. Sam is walking away. Mouths closed, normal expressions.
            with dissolve

            u "(Ahh, she's something else. I should head up to my room.)"

            scene v10ssap1k # TPP. Same camera as v10ssap1. Show MC standing up from the couch. Mouth closed, normal expression.
            with dissolve
            
            pause 0.5
 
        "I don't know":
            scene v10ssap3a
            with dissolve

            u "I don't know what you're talking about, we're just talking. As friends."

            scene v10ssap2e # FPP. Same camera as v10ssap2. Show Sam, with an expression of awkward disappointment, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap4 # TPP. Show MC and Sam sitting on the couch. Cameron is standing nearby, angry expression, mouth closed. Sam has an awkward, disappointed expression, mouth closed, and is standing up from the couch. MC has a normal expression, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap3
            with fade

            ca "Looked like more than just a friendly conversation to me. Just don't try shit and we won't have a problem."

            scene v10ssap3a
            with dissolve

            u "Right..."

            scene v10ssap3
            with dissolve

            ca "Samantha's been through enough already and doesn't need to deal with any of your bullshit too. You do anything to fucking upset her and you're fucking dead."

            scene v10ssap3a
            with dissolve

            u "Fine, whatever."

            scene v10ssap1k
            with fade

            u "(He can really be a dick sometimes. Good ol' Cameron. I should head up to my room.)"

    stop music fadeout 3

    jump v10_call_with_lauren1 # jump to scene 15