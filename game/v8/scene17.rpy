# SCENE 17: HELPING MS. ROSE MOVING
# Locations: Wolves house (MC's new room), Ms Rose's house
# Characters needed: MC (outfit 2 but Wolves jacket on top of it), Ms Rose (outfit 1), Chris (outfit 2), Finn (outfit 1), Imre (outfit 2 but Wolves jacket on top of it), Aaron (outfit 2)
# Time: Sunday afternoon
# Ms. Rose flashback pic (used as a prop in a few renders): Ms. Rose and her husband with him having his hand over her waist. Rose is happy in the pic. Use a random model for the husband (his face won't be shown to the viewer) and maybe a different outfit for Rose.
# Please look at the rpy file along with the render table to get a good idea of the scene's dynamics

label msrose_moving:
    $ MessengerService.add_reply(penelope, _("Hey, how you holding up?"))
    $ MessengerService.new_message(penelope, _("Better, thanks to you"))
    $ MessengerService.add_reply(penelope, _("No problem. I'm here for you. Let me know if you need anything else."))
    $ MessengerService.new_message(penelope, _("Thank you! :)"))

    scene v8smcrm99
    with dissolve
    pause 0.75

    scene v8rose1 # TPP. MC sitting on his bed in his room (Wolves) and looking at his phone. Neutral expression, mouth closed. If the floor is visible, there should be a few books strewn randomly
    with dissolve
    u "(Should I check how Penelope's doing?)"

    while MessengerService.has_replies(penelope):
        call screen phone
        if MessengerService.has_replies(penelope):
            u "(I should talk to Penelope.)"

