# SCENE 32: MC picks up Aubrey at Chicks' house
# Locations: Sidewalk-exterior, Chicks' front yard-exterior, Chicks' side yard-exterior, Chicks' House backyard-exterior, Chloe's window-exterior, Aubrey's window-exterior, Chicks' front door-exterior, Chicks' front door-interior, Street infront of Chicks' house-exterior
# Characters: MC (Outfit: Homecoming Suit), CHLOE (Outfit: 1), AUBREY (Outfit: 7), RILEY (Outfit: 3) Sunday 
# Time: Morning

label v15s32: #32) MC picks up Aubrey at Chicks' house 
    scene v15s32_1 # TPP. MC, smiling mouth closed walking [Sidewalk-exterior].
    with dissolve

    pause 0.75

    scene v15s32_1a # TPP. Close up on MC, smiling, mouth closed walking [Sidewalk-exterior].
    with dissolve

    pause 0.75

    scene v15s32_1b # TPP. MC, smiling, mouth closed, standing still, thinking, eyes looking up, finger on chin [Sidewalk-exterior].
    with dissolve

    u "(Hmm, it's a special day for Aubrey... I could just knock on the door, or I could do something more romantic and funnier.)"
        
    menu:
        "Simple approach":
            $ add_point(KCT.BRO)
            
            scene v15s32_1a
            with dissolve
            
            u "(I won't overthink it. I'll just knock on the door like a regular person.)"

        "Be her Romeo":
            $ add_point(KCT.BOYFRIEND)
            
            # -MC walks around the back of the house, picking up some random pebbles en route. Then he looks up at two windows. One window has vines creeping up to it, which is Aubrey's window-
            scene v15s32_2 # TPP. MC smiling, mouth closed, walking left-to-right; front door in background) [Chicks' house front yard-exterior].
            with dissolve

            pause 0.75
            
            scene v15s32_3 # TPP. MC smiling, mouth closed, walking left-to-right; side of house in background). [Chicks' house side yard-exterior].
            with dissolve

            pause 0.75

            scene v15s32_4 # TPP. MC smiling, mouth closed, walking left-to-right; back of house in the background). [Chicks' house back yard-exterior].
            with dissolve

            pause 0.75

            scene v15s32_4a # TPP. MC smiling, mouth closed, standing looking up at the second story of the house [Chicks' house back yard-exterior].
            with dissolve

            pause 0.75

            scene v15s32_4b # FPP. MC looking at the the two windows of Chloe and Aubrey's bedroom on the second floor [Chicks' house back yard-exterior].
            with dissolve

            u "(This'll be funny. It happens in all the corny romance movies, right? Now, which window do I aim at?)"

            menu:
                "Left window":
                    # -MC throws a pebble at the left window. It opens and Chloe looks out -
                    scene v15s32_4c # FPP. MC grabbing a pebble on the ground [Chicks' house back yard-exterior].
                    with dissolve

                    pause 0.75

                    scene v15s32_4d # TPP. MC smiling, mouth closed, winding up to throw the pebble at the window [Chicks' house back yard-exterior].
                    with dissolve

                    pause 0.75

                    # TODO: Rock hitting window sound effect [No mp3 found in current assets]
                    scene v15s32_4e # FPP. Close up on the pebble hitting the window [Chicks' house back yard-exterior]
                    with dissolve
                    
                    pause 0.75

                    scene v15s32_5 # FPP. Chloe, neutral, mouth closed, rasing her window [Chloe's window (left)-exterior].
                    with dissolve

                    pause 0.75

                    scene v15s32_5a # FPP. Chloe, neutral, mouth open, with her upper body leaning out the window looking downward [Chloe's window (left)-exterior].
                    with dissolve

                    cl "[name]? Why are you throwing stones at my window?"

                    scene v15s32_4f # TPP. MC smiling, mouth open looking up toward Chloe's window (off camera) [Chicks' house back yard-exterior].
                    with dissolve

                    u "Oh- Shit! Sorry Chloe, wrong window! *Laughs*"

                    scene v15s32_4g # TPP. MC neutral, mouth open looking up toward Chloe's window (off camera) [Chicks' house back yard-exterior].
                    with dissolve

                    u "I was just trying to get Aubrey's attention. We're going to her parent's wedding ceremony today."

                    scene v15s32_5a
                    with dissolve

                    cl "Get her attention by... breaking her window?"

                    scene v15s32_4g
                    with dissolve

                    u "Not exactly... Just trying out those smooth rom com moves, haha." 

                    if chloe.relationship.value >= Relationship.GIRLFRIEND.value: # -if ChloeGF
                        $ chloeSus += 1
                        # -Chloe looks a little pissed-
                        scene v15s32_5b # FPP. Chloe, slightly angry, mouth open, with her upper body leaning out the window looking downward [Chloe's window (left)-exterior].
                        with dissolve
                        
                        cl "You're trying to be romantic?"

                        scene v15s32_4g
                        with dissolve

                        u "Well, yeah, like they do in the movies. But, more funny than romantic. I-"

                        scene v15s32_4h # TPP. MC mouth closed, concerned looking up toward Chloe's window (off camera) [Chicks' house back yard-exterior].
                        with dissolve

                        u "(Shit...)"

                        scene v15s32_4g
                        with dissolve

                        u "Don't think anything by it. I'm just being silly."

                        scene v15s32_5a
                        with dissolve

                        cl "Okay. Well, you go have fun while I'm working hard on my campaign." 

                    else:
                        scene v15s32_5c # FPP. Chloe, smiling, mouth open, with her upper body leaning out the window looking downward [Chloe's window (left)-exterior].
                        with dissolve
                        
                        cl "Aw, her very own Romeo! Have a nice time."

                        scene v15s32_4g
                        with dissolve

                        u "Thanks. I'm sure we will. Sorry again!"

                    scene v15s32_5d # FPP. Chloe, neutral, mouth closed, lowering her window [Chloe's window (left)-exterior].
                    with dissolve

                    u "(Nice going... *Sighs* Let's try again.)" 

                    jump v15s32_right_window

                "Right window":
                    label v15s32_right_window:
                    scene v15s32_4c
                    with dissolve

                    pause 0.75

                    scene v15s32_4d
                    with dissolve

                    pause 0.75

                    # TODO: Rock hitting window sound effect. No mp3 found in current assets
                    scene v15s32_4e
                    with dissolve
                    
                    pause 0.75

                    scene v15s32_6 # FPP. Aubrey, smiling, mouth closed, rasing her window [Aubrey's window (right)-exterior].
                    with dissolve

                    pause 0.75

                    scene v15s32_6a # FPP. Aubrey, smiling, mouth open, with her upper body leaning out the window looking downward [Aubrey's window (right)-exterior].
                    with dissolve
                    
                    au "Haha, doing the old pebble throwing thing, are we?"

                    scene v15s32_4i # TPP. MC smiling, mouth open, on one knee, looking up at Aubrey's window, one hand on his chest, and his other held out (https://thumbs.dreamstime.com/z/elegant-business-man-holding-one-hand-his-chest-presenting-something-59714356.jpg) [Chicks' house back yard-exterior].
                    with dissolve

                    u "My Juliet! Thou Romeo art here to whisk you away for a fine day of merriment!"
                    
                    u "Might thy accompany me in the horse-drawn carriage that awaits thy beauty like the..."

                    u "Pale... Moon...? Um... something. *Chuckles*"

                    scene v15s32_6a
                    with dissolve

                    au "*Laughs* What the hell are you even saying?"

                    scene v15s32_4j # TPP. MC smiling, mouth open, explaining (https://gcdn.daz3d.com/p/73843/i/z-talking-and-explaining-pose-mega-set-02-daz3d.jpg; bottom row, 2nd from left, man on right) [Chicks' house back yard-exterior].
                    with dissolve

                    u "I'm Romeo! You know... Shakespeare stuff?"

                    scene v15s32_6a
                    with dissolve

                    au "I know Shakespeare, handsome. Whatever you're doing right now is definitely not Shakespeare. *Laughs*"
                    
                    au "Nice try though!"

                    scene v15s32_4j
                    with dissolve

                    u "Thou art most welcome."

                    scene v15s32_6a
                    with dissolve

                    au "Come to the front door, Romeo."

                    scene v15s32_4k # TPP. MC smiling. mouth open, both hands over his the middle of his chest (https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX14371097.jpg) [Chicks' house back yard-exterior].
                    with dissolve

                    u "I will see you there, fair maiden."

                    scene v15s32_6b # FPP. Aubrey, smiling, mouth closed, lowering her window [Aubrey's window (right)-exterior].
                    with dissolve

                    pause 0.75

            scene v15s32_3a # TPP. MC smiling, mouth closed, walking right-to-left; side of house in background [Chicks' house side yard-exterior].
            with dissolve

            pause 0.75
    
    play sound "sounds/knock.mp3"

    scene v15s32_7 # TPP. MC, smiling, mouth closed, knocking on the front door [Chicks' front door-exterior]
    with dissolve

    pause 0.75
    
    if not aubrey_riley_awkward: # -if not AubreyRileyAwkward from theatre conversation
        scene v15s32_7a # FPP. Riley, neutral, mouth closed, opening the front door [Chicks' front door-exterior]
        with dissolve

        pause 0.75

        scene v15s32_7b # FPP. Riley, smiling, mouth open, opening the front door [Chicks' front door-exterior]
        with dissolve

        ri "Hey, the groom is here!"

        scene v15s32_7c # FPP. Riley, smiling, mouth closed, standing in the front doorway [Chicks' front door-exterior].
        with dissolve

        u "Haha, that's a scary thought... I'm way too young to get married." 

        u "How come you're still here?"

        scene v15s32_7d # FPP. Riley, smiling, mouth open, standing in the front doorway [Chicks' front door-exterior].
        with dissolve

        ri "I've been helping Aubrey get ready. And I've done a pretty good job if I can say so myself!"

        scene v15s32_7c
        with dissolve

        u "Aww, that's sweet of you." 

        if riley.relationship.value >= Relationship.FWB.value: # -if RileyRS
            scene v15s32_7e # FPP. Riley, smiling, mouth open, stepping aside gesturing for MC to enter the house [Chicks' front door-exterior].
            with dissolve

            ri "You look amazing by the way."

            scene v15s32_7f # TPP. MC smiling, mouth closed, stepping through the front door [Chicks' front door-exterior].
            with dissolve

            pause 0.75

            # -She smiles and they have a quick kiss-
            play sound "sounds/kiss.mp3"

            scene v15s32_8 # FPP. Riley kissing MC on the lips, Riley's back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
            with dissolve

            pause 0.75

            scene v15s32_8a # FPP. Riley smiling, mouth closed, her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
            with dissolve

            u "Ha, thanks." 
        # -regardless-

        scene v15s32_8b # FPP. Riley smiling, mouth open, her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve

        ri "She'll be down any minute now."
            
        ri "I'm so excited for you guys. You're gonna have a blast."

        scene v15s32_8c # FPP. Riley smiling, yelling mouth open, hands cupped around her mouth, eyes looking up stairs (behind MC) her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve

        ri "Hey, come on, Aubrey!" 

        # -Aubrey then starts coming down the stairs. We see her slow-motion from her feet to her head, revealing her full outfit-
        # Special scene wth 1920x5000 pic the pans from feet to head
        scene v15s32_8d: # TPP. Full body shot of Aubrey, smiling, at the bottom of the stairs, beautiful pose (pic resolution 1920x5000 slow vertical pan from feet to head) [Chicks' front door-interior].
            subpixel True
            yalign 1.0
            linear 6.0 yalign 0.0
        with fade

        pause
                
        # -MC is mesmerized by her-

        if aubrey.relationship.value >= Relationship.FWB.value: # -if AubreyRs
            scene v15s32_8e # TPP. MC happily surprised smiling, mouth open looking at Aubrey (off camera) with Riley behind him smiling, mouth closed with the front door still open [Chicks' front door-interior].
            with dissolve

            u "Oh-"
            
            u "(Holy...)"

            scene v15s32_8f # TPP. Close up on Riley, smiling, giggling, the front door open behind her [Chicks' front door-interior].
            with dissolve

            ri "*Giggles*"

            scene v15s32_8e
            with dissolve

            u "Wow, she looks... Incredible."

            scene v15s32_8g # TPP. Close up on Riley, smiling, mouth open, the front door open behind her [Chicks' front door-interior].
            with dissolve

            ri "You're a very lucky guy, [name]."

            scene v15s32_8e
            with dissolve

            u "Haha, I know." 

        # -Regardless-

        # -Aubrey approaches and stands at the front door next to MC-
        scene v15s32_8h # TPP. MC (big smile, mouth closed) and Aubrey (smiling mouth closed) standing together in front of the open front door, with Riley, standing next to Aubrey, smiling mouth open (camera is at the stairs facing the front door) [Chicks' front door-interior].
        with dissolve

        ri "I helped you get ready, and my jaw still dropped when you came down those stairs!"

        scene v15s32_8i # FPP. Aubrey smiling mouth open looking at Riley (off camera) stairs are behind her [Chicks' front door-interior].
        with dissolve

        au "Aww, thanks babe."

        scene v15s32_8j # FPP. Aubrey smiling mouth closed looking at MC stairs are behind her [Chicks' front door-interior].
        with dissolve

        pause 0.75

        if aubrey.relationship.value >= Relationship.FWB.value: # -if AubreyRs 
            u "She's right. You look absolutely stunning."
            
        else: # -if AubreyFriend
            u "Yeah, seriously... It was like seeing an actual princess coming down the stairs." 

        # -Regardless-

        # -Aubrey blushes a little-
        scene v15s32_8k # FPP. Aubrey smiling, bashful, cheeks blushing, mouth open looking at MC [Chicks' front door-interior].
        with dissolve

        au "Haha, okay... Stop it you two, I'm already wearing too much blush."
            
        if aubrey.relationship.value >= Relationship.FWB.value: # -if AubreyRs
            scene v15s32_8l # FPP. Aubrey smiling mouth open looking at MC stairs are behind her [Chicks' front door-interior]. 
            with dissolve
            
            au "And you... You look very handsome today, [name]."

            scene v15s32_8j
            with dissolve

            u "Thank you very much. I thought I'd make the effort, haha."

            scene v15s32_8l
            with dissolve

            au "I'm grateful that you did. *Chuckles*" 

        # -Regardless-

        au "It certainly beats your Halloween costume, ha!"

        scene v15s32_8j
        with dissolve

        u "Damn, I was hoping people would start forgetting about that thing..."

        scene v15s32_8m # FPP. Aubrey smiling, mouth closed, looking at Riley, smiling mouth open, looking at Aubrey [Chicks' front door-interior]. 
        with dissolve

        ri "*Laughs* That costume will go down in history!"

            
        # -Aubrey looks away briefly-
        scene v15s32_8n # FPP. Aubrey glancing at the front door (off camera), mouth closed, Riley, smiling mouth closed, looking at Aubrey [Chicks' front door-interior].
        with dissolve

        pause 0.75

        scene v15s32_8l
        with dissolve
        
        au "I didn't realize the car was already here! Let's get in before it drives away without us, haha."

        scene v15s32_8j
        with dissolve

        u "Good! We can stop talking about the costume."

        scene v15s32_8m
        with dissolve

        ri "*Giggles* For now..."
        
        # -All three are smiling. Riley waves as she watches from the front door. 
        scene v15s32_8o # TPP. Aubrey, Riley, MC smiling together (camera at the stairs facing the open front door where there is a limo parked at the street [Chicks' front door-interior]. 
        with dissolve

        pause 0.75

    else: # -if AubreyRileyAwkward from theatre conversation
        # -Riley opens the door for MC, looking tired-
        scene v15s32_7g # TPP. Riley, tired, mouth closed, opening the front door [Chicks' front door-exterior]
        with dissolve

        u "Oh, hey Riley. You're still here?"

        scene v15s32_7h # TPP. Riley, tired, mouth open, opening the front door [Chicks' front door-exterior]
        with dissolve

        ri "I fell asleep watching that movie, ha. I had nothing else to do so I started the sequel..."

        scene v15s32_7i # TPP. Riley, tired, yawning, standing in the front doorway [Chicks' front door-exterior].
        with dissolve

        pause 0.75

        scene v15s32_7j # FPP. Riley, tried, mouth open, stepping aside gesturing for MC to enter the house [Chicks' front door-exterior].
        with dissolve

        ri "*Yawns* I'm halfway through it."

        scene v15s32_7f
        with dissolve

        pause 0.75
        
        scene v15s32_8p # FPP. Riley, neutral, mouth closed, her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve

        u "They made a sequel?"

        scene v15s32_8q # FPP. Riley, neutral, mouth open, her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve

        ri "Yeah, The Poly Dilemma 2."

        scene v15s32_8p
        with dissolve

        u "How original."

        scene v15s32_8q
        with dissolve

        ri "Yeah, I think they're running out of ideas. He's trying to get four wives in this one."

        scene v15s32_8p
        with dissolve

        u "Damn, that guy never learns, does he?"

        scene v15s32_8q
        with dissolve

        ri "I still like the concept, but... It's not as good as the original."

        scene v15s32_8p
        with dissolve

        u "They never are, haha."

        scene v15s32_8q
        with dissolve

        ri "You're going to Aubrey's parent's wedding today, right?"

        scene v15s32_8p
        with dissolve

        u "Yeah, how do I look?"

        scene v15s32_8b
        with dissolve

        ri "You're looking very handsome... *Chuckles*"

        scene v15s32_8p
        with dissolve

        u "Well, thanks! But I'm handsome every day, so..."

        scene v15s32_8q
        with dissolve

        ri "Hmm, depends on who you ask, doesn't it?"

        scene v15s32_8r # FPP. Riley, tired, slight smile (smirk), mouth closed, her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve

        u "Haha, ouch!"

        scene v15s32_8s # FPP. Riley, tired, laughing, mouth open, her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve

        ri "*Laughs*"

        scene v15s32_8t # FPP. Riley smiling, mouth open eyes looking up stairs (behind MC) her back is toward the open front door, where the street is visible behind her [Chicks' front door-interior].
        with dissolve
        
        ri "Oh, here she is."
        
        # special scene where image is 1920x5000 and a pan from feet to head
        # -Aubrey starts walking down the stairs. We see her slow-motion from her feet to her head, revealing her full outfit-

        # -MC is mesmerized by her-
        # Special scene wth 1920x5000 pic the pans from feet to head
        scene v15s32_8d:
            subpixel True
            yalign 1.0
            linear 6.0 yalign 0.0
        with fade

        u "(Oh, wow!)"

        scene v15s32_8u # TPP. MC (big smile, mouth open) and Aubrey (smiling mouth closed) standing together in front of the open front door, with Riley, standing next to Aubrey, smiling mouth closed (camera is at the stairs facing the front door) [Chicks' front door-interior].
        with dissolve

        u "Aubrey, you-"

        u "You look... incredible."

        scene v15s32_8l
        with dissolve

        au "Aw, haha! Thanks, [name]."

        scene v15s32_8m
        with dissolve

        ri "Yeah, stunning."

        scene v15s32_8i
        with dissolve

        au "Thanks." 

        if aubrey.relationship.value >= Relationship.FWB.value: # -if AubreyRs
            scene v15s32_8j
            with dissolve

            u "Like, holy hell... I'm one lucky guy."

            scene v15s32_8k # -Aubrey blushes a little-
            with dissolve

            au "Okay, easy tiger."

        # -Regardless-
        scene v15s32_8l
        with dissolve

        au "You're looking pretty great yourself"

        scene v15s32_8j
        with dissolve

        u "Thanks. It does feel nice to dress up for someone special."

        scene v15s32_8v # TPP. Aubrey, smiling mouth closed, MC smiling and winking mouth closed at Aubrey camera at the stairs facing the open front door [Chicks' front door-interior].
        with dissolve

        pause 0.75

        scene v15s32_8w # FPP. Riley, neutral, mouth open looking at Aubrey, smiling mouth closed [Chicks' front door-interior].
        with dissolve

        ri "I think I'll finish my movie now."
        
        ri "Have a great time you guys."

        scene v15s32_8x # FPP. Riley, neutral, mouth closed looking at MC, Aubrey, smiling mouth closed looking at MC [Chicks' front door-interior].
        with dissolve

        u "Thanks, Riley."

        scene v15s32_8y # TPP. Camera facing the stairs, MC (back to camera, Aubrey, smiling, mouth open, looking at Riley, neutral mouth closed climbing the stairs [Chicks' front door-interior].
        with dissolve

        au "Mhmm, bye."

        scene v15s32_8z # TPP. Camera facing the stairs, MC (back to the camera, Aubrey, turned looking over her sholder (at the open front door off camera, Riley further up the stairs [Chicks' front door-interior].
        with dissolve

        pause 0.75
        
        # -Aubrey looks away briefly-

        scene v15s32_8l
        with dissolve

        au "Oh, the car's already here?"

        scene v15s32_8j
        with dissolve

        u "Oh shit, haha. The poor driver's probably dying of boredom watching us stand here."

        scene v15s32_8l
        with dissolve

        au "Well, come on. Let's go to a wedding!"

    if not aubrey_riley_awkward:
        scene v15s32_7k # TPP. Camera aimed at the front door, Riley smiling, mouth closed, standing in the door way, waving toward MC and Aubrey (off camera) [Chicks' front door-exterior].
        with dissolve

        pause 0.75
    
    else:
        scene v15s32_7l # TPP. Camera aimed at the front door, MC and Aubrey smiling, mouths closed with Aubrey pulling the front door closed [Chicks' front door-exterior].
        with dissolve

        pause 0.75
    
    # MC and Aubrey go to the waiting car and get into it-
    scene v15s32_9 # TPP. Camera facing the street. MC and Aubrey (backs to camera) walk, arms joined (or holding hands) toward the limo [Street infront of Chicks' house-exterior].
    with dissolve

    pause 0.75

    scene v15s32_9a # TPP. Camera facing the street. MC opening the back door to the limo for Aubrey [Street infront of Chicks' house-exterior].
    with dissolve

    pause 0.75

    scene v15s32_9b # TPP. Camera facing the street. Limo with all doors closed [Street infront of Chicks' house-exterior].
    with dissolve

    pause 0.75

    # -Regardless of Awkward or not Awkward, the car drives away-
    scene v15s32_9c # TPP. Camera facing the street. Limo driving forward [Street infront of Chicks' house-exterior].
    with dissolve

    pause 0.75

    jump v15s33 # -Transition to Scene 33-