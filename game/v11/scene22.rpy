# SCENE 22: Mr Lee does a tour at the museum
# Location: Museum
# Characters: MC(outfit 1), Riley(outfit 2), Mr. Lee (Outfit 1), Nora (Outfit 1), Chris (Outfit 2)
# Time: Afternoon

label v11_museum_tour:
    scene v11mt1 # TPP. Show Mr Lee, MC and Nora walking up to the museum, MC is in slight pain, Nora slightly annoyed, Mr Lee is smiling, all mouths closed
    with fade
    play music music.ck1.v11.Track_Scene_11 fadein 2
    pause 0.75

    scene v11tm2 # TPP. Show Chris, Riley and MC standing next to each other inside the museum, Chris on his phone, MC is in slight pain, Riley is slightly smiling, Chris is smiling all mouths closed (Nora standing next to Chris, out of shot, Mr Lee in front of the students, out of shot)
    with dissolve

    pause 0.75

    scene v11tm3 # FPP. Same positioning as v11tm2, MC is looking at Mr Lee, Mr Lee has a dinosaur drawing behind him, Mr Lee smiling, mouth open, looking at MC
    with dissolve

    lee "Ahh, the museum. Students, look around, are you not just... enthralled? The past is right here, before you in all its glory. Gaze upon these dinosaurs, students."

    lee "Those of us that study history have debated whether the world is actually billions of years old and these are real..."
    lee "Or if it's only thousands of years old and these are just put together parts of a scientist's imagination."

    scene v11tm4 # FPP. Same positioning as v11tm2, MC looking at Nora, she is rolling her eyes, mouth closed, slightly annoyed, looking at Mr Lee (Lee out of shot)
    with dissolve

    pause 0.75

    scene v11tm4a # FPP. Same as v11tm4, Nora looking at Mr Lee, her mouth open, slightly annoyed
    with dissolve

    no "Dinosaurs aren't real."

    scene v11tm3a # FPP. Same as v11tm3, Lee looking at Nora's direction, mouth open, slight smile
    with dissolve

    lee "Some would call you a conspiracist... Though, how much can you believe if you've never seen one?"

    scene v11tm5 # FPP. Same positioning as v11tm2, MC looking at Riley, Riley looking at Nora (out of shot), Riley mouth open, slight smile
    with dissolve

    ri "But we have seen one... we're looking at it right now."

    scene v11tm4b # FPP. Same as v11tm4, Nora looking at Riley's direction, Nora mouth open, slightly annoyed
    with dissolve

    no "We're looking at molded bones of some old guys' drawings."

    scene v11tm6 # TPP. Show the dinosaur drawing on the wall (should be same one as v11tm3)
    with dissolve

    menu:
        "Real":
            $ nora.points -= 1
            $ riley.points += 1

            scene v11tm4c # FPP. Same as v11tm4, Nora looking at MC, slightly annoyed, mouth closed
            with dissolve

            u "Sorry Nora, but those are definitely real."

            scene v11tm4d # FPP. Same as v11tm4c, Nora slightly annoyed, mouth open
            with dissolve

            no "Keep dreaming, [name]."

        "Not real":
            $ nora.points += 1
            $ riley.points -= 1

            scene v11tm5a # FPP. Same as v11tm5, but Riley looking at MC, mouth closed, slightly annoyed
            with dissolve

            grant Achievement("just_a_theory", "Tell Riley dinosaurs aren't real")
            u "Sorry Riley, they definitely aren't real."

            scene v11tm5b # FPP. Same as v11tm5a, Riley mouth open, slightly annoyed
            with dissolve

            ri "Okay, Mr. Scientist."
    
    scene v11tm3
    with dissolve

    lee "Many historians have debated for centuries. Three students couldn't solve this mystery in a matter of minutes."

    scene v11tm7 # TPP. Show Mr Lee, Chris and MC walking through the museum (going to the paintings), Chris smiling, on a phone call, MC and Mr Lee, slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v11tm8 # FPP. MC and Lee looking at each other, show a few paintings behind Lee, Lee is smiling, mouth open (MC, Chris, Riley and Nora standing next to each other, make sure Riley and Nora are next to each other, oposite to Lee, all of them out of shot)
    with dissolve

    lee "Does anyone recognize any of these paintings?"

    scene v11tm9 # FPP. Same character positioning as v11tm8, MC is looking at Chris, Chris talking on the phone, mouth open, smiling, Chris looking towards Mr Lee
    with dissolve

    ch "I don't know what he likes! His entire bio is online, just look him up."

    scene v11tm8a # FPP. Same as v11tm8, Mr Lee is looking at Chris' direction, Mr Lee is slightly annoyed, mouth open
    with dissolve

    lee "Chris, is there something you'd like to share with the rest of us?"

    scene v11tm9a # FPP. Same as v11tm9, Chris lowers his phone, slightly worried, mouth open, looking at Mr Lee
    with dissolve

    ch "Sorry, Mr. Lee."
    
    scene v11tm9
    with dissolve

    ch "I'll call you back later Bash."

    scene v11tm8
    with dissolve

    lee "To continue, these paintings are some of London's most prestigious artworks. The woman in this painting here was the first woman to ever challenge the monarchy's rule."

    lee "She was the sister of a duke and when they insisted on marrying her off she revolted with many other women in tow."

    scene v11tm10 # FPP. Same character positioning as v11tm8, MC looking at Riley, Riley looking at Mr Lee (Lee out of shot), Riley mouth open, slight smile
    with dissolve

    ri "She was brave."

    scene v11tm11 # FPP. Same character positioning as v11tm8, MC looking at Nora and Riley looking at each other, Nora mouth open, slightly smiling, Riley slight smile, mouth closed (both of them in shot for this one)
    with dissolve

    no "That I can agree with."

    scene v11tm11a # FPP. Same as v11tm11, but Nora and Riley are hugging, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11tm11b # FPP. Same as v11tm11, Riley mouth open, slightly smiling, mouth open, Nora mouth closed, slightly smiling
    with dissolve

    ri "Look at us, agreeing. *Chuckles*"

    scene v11tm11
    with dissolve

    no "*Chuckles*"

    scene v11tm8
    with dissolve

    lee "I want you all to explore the museum. Find something meaningful to you and report back to me."

    scene v11tm10
    with dissolve

    ri "Sounds good."
    stop music fadeout 3
    
    $ v11s23_penelope_date = False #variable was introduced late and defaults as True to enhance playability of saves already in progress. This is an unavoidable toggle to False for new playthroughs that will make the variable act as intended.
    jump v11s23_freeroamstart