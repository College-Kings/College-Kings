# SCENE 31b: Chloe seduces Grayson
# Locations: Side of Apes House (Outside), Dininng Room (Table and Chairs), Bean Bag Room (Ape's House [Inside]), Grayson's Bedroom (Ape House [Inside]),Front of Apes House (outside).
# Characters: MC (Outfit: 2), CHLOE (Outfit: 1), AUBREY (Outfit: 1), GRAYSON (Outfit: 3) Wednesday
# Time: Afternoon

label v14s31b: # -MC arrives by the side of the Apes house and Chloe is already there waiting, she's nervous about asking MC if she can seduce Grayson on her own-
    scene v14s31b_1 # TPP. MC, mouth closed, neutral expression walking on the side walk (towards the Ape's house).
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 58.mp3" fadein 2

    scene v14s31b_2 # TPP. MC, back to camera, standing in front of the Ape's house.
    with dissolve

    pause 0.75

    scene v14s31b_2a # TPP. MC, walking towards the side of the Ape's house (where he meets Chloe).
    with dissolve

    pause 0.75

    scene v14s31b_3 # FPP. MC looks at Chloe, mouth closed and nervous and Chloe making eye contact back with MC.
    with dissolve

    u "Hey, you."

    scene v14s31b_3a # FPP. Same as v14s31b_3, but Chloe mouth open.
    with dissolve

    cl "Hey..."

    scene v14s31b_3
    with dissolve

    u "Are you okay? You look stressed."

    scene v14s31b_3a
    with dissolve

    cl "Yeah, it just feels weird..."

    scene v14s31b_3c # FPP. Same as v14s31b_3, but eyes down avoiding eye contact with MC, nervous, mouth closed.
    with dissolve

    u "Yeah, this idea is kinda risky. You said it'd be easy with a little alcohol in him right?"

    scene v14s31b_3a
    with dissolve

    cl "Well, yeah... It won't be hard at all."

    scene v14s31b_3d # FPP. Same as v14s31b_3c, but Chloe mouth open.
    with dissolve

    cl "But... I have something I wanted to say and I hope it doesn't come out wrong or anything."

    scene v14s31b_3c
    with dissolve

    u "What is it?"

    scene v14s31b_3
    with dissolve

    pause 0.75

    scene v14s31b_3c
    with dissolve

    pause 0.75

    scene v14s31b_3d
    with dissolve
    
    cl "I wanna try to seduce Grayson on my own."

    scene v14s31b_3
    with dissolve

    u "Umm... You will be on your own... I'm not flirting with him, haha."

    scene v14s31b_3a
    with dissolve

    cl "No, I mean like, I wanna go in the room with him on my own."

    cl "I think that's the only way it'll work."

    if chloe.relationship >= Relationship.GIRLFRIEND: 
        scene v14s31b_3c
        with dissolve

        u "You want to be alone..."

        scene v14s31b_3e # FPP. Same as v14s31b_3c, but eyes looking left avoiding eye contact with MC, nervous, mouth closed.
        with dissolve

        u "In a room..."

        scene v14s31b_3f # FPP. Same as v14s31b_3c, but eyes looking up avoiding eye contact with MC, nervous, mouth closed.
        with dissolve

        u "With your ex, ha."

        scene v14s31b_3g # FPP. Same as v14s31b_3c, but eyes looking right avoiding eye contact with MC, nervous, mouth closed.
        with dissolve

        u "So that you can try to seduce him?"

        scene v14s31b_3d
        with dissolve

        cl "That's not-"

        scene v14s31b_3c
        with dissolve

        u "It is."

        scene v14s31b_3a
        with dissolve

        cl "I know how this sounds, [name], but I think it's the only way this plan is going to work."

    elif chloe.relationship >= Relationship.FWB: # -If Chloe RS, NOT Chloe GF (extra dialogue)
        scene v14s31b_3
        with dissolve

        u "You really want to be alone in a room with your ex?"

        scene v14s31b_3a
        with dissolve

        cl "Trust me, this is not about what I want."
        
        cl "This plan has to work, [name]."

    # -Continue regardless of everything

    scene v14s31b_3h # FPP. Same as v14s31b_3, but Chloe's experession is nuetral/concentrating, mouth open, eye contact with MC.
    with dissolve

    cl "I know Grayson too well."

    cl "Or, I guess... We know each other too well."

    scene v14s31b_3a
    with dissolve

    cl "If you were there he'd know something was up. No matter how drunk he is."

    scene v14s31b_3i # FPP. Same as v14s31b_3h, but mouth closed.
    with dissolve

    u "*Sighs*"

    menu:
        "Trust Chloe":
            $ v14s31bTrustChloe = True
            $ v14_ApesPostChloePics = False
            $ add_point(KCT.BOYFRIEND)
            $ chloe.points +=1

            scene v14s31b_3
            with dissolve

            if chloe.relationship >= Relationship.GIRLFRIEND:
                $ grant_achievement("built_on_trust")
            
            u "*Sighs* I trust that you'll do what's best."

            scene v14s31b_3j # FPP. Same as v14s31b_3, but Chloe's smiling, mouth open, eye contact with MC.
            with dissolve

            cl "Thank you."

            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v14s31b_4 # TPP. Chloe hugging MC. 
                with dissolve

                pause 0.75

            scene v14s31b_3i
            with dissolve

            u "Yeah... Of course."
            
        "Don't trust Chloe":
            $ add_point(KCT.BRO)
            $ chloe.points -=1

            scene v14s31b_3
            with dissolve

            u "I'm sorry, but... I don't feel comfortable with that."

            scene v14s31b_3a
            with dissolve

            cl "*Sighs* Okay, I understand."

            scene v14s31b_3c
            with dissolve

            u "You sure?"

            scene v14s31b_3d
            with dissolve

            cl "Yeah, I get it."
    
    scene v14s31b_3h
    with dissolve

    cl "Let's go ahead and get inside. I'm pretty sure Aubrey is already here."

    scene v14s31b_5 # TPP. MC following Chloe, both neutral, mouths closed, are on the side of the Ape house walking to the front.
    with dissolve

    pause 0.75

    scene v14s31b_6 # TPP. MC following Chloe, both neutral, mouths closed, are in front of the Ape house, walking towards the front door.
    with dissolve

    pause 0.75

    scene v14s31b_7 # TPP. MC following Chloe, both neutral, mouths closed, pushing open the front door to the Ape house.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 10.mp3" fadein 2

    scene v14s31b_8 # FPP. MC at the kitchen entrace with Chloe sees Aubrey and Grayson sitting at the table with a couple beers each, mouthes open slightly angry with the other (There is a vaping machine on the table next to Grayson).
    with dissolve

    pause 0.75
    
    scene v14s31b_9 # FPP. Aubrey sitting back in the chair, holding a beer bottle, smiling, mouth open, head turned looking to Grayson (off camera).
    with dissolve

    au "Grayson, you work at a fucking gas station."

    scene v14s31b_10 # FPP. Grayson, sitting up in his chair, angry, mouth open, holding his beer and pointing at Aubrey (off camera) with his finger.
    with dissolve

    gr "Keep your mouth shut about that, Aubrey."

    scene v14s31b_9a # FPP. Same as v14s31b_9 but, Aubrey, mouth open, head turned toward Grayson, laughing.
    with dissolve

    au "Haha! I'm not one of your little frat boys that you can intimidate, Gray."

    au "You want something from me, you'll have to earn it."

    scene v14s31b_10
    with dissolve

    gr "You're such a sleazy-"

    scene v14s31b_11 # FPP. Chloe, neutral, mouth open, looking at Aubrey and Grayson (off Camera).
    with dissolve

    cl "Uhh, hey guys."

    scene v14s31b_9b # FPP. Aubrey, smiling, mouth open, looking at MC and Chloe (camera)
    with dissolve

    au "Hey! Finally! People other than Grayson!"

    # -Aubrey gets up to hug Chloe and then leaves the room to grab MC and Chloe a beer-
    scene v14s31b_12 # TPP. MC and Chloe, smile, mouth closed, looking at Aubrey, smiling, mouth closed, standing up from her chair at the table.
    with dissolve

    pause 0.75

    scene v14s31b_12a # TPP. Chloe and Aubey, smiling mouth closed, meet each other half way and hug each other.
    with dissolve

    pause 0.75

    scene v14s31b_12b # TPP. Aubrey, smiling, mouth closed, walks past MC, neutral, mouth closed, and through the dining room entrance.
    with dissolve

    pause 0.75

    scene v14s31b_12c # TPP. Chloe, mouth open sits in what was Aubrey's chair.
    with dissolve

    pause 0.75

    scene v14s31b_10a # FPP. Grayson, sitting back in his chair, slightly angry/annoyed, mouth slightly open, holding his beer.
    with dissolve

    gr "*Sighs*"

    scene v14s31b_13 # FPP. Chloe (sitting at table), mouth open, smiling, looking at Grayson (off camera).
    with dissolve

    cl "Ha, where's Cameron?"

    scene v14s31b_10b # FPP. Same as v14s31b_10a, but Grayson looking away from Chloe (off camera).
    with dissolve

    gr "Not in the mood."

    scene v14s31b_10c # FPP. Same as v14s31b_10a, but Grayson looking at MC (camera), mouth closed, slightly angry.
    with dissolve

    u "*Chuckles*"

    if joinwolves: # -If Wolf
        scene v14s31b_10d # FPP. Same as v14s31b_10c, but mouth open, a little more angry.
        with dissolve

        gr "Why's that funny, Wolf?"

        scene v14s31b_10c
        with dissolve

        u "Nah, it's not, ha."
    
    # -Aubrey returns and gives MC and Chloe a bottle of beer-
    scene v14s31b_14 # TPP. Aubrey, smiling, happy enters through dining room entrance holding two bottles of beer.
    with dissolve

    pause 0.75

    scene v14s31b_14a # TPP. Aubrey, smiling, mouth closed, hands a beer to MC.
    with dissolve

    pause 0.75

    scene v14s31b_14b # TPP. Aubrey, smiling, mouth closed, walks from MC towards Chloe.
    with dissolve

    pause 0.75

    scene v14s31b_14c # TPP. Aubrey, smiling, mouth closed, hands Chloe a bolttle of beer.
    with dissolve

    pause 0.75

    scene v14s31b_14d # TPP. Aubrey, smiling, mouth closed, sits in the chair opposite Chloe and next to Grayson.
    with dissolve

    pause 0.75

    scene v14s31b_15 # FPP. Aubrey, smiling, mouth open, looking at Chloe (off Camera).
    with dissolve

    au "Well, isn't this a crazy bunch. Two Greek heads who used to date, the hot shot freshman that everyone knows, and of course..."

    scene v14s31b_15a # FPP. Aubrey, smiling, laughing, pointing at herself. 
    with dissolve

    au "Me. The fun one."

    scene v14s31b_13a # FPP. Chloe (sitting at table), mouth open, laughing, looking at Aubrey (off camera).
    with dissolve

    cl "*Chuckles*"

    scene v14s31b_15b # FPP. Aubrey, smiling, mouth closed, while holding a beer bottle looking at MC (camera).
    with dissolve

    u "The hot shot freshman, huh? Haven't heard that one yet."

    scene v14s31b_15c # FPP. Same as v14s31b_15b, but Aubrey with mouth open.
    with dissolve

    au "There's a lot you haven't heard."

    if aubrey.relationship >= Relationship.FWB:
        scene v14s31b_15d # FPP. Same as v14s31b_15b, but Aubrey winking at MC, mouth closed. 
        with dissolve

        pause 0.75

    scene v14s31b_15b
    with dissolve

    u "Is that so?"

    scene v14s31b_13b # FPP. Chloe (sitting at table), mouth open, neutral, lookng at Grayson (off camera). 
    with dissolve

    cl "So, I wanted to-"

    scene v14s31b_10d
    with dissolve

    gr "Spark up already, Aubrey! I can't ease into this without being high."

    scene v14s31b_13c # FPP. Same as v14s31b_13b, but mouth closed, disappointed, looking at Grayson (off camera). 
    with dissolve

    cl "*Sighs*"

    # -Grayson grabs his vape and hits it-
    scene v14s31b_10e # FPP. Grayson smokes his varporize.
    with dissolve

    pause 0.75

    scene v14s31b_10f # FPP. Grayson, slight smile, eyelids slightly closed (he's stoned), holding the varporizer blowing out smoke.
    with dissolve
    
    pause 0.75

    scene v14s31b_10g # FPP. Grayson, sitting back in his chair, slight smile, eyelids slightly closed, mouth open.
    with dissolve

    gr "Ahh, off to a good start."

    scene v14s31b_9b
    with dissolve

    au "Are we just chillin' for now? I'm cool with that, if that's the case."

    scene v14s31b_13b
    with dissolve

    cl "There's some things I wanna talk about, but yeah. We can chill for now."

    scene v14s31b_9b
    with dissolve

    au "Bean bags?"

    scene v14s31b_10h # FPP. Grayson, mouth open, happy, yelling with one raised raised in the air (that holds the vaporizer). 
    with dissolve

    gr "Hell yeah!"

    # -They all go to the bean bag room in the Apes house, dim colorful lights, pillows and blankets everywhere, bongs, panties on the ground, beer cans in the corner-
    # -Chloe and Aubrey sit next to each other while MC and Grayson sit apart from each other, across from them.-
    scene v14s31b_16 # TPP. Aubrey leads Chloe, Grayson, and MC out of the dining room. Chloe and MC are neutral; others are happy. All mouths are closed.
    with dissolve

    pause 0.75

    scene v14s31b_16a # TPP. Same as v14s31b_16, except they are in a dim hallway, walking towards a room that has colored lights (the lights are slighly bleeding into the hallway).
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 23_2.mp3" fadein 2

    scene v14s31b_16b # FPP. Aubrey, Chloe, and Grayson are in a line in front of MC, who can only see the back of their heads, the edges of the room, and the dim colored lights.
    with dissolve

    pause 0.75

    scene v14s31b_16c # FPP. Aubrey, Chloe, are deeper in the room veering to the left towards two bean bags chairs that are very close to each other. The back of Grayson head blocks MC vision to the right.
    with dissolve

    pause 0.75

    scene v14s31b_16d # FPP. Aubrey, Chloe, smiling, mouths closed sit in bean bag chairs on the left. Grayson stands in front of a bean bag chair across from Chloe. There is another bean bag chair to his left (towards MC) but is further apart than Chloe and Aubrey's.
    with dissolve

    pause 0.75

    scene v14s31b_16e # FPP. Grayson is now sitting in the bean bag chair, and MC has full view of the dim, colored light room. There are pillows, blankets, marijuna paraphanialla, beer bottle/cans, bras and panties scattered all over and in the corner.
    with dissolve

    pause 0.75

    scene v14s31b_16f # TPP. MC sits down in the only remaining bean bag chair (Chloe faces Grayson and has Aubrey to her right. MC sits across from Aubrey, but is further apart from Grayson than Chloe and Aubrey are to each other.
    with dissolve

    pause 0.75
    # -Grayson looks at Aubrey and Chloe and smiles-

    scene v14s31b_17 # FPP. Grayson, smiling, eyelids slightly closed, mouth open holding his vaporizer.
    with dissolve

    gr "Ha, seeing you guys sit there like that takes me back."

    scene v14s31b_18 # FPP. Chloe, mouth closed, disappointed.
    with dissolve

    cl "I knew you were gonna do this..."

    scene v14s31b_19 # FPP. Aubrey, mouth open, netural.
    with dissolve

    au "Grayson, stop saying dumb shit. For like, two seconds."

    scene v14s31b_17
    with dissolve

    gr "What?! I haven't said anything bad. I'm just reminiscing..."

    gr "All of freshman year you'd sit right there and have like, twenty different books from god knows how many classes."

    scene v14s31b_18a # FPP. Same as v14s31b_18, but Chloe frowning, focused; not angry. 
    with dissolve

    cl "I was a focused student."

    scene v14s31b_19
    with dissolve

    au "You still are."

    scene v14s31b_18b # FPP. Same as v14s31b_18, but Chloe, mouth open, smiling. 
    with dissolve

    cl "Yeah... Not like I used to be."

    # -Grayson hits his vape again-
    scene v14s31b_17a # FPP. Grayson smokes his varporize.
    with dissolve

    pause 0.75

    scene v14s31b_17b # FPP. Grayson, slight smile, eyelids slightly closed (he's stoned), holding the varporizer blowing out smoke.
    with dissolve

    pause 0.75

    scene v14s31b_17c # FPP. Grayson, sitting back in his chair, smiling, eyelids slightly closed, mouth open.
    with dissolve

    gr "Have you ever seen her wear her glasses, [name]?"

    scene v14s31b_18c # FPP. Same as v14s31b_18, but Chloe, mouth closed, embarrassed. 
    with dissolve

    u "Chloe?"

    scene v14s31b_17
    with dissolve

    gr "No, my grandmother... Yes, Chloe."

    scene v14s31b_17d
    with dissolve

    menu:
        "Don't think so":
            u "Hmm, no... I don't think so."

        "Not yet":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.TROUBLEMAKER)

            u "Not yet, ha. I guess she's still got a few more surprises in store."

            scene v14s31b_18a
            with dissolve

            cl "Haha..."

    scene v14s31b_17c
    with dissolve

    gr "*Laughs* I have, and boy let me tell you..."
    
    gr "Those glasses make you wanna do something... *Whispers* Out of pocket."

    scene v14s31b_18a
    with dissolve

    cl "Grayson!"

    scene v14s31b_17e # FPP. Same as v14s31b_17c, but Grayson mouth open, slight smile, annoyed (eyelids still slightly closed).
    with dissolve

    gr "What?!"

    scene v14s31b_17
    with dissolve

    gr "You wanted to have a little kickback and I wanna kick back and relax."

    scene v14s31b_18c
    with dissolve

    u "You don't have to-"
   
    # -Grayson acts like MC isn't there and continues to talk to Chloe directly-

    scene v14s31b_17e
    with dissolve

    gr "I'm not a dumbass, Chloe. I know you came to ask for something so I'm enjoying myself before all the bullshit comes."

    scene v14s31b_18d # FPP. Same as v14s31b_18, but mouth closed.
    with dissolve

    u "*Sighs*"

    scene v14s31b_19a # FPP. Aubrey smiling, mouth open, laughing.
    with dissolve

    au "*Laughs*"

    scene v14s31b_17e
    with dissolve

    gr "What's so funny?"

    scene v14s31b_19a
    with dissolve

    au "You! *Laughs*"

    scene v14s31b_19
    with dissolve

    au "You obviously have no friends so when people try to just hang out with you, you think there's a secret motive."

    scene v14s31b_19b # FPP. Same as v14s31b_19, but smiling.
    with dissolve

    au "And honestly... Even if there is, why can't you just enjoy the company? You definitely need some."

    scene v14s31b_18e # FPP. Same as v14s31b_18, but Chloe, smiling, laughing.
    with dissolve

    cl "*Chuckles*"

    scene v14s31b_17f # FPP. Same as v14s31b_17e, but Grayson surprised/shocked. mouth open, avoiding eye contact.
    with dissolve

    gr "I..."

    scene v14s31b_17g # FPP. Same as v14s31b_17f, but mouth closed.
    with dissolve

    u "Not used to being spoken to so directly, huh?"

    scene v14s31b_18a
    with dissolve

    cl "He isn't, no."

    # -Chloe begins to smirk mischievously-
    scene v14s31b_18f # FPP. Same as v14s31b_18, but Chloe smiling naughty, mouth open.
    with dissolve

    cl "That's something I remember clearly. One time Gray popped off on Mr. Lee and got manhandled real quick. *Chuckles*"

    scene v14s31b_19a
    with dissolve

    au "Ah! *Laughs* I remember his girly scream like it was yesterday."

    scene v14s31b_17c
    with dissolve

    gr "Still calling me that, huh?"

    scene v14s31b_18b
    with dissolve

    cl "Ha... Calling you what?"

    scene v14s31b_17c
    with dissolve

    gr "Gray."

    scene v14s31b_18c
    with dissolve

    gr "I haven't heard that in a long time, you know?"

    scene v14s31b_18g # FPP. Same as v14s31b_18, but Chloe nervous, mouth open.
    with dissolve

    cl "I didn't even notice I called you that, sorry. Force of habit I guess since I'm looking at you."

    # -Chloe drinks her beer nervously-
    scene v14s31b_18h # FPP. Chloe, nervous, drinks her beer.
    with dissolve

    pause 0.75

    scene v14s31b_17c
    with dissolve

    gr "A lot of things were a force of habit when you looked at me, haha. Are you trying to start those again too?"

    if chloe.relationship >= Relationship.FWB:
        scene v14s31b_20 # TPP. MC sitting up in bean bag chair, frowning, angry, mouth open.
        with dissolve

        u "What the f-"

    # -continue regardless-
    scene v14s31b_19c # FPP. Aubrey sits up straight in her bean bag chair, uncomfortable, mouth open, fake smile.
    with dissolve

    au "OKAYYYYY! That's it."

    scene v14s31b_19d # FPP. Aubrey and Grayson each holding the vaporizer as if Grayson was handing it to Aubrey. Aubrey mouth open. Grayson, mouth closed, smiling, lids slightly closed.
    with dissolve

    au "Grayson, give me some of what you're smoking 'cause it's obviously working."

    # -Aubrey takes Grayson vape and hits it-
    scene v14s31b_19e # FPP. Aubrey smokes the vaporize.
    with dissolve

    pause 0.75

    scene v14s31b_19f # FPP. Aubrey, choking, blows out smoke as she coughs, eyes closed, slightly bending over to simulate coughing.
    with dissolve

    au "*Coughs* Fuck... *Coughs*"

    scene v14s31b_17c
    with dissolve

    gr "Strong shit, isn't it?"

    scene v14s31b_19f
    with dissolve

    au "*Coughs* Damn, where'd you get this?"

    scene v14s31b_17c
    with dissolve

    gr "You wouldn't believe me if I told you. *Laughs*"

    scene v14s31b_19g # FPP. Aubrey, sitting back in her chair, smiling, eyelids slightly closed, mouth open.
    with dissolve

    au "Pfft... Try me."

    scene v14s31b_17c
    with dissolve

    gr "Saw Rose hitting it."

    scene v14s31b_18i # FPP. Same as v14s31b_18, but Chloe suprised, mouth open.
    with dissolve

    cl "What?!"

    scene v14s31b_19g
    with dissolve

    au "Ms. Rose smokes?"

    scene v14s31b_17c
    with dissolve

    gr "Probably, but I wasn't talking about her. I was talking about her husband."

    scene v14s31b_19g
    with dissolve

    au "Ex-husband."

    scene v14s31b_17e
    with dissolve

    gr "Whatever, anyways..."

    gr "I saw him hitting it outside the gas station and asked him where he got it."

    scene v14s31b_17c
    with dissolve

    gr "Since the smell was so strong I knew it had to be good shit. He set me up with a guy and well, here we are."

    scene v14s31b_19g
    with dissolve

    au "Nice little opportunity, meathead. I'm gonna need that contact."

    scene v14s31b_17c
    with dissolve

    gr "Sure, I can make that happen."

    scene v14s31b_19g
    with dissolve

    au "Good deal."

    scene v14s31b_18a
    with dissolve

    cl "Glad you guys are hitting it off, but umm..."

    # -Chloe looks at Grayson with a flirty look-
    scene v14s31b_18f
    with dissolve

    cl "Is it okay if we go talk for a second?"

    scene v14s31b_17c
    with dissolve

    gr "Just us?"

    if v14s31bTrustChloe: # -If trust Chloe
        scene v14s31b_18f
        with dissolve

        cl "Yeah, just us."

        scene v14s31b_17c
        with dissolve

        gr "Okay, lead the way. You do know your way around here..."

        scene v14s31b_18
        with dissolve

        cl "*Sighs*"
        
        # -Chloe leads Grayson out of the room-
        scene v14s31b_21 # FPP. Chloe, neutral, mouth closed and Grayson, smiling, mouth closed, standing in front of their bean bag chairs.
        with dissolve

        pause 0.75

        scene v14s31b_21a # FPP. Same as v14s31b_21, but Chloe and Grayson half the distance to the hallway entrance, Chloe leading Grayson by the hand past Aubrey, who is watching Chloe and Grayson walk (holding vaporizer).
        with dissolve

        pause 0.75

        scene v14s31b_21b # FPP. Same as v14s31b_21a, but Chloe and Grayson disappearing into the dark hallway entrance, while Aubrey, holding the vaporizer is looking at MC, awkward, slight smile, mouth closed.
        with dissolve

        u "*Sighs*"

        scene v14s31b_19h # FPP, Aubrey, nervous, slight smile, mouth open, hand held out to MC, offering him the vaporizer.
        with dissolve

        au "Hit?"

        menu: # -Aubrey offers MC the vape that she took from Grayson-
            "Vape": # -Event1 Sure
                $ add_point(KCT.TROUBLEMAKER)
                # -Montage of MC and Aubrey passing the vape while they relax.-
                $ v14s31b_smoke_weed_with_aubrey = True
                scene v14s31b_23 # TPP. MC smokes the vaporizer
                with dissolve

                pause 0.75

                scene v14s31b_23a # TPP. MC, slight smile, eyelids slightly closed (he's stoned), holding the vaporizer blowing out smoke.
                with dissolve

                pause 0.75

                scene v14s31b_19e
                with dissolve

                pause 0.75

                scene v14s31b_19i # FPP. Aubrey, slight smile, eyelids slightly closed (she's stoned), holding the vaporizer, blowing out smoke.
                with dissolve

                pause 0.75

                scene v14s31b_23b # TPP. MC, smiling, mouth open, laughing.
                with dissolve

                pause 0.75
                
                scene v14s31b_19a
                with dissolve

                pause 1

            "Pass": # -Event 2 Nah
                $ add_point(KCT.BOYFRIEND)
                # -Montage of Aubrey smoking while MC relaxes-
                scene v14s31b_23c # TPP. MC, eyes closed, leaning back in the bean bag chair, hands behind his head, relaxing.
                with dissolve
                
                pause 0.75

                scene v14s31b_19e
                with dissolve

                pause 0.75

                scene v14s31b_19i
                with dissolve

                pause 0.75
                
                scene v14s31b_23d # TPP. Same as v14s31b_23c, but MC facing away from the camera.
                with dissolve

                pause 0.75

                scene v14s31b_19e
                with dissolve

                pause 0.75

                scene v14s31b_23e # TPP. Same as v14s31b_23d, but MC facing the camera, eyes open looking at Aubrey (off camera).
                with dissolve

                pause 1

        scene v14s31b_19g
        with dissolve

        au "They've been gone for a while now..."

        scene v14s31b_19j # FPP. Same as v14s31b_19b, but mouth closed. 
        with dissolve

        u "Really..."

        scene v14s31b_19
        with dissolve

        au "Sorry... Honestly, it's probably torture for her."

        # -Aubrey takes a long drink of beer-
        scene v14s31b_19k # FPP. Aubrey drinks her beer (tilting up and back to act like she is taking a long drink of beer).
        with dissolve

        pause 0.75

        scene v14s31b_19b
        with dissolve

        au "Or not... Who knows."

        scene v14s31b_19j
        with dissolve

        u "*Sighs*"

        # -Grayson and Chloe come back and Grayson sits down but Chloe keeps standing- # -Grayson is smiling-
        scene v14s31b_21d # FPP. Chloe appears from the dark hallway entrance, neutral, mouth closed.
        with dissolve

        pause 0.75

        scene v14s31b_21e # FPP. Same as v14s31b_21d, but Chloe, neutral, mouth closed, is half the distance from the hallway and Grayson, smiling, mouth closed, follows her.
        with dissolve

        pause 0.75

        scene v14s31b_21f # FPP. Same as v14s31b_21e, but Grayson, smiling, mouth closed, sitting in his bean bag chair, Chloe standing in front of Grayson.
        with dissolve

        pause 0.75

        scene v14s31b_24 # FPP. Chloe, looking at slight downward angle (she's standing, but looking at someone sitting),neutral, mouth open.
        with dissolve

        cl "So, it's official."

        scene v14s31b_17c
        with dissolve

        gr "Looks like the Chicks and the Apes are gonna be working together from here on out."

        scene v14s31b_19
        with dissolve

        au "Wait, that's what you guys were talking about in there? I should've joined you."

        scene v14s31b_17c
        with dissolve

        gr "You didn't need to be there..."

        scene v14s31b_24a # FPP. Same as v14s31b_24, but Chloe frowning, upset, mouth open.
        with dissolve

        cl "Grayson, oh my god, stop! We literally just talked, that was it."

        scene v14s31b_17c
        with dissolve

        gr "Yeah, we just talked..."

        scene v14s31b_24a
        with dissolve

        cl "*Sighs* Let's go, [name]."

        scene v14s31b_19
        with dissolve

        au "Wait... You're just leaving me here?"

        scene v14s31b_24
        with dissolve

        cl "You're enjoying yourself."

        scene v14s31b_19a
        with dissolve

        au "Ha, you know me well."
        
        # -Chloe and MC walk outside-
        scene v14s31b_25 # TPP. MC following Chloe into the dark hallway (their backs are to the camera).
        with dissolve

        pause 0.75

        scene v14s31b_26 # TPP. MC following Chloe walk out of the front door of the Ape House.
        with dissolve

        pause 0.75

        scene v14s31b_27 # TPP. MC and Chloe face each other in front of the Ape's House. Both neutral expression, mouth closed.
        with dissolve

        pause 0.75

        scene v14s31b_28 # TPP. Chloe, smiling mouth closed.
        with dissolve

        u "So, it went well?"

        scene v14s31b_28a # TPP. Same as v14s31b_28, but mouth open. 
        with dissolve

        $ set_presidency_percent(v14_lindsey_popularity - 3) #tick
        cl "Very, he actually listened. Maybe it was because he was high, I don't know, but I'll take it."

        menu: # -MC chooses Event1 or Event2-
            "Ask for details": # -If Ask for details
                $ add_point(KCT.TROUBLEMAKER)
                scene v14s31b_28
                with dissolve

                u "So, what exactly did you do to... You know, convince him?"

                scene v14s31b_28a
                with dissolve

                cl "A little flirting but nothing more than that. It was honestly a lot easier than I thought."

                scene v14s31b_28
                with dissolve

                u "So you didn't have to touch him?"

                scene v14s31b_28b # TPP. Same as v14s31b_28a, but Chloe rolling her eyes, mouth open.
                with dissolve

                cl "*Sighs* No, [name], I didn't touch him..."

                scene v14s31b_28
                with dissolve

                u "Good, I figured. Just don't want any mixed messages."
            
            "Leave it be": # -If Leave it be
                $ add_point(KCT.BOYFRIEND)
                scene v14s31b_28
                with dissolve

                u "(I'll leave it be, mission accomplished.)"

        scene v14s31b_28a
        with dissolve

        cl "Thanks again for trusting me, and for helping me."

        scene v14s31b_28
        with dissolve

        u "You're welcome again. I have to admit, I'm pretty exhausted after all this hard work today."

        scene v14s31b_28a
        with dissolve

        cl "Me too."

        if chloe.relationship >= Relationship.GIRLFRIEND: 
            scene v14s31b_29 # TPP. Chloe kisses MC on the cheek.
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 0.75
        
        scene v14s31b_28a
        with dissolve

        cl "Goodnight, [name]."

        scene v14s31b_28
        with dissolve

        u "Goodnight, Chloe."

        # -Chloe gives MC a hug-
        scene v14s31b_29a # TPP. Chloe hugs MC 
        with dissolve
        
        pause 0.75

        scene v14s31b_28a
        with dissolve

        cl "See you soon."

        scene v14s31b_28
        with dissolve

        u "Bye."

        stop music fadeout 3
        play music "music/v13/Track Scene 58.mp3" fadein 2

        if joinwolves:
            scene v14s31b_30 # TPP. In front of the Ape, Chloe on the side walk walking to the left, MC on the side walk walking right (away from each other), neutral, mouths closed.
            with dissolve
            
        else:
            scene v14s31b_30a # Same as v14s31b_30, but MC walking towards the front door of the Ape house.
            with dissolve

        pause 1

        stop music fadeout 3

        jump v14s33
    
    else: # -If Don't trust Chloe
        scene v14s31b_18g
        with dissolve

        cl "Well, us and [name]."

        scene v14s31b_17e
        with dissolve

        gr "Bummer..."

        scene v14s31b_21c # FPP. Chloe, neutral, mouth closed sitting in bean bag chair and Grayson, nuetral mouth open, standing in front of her, looking down at her. 
        with dissolve

        gr "*Sighs* C'mon."

        # -Grayson leads Mc and Chloe to his bedroom-
        scene v14s31b_21g # TPP. Grayson leads Chloe, with MC following toward the dark hallway entrance.
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 17_3.mp3" fadein 2

        scene v14s31b_21h # TPP. Grayson disappeared in the dark hallways (off camera), Chloe entering the dark hallway with MC following her.
        with dissolve

        pause 0.75

        scene v14s31b_21i # TPP. Grayson opening the door to his bedroom with Chloe following him and MC following Chloe.
        with dissolve

        pause 0.75

        scene v14s31b_21j # TPP. Grayson, smiling, mouth closed, sits on his bed, Chloe, nervous, mouth closed, stands in front of him. MC, nuetral, mouth closed, stands close to the door.
        with dissolve

        pause 0.75

        scene v14s31b_31 # Grayson, sitting on his bed, smiling, mouth open.
        with dissolve
        
        gr "So... What's up?"

        scene v14s31b_32 # Chloe, nervous, smiling, mouth open.
        with dissolve

        cl "I wanted to talk to you about my presidential race."

        scene v14s31b_31
        with dissolve

        gr "Obviously, Chloe. What about it and what does any of it have to do with me?"

        scene v14s31b_31a # Same as v14s31b_31, but Grayson frowning, angry mouth closed.
        with dissolve

        u "I'm sure you-"

        scene v14s31b_31b # Same as v14s31b_31a, but Grayson mouth open. 
        with dissolve

        gr "I'm sure I don't need you to speak for her. Honestly, I don't even know why you need to be here."

        scene v14s31b_32
        with dissolve

        cl "[name] has been helping me a lot throughout this entire process and I wanted him here."

        cl "But to be honest Grayson, considering our history together I thought that it might be easy for us to work together again."

        scene v14s31b_32a # Same as v14s31b_32, but Chloe, with sad eyes, slight pout (trying to manipulate Grayson).
        with dissolve

        cl "You know... Like we used to."

        scene v14s31b_31
        with dissolve

        gr "We used to do a lot and we did it well."

        scene v14s31b_32
        with dissolve

        cl "And we can do more, again. If we're working together on this campaign."

        scene v14s31b_31c # Same as v14s31b_31, but Grayson thinking, but slight smile.
        with dissolve

        gr "Hmm..."

        scene v14s31b_21k # FPP. Chloe, slight sex smile, braces herself on her thighs/knees as she leans in toward Grayson, smiling, mouth closed.
        with dissolve

        pause 0.75

        # -Chloe begins to lean towards Grayson a little and acts seductive, but not too heavily.
        scene v14s31b_33 # Close up of Grayson and Chloe looking into each other's eyes. Grayson, thinking, mouth closed, Chloe with a slight sexy smile, mouth open.
        with dissolve
        
        cl "I want this to be the start of something great between the Chicks and the Apes."

        # -Grayson smiles for a second but then he makes eye contact with MC and snaps out of it.-
        scene v14s31b_33a # FPP. Same as v14s31b_33, but Grayson smiling, mouth closed, Chloe, slight sexy smile, mouth closed, both looking into each other's eyes.
        with dissolve

        pause 0.75

        scene v14s31b_33b # FPP. Same as v14s31b_33b, but Grayson's eyes (head stays in same position; just eyes) are pointed in the direction of MC; not at Chloe.
        with dissolve

        pause 0.75

        scene v14s31b_33c # FPP. Same as v14s31b_33b, but Grayson, smiling, mouth closed, turns his head away from Chloe. 
        with dissolve

        gr "..."

        scene v14s31b_21l # FPP. Same as v14s31b_21k, but Chloe standing, angry, frowning, mouth open, looking at Grayson, smiling, mouth closed.
        with dissolve

        cl "What?"

        scene v14s31b_31
        with dissolve

        $ set_presidency_percent(v14_lindsey_popularity + 3) #tick
        gr "*Laughs* You're a fucking joke."

        scene v14s31b_31a
        with dissolve

        u "Hey, wait-"

        scene v14s31b_31
        with dissolve

        gr "You're both a fucking joke."

        scene v14s31b_32b # Same as v14s31b_32, but Chloe concerned, neutral, mouth open.
        with dissolve

        cl "Grayson, I'm-"

        scene v14s31b_31
        with dissolve

        gr "Ha... Get the fuck out."

        scene v14s31b_32b
        with dissolve

        cl "Gray-"

        scene v14s31b_31b
        with dissolve

        gr "You can go. Now."

        scene v14s31b_32c # Same as v14s31b_32b, but Chloe mouth closed.
        with dissolve

        cl "*Sighs*"

        scene v14s31b_21m # TPP. Same as v14s31b_21j, but Chloe, frowning, angry, mouth closed, past MC stomping out of Grayson room. MC confused, neutral, mouthc closed.
        with dissolve
        
        u "..."

        if chloe.relationship >= Relationship.FWB:
            scene v14s31b_31
            with dissolve

            gr "Good luck with her, [name], she's manipulative as fuck."

            scene v14s31b_31d # Same as v14s31b_31, but mouth closed.
            with dissolve

            menu:
                "Whatever":
                    u "Whatever, man."

                "Apologize":
                    u "Sorry man. I don't-"
                

        else:
            scene v14s31b_31
            with dissolve

            gr "She's manipulative as fuck."

            scene v14s31b_31d
            with dissolve

            menu:
                "Whatever":
                    
                    u "Whatever, man."
                    
                "Apologize":
                    
                    u "Sorry man. I don't-"

        scene v14s31b_31b
        with dissolve

        gr "I wanna be alone."

        scene v14s31b_31a
        with dissolve

        u "Sure."

        # -MC goes after Chloe outside-
        scene v14s31b_34 # TPP. MC exiting Grayson room.
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v13/Track Scene 58.mp3" fadein 2

        scene v14s31b_35 # Tpp./ MC walking out the front door of the Ape's House.
        with dissolve

        pause 0.75

        scene v14s31b_27
        with dissolve

        pause 0.75

        scene v14s31b_28c # TPP. Same as v14s31b_28 Chloe, frowning, angry, mouth open.
        with dissolve

        cl "Argh! I swear, I hate him! I don't even know why I try."

        scene v14s31b_28d # TPP. Same as v14s31b_28c, but Chloe mouth closed.
        with dissolve

        u "Chloe, look-"

        scene v14s31b_28c
        with dissolve

        cl "No, it's fine. This was a mistake. Goodnight."

        # -Chloe leaves-
        scene v14s31b_30b # TPP. Same as v14s31b_30, but MC standing centered in front of house on sidewalk, mouth closed, confused, watching Chloe, angry, mouth closed stomp away to the left.
        with dissolve

        pause 0.75
        
        scene v14s31b_36 # FPP. Chloe, back/butt to camera, stomping down the sidewalk, away from MC (Ape house would be on the right but off camera). 
        with dissolve

        u "*Sighs* What the fuck, man?"

        if joinwolves:
            scene v14s31b_30c # TPP. Same as v14s31b_30b, but cut Chloe from the scene and have MC walking on the side walk to the left (going to Wolf House).
            with dissolve
            
        else:
            scene v14s31b_30d # TPP. Same as v14s31b_30c, but cut Chloe, MC walking towards the front door of the Ape's house. 
            with dissolve

        pause 0.75

        stop music fadeout 3

        jump v14s33