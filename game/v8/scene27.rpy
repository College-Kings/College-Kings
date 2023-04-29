# Monday Evening in Room
# Location: MC Apes Room, MC Wolves Room, Josh's Room
# Outfits: MC Outfit 3 & 2, Josh Outfit1
# Time: Monday Evening

label mon_eve_room_josh:
    if joinwolves:
        scene v8spd1 # TPP. Show MC sat in his Wolves room at his desk on his phone.
        with Fade(0.75, 0.25, 0.75)
        pause 0.5

        play sound "sounds/vibrate.mp3"
        
        u "(Let's see who this is.)"

        if helpJosh:
            $ MessengerService.new_message(josh, _("Hey bro! It's time! Meet me at mine, okay?"), force_send=True)
            $ MessengerService.add_reply(josh, _("Okay, I'm on my way."))

            while MessengerService.has_replies(josh):
                call screen phone
                if MessengerService.has_replies(josh):
                    u "I should really check my phone."

            scene v8spd2 # TPP. Show MC getting up from his desk.
            with dissolve

            pause 0.5

            scene v8spd2a # TPP. Same camera as v8spd2, MC now fully stood up. Show MC removing his jumper, revealing the shirt from Outfit 2, (Back 2 School T, Mat 3).
            with dissolve

            u "(Fuck, I have a bad feeling about this.)"

            scene v8spd3 # TPP. Show MC leaving his wolves room, now wearing outfit 2, jumper fully off, slight concerned expression.
            with dissolve

            pause 0.5

            scene v8spd4 # FPP. Distant shot of Josh waiting outside his room leaning against the wall waiting, Josh looking slightly nervous.
            with fade

            u "(Ahh there's Josh.)"

            scene v8spd5 # TPP. MC now stood infront of Josh, MC and Josh fist bump, Josh smiling, MC looking slightly concerned. Josh mouth open.
            with dissolve

            jo "Hey, bro! You ready for this?"

            scene v8spd6 # FPP. Close up Josh, Josh smile, mouth closed.
            with dissolve

            u "I guess so. Let's go."

            scene v8spd6a # FPP. Same camera as v8spd6, Josh smile, mouth open.
            with dissolve

            jo "This is gonna be so dope! 1000 bucks! I can do so much with that kind of money, haha."

            scene v8spd6
            with dissolve

            u "Yeah, I'm sure you can."

            scene v8spd6b # FPP. Same camera as v8spd6, Josh slight concerned expression, mouth open.
            with dissolve

            jo "You don't seem too stoked, man. Something wrong?"

            scene v8spd6c # FPP. Same camera as v8spd6, Josh slight concerned expression, mouth closed.
            with dissolve

            u "Not really. I just feel like we shouldn't be doing this, is all."

            scene v8spd6a
            with dissolve

            jo "Hahaha! You worry too much, bro. Relax! We got this."

            scene v8spd7 # TPP. Show Josh and MC walking away from Josh's room.
            with dissolve

            pause 0.5

            jump drug_deal_w_josh

        else:

            $ MessengerService.new_message(josh, _("Hey bro, I got robbed and my ass kicked bad! Really wish you came with me, man."))
            $ MessengerService.add_reply(josh, _("Fuck! Are you ok??"))
            $ MessengerService.new_message(josh, _("No, man! I hurt everywhere! Plus my shit is gone!"))
            $ MessengerService.add_reply(josh, _("Hold on, I'll be right over"))

            while MessengerService.has_replies(josh):
                call screen phone
                if MessengerService.has_replies(josh):
                    u "I should really check my phone."
                    
            scene v8spd2
            with dissolve

            u "(Shit, I hope Josh is alright)"

            scene v8spd3
            with dissolve
            pause 0.5

            # jump josh's house
            jump after_drugs

    else:
        scene v8spd8 # TPP. Show MC sat in his Apes room at his desk on his phone.
        with Fade(0.75, 0.25, 0.75)
        pause 0.5

        play sound "sounds/vibrate.mp3"
        
        u "(Let's see who this is.)"

        if helpJosh:

            $ MessengerService.new_message(josh, _("Hey bro! It's time! Meet me at mine, okay?"), force_send=True)
            $ MessengerService.add_reply(josh, _("Okay, I'm on my way."))

            while MessengerService.has_replies(josh):
                call screen phone
                if MessengerService.has_replies(josh):
                    u "I should really check my phone."
                
            scene v8spd9 # TPP. Show MC getting up from his desk. (Apes)
            with dissolve

            pause 0.5

            scene v8spd9a # TPP. Same camera as v8spd9, MC now fully stood up. Show MC removing his jumper, revealing the shirt from Outfit 2, (Back 2 School T, Mat 3).
            with dissolve

            u "(Fuck, I have a bad feeling about this.)"

            scene v8spd10 # TPP. Show MC leaving his apes room, now wearing outfit 2, jumper fully off, slight concerned expression.
            with dissolve

            pause 0.5

            scene v8spd4 # FPP. Distant shot of Josh waiting outside his room leaning against the wall waiting, Josh looking slightly nervous.
            with fade

            u "(Ahh there's Josh.)"

            scene v8spd5 # TPP. MC now stood infront of Josh, MC and Josh fist bump, Josh smiling, MC looking slightly concerned. Josh mouth open.
            with dissolve

            jo "Hey, bro! You ready for this?"

            scene v8spd6 # FPP. Close up Josh, Josh smile, mouth closed.
            with dissolve

            u "I guess so. Let's go."

            scene v8spd6a # FPP. Same camera as v8spd6, Josh smile, mouth open.
            with dissolve

            jo "This is gonna be so dope! 1000 bucks! I can do so much with that kind of money, haha."

            scene v8spd6
            with dissolve

            u "Yeah, I'm sure you can."

            scene v8spd6b # FPP. Same camera as v8spd6, Josh slight concerned expression, mouth open.
            with dissolve

            jo "You don't seem too stoked, man. Something wrong?"

            scene v8spd6c # FPP. Same camera as v8spd6, Josh slight concerned expression, mouth closed.
            with dissolve

            u "Not really. I just feel like we shouldn't be doing this, is all."

            scene v8spd6a
            with dissolve

            jo "Hahaha! You worry too much, bro. Relax! We got this."

            scene v8spd7 # TPP. Show Josh and MC walking away from Josh's room.
            with dissolve

            pause 0.5

            jump drug_deal_w_josh

        else:
            $ MessengerService.new_message(josh, _("Hey bro, I got robbed and my ass kicked bad! Really wish you came with me, man."))
            $ MessengerService.add_reply(josh, _("Fuck! Are you ok??"))
            $ MessengerService.new_message(josh, _("No, man! I hurt everywhere! Plus my shit is gone!"))
            $ MessengerService.add_reply(josh, _("Hold on, I'll be right over"))

            while MessengerService.has_replies(josh):
                call screen phone
                if MessengerService.has_replies(josh):
                    u "I should really check my phone."
                
            scene v8spd9
            with dissolve

            u "(Shit, I hope Josh is alright)"

            scene v8spd10
            with dissolve
            pause 0.5

            # jump josh's house
            jump after_drugs
