# SCENE 16: Your Room Thus Night
# Locations: MC Apes/Wolves Room, Emily's Dorm
# Characters: MC (Outfit 1), Emily (Outfit 4)
# Time: Thursday Night
# Kiwii Images: v9emiKiwii (Emily's Cleavage)

init python:
    def v9s16_reply1():
        lindsey.messenger.newMessage(_("I see you're still riding high from that fight"))
        lindsey.messenger.addReply(_("Maybe a little. But I'm still happy you texted"))
        lindsey.messenger.newMessage(_("I just wanted to say goodnight... and I was thinking about you"))
        lindsey.messenger.addReply(_("I'll definitely be thinking about you now instead of sleeping ;)"))
        lindsey.messenger.newMessage(_("Can I text you before the Brawl?"))
        lindsey.messenger.addReply(_("YES! Can't wait. Goodnight to you too"))
        lindsey.messenger.newMessage(_("Goodnight"))

    def v9s16_reply2():
        lindsey.messenger.newMessage(_("Yeah, just wanted to say hi. I was thinking about you"))
        lindsey.messenger.addReply(_("Oooh, anything interesting? ;)"))
        lindsey.messenger.newMessage(_("A little ;)"))
        lindsey.messenger.addReply(_("Do tell!"))
        lindsey.messenger.newMessage(_("Maybe after the Brawl... if you win"))
        lindsey.messenger.addReply(_("I sure will now!"))
        lindsey.messenger.newMessage(_("Fingers crossed. Goodnight!"))
        
    def v9s16_reply3():
        lindsey.messenger.newMessage(_("I was thinking about you"))
        lindsey.messenger.addReply(_("Oh? Anything fun?"))
        lindsey.messenger.newMessage(_("Maybe ;)"))
        lindsey.messenger.addReply(_("I'd love to hear more"))
        lindsey.messenger.newMessage(_("What do you think about me checking on you again tomorrow?"))
        lindsey.messenger.addReply(_("I think I should get punched more often!"))
        lindsey.messenger.newMessage(_("You're so sweet, goodnight :)"))
        lindsey.messenger.addReply(_("Goodnight"))

    def v9s16_reply4():
        lindsey.messenger.newMessage(_("I just couldn't stop worrying about you"))
        lindsey.messenger.addReply(_("That's very nice of you"))
        lindsey.messenger.newMessage(_("Can I check on you again tomorrow?"))
        lindsey.messenger.addReply(_("Sure! Anytime"))
        lindsey.messenger.newMessage(_("Good, maybe we can meet up, let me get a good look at you before the Brawl"))
        lindsey.messenger.addReply(_("I'd love too!"))
        lindsey.messenger.newMessage(_("Great, goodnight :)"))
        lindsey.messenger.addReply(_("Goodnight"))

    def v9s16_reply5():
        emily.messenger.newImgMessage("images/v9/scene 16/v9emiKiwii.webp")
        emily.messenger.addReply(_("Be right there!"))
        emily.messenger.newMessage(_("See you soon!"))

    def v9s16_reply6():
        emily.messenger.newImgMessage("images/v9/scene 16/v9emiKiwii.webp")
        emily.messenger.addReply(_("Be right there!"))

