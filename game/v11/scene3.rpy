# SCENE 3: Apes Packing/ Samantha Invite
# Locations: MC's room (apes bedroom)
# Characters: MC (New outfit from scene 1), Samantha (outfit 1)
# Time: Thursday afternoon

label v11_samantha_packing:
    scene v11samp1 # FPP. MC is looking at his packed luggage, the luggage is open, with some clothes on the outside, next to the luggage
    with fade
    play music music.ck1.v11.Track_Scene_3 fadein 2
    u "(I really should get some more clothes.)"

    scene v11samp2 # FPP. MC is looking at his room's door, closed
    with dissolve

    play sound sound.knock
    pause 1

    play sound sound.door_open
    scene v11samp2a # FPP. MC is looking at Samantha at the door, which she is opening, she is moving in, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v11samp2b # FPP. Same cam as 2, Samantha is now inside the room, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v11samp2b
    with dissolve

    sa "..."

    scene v11samp2b 
    with dissolve

    u "What's up?"

    scene v11samp2c # FPP. Same positioning as 2b, Samantha mouth open, neutral expression
    with dissolve

    sa "Nothing... I'm bored."

    scene v11samp2b
    with dissolve

    u "Well I can't really keep you company right now."

    scene v11samp2c
    with dissolve

    sa "Why, what are you doing?"

    scene v11samp2b
    with dissolve

    u "Packing for the Europe trip, we leave Saturday morning."

    scene v11samp2d # FPP. Same as 2c, Samantha is annoyed, mouth open
    with dissolve

    sa "Wait what? No one told me about some kind of trip. How long are you going to be gone?"

    scene v11samp2e # FPP. Same as 2c, Samantha mouth closed, annoyed
    with dissolve

    u "A while, we're going to three different places."

    scene v11samp2d
    with dissolve

    sa "I assume I'm just gonna be here all by myself then. I'm sure Cameron and the whole monkey gang are going."

    scene v11samp2e
    with dissolve

    u "Actually, as of now only Ryan and I are going."

    scene v11samp2d
    with dissolve

    sa "Why didn't anyone tell me?"

    scene v11samp2e
    with dissolve

    u "I thought everyone knew."

    scene v11samp2d
    with dissolve

    sa "You know I don't pay attention to any of that stuff. I'm a little surprised you didn't tell me. You're gonna be gone for who knows how long and I'm stuck here with no one to talk to."

    scene v11samp2e
    with dissolve

    u "I can't be your only friend."

    scene v11samp2d
    with dissolve

    sa "No, but I just wasn't expecting you to just leave. Rude."

    menu:
        "Invite her" (samantha=1.0):
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ samantha.points += 1
            $ v11_invite_sam_europe = True
            scene v11samp2e
            with dissolve

            u "You can still come if you want, but like I said before, we leave Saturday."

            scene v11samp2f # FPP. Same as 2c, Samantha is happy, mouth open
            with dissolve

            sa "Why didn't you say that before I started complaining? *Chuckles* What do I need to do?"

            scene v11samp2g # FPP. Same as 2c, Samantha is happy, mouth closed
            with dissolve

            u "Just talk to Ms. Rose, she'll get you set up."

            scene v11samp2f
            with dissolve

            sa "That's it?"

            scene v11samp2g
            with dissolve

            u "Oh, there's also a $200 fee. Just give it to me and I'll make sure it gets to where it needs to go."

            scene v11samp2f
            with dissolve

            sa "Funny."

            scene v11samp2g
            with dissolve

            u "You don't even know anything about the trip. Why do you want to go?"

            scene v11samp2f
            with dissolve

            sa "A vacation in Europe and you said the only people from here going are you and Ryan. That means for however long we're there I can be away from my brother."

            scene v11samp2g
            with dissolve

            u "Knowing him he'll find a way to go if you're going. You have to tell him."

            scene v11samp2f
            with dissolve

            sa "I'll just tell him last minute when it's too late for him to come."

            scene v11samp2g
            with dissolve

            u "Haha, good luck with that."

            scene v11samp2f
            with dissolve

            sa "Who else is going?"

            scene v11samp2g
            with dissolve

            u "A lot of people, but I doubt you even know them."

            scene v11samp2f
            with dissolve

            sa "You don't know everyone I know. *Chuckles* C'mon who else is going?"

            scene v11samp2g
            with dissolve

            u "Nora, Lindsey, Chris, Riley, Amber... a lot of people."

            scene v11samp2f
            with dissolve

            sa "I obviously know Chris, I hear Grayson talk shit about him and the Wolves all the time. And is Riley the girl with the red hair?"

            scene v11samp2g
            with dissolve

            u "That's her."

            scene v11samp2f
            with dissolve

            sa "Okay then yeah, I know her too. She actually came to one of my impromptu things."

            sa "She tried giving me advice and I got a little bitchy with her cause I thought she was being rude, but in hindsight she probably just wanted to help..."

            scene v11samp2g
            with dissolve

            u "Yeah, I've never seen Riley rude a day in my life."

            scene v11samp2f
            with dissolve

            sa "Haha, I'm glad she's going. If I get tired of you I'll just hang out with her."

            scene v11samp2g
            with dissolve

            u "Am I that boring?"

            scene v11samp2f
            with dissolve

            sa "Relax, I'm just kidding."

            scene v11samp2g
            with dissolve

            u "Sure..."

            scene v11samp2f
            with dissolve

            sa "I'm gonna go get on the list before it's too last minute."

            scene v11samp2g
            with dissolve

            u "Alright, see ya."

            scene v11samp2h # FPP. Same cam as 2a, Samantha is walking towards the door, leaving the room
            with dissolve

            pause 0.75

            scene v11samp2i # FPP. Same cam as 2a, Samantha is now at the door, ready to leave the room
            with dissolve

            pause 0.75

            scene v11samp2
            with dissolve

            play sound sound.door_close

            u "(One more on the list.)"

            play sound sound.door_open
            scene v11samp2j # FPP. Same as 2a, Samantha has her upper body appearing through the doorway, happy expression, mouth open, looking at MC
            with dissolve

            sa "You said Ms. Rose right?"

            scene v11samp2k # FPP. Same as 2a, Samantha has her upper body appearing through the doorway, happy expression, mouth closed, looking at MC
            with dissolve

            u "Haha, yes."

            scene v11samp2j
            with dissolve

            sa "Okay, just making sure."

        "Don't invite her":
            scene v11samp2e
            with dissolve

            u "I'm sorry, I thought everyone knew. I would've invited you if I knew you didn't know, it's kinda late now. Like I said before, we leave Saturday morning."

            scene v11samp2d
            with dissolve

            sa "*Sighs* You could've at least asked me."

            scene v11samp2e
            with dissolve

            u "I said I'm sorry, I didn't know."

            scene v11samp2d
            with dissolve

            sa "Okay but you didn't even tell me you were going."

            scene v11samp2e
            with dissolve

            u "My bad, I don't know what you want me to do."

            scene v11samp2d
            with dissolve

            sa "Just forget it."

            scene v11samp2h
            with dissolve

            pause 0.75

            scene v11samp2i
            with dissolve

            pause 0.75

            scene v11samp2
            with dissolve

            play sound sound.door_close

            u "(Woah.)"

    scene v11samp2
    with dissolve
        
    play sound sound.call
    pause 2.25
            
    stop music fadeout 3

    jump v11_cafe_with_riley