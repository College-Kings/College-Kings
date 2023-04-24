# SCENE 45) Hotle lobby Fancy Dinner
# Locations: Hotel lobby,sidewalk, shuttle, restraunt
# Characters: MC (Outfit 3), Penelope (outfit1), Samantha (outfit1), Cameron (outfit1), Emily (outfit2), Josh(outfit1), Riley(Outfit 2), amber(outfit 2), Mr Lee(outfit 1), imre(outfit 1), ryan(outfit 1), nora(Outfit 2), chloe(outfit 1), chris(outfit 1), ms rose (outfit 1)
# Time: evening
label v11_lobby_mrlee:
    scene v11lob1 # FPP. Show Mr Lee, slight smile mouth open, stood in hotel lobby
    with dissolve
    play music "music/v11/Track Scene 9a_1.mp3" fadein 2
    lee "Students, so far it has been an absolute pleasure traveling with you all."

    scene v11lob2 # FPP. Show Nora and chris stood together, slight annoyed faces
    with dissolve

    lee "From the long plane ride here..."

    scene v11lob3 # FPP. Show Riley and amber looking at each other giggling.
    with dissolve

    lee "To the sights of, what would be underage students drinking at the bar..."

    if v11_pen_goes_europe:
        scene v11lob4 # FPP. Show Penelope slight smile
        with dissolve

        lee "The nostalgia while being at the museum and the deep dive into a dinosaur debate..."
    
    else:
        scene v11lob1
        with dissolve

        lee "The nostalgia while being at the museum and the deep dive into a dinosaur debate..."

    scene v11lob5 # FPP. Show Ryan and imre annoyed look at each other
    with dissolve

    lee "The teaching of maturity and manhood..."
  
    if emily_europe:
        scene v11lob6 # FPP. Show Chloe and lindsey slight smile
        with dissolve

        lee "The feeling of fantasy as we rode in the carriages..."

        scene v11lob7 # FPP. Show Emily, slight sad face
        with dissolve

        lee "Even the most trying times are moments that I look back on with great satisfaction. From every trial, there is much to be learned."
    
    else:
        scene v11lob1
        with dissolve
        
        lee "The feeling of fantasy as we rode in the carriages..."

        lee "Even the most trying times are moments that I look back on with great satisfaction. From every trial, there is much to be learned."
    
    if v11_invite_sam_europe:
        scene v11lob8 # FPP. Show samantha and cameron neutral look
        with dissolve

        lee "I know many of you were really looking forward to this trip, and I hope that so far it has reached your expectations, but if not... There are many more opportunities ahead."
    
    else:
        scene v11lob1
        with dissolve

        lee "I know many of you were really looking forward to this trip, and I hope that so far it has reached your expectations, but if not... There are many more opportunities ahead."

    if josh_europe:
        scene v11lob9 # FPP. Show josh, grinning, rubbing hands together. 
        with dissolve

        lee "To end our time here in London before we take off on our next Europe adventure, I'll be treating everyone to a wonderful dinner."
    
    else:
        scene v11lob1
        with dissolve

        lee "To end our time here in London before we take off on our next Europe adventure, I'll be treating everyone to a wonderful dinner."

    scene v11lob10 # FPP. Show imre, hands in the air, big smile mouth open
    with dissolve

    imre "LET'S GOOOOO!"

    scene v11lob1
    with dissolve

    lee "*Laughs* Throughout it all, food will always have a special way of bringing everyone together."
    lee "Tonight, we celebrate the experiences we've had so far and the fact that you're all legally allowed to drink here. *Chuckles* Please drink responsibly."
    lee "Now, the shuttles are prepared and ready to go so let's get moving."

    scene v11lob1a # FPP. same 1, mouth closed
    with dissolve

    u "(People can say what they want, even I have said some things about him in the past, but Mr. Lee really is such a cool guy...)"

    scene v11lob11 # TPP. Show mr. Lee, and a couple of the students walking through the front door (can be any from within the scene except Penelope, Samantha, Cameron, Emily and Josh)
    with dissolve

    pause 1

    scene v11lob12 # TPP. Show Mr. Lee and a couple of the students getting on the shuttle (again can be any from the scene except Penelope, Samantha, Cameron, Emily and Josh)
    with dissolve

    pause 1

    stop music fadeout 3
    play music "music/v11/Track Scene 7_3.mp3"

    scene v11lob22 # TPP. Show Mr Lee and a couple of the students walking through the entrance of the restraunt. 
    with dissolve

    pause 1

    scene v11lob13 # FPP. Show Mr Lee. in the restraunt, mouth open slight smile
    with dissolve
    lee "Please everyone, sit wherever you'd like. They only allow two to a table so, choose enjoyable company. *Chuckles* I'll be sitting with anyone except for Ms. Rose..."

    scene v11lob14 # fPP. Show Ms. Rose annoyed look, mouth open
    with dissolve

    ro "*Scoffs* Bruce!"

    scene v11lob13
    with dissolve

    lee "*Chuckles* I'm just teasing."

    scene v111lob14 # FPP. MC looks around and sees Amber with Riley, Nora with Chloe (pose Chloe as if she's asking Nora to sit), and Lindsey with Charli-
    with dissolve

    u "(Hmm, who to sit with?)"

    if v11_lauren_caught_aubrey:
        # -MC sees Aubrey sitting by herself-

        scene v11lob15 # FPP. Show aubrey sat alone, slight sad look
        with dissolve
        u "(I'll sit with Aubrey.)"

        scene v11lob16 # TPP. Show MC now stood at the table by the empty table opposite aubrey, mouth open
        with dissolve

        u "This seat taken?"

        scene v11lob23 # FPP. Show aubrey slight smile mouth open (camera as if mc is still stood.)
        with dissolve

        au "It is now."

        scene v11lob17 # TPP. Show MC now sat opposite aubrey
        with dissolve

        pause 1
        
        stop music fadeout 3
        jump v11_dinner_with_aubrey

    elif CharacterService.is_girlfriend(lauren):
        scene v11lob18 # FPP. Show Lauren sat alone, slight sad look
        with dissolve

        u "(Lauren, of course.)"

        scene v11lob19 # TPP. Show MC now stood at the table by the empty table opposite Lauren, mouth open
        with dissolve

        u "This seat taken?"

        scene v11lob20 # FPP. # FPP. Show Lauren slight smile mouth open (camera as if mc is still stood.)
        with dissolve

        la "Actually, I was just starting to wonder what was taking you so long. *Chuckles*"
        
        stop music fadeout 3
        jump v11_dinner_with_lauren

    else:
        menu:
            "Lauren":
                scene v11lob18 
                with dissolve

                u "(Lauren, of course.)"

                scene v11lob19 
                with dissolve

                u "This seat taken?"

                scene v11lob20
                with dissolve
                
                la "Haha, I was wondering when you'd get over here."
                
                stop music fadeout 3
                jump v11_dinner_with_lauren

            "Aubrey":
                scene v11lob15 
                with dissolve
                u "(I'll sit with Aubrey.)"

                scene v11lob16 
                with dissolve

                u "This seat taken?"

                scene v11lob16 
                with dissolve

                au "It is now."

                scene v11lob17
                with dissolve

                pause 1
                stop music fadeout 3
                jump v11_dinner_with_aubrey