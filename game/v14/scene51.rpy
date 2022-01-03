# SCENE 51: MC tries to steal money from Chloe's room
# Locations: Chloe's room.
# Characters: MC (Outfit: 1), UNKNOWN (Outfit: 1), LINDSEY (Outfit: 1)
# Time: Evening

init python:
    def v14s51_reply1():
        chloe.messenger.newMessage(_("I'm already full on breadsticks... Ugh! Hurry up, [name]. Please?"))
        chloe.messenger.addReply(_("I'll be there as soon as I can, Chloe."))
        chloe.messenger.newMessage(_("I'll give you 10 more minutes. If you're still not here by then, I'm going home."))

    def v14s51_reply2():
        if chloe.relationship.value >= Relationship.FWB.value:
            setattr(store, "chloeSus", chloeSus +1)
        chloe.messenger.newMessage(_("I'm already full on breadsticks... Ugh! Hurry up, [name]. Please?"))
        chloe.messenger.addReply(_("I'll be there as soon as I can, Chloe."))
        chloe.messenger.newMessage(_("I'll give you 10 more minutes. If you're still not here by then, I'm going home."))

label v14s51:
    play music "music/v12/Track Scene 23_1.mp3" fadein 2
    scene v14s51_1 # TPP. Show MC walking into Chloe's room and closing the door behind him, slight smile, mouth closed
    with dissolve

    if v14s50_listen_to_aubrey_lindsey >= 2:
        u "(Listening in for so long definitely cost me a lot of time. I won't be able to look through most of Chloe's stuff, so I really need to prioritize which locations I want to search.)"

    elif v14s50_listen_to_aubrey_lindsey == 1:
        u "(Listening in may have cost me a bit of time, hopefully I'll still have enough to look through most Chloe's stuff, but I definitely won't be able to search everywhere.)"
    
    else:
        u "(I think Lindsey will be able to hold Aubrey off a bit, so hopefully I'll have enough time to look everywhere.)"

    u "(So... where would Chloe keep the money?)"

    scene v14s51_2 # FPP. MC standing in Chloes room, make sure the bedside table, desk drawer, closet, purse, and bed pillow are all in sight.
    with dissolve

    call screen v14s51_room

# This is all for you Oscar ;) 
# -Free roam. There are 5 areas MC can choose from: Bedside table, Desk drawer, Closet, Purse, Underneath pillow -
# -if MC chose to keep listening to Lindsey and Aubrey's conversation more than one time, MC can only choose 2 areas.
# -if MC chose to keep listening to Lindsey and Aubrey's conversation once, MC can only choose 3 areas.
# -if MC chose to go to Chloe's room and did not choose to keep listening, MC can choose 4 areas.
# -Grey out areas that have been checked already, ad grey out all areas when MC has checked all allowed locations, giving them a button to continue-

label v14s51_bedside_table:
    $ freeroam12.add("bedside")
    scene v14s51_bedside_1 # FPP. MC looking at her bedside table, on the table there is a lamp, lip balm, hand lotion, and a pink vibrator.

    u "(No money here. But there is a vibrator.)"

    u "(Pretty basic bedside table for a woman... Wonder how often she uses that thing... Let's search somewhere else.)"

    if v14_date_distraction and len(freeroam12) == 1:
        jump v14s51_text

    else:
        call screen v14s51_room

label v14s51_text:
    if v14_date_distraction and len(freeroam12) == 1:
        scene v14s51_2

        play sound "sounds/vibrate.mp3"

        u "(That's probably Chloe texting me, fuck.)"

        scene v14s51_3 # TPP. Show MC looking at his phone, slight smile, mouth closed.
        with dissolve

        $ chloe.messenger.newMessage(_("Hey, where are you??"), force_send=True)
        $ chloe.messenger.addReply(_("Sorry, I'm running late. The cab broke down, waiting on another."))
        $ chloe.messenger.newMessage(_("I thought you'd already be here? Are you lying to me?"))
        $ chloe.messenger.addReply(_("I'm coming, I promise. Just order your starter."), v14s51_reply1)
        $ chloe.messenger.addReply(_("I'd never lie to you, I'll be there soon."), v14s51_reply2)

        label v14s51_PhoneContinue:
            if chloe.messenger.replies:
                call screen phone
            if chloe.messenger.replies:
                "(I should reply to Chloe.)"
                jump v14s51_PhoneContinue

        scene v14s51_3
        with dissolve

        u "(*Sighs* I can't worry right now about Chloe being angry with me. Back to the search.)"

        call screen v14s51_room

