# SCENE 8: Fight Results
# Locations: Abandoned Warehouse
# Characters: Ryan (Outfit 2), Josh (Outfit 2),MC (Outfit 7), Grayson (Outfit 3),Imre (Outfit 4), Sebastian (Outfit 1),Cameron (Outfit 3),Chris (Outfit 2)
# Time: Saturday Night
label v10_fight_result:
    $ renpy.end_replay()
    
    scene v10fr1 # FPP. Show close up of Josh pointing down towards the floor, slight smile, mouth open
    with dissolve
    
    jo "*Laughs* In the words of Smokey, \"you got knocked the fuck out!\""

    play music music.ck1.v10.Track_Scene_8 fadein 2

    if joinwolves:
        if v10_ryan_win: # -If MC wins the fight against Ryan-
            scene v10fr1
            with dissolve

            jo "I think as we all expected, [name] has dominated! So ladies if you're itching for a winner tonight, I found one."

            jo "Anything from the man himself?"

            scene v10fr2 # TPP. Show close up of MC hands in the air above head, excited face, mouth closed
            with dissolve

            if reaction == 0.5:
                $ grant_achievement("lights_out")

            u "This wasn't just a fight for me, it was a fight for me and my brothers."

            u "This is our win!"

            scene v10fr3 # TPP. Show MC and Josh standing in ring, ryan on the floor in the ring, Josh mouth open
            with dissolve

            jo "Glad to see the excitement! Congratulations on a well deserved win."

            scene v10fr5 # FPP. Show close up of MC exiting the ring, mouth closed
            with dissolve

            pause 0.75

            scene v10fr4 # FPP. Show chris and sebastian, chris one hand up in the air, excited face, chris mouth open, sebatian mouth closed
            with dissolve

            ch "*Wolf howls* You did us proud man, great fucking job!"

            u "(I fucking did it!)"
            
            u "(Phew, I'm so exhausted now... I just wanna go to bed.)"
            
            stop music fadeout 3

            jump v10_leave_fight

        else:
            scene v10fr3b # TPP. Show imre and Josh standing in ring, MC on the floor in the ring, Josh mouth open, imre mouth closed
            with dissolve
            jo "I definitely didn't see that happening, I don't think anyone did. Any words from the man himself?"

            scene v10fr3a # TPP. Show Ryan and Josh standing in ring, MC on the floor in the ring, Josh mouth closed, Ryan mouth open
            with dissolve

            ry "I worked hard for this and I got it! Wolves fucking suck!"

            scene v10fr3b # TPP. Show Ryan and Josh standing in ring, MC on the floor in the ring, Josh mouth open, Ryan mouth closed
            with dissolve

            jo "Glad to see the excitement! Congratulations on a well deserved win."

            scene v10fr6 # TPP. Show Ryan helping MC get up, Ryan mouth open, Mc mouth closed
            with dissolve

            ry "Hope you're alright, man. Can't afford to be a friend in a fight. You good?"

            scene v10fr7 # FPP. Show ryan in ring, neutral look, mouth closed
            with dissolve

            u "Yeah, I'm alright. Congrats."

            scene v10fr5
            with dissolve

            pause 0.75

            scene v10fr4a # FPP. Show chris and sebastian, both slight frown, chris mouth open, sebastian mouth open
            with dissolve

            ch "Losing's always hard, but you put up a good fight."

            scene v10fr4b # FPP. Show chris and sebastian, both slight frown, chris mouth closed, sebastian mouth closed
            with dissolve

            u "Sorry, Chris. I really wanted to do better."

            scene v10fr4a # FPP. Show chris and sebastian, both slight frown, chris mouth open, sebastian mouth open
            with dissolve

            ch "That's alright, man. You'll get him next time."

            scene v10fr4b # FPP. Show chris and sebastian, both slight frown, chris mouth closed, sebastian mouth closed
            with dissolve

            u "(Fuck, I let my entire frat down...)"

            u "(God, I just wanna go to bed.)"

            stop music fadeout 3

            jump v10_leave_fight

    else:
        if v10_imre_win:
            scene v10fr1
            with dissolve

            jo "I think as we all expected, [name] has dominated! So ladies if you're itching for a winner tonight, I found one."

            jo "Anything from the man himself?"

            scene v10fr2
            with dissolve

            if reaction == 0.5:
                $ grant_achievement("golden_boy")

            u "This wasn't just a fight for me, it was a fight for me and my brothers."

            u "This is our win!"

            scene v10fr3c # TPP. Show MC and Josh standing in ring, Imre on the floor in the ring, Josh mouth open
            with dissolve

            jo "Glad to see the excitement! Congratulations on a well deserved win."

            scene v10fr4c # FPP. Show Grayson and cameron, both slight smile, grayson mouth open, cameron mouth closed
            with dissolve

            gr "*Chanting* Apes! Apes! Apes!"
            gr "Fuck yeah, man!"

            u "(I fucking did it!)"
            
            u "(Phew, I'm so exhausted now... I just wanna go to bed.)"

            stop music fadeout 3

            jump v10_leave_fight
        
        else:
            scene v10fr3d # TPP. Show imre and Josh standing in ring, MC on the floor in the ring, Josh mouth open, imre mouth closed
            with dissolve

            jo "I definitely didn't see that happening, I don't think anyone did. Any words from the man himself?"

            scene v10fr3e # TPP. Show imre and Josh standing in ring, MC on the floor in the ring, Josh mouth closed, imre mouth open
            with dissolve

            imre "WOLVES FOR LIFE! Also, ladies hit me up."

            scene v10fr3d
            with dissolve

            jo "Glad to see the excitement! Congratulations on a well deserved win."

            scene v10fr5 # FPP. Show close up of MC exiting the ring, mouth closed
            with dissolve

            pause 0.75

            scene v10fr4d # FPP. Show grayson and cameron, both slight frown, grayson mouth open, cameron mouth closed
            with dissolve

            gr "That was absolute shit, man! You gotta do better if you wanna rep the Apes!"

            scene v10fr4e # FPP. Show grayson and cameron, both slight frown, grayson mouth closed, cameron mouth closed
            with dissolve

            u "Right, I'm sorry..."

            scene v10fr4d # FPP. Show grayson and cameron, both slight frown, grayson mouth open, cameron mouth closed
            with dissolve
            
            gr "Sorry's not fucking good enough. I saw something in you, don't make me regret it."

            u "(Fuck, I let my entire frat down...)"
            
            u "(God, I just wanna go to bed.)"
            
            stop music fadeout 3
            
            jump v10_leave_fight