label v9_room_thur_night:

    if joinwolves:
        scene v9emi1 # TPP. Show MC sat on his bed in his Wolves room, looking tired.
        with fade

        u "(Whew, glad to be alone... finally)"

        if CharacterService.is_fwb(emily):
            scene v9emi1a # TPP. Same camera as v9emi1, MC now on his phone on his bed.
            with dissolve

            play sound "sounds/vibrate.mp3"

            u "(Ugh, now what.)"

            $ emily.messenger.newMessage(_("I'm bored. Come hang out."), force_send=True)
            $ emily.messenger.addReply(_("Sure! Gimme a sec."))
            $ emily.messenger.addReply(_("It's kinda late"), v9s16_reply5)

            label s16_PhoneContinueW:
                if emily.messenger.replies:
                    call screen phone
                if emily.messenger.replies:
                    u "(I should reply to Emily.)"
                    jump s16_PhoneContinueW

            scene v9emi2 # TPP. Show MC getting up from his bed and leaving his Wolves room.
            with dissolve

            pause 1

            jump v9_emily_dorm

        else:
            jump v9_thur_night_aft_em_w
            
    else:
        scene v9emi4 # TPP. Show MC sat on his bed in his Apes room, looking tired.
        with dissolve

        u "(Whew, glad to be alone... finally)"

        if CharacterService.is_fwb(emily):
            scene v9emi4a # TPP. Same camera as v9emi4, MC now on his phone on his bed.
            with dissolve

            play sound "sounds/vibrate.mp3"

            u "(Ugh, now what.)"

            $ emily.messenger.newMessage(_("I'm bored. Come hang out."), force_send=True)
            $ emily.messenger.addReply(_("Sure! Gimme a sec."))
            $ emily.messenger.addReply(_("It's kinda late"), v9s16_reply6)
            
            label s16_PhoneContinueA:
                if emily.messenger.replies:
                    call screen phone
                if emily.messenger.replies:
                    u "(I should reply to Emily.)"
                    jump s16_PhoneContinueA

            scene v9emi5 # TPP. Show MC getting up from his bed and leaving his Apes room.
            with dissolve

            pause 1

            scene black
            with dissolve

        else:
            jump v9_thur_night_aft_em_a        

