# SCENE 19: Helping Lauren Clean Up
# Locations: Deer House Guest Room, Deer House Living Room, Deer House Kitchen 
# Characters: MC (Outfit: Halloween Costume), LAUREN (Outfit: 1)
# Time: Morning

label v15s19:
    # -TODO: Transition from Night to Morning-

    if v15s18_LaurensBed: # -if sleeping in Lauren's bed
        # -MC wakes up alone in Lauren's bed-
        scene v15s19_1 # TPP. Close up on MC (upper body) laying in bed facing the wall (not the door), no shirt, eyes closed, mouth closed smiling [Deer House Guest Room].
        with dissolve

        pause 0.75

        scene v15s19_1a # TPP. Close up on MC (upper body) laying in bed facing the wall (not the door), no shirt, waking up, smiling, mouth closed [Deer House Guest Room].
        with dissolve

        pause 0.75

        scene v15s19_1b # TPP. Widen out, MC laying on the bed facing the wall (not the door), no shirt, waking up, smiling, mouth closed with an emtpy bed next to him [Deer House Guest Room].
        with dissolve

        pause 0.75

        scene v15s19_1d # TPP. MC laying down, no shirt, smiling, mouth open, rolling over towards the door, reaching for Lauren in the empty space next to him [Deer House Guest Room].
        with dissolve

        u "(Hmm?) Lauren?"

        scene v15s19_1e # TPP. MC sitting on the bed facing the door, naked, yawning, netural expression [Deer House Guest Room].
        with dissolve

        u "(She must be up already.)"

        scene v15s19_1f # TPP. MC dressing in his costume, netural expression, mouth open. [Deer House Guest Room] 
        with dissolve

        u "I really should've brought an extra pair of clothes... *Sighs*"

        scene v15s19_1g # TPP. MC dressed in his costume, exiting the bedroom (camera behind him as he leaves) [Deer House Guest Room]
        with dissolve

        pause 0.75

        scene v15s19_2 # TPP. MC dressed in his costume, netural expression, mouth closed descending the stairs, there are cups, bottles of wine and beer (party trash) on the steps [Deer House Staircase].
        with dissolve
        
        pause 0.75

    else : # -if sleeping on the couch
        $ v15s18_LaurensBed = False

        scene v15s19_3 # TPP. MC dressed in his costume, laying on the couch, eyes closed, mouth closed, netural expression. There's cups, beer bottls, and party trash on the coffee table, on teh entertainment center (TV), and the dining table [Deer House Living Room].
        with dissolve

        pause 0.75

        scene v15s19_3a # TPP. MC dressed in his costume, laying on the couch, waking up, mouth closed, netural expression There's cups, beer bottls, and party trash on the coffee table, on teh entertainment center (TV), and the dining table [Deer House Living Room].
        with dissolve

        pause 0.75

        scene v15s19_3b # TPP. MC dressed in his costume, sitting on the couch, stretching, yawning, netural expression There's cups, beer bottls, and party trash on the coffee table, on teh entertainment center (TV), and the dining table [Deer House Living Room].
        with dissolve

        pause 0.75

    # -Regardless-

    # -Lauren is tidying up in the kitchen, putting trash in a bag. MC approaches her-
    scene v15s19_4 # TPP. MC dresssed in his costime enters the kitchen area, netural expression, mouth closed. There's cups, beer bottles, plates with scraps of food all of the counters in the ktichen. Lauren is next to the fridge, netural expression, mouth closed, cleaning by putting the trash in a trash bag she is holding [Deer House Kitchen].
    with dissolve

    pause 0.75

    scene v15s19_4a # FPP. Lauren next to the frige, smiling, mouth closed, looking at MC while holding a trash bag. The counter near Lauren is slightly cleaner (free of trash) than the previous scene [Deer House Kitchen].
    with dissolve

    u "Morning, Lauren."

    scene v15s19_4b # FPP. Lauren next to the frige, smiling, mouth open, looking at MC while holding a trash bag. The counter near Lauren is slightly cleaner (free of trash) than the previous scene [Deer House Kitchen].
    with dissolve

    la "Hey! Good morning."

    la "I officially regret not cleaning all of this up last night, haha."

    scene v15s19_4c # FPP. Lauren by the sink, smiling, mouth closed, looking at MC while throwing trash into the trash bag she is holding. The counter near the fridge is clean [Deer House Kitchen].
    with dissolve

    u "*Sighs* Yeah, we probably should've."

    scene v15s19_4d # FPP. Lauren by the sink, smiling, mouth open, looking at MC while throwing trash into the trash bag she is holding. The counter by the sink is slightly cleaner (free of trash) than the previous scene [Deer House Kitchen].
    with dissolve

    la "No worries though, it was worth it. I had a really good time."

    menu:
        "Help clean up":
            scene v15s19_5 # TPP. MC, smiling mouth open collects trash from the counter opposite the fridge (by the stove) while Lauren smiling mouth closed continues throwing away trash from counter by the sink, which is slightly cleaner than the preivous scene [Deer House Kitchen].
            with dissolve

            u "Haha, that it was."

            scene v15s19_5a # FPP. Lauren by the sink, apologetic, mouth open, holding a trash bag. The counter by the sink is clean (free from trash) [Deer House Kitchen].
            with dissolve
            
            la "Oh, no, I wasn't suggesting-"

            scene v15s19_5b # FPP. Lauren by the sink, happy, smiling, mouth closed, holding a trash bag. The counter by the sink is clean (free from trash) [Deer House Kitchen].
            with dissolve

            u "It's okay, Lauren. You don't have to clean up your own birthday party all by yourself. *Laughs*"

            scene v15s19_5c # FPP. Lauren by the sink, happy, big smile, mouth open, holding a trash bag. The counter by the sink is clean (free from trash) [Deer House Kitchen].
            with dissolve

            la "Thank you, [name]."

            scene v15s19_5b
            with dissolve

            u "Of course, now where should I start?"

            scene v15s19_5c
            with dissolve

            la "Can you hold this bag open for me? And I'll put this trash in it."

            scene v15s19_5b
            with dissolve

            u "Sure, I can do that."

            # -Quick shots of MC taking the bag off of Lauren, holding it open while she throws in some old cups, used napkins, and half-eaten food-

            scene v15s19_5d # TPP. MC, smiling mouth closed in the kitchen smiling holding the trash bag with Lauren, smiling mouth closed, putting trash in the bag. The counter by the stove is clean. The entire kitchen at this point is clean (free of trash) [Deer House Kitchen].
            with dissolve

            pause 0.75

            scene v15s19_6 # TPP. MC, smiling mouth closed in the dining area holding the trash bag with Lauren, smiling mouth closed, putting trash in the bag. The dining table has cups, beer bottles napkins, plates of food scraps all (party trash) all over it [Deer House Dining Area/Living Room].
            with dissolve

            pause 0.75

            scene v15s19_6a # TPP. MC, smiling mouth closed in the dining area holding the trash bag with Lauren, smiling mouth closed, putting trash in the bag. The dining table is clean (free of trash) [Deer House Dining Area/Living Room].
            with dissolve

            pause 0.75

            scene v15s19_7 # TPP. MC, smiling mouth closed in the living room holding the trash bag with Lauren, smiling mouth closed, putting trash in the bag There's cups, beer bottls, and party trash on the coffee table and on the entertainment center (TV) [Deer House Living Room]. 
            with dissolve

            pause 0.75

            scene v15s19_7a # TPP. MC, smiling mouth closed in the living room holding the trash bag with Lauren, smiling mouth closed, putting trash in the bag The coffee table and entertainment center (TV) are clean [Deer House Living Room].
            with dissolve

            pause 0.75

            # -she makes a disgusted face-
            scene v15s19_7b # FPP. Lauren, disgusted mouth open, scraping food scraps into the trash bag. The living room is clean [Deer House Living Room].
            with dissolve

            la "Ugh... Gross!"
            
            scene v15s19_7c # FPP. Lauren, smiling, mouth closed, looking at MC still holding that trash bag. The living room is clean [Deer House Living Room].
            with dissolve

            u "*Laughs*"

            scene v15s19_7d # FPP. Lauren, smiling, mouth open, looking at MC still holding that trash bag. The living room is clean [Deer House Living Room].
            with dissolve

            la "Okay. I'm so glad that's done, haha. You're the best."

            scene v15s19_7c
            with dissolve

            u "Yeah, I am."

            scene v15s19_7e # TPP. MC, smiling mouth closed, placing the trash bag on the floor. Lauren smiling mouth closed, looking at MC. The living room is clean [Deer House Living Room]. # -they laugh- // TN: no dialog skipped the laugh # -MC puts down the trash bag-
            with dissolve

            pause 0.75

        "Don't help clean up":
            scene v15s19_4c
            with dissolve

            u "Yeah, everyone did. It was a great party."
            
            u "I'm sorry, Lauren... I would offer to help, but I really have to get on with my day."

            scene v15s19_4d
            with dissolve

            la "It's okay, really. I'll get it." 

    # -Regardless-

    play sound "sounds/vibrate.mp3" 

    if v15s18_LaurensBed:
        scene v15s19_8 # TPP. MC, smiling mouth closed gets his phone from his pocket while Lauren, smiling mouth closed, watches him. The kitchen is in the same condition is a v15s19_4d [Deer House Kitchen].
        with dissolve
        
        pause 1

    else:
        scene v15s19_7f # TPP. MC, smiling mouth closed gets his phone from his pocket while Lauren, smiling mouth closed, watches him. The living room is clean and there is a trash bag on the floor in front of MC [Deer House Living Room].
        with dissolve
        
        pause 1

    if v14_help_chloe and not v15_chloe_lindseysabotage: # -if helping Chloe with meeting the Dean # -MC checks his texts to see a message from Chloe-
        if v15_chloe_mrleesupport: # -if meeting with Mr. Lee (Transcriber Note: Again, mutually exclusive)
            $ chloe.messenger.newMessage("Hey, the meeting with Mr. Lee is this morning, so I'll see you in the library soon. Don't be late!", queue=False)

        else: # -if meeting with Ms. Rose
            $ chloe.messenger.newMessage("Hey, the meeting with Ms. Rose is this morning, so I'll see you in the library soon. Don't be late!", queue=False)

        $ chloe.messenger.addReply("Okay, OMW :)")

        label v15s19_PhoneContinueChloe:
        if chloe.messenger.replies:
            call screen phone
        if chloe.messenger.replies:
            u "(I should check my phone.)"
            jump v15s19_PhoneContinueChloe

    if v14_help_lindsey: # -if helping Lindsey TN: Helping Chloe and Lindsey are NOT mutually exclusive-- no else if
        if v15_lindsey_gamenight: # -if helping Lindsey with Game night
            $ lindsey.messenger.newMessage("Hey, can you come meet me now to buy the alcohol for our game night? I have a plan. I'll send the details of which store to come to.", queue=False)
            $ lindsey.messenger.addReply("Okay, sounds good.")

        else: # -if helping Lindsey with VIP club night
            $ lindsey.messenger.newMessage("Hey, can you call the club and book the VIP package, please? See what you can do in terms of them serving us alcohol and negotiating the price <3 Thank you!", queue=False)
            $ lindsey.messenger.addReply("Okay, I'll put on the charm ;) I'll let you know how it goes")

        label v15s19_PhoneContinueLindsey:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
                u "(I should check my phone.)"
                jump v15s19_PhoneContinueLindsey

    # -Regardless of helping Chloe or Lindsey-
    # -MC exits his texts, puts his phone away-

    if v15s18_LaurensBed: 
        scene v15s19_8a # FPP. Lauren by the sink, smiling, mouth closed, looking at MC while throwing trash into the trash bag she is holding. The kitcen is in the same condition is a v15s19_4d [Deer House Kitchen].
        with dissolve

        u "Well, I gotta go."

        scene v15s19_8b # TPP. Lauren, smiling mouth closed following MC, smiling mouth closed, to the front door. The house is still dirty from the party. [Deer House Living Room].
        with dissolve
        
        pause 0.75
    
    else: 
        scene v15s19_7g # FPP. Lauren, smiling mouth closed looking at MC. The living room is clean and there is a trash bag on the floor in front of MC [Deer House Living Room].
        with dissolve

        u "Well, I gotta go."
        
        scene v15s19_7h # TPP. Lauren, smiling mouth closed following MC, smiling mouth closed, to the front door. The house is clean. [Deer House Living Room].
        with dissolve
        
        pause 0.75

    # All scenes converge to the living room front door.

    scene v15s19_9 # FPP. Lauren, smiling mouth open, looking at MC (Lauren has her back to the front of the house, the front door is to her right.) [Deer House Living Room Front Door].
    with dissolve

    la "Alright, I'll see you later."

    scene v15s19_9a # FPP. Lauren, smiling mouth closed, looking at MC (Lauren has her back to the front of the house, the front door is to her right.) [Deer House Living Room Front Door].
    with dissolve

    u "Thanks again for an amazing party last night."

    scene v15s19_9
    with dissolve

    la "Are you kidding? Thank you for coming. It was such a special night for me!"

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        play sound "sounds/kiss.mp3"

        scene v15s19_9c # FPP. Lauren, eyes closed, kissing MC on the lips [Deer House Living Room Front Door]. 
        with dissolve
        
        pause 0.75

    else: # LaurenFriend
        scene v15s19_9b # TPP. Camera facing the front door. MC smiling mouth closed and Lauren smiling mouth closed friendly hug each other in front of the door [Deer House Living Room Front Door].
        with dissolve
        
        pause 0.75
  
    scene v15s19_9a
    with dissolve
    
    u "I seriously need to go home and change..."

    scene v15s19_9
    with dissolve

    la "Yeah... that might be a good idea, haha."

    scene v15s19_9a
    with dissolve

    u "You think I should wear one of those trash bags over top of it?"

    scene v15s19_9
    with dissolve

    la "*Chuckles* I know it sounds crazy, but that might just draw more attention to you."

    scene v15s19_9a
    with dissolve

    u "Haha, you're right. *Sighs*"

    u "It'll be okay. I just have to make a run for it."

    scene v15s19_9
    with dissolve

    la "And avoid as many people as you possibly can, hehe."

    scene v15s19_9a
    with dissolve

    u "*Chuckles* Exactly."

    scene v15s19_9
    with dissolve

    la "I'll see you later, good luck!"

    scene v15s19_9a
    with dissolve

    u "Yeah, thanks. Bye!" 

    # -MC leaves out the front door with Lauren watching him go, smiling-
    
    if v14_help_chloe and not v15_chloe_lindseysabotage:
        jump v15s20 # -if helping Chloe with tuition-

    elif v15_lindsey_gamenight: 
        jump v15s24 # -if helping Lindsey with Games night, transition to Scene 24-

    elif v14_help_lindsey:
        jump v15s25 # -if helping Lindsey with VIP club night, transition to Scene 25-

    else:
        jump v15s23 # -if not helping Chloe (with tuition) or Lindsey, transition to Scene 23-