label phn_penelope6_done:

    scene v8rose1a # MC looking towards his room door (not visible in the shot) and talking
    with dissolve
    play sound sound.knock

    pause 1.5

    scene v8rose1a
    u "Come in!"

    play sound sound.door_open
    scene v8rose2 # FPP. Chris walks in and is now standing somewhere near MC's bed. Serious expression, mouth open
    with dissolve
    ch "Hey man, you busy?"

    scene v8rose2a # Same as v8rose2 but Chris mouth closed
    with dissolve
    u "Naw, just studying."

    scene v8rose0 # TPP. MC gesturing to his books across the floor, chuckling, mouth closed. Chris chuckling, mouth open
    with dissolve
    ch "Heh! Same, bro."

    scene v8rose2
    with dissolve
    ch "Listen, Ms. Rose is in trouble and needs our help. Some of us are heading over to help her move out of her house. You in?"

    if checkonrose:
        u "(Aww, I knew something was up.)"
    else:
        scene v8rose2a
        with dissolve
        u "Wow, what happened? Of course I'm in."

    scene v8rose2
    with dissolve
    ch "She's having some trouble with her old man. I don't know all the details..."
    ch "...but she sounded very upset when I ran into her a few minutes ago and I said we'd help."

    stop music fadeout 3

    scene v8rose2a
    with dissolve
    u "Let's go!"

    scene v8rose3 # TPP. Location: Ms Rose's house. Imre placing a huge carrying box into a moving truck outside her house (there should be more boxes inside of it already). Aaron walking towards the truck with a box in his hand
    with Fade(0.75, 0.25, 0.75)
    pause 1

    scene v8rose4 # TPP. Shot of MC and Chris standing in front of Rose who is looking upset. Finn can be seen walking towards the entrance with a box in hand
    with dissolve
    pause 1

    scene v8rose5 # FPP. Shot of Rose looking upset, but grateful and forcing a smile, mouth open. She's looking towards Chris (not visible in frame)
    with dissolve
    ro "Thank you so much, boys. I don't know how I'd get this all done before Mr. Rose gets home."

    scene v8rose5a # Same as v8rose5 but mouth closed and she's looking into the camera
    with dissolve
    u "When will he be back?"

    play music "music/msad.mp3" fadein 2

    scene v8rose5b # Rose upset, not smiling anymore and mouth open. She's looking into the camera
    with dissolve
    ro "I... I don't know."

    scene v8rose6 # FPP. Chris looking towards Rose (need not be visible in frame). Serious, empathetic and mouth open
    with dissolve
    ch "Don't worry about it. We'll get you out of here."

    scene v8rose5c # Same as v8rose5b but mouth closed
    with dissolve
    u "We're all here to help. Just tell us what to do."

    scene v8rose5b
    with dissolve
    ro "Um... when you're done in here, there are more boxes in the kitchen."
    ro "I brought what I could from the other rooms..."

    scene v8rose5d # Rose crying but not too much, tears in her eyes, mouth open. She's looking towards Chris (not visible in frame)
    with dissolve
    ro "...the ones I could carry."

    scene v8rose5e # Same as v8rose5d but mouth closed and looking into the camera
    with dissolve
    u "Are you alright, Ms. Rose?"

    scene v8rose5g # Rose touching her cheek as if it hurts and a bruise can be seen on her arm (make that stand out so it can't be missed), mouth open. Tears still in her eyes. She's looking away from the camera as if trying to avoid eye contact
    with dissolve
    ro "I'm alright, th-thank you. It... it's been a long time coming. I just want it to be over with."

    scene v8rose6a # Chris looking into the camera with a shocked and empathetic face, mouth closed
    with dissolve
    pause 0.5

    scene v8rose6
    with dissolve
    ch "Did he hurt you?"

    scene v8rose5d
    with dissolve
    ro "He's had it rough. It's not him. It's..."

    scene v8rose5g # Rose crying (slightly more tears than before but not too much) with her hand trying to wipe the tears, mouth open. She's looking towards Chris (not visible in frame)
    with dissolve
    ro "*Sniff* I don't want to be here anymore. I need to get out before he shows up."

    scene v8rose5e
    with dissolve
    u "Hey, we're here. Nothing's gonna happen to you."

    scene v8rose5h # Same as v8rose5e but mouth open
    with dissolve
    ro "He's just not the same after the accident."

    scene v8rose5e
    with dissolve
    u "(Ms. Rose is so upset, but we also really need to hurry if we're gonna finish this before her husband shows up.)"

    menu:
        "Stay to console her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ consoledRose = True

            u "(This is important. There are enough Wolves to move boxes quickly.)"

            scene v8rose6
            with dissolve
            ch "That's no excuse. You deserve to feel safe in your own home."

            scene v8rose5e
            with dissolve
            u "Yeah, and we're gonna make sure that happens."

            scene v8rose5h
            with dissolve
            ro "Thank you, boys. I know I'll be alright once I'm out of here."

            scene v8rose5d
            with dissolve
            ro "I can't stand to look at these four walls anymore *Sniff*"

            scene v8rose5g
            with dissolve
            ro "The whole place is... tainted!"

            scene v8rose5e
            with dissolve
            u "It won't be long Ms. Rose. We brought our best Wolves."

            scene v8rose6
            with dissolve
            ch "And it's the least we could do after everything you've done for us."
            ch "You're our favorite teacher after all!"

            scene v8rose5
            with dissolve
            ro "Really?"

            scene v8rose5a
            with dissolve
            u "Of course, Ms. Rose!"

            scene v8rose7 # TPP. Shot of Imre carrying a box out of a room that is on the side where MC is standing as opposed to Chris, smiling and mouth open. This box has the flashback pic sticking out of it. Make sure to place this pic in such a way that Rose is visible (at least her face if not fully) but husband's face is not visible. Angle the shot so the part of the pic that's sticking out is visible clearly
            with dissolve
            imre "Mine too!"

            scene v8rose13 # TPP. For context, now Imre is next to Rose. She's reaching her hand to pull the pic out (not close though). Their faces should not be visible, just focus on the box, the pic and her hand.
            with dissolve
            ro "Awww, this was from before the accident. Before everything... How did this happen?"

        "Focus on moving the boxes":
            $ reputation.add_point(RepComponent.BRO)

            u "Don't worry. We'll be out of here in no time."
            u "I'll uh... go and get more boxes."

            scene v8rose5h
            with dissolve
            ro "Thank you *Sniff*"

            scene v8rose8 # TPP. Shot of MC walking into the room (empty handed) Imre is in (the one he's coming out of in v8rose7). For context, there's multiple boxes in the room and one of them is the box with the picture. Imre can be seen standing beside that box (not facing the camera)
            with dissolve
            ro "I can't stand to look at these four walls anymore *Sniff*"

            scene v8rose9 # FPP. (For context, Imre turned to face the MC and they're talking now). Imre serious and mouth open
            with dissolve
            imre "How bad is it?"

            scene v8rose9a # Same as v8rose9 but mouth closed
            with dissolve
            u "Bad. We gotta hurry."

            scene v8rose10 # TPP. Shot of Imre picking up the box with the picture. Make sure that the part of the pic sticking out is clearly visible
            with dissolve
            imre "Here, I'll grab this one and you take that one."

            scene v8rose11 # FPP. Imre and MC walking out of the room with boxes. MC is behind Imre and so he's visible in the shot
            with dissolve
            pause 0.5

            scene v8rose12 # FPP. (For context, MC and Imre are walking back with the boxes towards Chris and Rose in living room. The direction they're coming in from should be such that MC is on the same side to Chris as before so MC can take his previous position) Chris and Rose can be seen talking. Rose is looking upset but forcing a smile, mouth open. Chris smiling, empathetic, mouth open. Imre is not in the frame
            with dissolve
            ch "You're our favorite teacher after all!"
            ro "Really?"

            scene v8rose13
            with dissolve
            imre "Really!"
            ro "Awww, this was from before the accident. Before everything... How did this happen?"

    scene v8rose14 # FPP. Chris gesturing Imre (with the box in hand) to go away without making it too obvious, mouth closed. Imre looking at him, alerted, mouth closed. Might have to get creative with the camera angle to not show the MC in this shot
    with dissolve
    pause 0.5

    u "Maybe talking about it will help. Get it all out."

    scene v8rose5a
    with dissolve
    pause 0.5

    scene v8rose5b
    with dissolve
    ro "Things were so good before the accident. But he..."
    ro "...he's changed so much now. I told him to get rid of that damn motorcycle!"

    scene v8rose5h
    with dissolve
    ro "I took care of him for weeks after the accident. I did everything for him."

    scene v8rose5d
    with dissolve
    ro "He broke both his legs and... They gave him some pain killers. At first I was giving them to him when he needed them..."

    scene v8rose5g
    with dissolve
    ro "...but I had to go back to work and he started..."

    scene v8rose6
    with dissolve
    ch "It's not your fault. He's an adult."

    scene v8rose5e
    with dissolve
    u "And it's still not an excuse for..."

    play sound sound.ring

    scene v8rose5e
    with vpunch
    u "One moment."

    play sound sound.answer_call

    scene v8rose15a # TPP. MC moves to a side away from the convo with Rose and Chris to take a call. He's holding the phone to his head, neutral expression, mouth open
    with dissolve
    u "Hey Lauren, what's up?"

    scene v8rose15 # Same as v8rose15a but MC mouth closed
    with dissolve
    la "Hey [name], you wanna meet up? I've had enough Econ assignments for the day."

    scene v8rose15a
    with dissolve
    u "Listen, I'm in the middle of something..."

    if CharacterService.is_girlfriend(lauren):
        scene v8rose15
        with dissolve
        la "Whatcha doooin?"

        scene v8rose15a
        with dissolve
        u "Helping a... friend."

        scene v8rose15
        with dissolve
        la "OK... talk later I guess?"

        scene v8rose15a
        with dissolve
        u "Yeah, bye."

    else:
        scene v8rose15
        with dissolve
        la "Oh, well let me know if you get time later."

        scene v8rose15a
        with dissolve
        u "Sure, bye."

    play sound sound.answer_call

    scene v8rose5d
    with dissolve
    ro "...been so angry lately."

    scene v8rose5g
    with dissolve
    ro "I thought he was doing better but last night..."

    scene v8rose6
    with dissolve
    ch "You sure you don't want us to call the police? Or someone? Do you have family nearby?"

    scene v8rose5d
    with dissolve
    ro "I'm sure I'll be fine when I get out of here."

    scene v8rose5e
    with dissolve
    u "(Man... her situation is so bad.)"
    u "You don't deserve this Ms. Rose."

    scene v8rose16 # TPP. Chris picks up a box, and starts talking with a commanding voice. Others need not be visible in the shot but make sure the camera angle doesn't show the place where Rose, MC and Chris were standing
    with dissolve
    ch "Let's pick up the pace, Wolves!"

    scene v8rose17 # Same as v8rose7 but there's no pic. Can be photoshopped or spot-rendered
    with dissolve
    imre "Other room's done. Just finishing up here."

    scene v8rose5e
    with dissolve
    u "Told ya we'd take care of you Ms. Rose!"

    scene v8rose5i # Rose wiping her tears off, looking into the camera, smiling/chuckling genuinely and mouth open.
    with dissolve
    ro "I owe you boys some pizza after this!"

    scene v8rose6
    with dissolve
    ch "We're just glad to help, Ms. Rose."

    scene v8rose17
    with dissolve
    imre "And this room is done!"

    stop music fadeout 3

    scene v8rose18 # Shot of Aaron and Finn loading stuff into the truck. The truck should be filled more than in v8rose3
    with dissolve
    pause 1

    scene black
    with Dissolve(2)
    pause 0.3

    jump sun_eve_room