label v9_emily_dorm:
    scene v9emi7 # TPP. Show MC knocking on Emily's dorm door.
    with fade

    play sound "sounds/knock.mp3"

    pause 0.8

    scene v9emi8 # FPP. Show Emily who has just opened the door, Emily smile, mouth closed.
    with dissolve

    u "Bedtime?"

    scene v9emi8a # FPP. Same camera as v9emi8, Emily smile, mouth open.
    with dissolve

    em "I couldn't sleep."

    scene v9emi8
    with dissolve

    u "Yeah, me neither."

    pause 0.8

    scene v9emi9 # TPP. Show MC and Emily walking towards Emily's bed.
    with dissolve

    pause 0.8

    scene v9emi10 # TPP. Show MC and Emily sat on the edge of Emily's bed.
    with dissolve

    pause 0.8

    if hl_punch:
        scene v9emi11 # FPP. Show Emily now sat on bed, smile, mouth open.
        with dissolve

        em "Boxer's high?"

        scene v9emi11a # FPP. Same camera as v9emi11, smile, mouth closed.
        with dissolve

        u "You could say that."

    else:
        scene v9emi11b # FPP. Same camera as v9emi11, neutral expression, mouth open.
        with dissolve

        em "I was worried about you."

        scene v9emi11c # FPP. Same camera as v9emi11, neutral expression, mouth closed.
        with dissolve

        u "(Aw, great. Pity.)"

        u "I'm alright. Just more attention than I'd like."

        scene v9emi11b
        with dissolve

        em "I can imagine. It'll blow over, though."

        scene v9emi11c
        with dissolve

        u "That's what I said. I sure hope we're right."


    u "So what have you been up to? Haven't seen much of you lately."

    scene v9emi11
    with dissolve
    
    if emilyArcade > 0:
        em "Not since I kicked your ass at the arcade!"

        scene v9emi11a
        with dissolve

        menu:
            "Let Emily gloat":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "You're just so much better than me."

                scene v9emi11
                with dissolve

                em "I think you bring out the best in me. I was at the top of my game."

                scene v9emi11a
                with dissolve

                u "Does that mean I still owe you that last bet?"

                scene v9emi11
                with dissolve

                em "Oh yeah! And what was that again?"

                scene v9emi11a
                with dissolve

                u "Oral."

                scene v9emi11
                with dissolve

                em "Pretty sure it was a kiss."

                scene v9emi11a
                with dissolve

                u "That's oral."

                scene v9emi11d # FPP. Same camera as v9emi11, flirty expression, mouth open.
                with dissolve

                em "You always were a slick one, [name]."

            "Say you were winning":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "I was one second away from the holy grail."

                scene v9emi11e # FPP. Same camera as v9emi11, smug expression, mouth open.
                with dissolve

                em "Remind me again what that final bet was?"

                scene v9emi11a
                with dissolve

                u "Oral."

                scene v9emi11
                with dissolve

                em "Close, but no."
    
    scene v9emi11a
    with dissolve

    u "So you can't sleep, huh? I know a surefire remedy for that."

    scene v9emi11d
    with dissolve

    em "Why do you think I texted you?"

    scene v9emi11f # FPP. Same camera as v9emi11, flirty expression, mouth closed.
    with dissolve

    u "My oral skills."

    scene v9emi11d
    with dissolve

    em "Exactly."

    scene v9emi12 # TPP. Show MC and Emily kissing.
    with dissolve

    play sound "sounds/kiss.mp3"

    u "Mmmm."

    if hl_punch:
        scene v9emi11d
        with dissolve

        em "Am I still a good kisser??"

        scene v9emi11f
        with dissolve

        u "Very much."

        scene v9emi11d
        with dissolve

        em "Good. More where that came from. Gotta get some while I can. You're very popular... Rocky."

        play sound "sounds/kiss.mp3"

        scene v9emi12
        with dissolve

        pause 1

        scene v9emi11f
        with dissolve

        menu:
            "Make a move on Emily":
                u "(This feels like the right time)"

            "Head home":
                scene v9emi37 # TPP. Show MC walking towards the exit of Emily's room, Emily in view still sat on the bed, cheeky grin, mouth open, MC smile, mouth closed.
                with dissolve

                u "Anyways, I should probably head home."
                $ renpy.end_replay()

                if joinwolves:
                    jump v9_thur_night_aft_em_w

                else:
                    jump v9_thur_night_aft_em_a         

        menu:
            "Brag":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "I guess that makes you my Adrian."

                scene v9emi11d
                with dissolve

                em "And how does Rocky want Adrian to reward her big, strong man?"

                scene v9emi11f
                with dissolve

                u "Pretty sure they have a standing agreement. One BJ per KO."

                scene v9emi11
                with dissolve

                em "Well, in that case..."

            "Play it off":
                $ reputation.add_point(RepComponent.BRO)

                u "Aww, you don't have anything to worry about. One punch isn't gonna change me."

                scene v9emi11d
                with dissolve

                em "Don't be so sure about that. I heard some girls talking in the hallway. You're a hot commodity."

                scene v9emi11f
                with dissolve

                u "For a day maybe, nothing more."

                scene v9emi11d
                with dissolve

                em "Then I suppose the clock's ticking on your prize."

                scene v9emi11f
                with dissolve

                u "What prize?"

                scene v9emi11d
                with dissolve

                em "What would you like the prize to be?"

                scene v9emi11f
                with dissolve
                
                u "You always gave amazing BJs."

                scene v9emi11d
                with dissolve

                em "Because you always made so much noise. Let me know I was doing a good job."

                scene v9emi11f
                with dissolve

                u "Great job."

    else:
        scene v9emi11b
        with dissolve

        em "Am I hurting you?"

        scene v9emi11c
        with dissolve

        u "No!"

        scene v9emi11b
        with dissolve

        em "Are you sure? Looked like you got hit pretty hard."

        scene v9emi11c
        with dissolve

        menu:
            "Make a move on Emily":
                u "(This feels like the right time)"

            "Head home":
                scene v9emi37 # TPP. Show MC walking towards the exit of Emily's room, Emily in view still sat on the bed, cheeky grin, mouth open, MC smile, mouth closed.
                with dissolve

                u "Anyways, I should probably head home."
                $ renpy.end_replay()

                if joinwolves:
                    jump v9_thur_night_aft_em_w

                else:
                    jump v9_thur_night_aft_em_a         

        menu:
            "Be macho":
                $ reputation.add_point(RepComponent.BRO)

                u "I've been training. Gotta learn to take a punch as much as land one."

                scene v9emi11b
                with dissolve

                em "I'll be gentle."

                scene v9emi11c
                with dissolve

                u "Don't. I'm pumped up for a rematch. I'll find that guy and kick his ass."

                scene v9emi11
                with dissolve

                em "Fine, then I won't be gentle."

            "Be dismissive":
                u "Yeah, it was a lucky shot, but I'm good."

                scene v9emi11d
                with dissolve

                em "I remember how good you are."

                scene v9emi11f
                with dissolve

                u "Mmmm. You too."

                scene v9emi11d
                with dissolve

                em "If you think you can handle it, I'd like to get another fix."

                scene v9emi11f
                with dissolve

                u "I could be in a coma and still get hard when you come in the room."

                scene v9emi11d
                with dissolve

                em "What are we gonna do with that?"

                scene v9emi11f
                with dissolve

                u "Whatever you want."

    scene v9emi13 # FPP. Show Emily getting on her knees infront of MC beginning to pull his pants down, looking up at camera, seductive expression, mouth closed.
    with dissolve

    pause 1

    scene v9emi13a # FPP. Same camera as v9emi13, on her knees on the floor looking up at camera, seductive expression, Emily mouth closed.
    with dissolve

    u "Oh God. I've missed this."

    play music "music/v9/Track Scene 16.mp3" fadein 2

    scene v9emi13b # FPP. Same camera as v9emi13, on her knees on the floor looking up at camera, seductive expression, Emily mouth open.
    with dissolve

    em "You ain't seen nothing yet."

    image v9emibj = Movie(play="images/v9/Scene 16/v9emibj.webm", loop=True, image="images/v9/Scene 16/v9emibjStart.webp", start_image="images/v9/Scene 16/v9emibjStart.webp") # FPP. Emily on her knees giving MC a blowjob who is sat on the edge of Emily's bed.
    image v9emibjf = Movie(play="images/v9/Scene 16/v9emibjf.webm", loop=True, image="images/v9/Scene 16/v9emibjStart.webp", start_image="images/v9/Scene 16/v9emibjStart.webp")

    image v9emimi = Movie(play="images/v9/Scene 16/v9emimi.webm", loop=True, image="images/v9/Scene 16/v9emimiStart.webp", start_image="images/v9/Scene 16/v9emimiStart.webp") # TPP. MC and Emily, missionary, camera from the side, try and show as much action as possible.
    image v9emimif = Movie(play="images/v9/Scene 16/v9emimif.webm", loop=True, image="images/v9/Scene 16/v9emimiStart.webp", start_image="images/v9/Scene 16/v9emimiStart.webp")

    image v9emicg = Movie(play="images/v9/Scene 16/v9emicg.webm", loop=True, image="images/v9/Scene 16/v9emicgStart.webp", start_image="images/v9/Scene 16/v9emicgStart.webp") # FPP. Show Emily riding MC's penis (cowgirl). First person perspective as if MC is looking at her whilst lying down.
    image v9emicgf = Movie(play="images/v9/Scene 16/v9emicgf.webm", loop=True, image="images/v9/Scene 16/v9emicgStart.webp", start_image="images/v9/Scene 16/v9emicgStart.webp")

    image v9emian = Movie(play="images/v9/Scene 16/v9emian.webm", loop=True, image="images/v9/Scene 16/v9emianStart.webp", start_image="images/v9/Scene 16/v9emianStart.webp") # TPP. MC and Emily, doggy style Anal show as much action as possible.
    image v9emianf = Movie(play="images/v9/Scene 16/v9emianf.webm", loop=True, image="images/v9/Scene 16/v9emianStart.webp", start_image="images/v9/Scene 16/v9emianStart.webp")

    if is_censored:
        call screen censored_popup("v9s16_nsfwSkipLabel1")

    show screen v9s16_emilySexOverlay