label v14s51_desk_drawer:
    $ freeroam12.add("desk")
    scene v14s51_deskdrawer_1 # FPP. MC looking at Chloe's Desk

    u "(Let's see what's hiding in this drawer.)"

    scene v14s51_deskdrawer_2 # FPP. Show MC opening the drawer of the desk, inside the drawer is a list of passwords, a old video game cartridge, and a family photo of Chloe and her parents with their pet pig.
    with dissolve

    pause

    scene v14s51_deskdrawer_2a # FPP. Same as v14s51_deskdrawer_2, Show MC holding the list of passwords (Can be a blank piece of paper that we put passwords on in photoshop. Username and Password list: AlwaysInMind;07-10-98, Chloe101;ChicksRuleGraysonDrools, ChloChlo;BlondeAndDirty, PrettyKittyChloeXO;ChicksWithDicks (For the Chloe Cucumber Fan club) )
    with dissolve

    u "(A list of Chloe's passwords... This could probably help Lindsey in some way, but I'm not comfortable with something like that.)"

    scene v14s51_deskdrawer_2b # FPP. Same as v14s51_deskdrawer_2a, Show MC now holding the video game cartridge 
    with dissolve

    u "(And what's this? I didn't know Chloe was into old-school video games...? Hmm, that knowledge might come in handy someday...)"

    scene v14s51_deskdrawer_2c # FPP. Same as v14s51_deskdrawer_2b, Show MC holding the family photo with Chloe, her mom, her dad, and the pet pig.
    with dissolve

    u "(This must be Chloe's parents. And she has a pig as a pet? I'm learning a lot about her today...)"

    scene v14s51_deskdrawer_2d # FPP. Same as v14s51_deskdrawer_2c, MC with the photo flipped over, on the back it says Mom, Dad, Chloe and Porkchop with a heart.
    with dissolve

    u "(No money here though, so that's more time wasted. *Sighs*)"

    if v14_date_distraction and len(freeroam12) == 1:
        jump v14s51_text

    else:
        call screen v14s51_room

label v14s51_closet:
    $ freeroam12.add("closet")

    scene v14s51_closet_1 # FPP. MC looking in the open closet, a shoe box in sight on the top shelf.

    u "(A mystery box? Perfect.)"

    scene v14s51_closet_2 # FPP. MC reaching up and grabbing the shoe box.
    with dissolve

    pause 

    scene v14s51_closet_3 # FPP. MC looking down at the shoebox in his hand and taking the lid off.
    with dissolve 

    pause 

    scene v14s51_closet_3a # FPP. Same as v14s51_closet_3, MC holding the opened box with a pair of shoes in them, in between the shoes a stack of cash.
    with dissolve

    if v14_realwolf:
        u "(Jackpot! That's $500, baby! *Laughs*)"
    else:
        u "(Jackpot! That's $900, baby! *Laughs*)"

    u "(I'm here for the money and all, but now that it's in my hands...)"

    u "(Can I really do this to her?)"

    if v14_realwolf:
        menu:
            "Take the $500":
                $ freeroam12stolen.add("cash_large")
                $ lindsey_board.money += 500
                $ chloe_board.money -= 500
                scene v14s51_closet_3b # FPP. Same as v14s51_closet_3a, MC holding the money, the box not in sight
                with fade

                u "(I've come this far already. I'm here to help Lindsey, and that's what I'm going to do.)"

            "Don't take the money":
                scene v14s51_closet_3c # FPP. Same as v14s51_closet_3b, MC putting the lid back on the shoe box.
                with dissolve

                u "(I guess I'm having second thoughts about this... I can't take nearly a thousand dollars from Chloe's private closet. What the fuck was I thinking?)"

    else:
        menu:
            "Take the $900":
                $ freeroam12stolen.add("cash_large")
                $ lindsey_board.money += 900
                $ chloe_board.money -= 900
                scene v14s51_closet_3b # FPP. Same as v14s51_closet_3a, MC holding the money, the box not in sight
                with fade

                u "(I've come this far already. I'm here to help Lindsey, and that's what I'm going to do.)"

            "Don't take the money":
                scene v14s51_closet_3c # FPP. Same as v14s51_closet_3b, MC putting the lid back on the shoe box.
                with dissolve

                u "(I guess I'm having second thoughts about this... I can't take nearly a thousand dollars from Chloe's private closet. What the fuck was I thinking?)"

    if v14_date_distraction and len(freeroam12) == 1:
        jump v14s51_text

    else:
        call screen v14s51_room

