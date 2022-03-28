# SCENE 71a: Penelope sex scene
# Locations: Dean's Office
# Characters: MC (Outfit: 5/Naked), PENELOPE (Outfit: 1/Sexy Lingerie/Naked)
# Time: Friday Morning


label v16s71a: ### ERROR: 71a) Penelope sex scene

    $ sex_overlay_options = [] # Reset the variable to default values
    $ sex_overlay_options = [("Neck", "v16s71a_neck"),("Boobs", "v16s71a_boobs"), ("Feet", "v16s71a_feet")]
    $ sceneList.add("v16_penelope")

    # -MC and Penelope are kissing passionately by the Dean's desk-
    # -Then Penelope starts taking her clothes off, revealing sexy lingerie underneath-
    scene v16s71a_1    # TPP  MC(eyes closed), Penelope (eyes closed) standing by Dean's chair and bookshelf, kissing passionately with tongue.
    with dissolve

    pause 0.75

    scene v16s71a_1a   # TPP  Close on the floot of Penelope's feet where we see her skit on the ground by her ankles.
    with dissolve

    pause 0.75

    scene v16s71a_1b   # TPP  Close on Penleope's head (smiling sexy, mouth closed if in the shot) (no body in the shot) showing her taking off her shirt.
    with dissolve

    pause 0.75
    
    scene v16s71a_1c   # FPP  Wide view of Penelope (smiling sexy, fuck me eyes, mouth closed) posing sexy for MC by the Dean's chair in lingerie.
    with dissolve

    u "Oh, wow. Did you plan this?"

    scene v16s71a_1d   # FPP  Penelope( smiling sexy, mouth open) looking at MC.
    with dissolve

    pe "*Giggles* Maybe."
    
    # -if MC woke up with Penelope
    # This is the same condition used in s68 to branch to s69 (spend night with penelope) s68:206
    # if penelope.relationship == Relationship.LOYAL and 0x20 & v16s27_mc_baby_duty_night != 0x20: v16s27_mc_baby_schedule["wednesday"] == BabyDuty.WITH_PARTNER
    if penelope.relationship == Relationship.LOYAL and v16s27_mc_baby_schedule["thursday"] != BabyDuty.WITH_PARTNER: 

        scene v16s71a_1d
        with dissolve

        pe "I slipped this on without you seeing it this morning."

    # -Regardless of that-

    scene v16s71a_1e   # FPP  Penelope( smiling sexy, mouth closed) looking at MC.
    with dissolve
    
    u "I approve."

    # -Penelope sits on the edge of the Dean's desk. They kiss passionately. MC's hand around her throat while they kiss (Penelope is submissive and MC is dominant in this sex scene - Community voted scene)-
    # -MC pulls off Penelope's lingerie and she is now naked. Then MC takes his clothes off-
    # -With his hand around her throat, MC eases her back so she's lying down on the desk-
    scene v16s71a_2    # TPP  Penelope (eyes closed) sits on the front corner of the Dean's desk kissing MC(eyes closed) passionately with tongue. MC slightly dominates her with his hand around her throat while they kiss.
    with dissolve

    pause 0.75

    scene v16s71a_2a   # TPP  Alternate angle of v16s71a_2.
    with dissolve

    pause 0.75

    scene v16s71a_2b   # TPP  MC(smiling, mouth closed) removing Penelope(smiling sexy, mouth closed, looking at MC with fuck me eyes) bra.
    with dissolve

    pause 0.75

    scene v16s71a_2c   # TPP  Penelope naked (smiling sexy, mouth closed) helping MC (smiling, mouth closed) remove his shirt.
    with dissolve

    pause 0.75

    scene v16s71a_2d   # Same as v16s71a_2 but MC and Penelope naked.
    with dissolve

    pause 0.75

    scene v16s71a_2e   # same as v16s71a_2a but MC and Penlope naked.
    with dissolve

    pause 0.75

    scene v16s71a_2f   # MC(smiling, mouth closed) eases Penlope (smiling, fuck me eyes, mouth closed, looking at MC) to lie back on the Dean's desk by her throat.
    with dissolve

    pause 0.75

    # -We enter the Foreplay Free Roam. MC can click on her Neck, Boobs, Feet or Vagina. Clicking on her Vagina will end the free roam-
    #!  v16s71a_sex_screen     Penelope(smiling sexy, fuck me eyes, mouth closed) laying on her back on the Dean's desk, legs draped over each side of the corner showing her vagina and feet, looking at the camera. MC can click on her Neck, Boobs, Feet or Vagina. Clicking on her Vagina will end the free roam-
    call screen sex_overlay("v16s71a_continue")

    # -if Neck