label v9s16_emilyBlowjob:
    scene v9emibj
    with dissolve
    pause 

    u "Fuck, that's amazing."
    em "Mhmmmm..."
    u "Moans* Ahhh... This is so good, go faster!"

    scene v9emibjf
    with dissolve
    pause

    u "Oh wowwww!"
    em "*Suck* *Suck*"
    u "(I'm gonna blow if I don't do something.)"

    scene v9emi13c
    with dissolve

    pause 1

    scene v9emi14 # TPP. Show MC pulling Emily from the floor back on to the bed, both smiling, mouth closed.
    with dissolve

    pause 1

    scene v9emi15 # TPP. Show MC lying Emily down onto the bed, MC sat near Emily's legs, MC removing his shirt.
    with dissolve
    
    pause 1

    scene v9emi16 # FPP. Show Emily, now lying down looking up into the camera, Emily seductive expression, mouth open.
    with dissolve

    em "Aww, I was enjoying that."

    scene v9emi16a # FPP. Same camera as v9emi16, Emily seductive expression, mouth closed.
    with dissolve

    u "So was I... way too much!"

    scene v9emi17 # FPP. Show Emily removing her top.
    with dissolve
    
    pause 1

    # scene v9emi18 # FPP. Same camera as v9emi16 (different number due to change of clothing), Emily seductive expression, mouth closed.
    # with dissolve

    # u "My turn."

    scene v9emi19 # TPP. Show MC removing Emily's shorts, emily turned on expression, both mouths closed.
    with dissolve

    em "Mmmm."

    scene v9emi20 # TPP. Show MC spreading Emily's legs, knees up.
    with dissolve

    pause 1

    scene v9emi23 # FPP. Show Emily looking at camera, Emily, flirty grin, mouth open.
    with dissolve

    em "I want you inside me. Now."

    scene v9emi23a # FPP. Same camera as v9emi23, Emily flirty grin, mouth closed.
    with dissolve

    u "You ready?"

    scene v9emi23
    with dissolve

    em "YES!"

