# SCENE 69a: MC wakes up at Penelope's
# Locations: Penelopes Room
# Characters: PENELOPE (Outfit: 1), MC (Outfit: 2)
# Time: Morning


label v16s69a:

    # -Night to morning transition-
    scene sleep_transition_fast # Ignore animation 
    with fade

    pause 2.2
            
    scene black
    with dissolve
        
    pause 1

    scene v16s69a_1 # TPP. Show MC (yawning and strecthing, eyes closed), wearing just his boxers (check scene 69 for boxer type) and Penelope (Slight smile, mouth closed, looking at MC), wearing just her bra and panties (check scene 69 for bra and panties type), wake up next to each other in Penelope's bed.
    with dissolve

    pause 0.75

    scene v16s69a_2 # FPP. Show just Penelope (slight smile, mouth open, looking at MC) lying in bed with her head on her pillow, wearing just her bra and panties
    with dissolve

    pe "Mmm... I slept so well, haha. Especially with my big spoon."

    scene v16s69a_2a # FPP. Show just Penelope (slight smile, mouth closed, looking at MC) lying in bed with her head on her pillow, wearing just her bra and panties
    with dissolve

    u "You're right. That was the most rest I've gotten in a long time."

    scene v16s69a_2
    with dissolve

    pe "Ugh, I don't want it to end."

    scene v16s69a_2a
    with dissolve

    u "Neither do I."

    scene v16s69a_2
    with dissolve

    pe "I have to get to campus soon, though. I'm on dog duty for Dean Harrison's new dog."

    scene v16s69a_2a
    with dissolve

    u "Oscar?"

    scene v16s69a_2
    with dissolve

    pe "Is that his name?"

    scene v16s69a_2a
    with dissolve

    u "Yeah, I was there when she adopted him, ha."

    scene v16s69a_2
    with dissolve

    pe "You really get everywhere, don't you? *Giggles*"

    scene v16s69a_2a
    with dissolve

    u "Haha, I just like to be where the action is, you know?"

    scene v16s69a_2
    with dissolve

    pe "Stop it. You like helping people. Admit it."

    scene v16s69a_2a
    with dissolve

    u "Mmm... Maybe..."

    scene v16s69a_2
    with dissolve

    pe "Haha, well come help me then. I'm sure he'd like to see a familiar face."

    pe "Or smell a familiar hand I guess? Hehe."

    scene v16s69a_2a
    with dissolve

    u "*Laughs* Okay, sounds like a plan."

    u "*Laughs* I should probably stop at my place, for a change of clothes first"

    scene v16s69a_2
    with dissolve

    pe "*Giggles* What? You don't want to smell like Oscar?"

    scene v16s69a_2a
    with dissolve

    u "*Laughs* Not really!"

    if 2 & v16s27_mc_baby_duty_night == 2: # -if MC has baby Thursday night 

        scene v16s69a_2a
        with dissolve

        u "I also need to drop off the baby when we get to campus, then I'm all yours."

        scene v16s69a_2
        with dissolve

        pe "Good. I like it when you're all mine."

    scene v16s69a_1a # TPP. Show MC (kissing Penelope, eyes closed), wearing just his boxers (check scene 69 for boxer type) and Penelope (kissing MC, eyes closed), wearing just her bra and panties (check scene 69 for bra and panties type) lying in Penelope's bed, laying on top of MC as they kiss
    with dissolve

    pause 0.75

    scene v16s69a_1b # TPP. Show Mc (slight smile, mouth closed, looking at Penelope) getting dressed (outfit 2), and Penelope (slight smile, mouth closed, looking at MC) getting dressed
    with dissolve

    pause 0.75

    jump v16s70 # -Transition to Scene 70-