label v16s71a_neck:

    # -MC chooses event1 or event2
    # -event1 Kiss neck
    # -event2 Choke her
    menu: 

        "Kiss neck": # -if Kiss neck

            # -MC kisses Penelope's neck-
            scene v16s71a_3    # TPP Penelope (eyes closed, smiling, mouth open) enjoying MC(eyes closed) kissing her neck where it meets the shoulder.
            with dissolve
            
            pe "Mmm, yeah, I like that."

            scene v16s71a_3a   # TPP Penelope(eyes closed, smiling, mouth open) head turned toward camera, enjoying MC(eyes closed) kissing the middle of her neck.
            with dissolve

            pe "I cannot get enough of your kisses, [name]."

            scene v16s71a_3b   # TPP Penelope (eyes closed, smiling, mouth open) head turned, back arched, enjoying MC(eyes closed) kissing where her neck and ear meet. 
            with dissolve

            pe "Mmm, this is making me so... horny."

        "Choke her": # -if Choke her

            # -MC puts his hand around Penelope's neck, squeezing-
            scene v16s71a_4    # TPP Penelope (eyes open, shocked, smiling, mouth slight gasping) suprised, looking at MC(eyes open looking at Penelope, smiling, mouth closed) who has his hand gripped firmly around her throat.
            with dissolve

            pe "*Gasps*"            

            pe "Oh... Ha. *Moans*"

            scene v16s71a_4a   # TPP Penelope (eyes open, fuck me eyes, smiling, mouth closed) looking at MC (eyes open looking at Penelope, smiling, mouth open) who has his hand gripped firmly around her throat.
            with dissolve

            u "You like that?"

            scene v16s71a_4b   # TPP Penelope (eyes open, fuck me eyes, smiling, mouth open) with both hands grasping MC's hand that chokes her looking at MC (eyes open looking at Penelope, smiling, mouth closed) who has his hand gripped firmly around her throat (maybe he her cheeks/face just turn slightly pinkish to show mild choking-- not much; he's not trying to kill her--subtle).
            with dissolve

            pe "I-I do."            

            pe "I want you to take control."
            
    # -Return to free roam-
    call screen sex_overlay("v16s71a_continue")

    # -if Boobs
label v16s71a_boobs:

    # -MC chooses event1 or event2
    # -event1 Massage boobs
    # -event2 Suck boobs
    menu:

        "Massage boobs": # -if Massage boobs

            # -MC massages Penelope's boobs-
            scene v16s71a_5    # TPP Penelope (smiling, mouth open,looking at MC) enjoying MC (smiling, mouth closed, looking at Penelope) massaging her boobs (erect nipples) with his hands.
            with dissolve
            
            pe "Do you like my boobs?"

            scene v16s71a_5a   # TPP Penelope (smiling, mouth closed, head back biting her lip) enjoying MC (smiling, mouth open, looking at Penelope) massaging her boobs (erect nipples) with his hands.
            with dissolve

            u "Yeah, a lot."

            scene v16s71a_5b   # TPP Penelope (smiling, mouth open, looking at MC's thumbs on her nipples) enjoying MC (smiling, mouth closed, looking at Penelope) massaging her boobs (erect nipples) with his hands and thumbs on her nipples.
            with dissolve

            pe "*Giggles* I like it when you play with them."            

            pe "Mmm..."

        "Suck boobs": # -if Suck boobs

            # -MC sucks on Penelope's boobs-
            scene v16s71a_6    # TPP Penelope (aroused/excited, smiling, mouth slight gasped open) looking at MC (eyes closed) sucking on her erect nipple. 
            with dissolve

            pe "Oh, fuck... your mouth feels so good."

            scene v16s71a_6a   # TPP Penelope (eyes closed, aroused/excited, smiling, head back, bitting lip) holding on to the back of MC's head while MC (eyes closed) sucking on her other erect nipple.
            with dissolve

            u "Mm-hmm."
            
            pe "Mmm..."

            scene v16s71a_6b   # TPP Penelope (aroused/excited, smiling, mouth open) looking at MC (eyes closed) sucking on her erect nipple. 
            with dissolve

            pe "You're making me really wet, [name]."

            scene v16s71a_6c   # FPP Penelope (aroused/excited, smiling, mouth closed) looking at MC who has a view full of her boobs and her face.
            with dissolve

            u "Am I?"

            scene v16s71a_6d   # FPP Penelope (aroused/excited, smiling, fuck me eyes, mouth open) looking at MC who has a view full of her boobs and her face.
            with dissolve

            pe "Yes... And you need to do something about it."            

    # -Return to free roam-
    call screen sex_overlay("v16s71a_continue")

    # -if Feet