label v9s16_emilyMissionary:
    scene v9emi24 # TPP. Show MC getting into missionary with Emily, Emily biting her lip slightly. MC penis just outside of Emily's pussy.
    with dissolve

    pause 1

    scene v9emi24a # TPP. Same camera as v9emi24, MC penis now fully inside Emily.
    with vpunch

    em "Ahhhh!"

    scene v9emimi
    with dissolve
    pause

    u "Mmmm. You're so wet."
    em "*Moan* Ahhhhh you feel so good."

    scene v9emimif
    with dissolve
    pause

    em "*Moans* Ahhhh keep going!"
    em "*Moans Louder* Oh god [name] you're so fucking goooood!!"
    u "*Groans* Mhmmm fuck."

    scene v9emi25 # TPP. Show MC lying down and Emily mounting over him, Emily holding MC's penis whilst sat above MC's penis.
    with dissolve

    pause 0.75

    scene v9emi26 # FPP. Show Emily, Emily seductive smile, mouth open.
    with dissolve

    em "I wanna ride you."

    scene v9emi26a # FPP. Same camera as v9emi26, Emily seductive smile, mouth closed.
    with dissolve

    u "Please do."

    scene v9emi27 # FPP. Close up of Emily's vagina on the tip of MC's penis.
    with dissolve

    pause 1

