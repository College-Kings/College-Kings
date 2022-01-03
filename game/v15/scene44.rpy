# SCENE 44: Finding Nora, Penelope trying to get info from analyzing Nora's Kiwii
# Locations: Room 103 where the pinboard is
# Characters: MC (Outfit: 1), AMBER (Outfit: 1), PENELOPE (Outfit: 1)
# Time: Morning

label v15s44:
    scene v15s44_1 # TPP. Show MC and Amber entering room 103, both serious, mouths closed
    with dissolve

    pause 0.75

    scene v15s44_2 # TPP. Show MC and Amber approaching the pinboard, both serious, mouths closed
    with dissolve

    pause 0.75

    call screen clues_ui

# -MC and Amber enter room 103 where the pinboard is. They approach the pinboard-

# -The UI pops up to show all the clues achieved from the Chris interrogation (CLUES UNLOCKED: Nora wanted to be alone after the breakup. Nora hates her dad. LOCATIONS UNLOCKED: Her Dad's house. Ms Rose's House. Nora's Dad's cabin. Camping by herself)-

label v15s44_continue:
    scene v15s44_3 # FPP. MC standing next to Amber, both facing the pinboard, MC looking at Amber, Amber looking at the pinboard, mouth closed, serious expression (don't actually show the pinboard)
    with dissolve

    menu:
        "Ready to guess":
            scene v15s44_3a # FPP. Same as v15s44_3, Amber looking at MC, Amber serious expression, mouth closed
            with dissolve

            u "I can already guess where she is."

            scene v15s44_3b # FPP. Same as v15s44_3a, Amber serious, mouth open
            with dissolve

            am "Easy there, detective. Anyone can guess, but we need more evidence to be sure."

        "Not enough clues":
            scene v15s44_3a
            with dissolve

            u "We've made some progress, but still need some more evidence."

            scene v15s44_3b
            with dissolve

            am "Yeah, we need more answers."

    scene v15s44_3c # FPP. Same as v15s44_3b, Amber looking down at her phone, serious, mouth open
    with dissolve

    am "Let me check in with our tech expert."

    scene v15s44_3d # FPP. Same as v15s44_3c, Amber looking at MC, holding her phone, serious, mouth closed
    with dissolve

    u "We have a tech expert?"

    scene v15s44_3e # FPP. Same as v15s44_3d, Amber looking at MC, holding her phone, serious, mouth open
    with dissolve

    am "Every crime show these days has a tech expert, [name]!"

    scene v15s44_4 # TPP. Amber in front of the pinboard next to MC, only show Amber, Amber slight smile, mouth closed / Penelope sitting in the cafe, talking on the phone, show her laptop (not the screen), Penelope slight smile, mouth open
    with dissolve

    pe "Hey, Amber!"

    scene v15s44_4a # TPP. Same as v15s44_4, Amber mouth open, slight smile / Penelope mouth closed, slightly confused
    with dissolve

    am "Hey, Techie."

    scene v15s44_4b # TPP. Same as v15s44, Amber mouth closed, slight smile / Penelope mouth open, slightly confused
    with dissolve

    pe "Techie?"

    scene v15s44_4c # TPP. Same as v15s44_4, Amber mouth open, slight smile / Penelope mouth closed, slight smile
    with dissolve

    am "We're trying to get to the bottom of Nora's sudden disappearance too. Can you help us?"

    scene v15s44_4
    with dissolve

    pe "Oh! Yeah, of course. What can I do to help?"

    scene v15s44_4c
    with dissolve

    am "We need you to check Nora's Kiwii for any clues."

    scene v15s44_4b
    with dissolve

    pe "Okay, I'll try but-"

    scene v15s44_4a
    with dissolve

    am "Thanks, Techie!"

    scene v15s44_4b
    with dissolve

    pe "I'm not sure I like that nickna-"

    scene v15s44_3c
    with dissolve

    am "She's on the case."

    scene v15s44_3f # FPP. Same as v15s44_3a, Amber slight smile, mouth closed
    with dissolve

    u "Techie?"

    scene v15s44_3g # FPP. Same as v15s44_3f, Amber slight smile, mouth open
    with dissolve

    am "Techie!"

    am "Okay, coffee refill..."

    scene v15s44_5 # TPP. Amber pouring two coffees, slight smile, mouth closed
    with dissolve

    menu:
        "Take the coffee":
            scene v15s44_3h # FPP. Same as v15s44_3g, Amber holding both coffees in her hand, no phone, looking at MC, slight smile, mouth closed
            with dissolve

            u "I need to get on your level... *Chuckles*"

            scene v15s44_6 # TPP. Show MC and Amber drinking their coffees
            with dissolve

            pause 0.75

            scene v15s44_7 # TPP. Show Amber throwing away her coffee cup
            with fade

            pause 0.75

        "Leave it":
            scene v15s44_3h
            with dissolve

            u "No idea how you're already drinking a second cup..."

            scene v15s44_3i # FPP. Same as v15s44_3h, Amber slight smile, mouth open
            with dissolve

            am "Ha! Second? Yeah, let's go with that..."
            
            scene v15s44_7
            with fade

            pause 0.75
        
    play sound "sounds/calling.mp3"

    scene v15s44_3j # FPP. Same as v15s44_3c, Amber slight smile, mouth open, looking down at her phone
    with dissolve

    am "I'll put her on speaker this time."

    scene v15s44_3k # FPP. Same as v15s44_3j, Amber slight smile, mouth closed
    with dissolve

    u "How kind."

    stop sound
    play sound "sounds/rejectcall.mp3"
    scene v15s44_8 # TPP. Amber and MC standing next to each other, Amber holding out the phone since they are on speaker, both slight smiles, Amber mouth open, MC mouth closed // Penelope sitting in the cafe, talking on the phone, show her laptop (not the screen), Penelope slight smile, mouth closed
    with dissolve

    am "What have you got for us, Techie?"

    scene v15s44_8a # TPP. Same as v15s44_8, Amber and MC slight smiles, mouths closed // Penelope slight smile, mouth open
    with dissolve

    pe "Is that seriously my name now?"

    scene v15s44_8
    with dissolve

    am "Yes! On with it!"

    scene v15s44_8a
    with dissolve

    pe "*Laughs* Right, okay."

    scene v15s44_8b # FPP. Same as v15s44_8, Amber and MC slight smiles, MC mouth open, Amber mouth closed // Penelope slight smile, mouth closed
    with dissolve

    u "Hi, Penelope!"

    scene v15s44_8a
    with dissolve

    pe "Oh, hi [name]! You're playing detective too, huh?"

    scene v15s44_8b
    with dissolve

    u "Yeah, we've been on the case since the crack of dawn!"

    scene v15s44_8a
    with dissolve

    pe "You cracked what at dawn?"

    scene v15s44_8b
    with dissolve

    u "Never mind. *Laughs*"

    scene v15s44_8
    with dissolve

    am "So, what's up?"

    scene v15s44_8c # TPP. Same as v15s44_8a, Amber and MC concerned, mouths closed // Penelope serious expression, mouth open
    with dissolve

    pe "Well, Nora hasn't posted on Kiwii since we landed, so that was a bit of a dead end."

    scene v15s44_8d # TPP. Same as v15s44_8c, Amber and MC concerned, Amber mouth open, MC mouth closed // Penelope slightly concerned, mouth closed
    with dissolve

    am "Shit."

    scene v15s44_8e # TPP. Same as v15s44_8d, Amber and MC looking at each other, smiling, mouths closed, Penelope slight smile, mouth open
    with dissolve

    pe "However..."

    scene v15s44_8a
    with dissolve

    pe "I sent friend requests to her family members and some of them accepted. One of them, her aunt?"

    scene v15s44_8b
    with dissolve

    u "Oh shit!"

    scene v15s44_8a
    with dissolve

    pe "She said something that might help."

    scene v15s44_8
    with dissolve

    am "Oh, really?"

    scene v15s44_8a
    with dissolve

    pe "Mhmm... Looks like she posted a photo on the day we got back from Europe."

    pe "It's a selfie of her and Nora, and the caption says..."

    scene v15s44_8e
    with dissolve

    pe "\"Was so nice to see my baby niece today... She never stays for long, but it's always perfect <3 See you soon, Nora Bora!\""
    $ v15_nora_clues.add("visited_aunt")
    $ v15_nora_locations.add("aunt")

    scene v15s44_8
    with dissolve

    am "Holy shit!"

    scene v15s44_8b
    with dissolve

    u "That's really useful, Penelope. You're amazing."

    scene v15s44_8a
    with dissolve

    pe "I think her whole family are huge nature freaks. There's pictures of them camping, fishing... You name it."
    $ v15_nora_clues.add("loves_nature")

    if "camping" in v15_nora_clues:
        scene v15s44_8
        with dissolve

        am "Hmm, that's the second time today someone's mentioned the outdoors when it came to Nora."
    
    else:
        scene v15s44_8
        with dissolve
        
        am "Camping... now that's an activity for someone who wants some peace and quiet."
        
        $ v15_nora_locations.add("camping")

    menu:
        "Ask about Nora's family":
            scene v15s44_8b
            with dissolve

            u "Any other clues from her other family members?"

            if v11_pen_goes_europe:
                scene v15s44_8e
                with dissolve

                pe "Sadly not much."
                
            else:
                scene v15s44_8e
                with dissolve

                pe "Oh... Uhm... Uh, no."

            pe "I didn't find a lot of pictures with Nora, strangely enough."

            pe "But most of her relatives are from this area, so if she's with them, she's probably not too far away."

            scene v15s44_8b
            with dissolve

            u "Well, at least that's something."
        
        "Ask about Nora's posts":
            scene v15s44_8b
            with dissolve

            u "Was there anything interesting in Nora's post history?"

            scene v15s44_8a
            with dissolve

            pe "Well, it looks like she was in a relationship before Chris."
            
            pe "Nora's still friends with that guy on Kiwii, so I thought I'd send him a request as well-"

            scene v15s44_8b
            with dissolve

            u "Wait, they're still friends?"
            
            u "That's an interesting development."
            $ v15_nora_clues.add("likes_ex")
            
            scene v15s44_8a
            with dissolve

            pe "But he hasn't added me yet so I couldn't look much further. I only know he's a local here to San Vallejo."
            
            scene v15s44_8
            with dissolve

            am "Hmm, that's something that we might want to consider. Maybe Nora ran off to this ex."
            $ v15_nora_locations.add("ex")

    scene v15s44_8a
    with dissolve

    pe "Well, there you go. *Giggles*"

    scene v15s44_8
    with dissolve

    am "Okay, well thanks for all your help, Techie. We gotta run!"

    scene v15s44_8b
    with dissolve

    u "Yeah, thank you so much."

    scene v15s44_8a
    with dissolve

    pe "Anytime detectives, haha. Good luck!"

    scene v15s44_3f
    with dissolve

    u "Okay, so let's add those clues to the board and see how things are shaping up."

    call screen clues_ui