label v16s71a_feet:

    # -MC chooses event1 or event2
    # -event1 Massage feet
    # -event2 Suck toes
    menu:

        "Massage feet": # -if Massage feet

            # -MC massages Penelope's foot-
            scene v16s71a_7   # TPP Penelope (excited, smiling mouth open) looking at MC (smiling, mouth closed) who holds her leg in front of him and is massaging her foot.
            with dissolve
            
            pe "Ooh, a foot massage?"
            
            pe "You're really spoiling me, [name]. *Giggles*"

            scene v16s71a_7a  # TPP Penelope (excited, smiling mouth closed) looking at MC (smiling, mouth open) who holds her leg in front of him and is massaging her foot.
            with dissolve

            u "I need to give you some attention before it's my turn."

            scene v16s71a_7
            with dissolve

            pe "Oh, no... *Giggles* What are you going to do to me?"

            scene v16s71a_7a
            with dissolve

            u "You're about to find out."            

        "Suck toes": # -if Suck toes

            # -MC sucks on Penelope's toes-
            scene v16s71a_8   # TPP Penelope (smiling, mouth open,looking at MC) taken by surprise as MC (looking at Penelop) licks the bottom of Penelope's foot that he holds up in the air.
            with dissolve

            pe "Oh, fuck, [name]."

            scene v16s71a_8a  # TPP Penelope (smiling, mouth closed) enjoying MC (looking at Penelop) lick the bottom of Penelope's foot that he holds up in the air.
            with dissolve

            pe "Mmm..."

            scene v16s71a_8b  # TPP Penelope (eyes closed, aroused/excited, mouth open, head back, enjoying MC(only showing his mouth) suck on her big toe.
            with dissolve

            pe "I didn't even know this would feel like this... *Gasps*"            

            pe "That feels... amazing."

            scene v16s71a_8c  # Same as v16s71a_8b, but Penleope arching her back in pleasure.
            with dissolve

            pe "*Moans* Oh, fuck."            

    # -Return to free roam-
    call screen sex_overlay("v16s71a_continue")

    # -if Vagina
    # -The option appears to end the free roam-