label v14s51_purse:
    $ freeroam12.add("purse")
    scene v14s51_purse_1 # FPP. MC standing near the purse and looking at the purse.

    u "(Surely this is too obvious...)"

    scene v14s51_purse_2 # FPP. MC looking down at the purse he is holding in one hand the other hand reaching in the purse.
    with dissolve

    pause 

    scene v14s51_purse_2a # FPP. Same as v14s51_purse_2, MC holding the first item he pulls out which is a random receipt.
    with dissolve

    pause

    scene v14s51_purse_2
    with dissolve 

    pause 

    scene v14s51_purse_2b # FPP. Same as v14s51_purse_2a, MC holding some tampons that he pulled out of Chloe's purse
    with dissolve

    pause

    scene v14s51_purse_2 
    with dissolve

    pause

    scene v14s51_purse_2c # FPP. Same as v14s51_purse_2b, MC holding a stack of cash that he pulled out of Chloe's purse
    with dissolve
    
    u "(Oh shit! Cash in a purse? Who would have thought?)"

    u "($300 is a lot of money... Lindsey really needs it, but ultimately this is my choice.)"

    menu:
        "Take the $300":
            $ add_point(KCT.TROUBLEMAKER)
            $ freeroam12stolen.add("cash_small")
            $ lindsey_board.money += 300
            $ chloe_board.money -= 300

            scene v14s51_purse_2d # FPP. Same as v14s51_purse_2c, MC holding just the money and not the purse
            with dissolve

            u "(If I don't take this money, I could be the reason Lindsey loses this race. I don't want it to be my fault.)"

        "Don't take the money":
            $ add_point(KCT.BOYFRIEND)
            scene v14s51_purse_2
            with dissolve

            u "(I guess my conscience has caught up with me. It doesn't feel right to take it.)"

    if v14_date_distraction and len(freeroam12) == 1:
        jump v14s51_text

    else:
        call screen v14s51_room

label v14s51_pillow:
    $ freeroam12.add("pillow")
    scene v14s51_pillow_1 # FPP. MC standing at the side of her bed looking at her pillow, Next to the pillow sits the teddy bear from the hotel scene in Amsterdam.

    pause 

    scene v14s51_pillow_2 # FPP. Close up of the Teddy bear sitting next to Chloe's pillow.
    with dissolve

    u "Hey, man. You don't have a secret camera in your eye, do you? *Chuckles*"

    u "(Let's fucking hope not.)"

    scene v14s51_pillow_1
    with dissolve

    u "(There could be something under her pillow.)"

    scene v14s51_pillow_3 # FPP. MC starting to lift up the pillow 
    with dissolve

    pause

    scene v14s51_pillow_3a # FPP. Same as v14s51_pillow_3, The pillow laying on a different part of the bed. A diary with a lock on it laying where the pillow was.
    with dissolve 

    pause 

    scene v14s51_pillow_1a # FPP. Same as v14s51_pillow_1, MC holding the Diary with the lock on it.
    with dissolve

    u "(Chloe's diary... Shit. I wonder what secrets are waiting to be found in here.)"

    u "(It's locked but I'm sure it wouldn't be too hard to open, and Lindsey could find something useful to help her win.)"

    u "(But this contains all of Chloe's secrets... Should I take it?)"

    menu:
        "Take Chloe's diary":
            $ add_point(KCT.TROUBLEMAKER)
            $ freeroam12stolen.add("diary")
            scene v14s51_pillow_1a
            with dissolve

            u "(I think Lindsey will appreciate this little bonus item. Plus, I'm curious to see what we'll learn.)"

        "Don't take the diary":
            $ add_point(KCT.BOYFRIEND)
            scene v14s51_pillow_3b # FPP. Same as v14s51_pillow_3a, MC putting the Diary back where it was
            with dissolve

            u "(There's going to be some extremely private things in here... It's best if I leave it.)"
    
    if v14_date_distraction and len(freeroam12) == 1:
        jump v14s51_text

    else:
        call screen v14s51_room

