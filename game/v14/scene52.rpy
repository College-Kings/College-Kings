# SCENE 52: If Wolves Night (Nora and Chris Breakup)
# Locations: Wolves Frat House
# Characters: IMRE (Outfit: 2), MC (Outfit: 1), CHRIS (Outfit: 2), SEBASTIAN (Outfit: x), FINN (Outfit: x)
# Time: Night
# Render Count: 19 Unique Renders, 53 Total

init python:
    def v14s52_reply1():
        setattr(store, "v14_noraWhere", True)

    def v14s52_reply2():
        setattr(store, "v14_noraWorry", True)

label v14s52:
    play music "music/v13/Track Scene 40_2.mp3" fadein 2
    scene v14s52_1 # TPP. mc walks up and see's the wolves frat house
    with dissolve

    pause 0.75

    scene v14s52_2 # TPP. MC enters the front door of the Wolves house and Imre is seen in the hallway looking at mc, imre no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s52_3 # FPP. Show Imre looking at Mc, no expression, mouth open
    with dissolve

    imre "Hey, come on. Chris wants to talk to us all."

    scene v14s52_3a # FPP. same as v14s52_3 Imre mouth closesd
    with dissolve

    u "Oh, okay. What about?"

    scene v14s52_3
    with dissolve

    imre "No idea, he just said he needs to talk to all the Wolves about something."

    scene v14s52_3a
    with dissolve

    u "Oh. (Nora? Fight King? What could possibly be happening now?)"

    scene v14s52_4 # TPP. MC follows Imre into the next room, no expressions, mouths closed
    with dissolve

    pause 0.75

    scene v14s52_5 # TPP. In the next room, MC and Imre are standing in the back row by themselves from left to right, Sebastian, Aaron, Finn and Perry are standing in front of them in that order from left to right all of them are looking at Chris standing in front of them, Chris is looking at Mc, no expression, mouth open
    with dissolve

    ch "Thanks for coming, guys. I appreciate that you all made the time to be here together, so that I only have to say this once."

    scene v14s52_6 # FPP. Close up shot of just Chris, no expression, mouth open, looking in the direction of the guys
    with dissolve

    ch "I'm not going to make this a long, drawn out thing."

    scene v14s52_6a # FPP. Chris's mouth is closed
    with dissolve

    u "(This sounds too serious to be about fighting.)"

    scene v14s52_6
    with dissolve

    ch "I know this probably won't come as a shock."

    ch "I mean, it's no secret that Nora and I have been going through a difficult time lately."

    scene v14s52_6a
    with dissolve

    u "(No shit...)"

    scene v14s52_6
    with dissolve

    ch "But we've decided to break up. Officially, for good. I thought you should all know."

    if v13_imre_disloyal:
        scene v14s52_5a # TPP. same as v14s52_5 Mc and Imre are looking at each other, Mc no expression mouth closed Imre has a pissed off expression mouth closed, All the other Wolves have a shocked expression, mouths open, looking at Chris, Chris holding a hand behind his head with a look of disbelief in it himself, looking down and away from the wolves
        with dissolve

        pause 1.25

    else:
        scene v14s52_5b # TPP. same as v14s52_5a All the Wolves have a shocked expression, mouths open, looking at Chris, Chris holding a hand behind his head with a look of disbelief in it himself, looking down and away from the wolves
        with dissolve

        pause 1.25

    scene v14s52_7 # FPP. Show a close up shot of sebastian, Mc is standing behind Sebastian and can see his face from a back right angle, sebastian is looking at chris, no expression, mouth open
    with dissolve

    se "Y-You broke up?"

    scene v14s52_6
    with dissolve

    ch "Yeah."

    scene v14s52_8 # FPP. Show a close up shot of Finn, Mc is standing behind Finn and can see his face from a back left angle, Finn is looking at chris, no expression, mouth open
    with dissolve

    finn "But, you've been together since forever."

    scene v14s52_6
    with dissolve

    ch "I know it's going to be a weird adjustment for everyone. You guys are also used to Nora being around. But we'll be perfectly fine."

    scene v14s52_9 # FPP. show a close up shot of Imre standing to Mc's left, Imre is looking at Chris, no expression, mouth open
    with dissolve

    imre "Is there anything we can do to help?"

    scene v14s52_6
    with dissolve

    ch "Thanks, Imre."

    scene v14s52_9
    with dissolve

    imre "Of course..."

    scene v14s52_6
    with dissolve

    ch "But, no. There's nothing you can do. Nora made it pretty clear how she felt."

    scene v14s52_6
    with dissolve

    ch "She's got a whole list of issues about how I've treated her lately."

    scene v14s52_6
    with dissolve

    ch "I don't think I have to change for her. I shouldn't have to, you know. I'm still the same guy she fell in love with... But whatever."

    scene v14s52_6b # FPP. same as v14s52_6 Chris has a fist in the air, frustrated/angry half smile, mouth open
    with dissolve

    ch "Her fucking loss, right boys?"

    scene v14s52_6a
    with dissolve

    u "(He seems more frustrated or angry than he is sad... I wonder how Nora's doing.)"

    scene v14s52_9a # FPP. same as v14s52_9 Imre has also raised a fist in the air, full smile, mouth open
    with dissolve

    imre "Absolutely."

    scene v14s52_7a # FPP. same as v14s52_7 Sebastian has a full smile, mouth open, looking at chris
    with dissolve

    se "Bros before those hoes! *Laughs*"

    scene v14s52_10 # TPP. Sebastian gives chris a hug, chris and sebastian full smiles mouths closed, Imre and Finn high five Full smiles mouths closed, Perry standing next to Imre and Finn with his hand up waiting for a high five full smile mouth closed, Aaron and mc looking at each other full smile's mc with a hand extended like his explaining something, mc mouth open Aaron mouth closed
    with dissolve

    pause 1.25

    scene v14s52_11 # FPP. close up shot of Aaron face to face with mc, half smile, mouth closed
    with dissolve

    u "People just grow apart sometimes, man. It sucks but I've seen it happen with my parents."

    scene v14s52_11a # FPP. same as v14s52_11 Aaron no expression, mouth open
    with dissolve

    aa "Yeah, mine too."

    scene v14s52_11a
    with dissolve

    aa "You grow up seeing them so happy together and then one day your dad is packing up all his clothes and your mom is screaming at him to get the hell out, ha"

    scene v14s52_6
    with dissolve

    ch "Thankfully there was no screaming or punching involved. We were both really calm about it. Upset obviously, but calm."

    scene v14s52_9
    with dissolve

    imre "Where is she even? I haven't seen her since the airport when we landed home."

    scene v14s52_6a
    with dissolve

    u "(Yeah, Chris. Where is she?)"

    scene v14s52_6c # FPP. same as v14s52_6 Chris looks down and away from the guys
    with dissolve

    ch "Honestly, I uh... I don't want to talk about her anymore for right now."

    scene v14s52_6
    with dissolve

    ch "I just wanted to let you guys know what happened."

    scene v14s52_5c # TPP. same as v14s52_5 Chris is leaving the room, and all the wolves are looking at him leave
    with dissolve

    u "(Something just doesn't feel right about this...)"

    scene v14s52_12 # TPP. close up shot of Mc appearing to be deep in thought, hand on his chin, no expression, mouth closed, looking at the floor
    with dissolve

    u "(Why did he suddenly end the conversation when Imre asked where Nora is? He could have just said...)"

    if "v12_nora" in sceneList: ###addition just in case rs variable was not triggered
        $ nora.relationship = Relationship.FWB

    if nora.relationship >= Relationship.FWB:
        scene v14s52_12
        with dissolve

        u "(I can try to ask him, but I don't want to seem suspicious.)"

        scene v14s52_12
        with dissolve
        menu:
            "Ask Chris about Nora":
                $ chrissus += 1
                $ add_point(KCT.TROUBLEMAKER)

                scene v14s52_12a # FPP. Mc sees chris waling away from him back turned to mc
                with dissolve

                u "(Let's see what he says when I ask him...)"

                scene v14s52_13 # FPP. Chris is seen standing in front of bedroom door, his hand is on the door handle, but does not open it yet, back turned to mc
                with dissolve

                u "Chris, hey."

                scene v14s52_13a # FPP. same as v14s52_13 Chris turns around to face MC, chris is still holding the door handle, looking at mc, no expression, mouth closed
                with dissolve

                u "I, uh, just wanted to personally say that I hope you're doing alright."

                scene v14s52_13a
                with dissolve

                u "You and Nora are both my friends so, I do care, you know?"

                scene v14s52_13b # FPP. same as v14s52_13a Chris has a slight smile, mouth open
                with dissolve

                ch "Yeah, I know. That means a lot, [name]. Thanks man."

                scene v14s52_13a
                with dissolve

                u "Yeah, of course."

                scene v14s52_13c # FPP. same as v14s52_13 Chris has opened the door to his bedroom and starts to go into his room, his back is turned to mc
                with dissolve

                u "By the way, I know you said you didn't want to talk about it but... Is there any way you could tell me where Nora is?"

                scene v14s52_13d # FPP. same as v14s52_13c Chris turns back around and looks at MC a bit confused
                with dissolve

                u "I just feel bad that she doesn't have a friend right now, I guess. Or maybe she does? Do you even know where she's at?"

                scene v14s52_13e # FPP. same as v14s52_13d Chris laughs, looking into the air, slightly angry, mouth open
                with dissolve

                ch "Ha..."

                scene v14s52_13f # FPP. same as v14s52_13e Chris is now looking at mc, mouth closed
                with dissolve

                u "(He's not happy with that question...)"

                scene v14s52_13g # FPP. same as v14s52_13f Chris's mouth is open
                with dissolve

                ch "She told me to leave, never come back, and to not tell a single person where she is."

                scene v14s52_13f
                with dissolve

                u "Oh, wow. That's-"

                scene v14s52_13f
                with dissolve

                u "That's really shitty. I'm sorry. Guess I just wanted to make sure she's safe at least, you know?"

                scene v14s52_13h # FPP. same as v14s52_13f Chris is looking very intently with an eyebrow raised looking at Mc, Chris has taken his hand off the door handle and placed it on his chin, mouth closed, no expression
                with dissolve

                pause 0.75

                scene v14s52_13i # FPP. same as v14s52_13h Chris shakes his head in disbelief of his own thought, slight smile, mouth open
                with dissolve

                pause 0.75

                scene v14s52_13b
                with dissolve

                ch "Yeah, ha. I do know. Or I did. Not anymore."

                scene v14s52_13b
                with dissolve

                ch "Sleep tight, man."

                scene v14s52_13c
                with dissolve

                u "Yeah, you-"

                scene v14s52_13j # FPP. Chris has walked into his bedroom and is no longer visible and the door is shut
                with dissolve

                u "Too."

                scene v14s52_13j 
                with dissolve

                u "(Well, that didn't go great... I wonder if I can get a hold of her myself?)"

            "Go to your room":
                $ add_point(KCT.BRO)

                scene v14s52_12a
                with dissolve

                u "(Not about to put any ideas into his head. I'll find her myself.)"

    scene v14s52_14 # TPP. Mc is seen entering his wolves room, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s52_15 # TPP. Mc is seen sitting at the edge of his bed hands clenched together, propping up his chin, appearing to be in thought, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s52_15
    with dissolve

    u "(I hate to even think about it but... Chris is capable of being violent towards Nora. I witnessed that in Europe.)"

    scene v14s52_15a # TPP. same as v14s52_15 Mc lowers his hands to his lap
    with dissolve

    u "(Is he capable of doing something worse, though?)"

    scene v14s52_15b # TPP. same as v14s52_15a mc makes a fist and hits his other hand palm open with it
    with dissolve

    u "(Fuck... I hope I'm just overthinking this.)"

    scene v14s52_15
    with dissolve

    u "(I'd rather stay out of this shit show, but I feel like I should try to text her.)"

    scene v14s52_16 # TPP. Mc walks over to his study desk and sit's down, worried expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s52_16a # TPP. same as v14s52_16 Mc pull's out his phone and looks at it
    with dissolve