label v16s71a_continue:
    # -End of free roam-

    image v16pensex = Movie(play="images/v16/scene71a/v16pensex.webm", loop=True, image="images/v16/scene71a/v16pensexStart.webp", start_image="images/v16/scene71a/v16pensexStart.webp")
    image v16pensex2 = Movie(play="images/v16/scene71a/v16pensex2.webm", loop=True, image="images/v16/scene71a/v16pensex2Start.webp", start_image="images/v16/scene71a/v16pensex2Start.webp")
    image v16pensexf = Movie(play="images/v16/scene71a/v16pensexf.webm", loop=True, image="images/v16/scene71a/v16pensexStart.webp", start_image="images/v16/scene71a/v16pensexStart.webp")
    image v16pensex2f = Movie(play="images/v16/scene71a/v16pensex2f.webm", loop=True, image="images/v16/scene71a/v16pensex2Start.webp", start_image="images/v16/scene71a/v16pensex2Start.webp")
 

    scene v16s71a_10  # TPP Penelope(excitedly anxious, horny smiling, mouth closed) looking into MC's eyes laying back on the dean's desk, while MC(smiling, mouth open) stands between her spread legs with his penis positioned to enter her vagina looking into her eyes
    with dissolve

    u "I've been looking forward to this since the day I met you, Penelope."

    scene v16s71a_10a # FPP Penelope(excited, horny, smiling, mouth open) looking into MC eyes, MC's hands around her neck and throat can be seen.
    with dissolve

    pe "Ha... Yeah, I've... *Gasps*"    

    pe "I've been waiting for this, too."
    
    # -ANIMATION 1: MC with hand around Penelope's throat, penetrating her while she is lying on her back on the desk-

    scene v16pensex # ignore as animation
    with dissolve
    
    pe "And your dick is so fucking... big. *Moans*"
   
    scene v16pensex2 # ignore as animation
    with dissolve

    u "You like how it feels?"

    scene v16pensexf # ignore as animation
    with dissolve

    pe "Mmhmm."

    scene v16pensex2f # ignore as animation
    with dissolve

    pe "I love it."
    
    # -END ANIMATION 1-

    # -MC lifts Penelope up, and he turns to the shelves behind them, carrying her, face to face-
    scene v16s71a_11  # TPP MC(smiling, mouth closed) by the corner of the desk, now holds Penelope(excited, looking at MC, mouth closed) while his penis remains inside her vagina.
    with dissolve

    pause 0.75

    scene v16s71a_11a # TPP MC(smiling, mouth closed) holds Penelope(eyes closed, head back, mouth slightly open) against right side bookshelf of the Deans office while his penise remains inside her vagina. 
    with vpunch

    pause 0.75

    scene v16s71a_11b # FPP Penlope(smiling, excited, mouth open) looking at MC. 
    with dissolve

    pe "Oh my - Fuck, [name], you're so strong!"

    # -ANIMATION 2: Face to face, with MC holding Penelope off the ground, he penetrates her up against the shelves-
    image v16penst = Movie(play="images/v16/scene71a/v16penst.webm", loop=True, image="images/v16/scene71a/v16penstStart.webp", start_image="images/v16/scene71a/v16penstStart.webp")
    image v16penst2 = Movie(play="images/v16/scene71a/v16penst2.webm", loop=True, image="images/v16/scene71a/v16penst2Start.webp", start_image="images/v16/scene71a/v16penst2Start.webp")
    image v16penstf = Movie(play="images/v16/scene71a/v16penstf.webm", loop=True, image="images/v16/scene71a/v16penstStart.webp", start_image="images/v16/scene71a/v16penstStart.webp")
    image v16penst2f = Movie(play="images/v16/scene71a/v16penst2f.webm", loop=True, image="images/v16/scene71a/v16penst2Start.webp", start_image="images/v16/scene71a/v16penst2Start.webp")

    scene v16penst # ignore as animation
    with dissolve

    pe "Shiiit... You're so deep.... *Gasps*"

    scene v16penst2 # ignore as animation
    with dissolve

    u "Your body is perfect..."

    scene v16penstf # ignore as animation
    with dissolve

    u "You're so fucking hot, Penelope."

    scene v16penst2f # ignore as animation
    with dissolve

    pe "Mmm... Keep talking to me like that and I'm going to cum, [name]."    

    # -END ANIMATION 2-

    # -MC puts Penelope down so she's standing. With his hand on her arm, MC moves Penelope to the Dean's chair, bending her over for doggie style-

    # -ANIMATION 3: MC penetrates Penelope from behind, with one hand on her shoulder, the other hand on her hip-

    image v16pendg = Movie(play="images/v16/scene71a/v16pendg.webm", loop=True, image="images/v16/scene71a/v16pendgStart.webp", start_image="images/v16/scene71a/v16pendgStart.webp")
    image v16pensdg2 = Movie(play="images/v16/scene71a/v16pendg2.webm", loop=True, image="images/v16/scene71a/v16pendg2Start.webp", start_image="images/v16/scene71a/v16pendg2Start.webp")
    image v16pendgf = Movie(play="images/v16/scene71a/v16pendgf.webm", loop=True, image="images/v16/scene71a/v16pendgStart.webp", start_image="images/v16/scene71a/v16pendgStart.webp")
    image v16pensdg2f = Movie(play="images/v16/scene71a/v16pendg2f.webm", loop=True, image="images/v16/scene71a/v16pendg2Start.webp", start_image="images/v16/scene71a/v16pendg2Start.webp")

    scene v16s71a_12  # TPP Penelope(smiling, mouth open) standing by the right bookshelf facing the Dean's chair, with MC(smiling, mouth closed) standing behind her. Penelope is slightly looking back at MC.
    with dissolve
    
    pe "Yes! *Moans* Fuck me on the Dean's chair..."

    scene v16pendg # ignore as animation
    with dissolve

    u "*Grunts*"

    pe "*Panting* Oh, fuck..."

    scene v16pensdg2 # ignore as animation
    with dissolve

    pe "This feels so bad..."

    pe "We're being so naughty."
    
    scene v16pendgf # ignore as animation
    with dissolve

    u "You like being naughty, huh?"

    pe "Hehe... I do."    

    pe "*Moans* Harder, [name]..."

    scene v16pensdg2f # ignore as animation
    with dissolve

    u "Mmm, fuck! *Grunts*"
    
    pe "I'm gonna cum!"

    pe "I'm- *Moans*"

    u "Cum for me."