# -The UI pops up to show all the clues achieved from Penelope's search (CLUES UNLOCKED: Nora loves nature. Nora visited her aunt the day she landed from Europe. LOCATION UNLOCKED: Staying at her Aunt's apartment)-

# -MC exits the UI whenever-
label v15s44_continue2:
    scene v15s44_3l # FPP. Same as v15s44_3b, Amber slight smile, mouth open, different pose
    with dissolve

    am "Alright, it's looking good. So, walk me through your current thoughts."

    scene v15s44_3m # FPP. Same as v15s44_3l, Amber slight smile, mouth closed
    with dissolve

    menu:
        "No idea":
            u "No idea, really. She could be at any of these places."

            scene v15s44_3n # FPP. Same as v15s44_3, Amber slight smile, mouth open
            with dissolve

            am "Yeah, we need to dig deeper."

            scene v15s44_3l
            with dissolve

            am "You thinking what I'm thinking?"

            scene v15s44_3m
            with dissolve

            u "Umm, sure?"

            scene v15s44_3l
            with dissolve

            am "Interrogation number two!"

        "I think I know":
            u "I think I know where she is."

            scene v15s44_3l
            with dissolve

            am "You think you know? Or you know, you know?"

            am "I mean... We've only interrogated one person so far. *Laughs* That's just not enough to make a final decision."

    scene v15s44_3m
    with dissolve

    u "Another interrogation? I think we kind of scared Chris a little."

    scene v15s44_3l
    with dissolve

    am "He's a big boy, he'll get over it."

    scene v15s44_3m
    with dissolve

    u "Ha, true. So, who's next on the list?"

    scene v15s44_3o # FPP. Same as v15s44_3l, Amber slight evil grin, mouth open
    with dissolve

    am "The blonde bombshell... *Giggles*"

    scene v15s44_3m
    with dissolve

    u "Chloe?"

    scene v15s44_3o
    with dissolve

    am "Ha, yes."

    scene v15s44_3n
    with dissolve

    am "All great mysteries have a jaw-dropping blonde that distracts the detectives but gives golden information."

    scene v15s44_3l
    with dissolve

    am "It's the last place the doofus detectives expect to look."

    scene v15s44_3m
    with dissolve

    u "Ha. I wouldn't even consider talking to Chloe when looking for Nora. They're enemies, no?"

    scene v15s44_3l
    with dissolve

    am "Lo and behold, they have all the answers."

    scene v15s44_3m
    with dissolve

    u "Enemies? *Scoffs*"

    scene v15s44_3l
    with dissolve

    am "It's true that they hate each other, but they've hated each other for a long, long, long time now."

    scene v15s44_3m
    with dissolve

    u "Oh shit, you're right!"

    scene v15s44_3n
    with dissolve

    am "Chloe's going to know things about Nora that nobody else has ever paid attention to."

    scene v15s44_3m
    with dissolve

    u "Very sneaky..."

    scene v15s44_3l
    with dissolve

    am "The real question is, will she care enough to help us find Nora?"

    scene v15s44_3m
    with dissolve

    u "I guess we're about to find out, huh?"

    scene v15s44_3l
    with dissolve

    am "Damn right we are."

    scene v15s44_9 # TPP. Show Amber and MC standing next to each other, Amber mouth open, posing with a handgun, MC mouth closed, both smiling, MC not posing
    with dissolve

    am "House call number two."

    scene v15s44_9a # TPP. Same as v15s44_9, Amber already posing, MC now posing wit a handgun as well, both smiling, Amber mouth clsoed, MC mouth open
    with dissolve

    u "The blonde bombshell."

    scene v15s44_9b # TPP. Same as v15s44_9a, both pretending to blow the steam off their guns
    with dissolve

    pause 0.75

    scene v15s44_10 # TPP. MC and Amber exiting the room, both smiling, Amber exiting in front of MC, nouths closed
    with dissolve

    pause 0.75

    jump v15s45