label v9s16_emilyCowgirl:
    scene v9emi27a # FPP. Same camera as v9emi27, Emily now fully sat on MC's penis.
    with vpunch

    em "*Moans* [name] I've missed your cock so much!"

    scene v9emicg
    with dissolve
    pause

    u "*Groan* This feel so good."
    em "*Moans* Ahhhhhh..."
    em "Fuck me harder [name]!"

    scene v9emicgf
    with dissolve
    pause

    em "Fuuuuuuck!!"
    em "Can I cum now? Please? God, it's so good."

    scene v9emi28 # FPP. Show Emily sat on MC's dick, Emily looking into camera, pleasured expression, mouth closed.
    with dissolve

    u "Not yet. I have an idea."

    scene v9emi28a # FPP. Same camera as v9emi28, Emily pleasured expression, mouth open.
    with dissolve

    em "Are you thinking what I'm thinking?"

    scene v9emi28
    with dissolve

    u "I sure hope so."

    scene v9emi29 # TPP. Show MC grabbing Emily's waist and lays her back onto the bed.
    with dissolve

    pause 1

    scene v9emi30 # FPP. Show Emily lying back down on the bed on her back, camera as if MC is sat inbetween Emily's legs. Emily looking at camera, smile, mouth closed.
    with dissolve

    u "Flip over and lay flat."

    scene v9emi30a # FPP. Same camera as v9emi30, Emily now flips over so she is lying on her stomach.
    with dissolve

    em "Like this?"

    u "Perfect."

label v9s16_emilyDoggy:
    scene v9emi31 # TPP. Show MC grabbing Emily's waist from behind and lifting her up so she is in a doggy style position.
    with dissolve
    
    pause 1

    scene v9emi32 # FPP. Close up of MC's penis about to enter Emily's ass.
    with dissolve

    pause 0.75

    scene v9emi32a # FPP. Same camera as v9emi32, MC's penis now inside Emily's ass.
    with vpunch
    
    em "OH FUUUCK!!"

    scene v9emian
    with dissolve
    pause

    u "Ahhhh."
    em "Oh, wow. Oh my God."
    u "You like it?"
    em "It feels so good. I'm gonna cum."

    scene v9emianf
    with dissolve
    pause

    em "*Moans* Ohhh. Now. Now!"
    u "Cum for me!"
    em "*Moans Louder* Ahhhh!!"

    scene v9emi32b # FPP. Same camera as v9emi32, MC's penis outside of Emily's ass with cum dripping from Emily's ass.
    with flash

    pause 0.5

    scene v9emi32b
    with flash

    pause 1

    hide screen v9s16_emilySexOverlay

    scene v9emi33 # TPP. Show MC and Emily lying next to eachother on Emily's bed. Both looking tired.
    with Fade(0.75, 0.25, 0.75)

    pause 1

    scene v9emi34 # FPP. Show Emily, tired smile, mouth open.
    with dissolve

    em "You've learned a few tricks, college boy."

    scene v9emi34a # FPP. Same camera as v9emi34, tired smile, mouth closed.
    with dissolve

    u "That thing you did with your mouth. I almost blew my load right away."

    scene v9emi34
    with dissolve

    em "I'll have to remember that for next time."

    $ renpy.end_replay()

    scene v9emi34a
    with dissolve

    u "Please do. Are you okay? I didn't hurt you, did I?"

    scene v9emi34
    with dissolve

    em "No, I'm great. I can't believe I came that way. It was so intense."

    scene v9emi34a
    with dissolve

    u "Well, if you ever want a repeat, I'm your man."

    scene v9emi34b # FPP. Same camera as v9emi34, Emily giggle, mouth open.
    with dissolve

    em "You and your sex kill switch."

    scene v9emi34a
    with dissolve

    u "It was so good. You wore me out."

    label v9s16_nsfwSkipLabel1:
    scene v9emi35 # TPP. Show MC and Emily now sat on the edge of Emily's bed, both fully dressed, MC and Emily kissing.
    with fade

    pause 0.75

    scene v9emi36 # FPP. Show Emily, Emily smile, mouth closed.
    with dissolve

    u "Thank you."

    scene v9emi36a # FPP. Same camera as v9emi36, Emily smile, mouth open.
    with dissolve

    em "Thank you. You heading out?"

    scene v9emi36
    with dissolve

    u "You really did knock me out. I better get to my room."

    scene v9emi36a
    with dissolve

    em "Alright. I'll talk to you tomorrow."

    scene v9emi36
    with dissolve

    u "You really were amazing."

    scene v9emi37 # TPP. Show MC walking towards the exit of Emily's room, Emily in view still sat on the bed, cheeky grin, mouth open, MC smile, mouth closed.
    with dissolve

    em "I know."

    stop music fadeout 3
    
    $ sceneList.add("v9_emily")

    $ CharacterService.set_relationship(emily, Relationship.FWB, mc)
    
    if joinwolves:
        jump v9_thur_night_aft_em_w

    else:
        jump v9_thur_night_aft_em_a