# -END OF ANIMATION 3- 

    scene v16s71a_12a # TPP Frame of v16pensdg2f animation with MC(neutral, mouth closed) thrusting forward and Penelope(orgasming hard, eyes closed, mouth open)
    with vpunch
    
    pe "Oh... Fuuuck..."

    scene v16s71a_12b # TPP Frame of v16pensdg2f animation with MC(neutral, mouth closed) thrusting forward and Penelope(very happy, stress free, smiling, mouth open).
    with vpunch
    
    pe "*Gasps*"

    scene v16s71a_12c # TPP Frame of v16pensdg2f animation with MC(neutral, mouth open) thrusting forward and Penelope(very happy, stress free, smiling, mouth closed).
    with dissolve

    u "I'm almost ready, too."

    scene v16s71a_12b
    with dissolve

    pe "*Panting* Here, let me finish you off."
    
    scene v16s71a_13  # TPP MC (smiling, mouth open) pushing Penelope (smiling, mouth closed) to sit down in the Dean's chair

    with dissolve
    
    # -MC sits on the Dean's desk-

    u "Sit down."

    scene v16s71a_13a # TPP Penelope(smiling, seductive eyes looking up at MC, mouth open) siting in the Dean's chair (between MC's legs ) while her right hand holds MC's dick, her thumb on the head of MC's dick. MC(smiling, mouth closed) looking down at Penelope.
    with dissolve

    pe "Yes sir."

    # -Penelope sits on the Dean's chair. MC is sitting on the desk in front of her-

    # -ANIMATION 4: With Penelope sat in the chair and MC sat on the desk with foot up on chair armrest, she gives MC oral, his hand on the top of her head-
    image v16penbj = Movie(play="images/v16/scene71a/v16penbj.webm", loop=True, image="images/v16/scene71a/v16penbjStart.webp", start_image="images/v16/scene71a/v16penbjStart.webp")
    image v16pensdbj2 = Movie(play="images/v16/scene71a/v16penbj2.webm", loop=True, image="images/v16/scene71a/v16penbj2Start.webp", start_image="images/v16/scene71a/v16penbj2Start.webp")
    image v16penbjf = Movie(play="images/v16/scene71a/v16penbjf.webm", loop=True, image="images/v16/scene71a/v16penbjStart.webp", start_image="images/v16/scene71a/v16penbjStart.webp")
    image v16pensdbj2f = Movie(play="images/v16/scene71a/v16penbj2f.webm", loop=True, image="images/v16/scene71a/v16penbj2Start.webp", start_image="images/v16/scene71a/v16penbj2Start.webp")

    scene v16penbj # ignore as animation
    with dissolve

    u "*Groans* Holy..."

    u "Fuck, Penelope. You're so damn good..."

    pe "Mmhmm!"    

    scene v16pensdbj2 # ignore as animation  
    with dissolve

    pe "*Gagging*"
    
    u "*Moans*"
    
    u "Fuck..."

    scene v16penbjf # ignore as animation
    with dissolve

    u "Me..."

    pe "Mmm..."

    u "*Gasps* Fuck, I'm gonna cum..."
    
    scene v16pensdbj2f # ignore as animation
    with dissolve

    pe "*Gagging*"

    # -END OF ANIMATION 4-

    scene v16s71a_14  # TPP frame from v16penbjf where Penelope has MC's dick deep in her mouth, MC (orgasming hard, eyes closed, mouth closed) has his hands on the back of Penelope's head.
    with vpunch

    u "*Groans* Fuuuck..."    

    scene v16s71a_14a # FPP Same position as v16s71a_14, Penelope(happy, smiling, mouth closed with cum on the corner of her mouth) looking at MC.
    with dissolve

    pause 0.75

    scene v16s71a_14b # FPP Same position as v16s71a_14, Penelope(happy, smiling, mouth closed with cum on the corner of her mouth) using her finger to push the cum on her mouth into her mouth while looking at MC.
    with dissolve

    pause 0.75

    scene v16s71a_14c # FPP Same position as v16s71a_14, Penelope(happy, smiling, mouth closed, swallowing) looking at MC.
    with dissolve

    pe "*Moans* Mmm..."

    # -MC cums in her mouth, a little spilling out on her lips, which she wipes off with the back of her hand. She smiles at MC-

    # -Then Penelope looks over to the door, suddenly in shock-

    scene v16s71a_14d # FPP Same position as v16s71a_14, Penelope(shocked, concenred, mouth open big) looking towards the door of the Dean's office.
    with dissolve

    pe "Oh, shit! The door is open!"

    label v16_end_2:
        show screen save_now(17)
        with Fade(1,0,1)

        " "
    jump v17start

