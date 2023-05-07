# SCENE 5: Imre vs Caleb
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Josh (Outfit 2), Imre (Outfit 4), Caleb (Outfit 2)
# Time: Saturday Night

label v10_imre_vs_caleb_fight:
    play music "music/v10/Track Scene 4.mp3" fadein 2
    scene v10ivc3b # TPP. Show Josh in the ring strolling around as if he's adressing a crowd, mouth open.
    with fade

    jo "Well, the show must go on."
    
    jo "After this small delay, we're now finally ready for the first fight of the night."
    
    jo "Imre versus Caleb!"

    scene v10ivc4b # TPP. Show Imre stepping into the ring.
    with dissolve

    pause 0.75

    scene v10ivc5b # TPP. Show Caleb stepping into the ring.
    with dissolve

    pause 0.75

    scene v10ivc6 # TPP. Show Josh addressing both Imre and Caleb who are stood in opposite corners of the ring, Caleb and Imre angrily starring at eachother, Josh mouth open.
    with dissolve

    jo "Don't kill each other, stay in the ring, yada, yada, yada. Have fun!"

    scene v10ivc7 # TPP. Show Josh leaving the ring, Imre and Caleb stepping up closer to eachother, guards up, starring angrilly, Caleb mouth open.
    with dissolve

    cal "You better be ready, cause I'm about to dance circles around you."

    scene v10ivc8 # TPP. Show Imre, imre drops his guard and sarcastically laughs, mouth open.
    with dissolve 

    imre "Hope you're watching ladies!"

    scene v10ivc9 # TPP. Show Caleb swinging a punch at Imre, Imre dodges to the side easilly.
    with dissolve

    pause 0.75

    scene v10ivc9a # TPP. Same as ivc9, show Imre, returning from his dodge with a punch square to Caleb's jaw, Caleb in pain, begins to fall.
    with hpunch

    play sound sound.hit

    pause 0.75

    scene v10ivc9b # TPP. Same as ivc9, Caleb now knocked out on the floor, Imre stood over him with a saractic smile.
    with dissolve

    play sound sound.fall

    pause 1

    scene v10ivc10 # TPP. Show Josh climbing back into the ring, mouth open looking at Caleb on the floor.
    with dissolve

    jo "Doesn't look like he's getting up anytime soon! Not sure any of us expected this to happen so quickly... Is he alive?"

    scene v10ivc11 # TPP. Show Josh walking around the ring as if he's announcing again, Josh smile.
    with dissolve

    jo "Ah, who cares, this is fight night."

    scene v10ivc12 # TPP. Show Josh now stood with Imre, Josh looking at Imre, both smiling, Josh mouth open.
    with dissolve
    
    jo "Anyways, looks like we have a winner everyone! Most likely in record time!"

    jo "Any words to the crowd after that amazing performance?"

    scene v10ivc12a # TPP. Same as ivc12, Imre mouth open.
    with dissolve

    imre "To all the fine ass ladies out there, that was for you."

    scene v10ivc12
    with dissolve

    jo "Sounds like you know what you're here for!"
    stop music fadeout 3
    jump v10_mc_vs_imre_fight