label v9_thur_night_aft_em_w:
    if "v9_emily" in sceneList:
        scene v9emi3 # TPP. Show MC on his bed on his phone looking exhausted.
        with fade

        u "(I'm about to pass out.)"

    else:
        scene v9emi3
        with dissolve

        u "(I need to get some sleep.)"

    if hl_punch:
        $ lindsey.messenger.newMessage(_("How are you doing tonight?"), force_send=True)
        $ lindsey.messenger.addReply(_("Better now that I'm talking to you"), v9s16_reply1)
        $ lindsey.messenger.addReply(_("Super. You getting ready for bed?"), v9s16_reply2)

    else:
        $ lindsey.messenger.newMessage(_("Hey, how you feeling?"), force_send=True)
        $ lindsey.messenger.addReply(_("Better now that I'm talking to you"), v9s16_reply3)
        $ lindsey.messenger.addReply(_("I'm ok, it's really not that bad"), v9s16_reply4)

    label s16_ContinueW1:
        if lindsey.messenger.replies:
            call screen phone
        if lindsey.messenger.replies:
            u "(I should reply to Lindsey.)"
            jump s16_ContinueW1

        

    scene v9emi3a # TPP. Same camera as v9emi3, MC puts his phone down and smiles.
    with dissolve

    pause 1

    scene v9emi3b # TPP. Same camera as v9emi3, MC lies down on his side and starts to go sleep.
    with dissolve

    pause 1

    scene black
    with dissolve

    jump v9_room_fri_morn

label v9_thur_night_aft_em_a:
    if "v9_emily" in sceneList:
        scene v9emi6 # TPP. Show MC on his bed on his phone looking exhausted.
        with fade

        u "(I'm about to pass out.)"

    else:
        scene v9emi6
        with dissolve

        u "(I need to get some sleep.)"

    if hl_punch:
        $ lindsey.messenger.newMessage(_("How are you doing tonight?"), force_send=True)
        $ lindsey.messenger.addReply(_("Better now that I'm talking to you"), v9s16_reply1)
        $ lindsey.messenger.addReply(_("Super. You getting ready for bed?"), v9s16_reply2)

    else:
        $ lindsey.messenger.newMessage(_("Hey, how you feeling?"), force_send=True)
        $ lindsey.messenger.addReply(_("Better now that I'm talking to you"), v9s16_reply3)
        $ lindsey.messenger.addReply(_("I'm ok, it's really not that bad"), v9s16_reply4)

    label s16_ContinueA1:
        if lindsey.messenger.replies:
            call screen phone
        if lindsey.messenger.replies:
            u "(I should reply to Lindsey.)"
            jump s16_ContinueA1

    scene v9emi6a # TPP. Same camera as v9emi6, MC puts his phone down and smiles.
    with dissolve

    pause 1

    scene v9emi6b # TPP. Same camera as v9emi6, MC lies down on his side and starts to go sleep.
    with dissolve

    pause 1

    scene black
    with dissolve

    pause 1

    jump v9_room_fri_morn