# -remember variable of what he sent for future scene. NoraWorry would be text2 or NoraWhere would be text1

    $ nora.messenger.addReply(_("Hey, Nora. Just checking in since I haven't heard from you in a while... Where are you?"), v14s52_reply1)
    $ nora.messenger.addReply(_("Hey, you. I'm starting to worry that I haven't seen you around. At least let me know that he didn't hurt you... Please text me back, ASAP"), v14s52_reply2)

    label v14s52_PhoneContinueNora:
        if nora.messenger.replies:
            call screen phone
        if nora.messenger.replies:
            u "(I should text Nora.)"
            jump v14s52_PhoneContinueNora

# -regardless of choice, MC exits his texts and puts the phone down on the desk-

    scene v14s52_16b # TPP. same as v14s52_16a Mc puts his phone on the desk, and is looking at it, worried expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s52_16c # TPP. same as v14s52_16b MC stays sitting at his study desk, face in his hands, phone still on the desk
    with dissolve

    pause 0.75

    scene v14s52_16d # TPP. same as v14s52_16c Mc is holding a book with one hand looking at it, with the other hand behind his head holding his neck, his phone is still on the desk
    with dissolve

    pause 0.75

    scene v14s52_16e # TPP. same as v14s52_16d Mc closes the book slamming it on the desk, picking his phone up with his other hand and looking at it, slightly distressed/worried expression
    with dissolve

    pause 0.75

    scene v14s52_16c
    with dissolve

    pause 0.75

    scene v14s52_16b
    with dissolve

    u "*Sighs*"

    play sound "sounds/vibrate.mp3"

    scene v14s52_16a
    with dissolve

    u "Nora...?"

    $ nora.messenger.newMessage("UNABLE TO DELIVER MESSAGE AT THIS TIME, PLEASE TRY AGAIN LATER.", force_send=True)

    call screen phone

    scene v14s52_16f # TPP. same as v14s52_16d Mc now has an angry expression
    with dissolve

    u "(What the fuck does that mean?!)"

    if v13_imre_disloyal:
        scene v14s52_17 # FPP. show a full size image of mc's wolves bedroom door closed
        with dissolve

        pause 0.75

        stop music fadeout 3

        play music "music/v12/Track Scene 1_1.mp3" fadein 2

        scene v14s52_17a # FPP. same as v14s52_17 Imre walks through the door angry expression, mouth closed
        with dissolve

        pause 0.75

        scene v14s52_16g # TPP. same as v14s52_16f Imre is now standing behind Mc looking at mc with an angry expression mouth open, mc is looking at Imre no expression mouth closed, mc is still holding his phone
        with dissolve

        pause 0.75

        scene v14s52_18 # FPP. Show a close up shot of Imre standing over Mc, mc is still sitting, Imre has an angry expression, mouth open
        with dissolve

        imre "Now's the time, [name]. I can't do it anymore."

        scene v14s52_18a # FPP. same as v14s52_18 Imre's mouth is closed
        with dissolve

        u "Do what? What's happening?"

        scene v14s52_18
        with dissolve

        imre "We're going to Chris right now, and you're going to tell him what happened between you and Nora. All of it."

        scene v14s52_18a
        with dissolve

        u "Imre- Imre, wait!"

        scene v14s52_18b # FPP. Imre holds a fist up to mc
        with dissolve

        imre "I'm not listening to any lame-ass excuses either."

        scene v14s52_16h # TPP. same as v14s52_16g Imre slams his fist against the wall, mc and imre looking at each other with angry expressions, mouth's closed
        with hpunch

        pause 0.75

        scene v14s52_17b # FPP. same as v14s52_17a Imre is holding the door open for MC angrily, holding his other hand out towards mc in a come here fashion
        with dissolve

        imre "Come the fuck on, [name]!"

        stop music fadeout 3

        jump end14

    else: 
        scene v14s52_19 # TPP. Show a side view image of just Mc holding his phone in front of his face, looking at his phone, extremely angry expression, mouth open
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump end14