# More stuff for Oscar :D
# -if MC chose to keep listening to Lindsey and Aubrey's conversation more than once and has searched 2 areas
# -Automatic end of free roam

# -if MC chose to keep listening to Lindsey and Aubrey's conversation once, and has searched 3 areas
# -Automatic end of free roam

# -if MC chose to go to Chloe's room and did not keep listening, and has searched all 4 areas

label v14s51_continue:
    play sound "sounds/doorclose.mp3"
    scene v14s51_4 # TPP. Show MC slightly worried, mouth closed

    u "(Huh? What was that?)"

    scene v14s51_5 # FPP. MC looking at the bedroom door.
    with dissolve

    unknown "*Distant chatter*"

    u "(Sounds like some of the girls just got home. I need to get out of here, NOW!)"

    stop music fadeout 3

    play music "music/v14/Track Scene 51_2.mp3" fadein 2

    scene v14s51_6 # TPP. Show MC carefully closing the door behind him as he leaves Chloe's room into the hallway of the Chicks' house, slight worried face, mouth closed.
    with dissolve

    pause 

    scene v14s51_7 # TPP. Show MC shimming along the wall of the hallway, slight worried face, mouth closed.
    with dissolve

    pause 

    scene v14s51_8 # FPP. Show MC looking at a pink door with a sign on it that has fancy lettering reading "Our Secret Place"
    with dissolve

    u "('Our secret place'?)"

    play sound "sounds/lock.mp3"

    scene v14s51_8a # FPP. Same as v14s51_8, Show MC trying to open the pink door.
    with vpunch

    u "(Locked. Damnit! What the hell is in here, though?)"

    scene v14s51_9 # TPP. MC walking down more of the hallway, slight worried face, mouth closed.
    with dissolve

    pause 

    scene v14s51_10 # TPP. Show MC entering into the Chicks' bathroom that has a window in it.
    with dissolve

    pause

    scene v14s51_11 # FPP. Focus in on the shower, the shower glass steamy so that the girl can't see him.
    with dissolve

    unknown "*Whistling badly*"

    u "(Shit, shit, shit!!! There's someone in the shower...) *Whispers* Fuck."

    unknown "Hello? Who's there?"

    u "(OH. SHIT.)"

    unknown "Catie, is it you?"

    u "(Quick! Think of something before she steps out and sees me!)"

    menu:
        "Return to the hallway":
            $ freeroam12.add("kitchen_window")

            u "(Why am I even in here? I need to get the fuck out.)"

            unknown "If it's you, make sure you lock the door this time..."

            u "(These Chicks are wildin'.)"

            scene v14s51_12 # TPP. Show MC pressing his ear to the door he entered listening for chatter. MC slightly worried, mouth closed.
            with dissolve

            u "(I don't hear those girls talking anymore. Maybe I can creep downstairs...)"

            scene v14s51_13 # TPP. Show MC exiting the bathroom and closing the door behind him quietly and carefully, slightly worried face, mouth closed.
            with dissolve

            pause 

            scene v14s51_14 # TPP. MC creeping along the hallway, slightly worried, mouth closed
            with dissolve

            pause

            scene v14s51_15 # TPP. Show MC creeping down the stairs like a ninja, slightly worried, mouth closed.
            with dissolve

            pause

            scene v14s51_16 # FPP. MC looking down the way after he gets to the bottom of the stairs.
            with dissolve

            u "(Okay, now what? Go out the same way we came in? Or try the kitchen?"

            menu:
                "Front door":
                    play sound "sounds/lock.mp3"

                    scene v14s51_17 # FPP. MC Reaching for the front door knob but doesn't grab it.
                    with vpunch

                    unknown "*Muffled chatter*"

                    u "(Fuck me! Whoever that is, it sounds like they're about to come in. Let's try the kitchen!)"

                "Kitchen":
                    scene v14s51_18 # FPP. Show MC in the kitchen, A back door and a window in view.
                    with dissolve

                    pause 0.10
                    
            scene v14s51_18
            with dissolve

            menu:
                "Back door":
                    scene v14s51_19 # FPP. Show MC reaching for the back door knob.
                    with dissolve
                    
                    u "*Whispers* Please be unlocked, please be unlocked..."

                    scene v14s51_20 # FPP. Show MC trying to turn the door knob on the back door
                    with vpunch

                    play sound "sounds/lock.mp3"

                    u "(YOU'RE FUCKING KIDDING ME?! Why is the back door locked?!)"

                    scene v14s51_21 # TPP. Show an Unknown Girl at the entrance of the front door putting her stuff down and looking at her phone too distracted to see MC, slight smile, mouth closed.
                    with dissolve

                    pause

                    scene v14s51_22 # FPP. Show MC looking at the window in the kitchen
                    with dissolve

                    pause

                "Window":
                    scene v14s51_22
                    with dissolve

                    pause 
                    
            scene v14s51_23 # FPP. Show MC trying to pull up the window
            with dissolve

            u "*Grunts* (Come... On...)"

            scene v14s51_23a # FPP. Same as v14s51_23, Show MC pushing the window up as it finally opened.
            with dissolve

            u "(YES! FREEDOM!)"

            scene v14s51_24 # TPP. Show MC climbing out of the window
            with dissolve

            pause 0.25

            scene v14s51_25 # TPP. Close up of MC's leg hitting a small vase that was on the counter
            with vpunch

            u "*Whispers* Damnit..."

            scene v14s51_26 # TPP. Close up of the Vase falling
            with dissolve

            pause 0.25

            play sound "sounds/thud.mp3"

            scene v14s51_26a # TPP. The Vase hitting the floor still in tact not shattered.
            with vpunch

            pause 

            scene v14s51_27 # TPP. Show MC shutting the window he exited through carefully.
            with dissolve

            pause 

            scene v14s51_21a # TPP. Show the unknown girl walking down the hallway, confused look, mouth closed.
            with dissolve

            pause 

            scene v14s51_28 # TPP. Show MC sitting under the window hiding from the unknown girl looking out. She doesn't see him. Unknown girl confused face, mouth closed, MC slight worried face, mouth closed.
            with dissolve

            u "(So lucky that the vase didn't smash... Holy shit.)"

        "Go out the window":
            $ freeroam12.add("bathroom_window")
            scene v14s51_29 # TPP. Show MC Tip-toeing past the steamed up shower glass, slight worried face, mouth closed.
            with dissolve

            u "(I need to get the fuck out this house ASAP! Let's try the window.)"

            unknown "If it's you, make sure you lock the door this time..."

            u "(Lock the door... What do these Chicks get up to in private?)"

            play sound "sounds/thud.mp3"

            scene v14s51_30 # FPP. Show MC looking at the fogged up shower glass. Feint silhouette of a naked lady on the other side.
            with dissolve
            
            unknown "Ow- Fuck! My toe! *Whines* Damn you, shampoo..."
            
            menu:
                "Peek":
                    $ add_point(KCT.TROUBLEMAKER)
                    scene v14s51_31 # FPP. MC peaking over the Shower door, the unknown girl bent over facing away from MC.
                    with dissolve

                    pause 

                    scene v14s51_44 # TPP. Close up of the unknown girls wet naked butt.
                    with dissolve

                    u "(Sheeeeeesh...)"

                    scene v14s51_31a # FPP. Same as v14s51_31, The unknown girl starting to stand up straight.
                    with dissolve

                    pause 

                    scene v14s51_44 # FPP. Show MC looking at the window in the bathroom.
                    with dissolve

                    u "(What a nice little treat... Now it's time to get the fuck out of here.)"

                "Don't peek":
                    $ add_point(KCT.BOYFRIEND)
                    scene v14s51_32
                    with dissolve

                    u "(No time for peeking, [name]. Don't even think about it. FOCUS!)"

            scene v14s51_33 # FPP. Show MC opening the Bathroom window.
            with dissolve

            pause

            scene v14s51_34 # TPP. Show MC climbing down the side of the house carefully, MC slightly worried, mouth closed.
            with dissolve

            pause

            play sound "sounds/slam.mp3"

            scene v14s51_35 # TPP. Close up of the window shut.
            with vpunch

            u "(Fuck! That was loud.)"

            scene v14s51_34
            with dissolve

            u "(And it's not over yet... I need to get down without breaking my legs.)"

            scene v14s51_36 # TPP. Show MC touching the ground as he climbs down.
            with dissolve

            u "*Grunts* (This better... have been... worth it...) *Panting*"

            scene v14s51_37 # TPP. Show MC standing on the side of the house, his facial expressio showing he is relieved, mouth open.
            with dissolve

            u "Phew!"

    scene v14s51_38 # TPP. Show MC standing at the back of this Chicks house looking at his phone, slight smile, mouth closed.
    with dissolve

    stop music fadeout 3

    play music "music/v13/Track Scene 21.mp3" fadein 2

    u "(And now, a quick text to Lindsey...)"

    $ lindsey.messenger.addReply(_("I'm around the back of the house. Come quick!"))
    $ lindsey.messenger.newMessage(_("OMW!"))

    label v14s51Lindsey_PhoneContinue:
        if lindsey.messenger.replies:
            call screen phone
        if lindsey.messenger.replies:
            "(I should reply to Lindsey.)"
            jump v14s51Lindsey_PhoneContinue

    if v14_date_distraction:
        play sound "sounds/vibrate.mp3"

        u "(Uh oh... it's a message from Chloe...)"
        $ chloe.messenger.newMessage(_("What the hell is going on?!"), force_send=True)
        $ chloe.messenger.newMessage(_("[name]??? I'm about to order food to go"))
        $ chloe.messenger.newMessage(_("Well, you were right. The food was to die for. You fucking prick."))

        label v14s51Chloe_PhoneContinue:
            if chloe.messenger.replies:
                call screen phone
            if chloe.messenger.replies:
                "(I should reply to Chloe.)"
                jump v14s51Chloe_PhoneContinue

    scene v14s51_39 # FPP. Show Lindsey walking up to MC, slight smile, mouth closed.
    with dissolve

    pause

    scene v14s51_40 # FPP. Show Lindsey standing infront of MC, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth closed.
    with dissolve

    pause 0.25

    scene v14s51_41 # TPP. Show Lindsey and MC hugging, both slight smile, mouth closed.
    with dissolve

    pause 0.25

    scene v14s51_40a # FPP. same as v14s51_40, Lindsey slight smile, mouth open.
    with dissolve 

    li "*Whispers* Thank God that's over!"

    if "bathroom_window" in freeroam12:
        li "*Whispers* What was that loud bang?! Was that you?"

        scene v14s51_40
        with dissolve

        u "*Whispers* Yeah, that was me risking my life by jumping out of the bathroom window!"

        scene v14s51_40a
        with dissolve

        li "*Whispers* Oh shit..."

        scene v14s51_40
        with dissolve

        u "*Whispers* Oh shit is right, haha."

        scene v14s51_40a
        with dissolve

        li "*Whispers* Aubrey heard it."

        scene v14s51_40
        with dissolve

        u "Oh..."

        scene v14s51_40a
        with dissolve

        li "I thought it must have been you, so I just said something about how I think we've got a nest of pigeons."

        li "I always hear them banging like that."

        scene v14s51_40
        with dissolve

        u "*Whispers* Fucking pigeons."

        scene v14s51_40a
        with dissolve

        li "*Quiet laugh* *Whispers* I'm glad you survived."

        scene v14s51_40
        with dissolve

        u "*Whispers* Yeah, just about."

    if "kitchen_window" in freeroam12:
        scene v14s51_40a
        with dissolve

        li "*Whispers* Happy to see you survived!"

        scene v14s51_40
        with dissolve

        u "*Whispers* Yeah, my body is intact, but my nerves are shot."

        scene v14s51_40a
        with dissolve

        li "*Quiet chuckle* *Whispers* I'm proud of you."

    if not ("cash_large" in freeroam12stolen or "cash_small" in freeroam12stolen) and "diary" in freeroam12stolen:
        scene v14s51_40c # FPP. Same as v14s51_40, Lindsey slight frown, mouth closed.
        with dissolve

        u "*Whispers* I'm sorry, but I didn't find any money."

        scene v14s51_40d # FPP. same as v14s51_40a, Lindsey slight frown, mouth open.
        with dissolve

        li "*Whispers* Seriously? Ugh! She must have hidden it somewhere insane."

        scene v14s51_40c
        with dissolve

        u "*Whispers* Yeah, I did my best. Sorry, Linds."

        scene v14s51_40d
        with dissolve

        li "*Whispers* I know, yeah... My campaign is really going to suffer without that money."

        scene v14s51_40c
        with dissolve

        u "*Whispers* Well, I did find this..."

        scene v14s51_40a
        with dissolve

        li "*Whispers* Chloe's diary?!"

        scene v14s51_40
        with dissolve

        u "*Whispers* It might have some useful information for you."

        scene v14s51_40d
        with dissolve

        li "*Whispers* True. That's a great idea, [name]. Thanks for getting this at least. Really sucks about the money though."

        scene v14s51_40c
        with dissolve

        u "*Whispers* Yeah. I know, I'm really sorry."

        u "*Whispers* I should really get home now, though. Getting a little tired."

        scene v14s51_40d
        with dissolve

        li "*Whispers* Yeah, okay. Thanks again. See you..."

        scene v14s51_42 # TPP. Show MC walking away from Lindsey, MC Neutral face, mouth closed, Lindsey in the background, Lindsey slight frown, mouth closed.
        with dissolve

    elif not ("cash_large" in freeroam12stolen or "cash_small" in freeroam12stolen):
        scene v14s51_40c
        with dissolve

        u "*Whispers* I'm so sorry, Linds. I didn't find anything."

        scene v14s51_40d
        with dissolve

        li "*Whispers* What? How?! That money must be in her room somewhere, [name]."

        scene v14s51_40c
        with dissolve

        u "*Whispers* I don't know what to say. I did my best... I'm sorry"

        scene v14s51_40d
        with dissolve

        li "*Whispers* I'm sure you did, [name], but that doesn't help my campaign. *Sighs*"

        li "Thanks for trying anyway."

        scene v14s51_40c
        with dissolve

        u "*Whispers* I should really get home now, though. Getting a little tired."

        scene v14s51_40d
        with dissolve

        li "*Whispers* Yeah, okay. Thanks again. See you..."

        scene v14s51_42
        with dissolve

    else: #if take money
        scene v14s51_40
        with dissolve

        u "*Whispers* Here's what I managed to find."

        scene v14s51_40b # FPP. Same as v14s51_40a, Lindsey full smile, mouth open.
        with dissolve

        li "*Whispers* This is... amazing! This is going to help tremendously, [name]! You're incredible."

        scene v14s51_41
        with dissolve

        pause 0.25

        scene v14s51_40
        with dissolve

        u "*Whispers* So it was worth risking my life for, then?"

        scene v14s51_40a
        with dissolve

        li "*Whispers* Of course! *Chuckles*"

        if "diary" in freeroam12stolen:
            scene v14s51_40
            with dissolve

            $ grant_achievement("grand_theft_chloe")

            u "*Whispers* I also found this..."

            scene v14s51_40a
            with dissolve

            li "*Whispers* What's that- Wait, Chloe's... diary?"

            scene v14s51_40
            with dissolve

            u "*Whispers* Yeah. You might find something useful there, but it is locked."

            scene v14s51_40a
            with dissolve

            li "*Whispers* I'm sure I can get it open; this is crazy!"

            scene v14s51_40
            with dissolve

            u "*Whispers* Your best friend, the janitor, can probably help."

            scene v14s51_40a
            with dissolve

            li "*Whispers* True, he probably can."

        scene v14s51_40
        with dissolve

        u "*Whispers* Anyways, I better get home. I'm getting a little tired after all that, haha."

        scene v14s51_40a
        with dissolve

        li "*Whispers* Okay. Thank you, [name]. I really mean it. You did an amazing job."

        scene v14s51_40
        with dissolve

        u "*Whispers* Anytime, Linds."

        if lindsey.relationship.value >= Relationship.FWB.value:
            play sound "sounds/kiss.mp3"

            scene v14s51_43 # FPP. Lindsey kissing MC on the lips
            with dissolve
            
            pause 1.75

        else:
            play sound "sounds/kiss.mp3"

            scene v14s51_43a # FPP. Same as v14s51_43, Lindsey kissing MC on the cheek
            with dissolve

            pause 1

        scene v14s51_42a # FPP. Same as v14s51_42, Lindsey slight smile, mouth closed.
        with dissolve
    
        pause 0.75

    stop music fadeout 3
    
    if joinwolves:
        jump v14s52

    else:
        jump v14s53