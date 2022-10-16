# SCENE 24: Walk With Samantha
# Locations: the park
# Characters: MC (Outfit 3), Samantha (Outfit 1)
# Time: Friday Afternoon

label v9_walk_w_sam:
    scene v9wws1 # FPP. Show Samantha, in park, close to mc, smiling, mouth open
    with fade  
    sa "Thanks for walking with me."

    play music "music/v9/Track Scene 9.mp3" fadein 2

    menu:
        "Joke around":
            $ reputation.add_point(Reputations.BOYFRIEND)
            jump v9_walk_w_sam_joke
        "Be serious":
            jump v9_walk_w_sam_serious
        
label v9_walk_w_sam_joke:
    scene v9wws1a # FPP. Same camera as v9wws1, Show Samantha, in park, close to mc, smiling, mouth closed
    with dissolve
    u "Ha! Not like you gave me much choice!"

    scene v9wws1b # FPP. Same camera as v9wws1, Show Samantha, in park, close to mc, surprised, mouth closed
    with dissolve    
    u "No! No, not like that. Just... you kinda told me to come."

    scene v9wws1c #Same camera as v9wws1, Show Samantha, in park, close to mc, nervous smile, mouth open
    with dissolve
    sa "Yeah, well, I don't like being out here alone. I still don't know my way around."

    scene v9wws1
    with dissolve    
    u "No, it's fine. I totally get it. And I'm glad to be out here with you."

    jump v9_walk_w_sam_cont1

label v9_walk_w_sam_serious:
    scene v9wws2 # FPP. close up of samantha, in park, close to mc, neutral face, mouth closed
    with dissolve
    u "You looked like you needed company."

    scene v9wws2a # FPP. same camera as v9wws2, close up of samantha, in park, close to mc, neutral face, mouth open
    with dissolve
    sa "That obvious?"

    scene v9wws2
    with dissolve    
    u "It's understandable. You've had a lot going on lately. I might not want to be alone with my thoughts, either."

    scene v9wws1c
    with dissolve
    sa "It's a strange place up here."

    scene v9wws1a
    with dissolve
    u "Here, too. Don't worry. There's a reason we can't all read minds."

    jump v9_walk_w_sam_cont1

label v9_walk_w_sam_cont1:
    scene v9wws3 # TPP. Show MC and samantha in park, Both slight smile, MC mouth closed, Samanthan mouth open
    with dissolve
    sa "How are you liking school so far?"

    scene v9wws4 # FPP. Show Samantha in park, looking into the distance at the park. Slight smile, mouth closed
    with dissolve
    u "It's fine... as far as school goes. Only doing core classes right now."

    scene v9wws4a # FPP. Same Camera as v9wws4, Show Samantha in park, looking into the distance at the park. Slight smile, mouth open
    with dissolve
    sa "That's smart, actually. Ease yourself in."

    scene v9wws4
    with dissolve
    u "Yeah, that's what I figured."

    scene v9wws4a
    with dissolve
    sa "What are you gonna be when you grow up?"

    scene v9wws4
    with dissolve
    u "*Laughs* No idea!"

    scene v9wws4b # FPP. Same Camera as v9wws4, Show Samantha in park, Now looking at MC. Slight smile, mouth open
    with dissolve
    sa "Good!"
    sa "I mean... good I'm not the only one who doesn't have her shit figured out."

    scene v9wws4c # FPP. Same Camera as v9wws4, Show Samantha in park, looking at MC. Slight smile, mouth closed
    with dissolve    
    u "You have nothing to worry about there. Trust me!"

    scene v9wws4b
    with dissolve
    sa "This is nice."

    scene v9wws5 # FPP. Show the scenery including the pond and trees
    with dissolve
    u "Yeah, I don't spend a lot of time out here, but I probably should."

    if sideWithCameron:
        jump v9_walk_w_sam_cameron
    else:
        jump v9_walk_w_sam_grayson

label v9_walk_w_sam_grayson:   
    scene v9wws6 # FPP. Show Samantha, lake behind, Slight smile, looking at mc, mouth open
    with dissolve
    sa "I think I'll start."

    scene v9wws6a # FPP. Show Samantha, lake behind, Slight smile, looking at mc, mouth closed
    with dissolve
    u "It would do you some good. All this fresh air."

    scene v9wws6
    with dissolve
    sa "I don't want to come out here alone, though."

    scene v9wws6a
    with dissolve
    u "No, probably not."

    scene v9wws7 # TPP. Rear shot showing Samantha and MC walking past the lake
    with dissolve
    sa "Maybe if I had someone to walk with me..."

    scene v9wws7a # TPP. Same camera as v9wws7, MC and samantha now further away from camera
    with dissolve
    u "(Duh! She's talking about you, dumbass!)"
    u "Oh! Uh, I'd love to keep you company. Just say when."

    scene v9wws8 # FPP. Show Samantha, threes in background, smiling, mouth open
    with dissolve
    sa "Cool."

    scene v9wws8a # FPP. Same camera as v9wws8, show Samantha, threes in background, smiling, mouth closed
    with dissolve
    u "I should get some cardio in since I'm training now, anyway."

    scene v9wws8b # FPP. Same camera as v9wws8, Show Samantha, threes in background, dissapointed look, mouth open
    with dissolve
    sa "Yeah."
    jump v9_walk_w_sam_cont2

label v9_walk_w_sam_cameron: 
    scene v9wws8c # FPP. Same camera as v9wws8, Show Samantha, threes in background, nervous smile, mouth open
    with dissolve
    sa "I was talking about you... us walking... together."

    scene v9wws8d # FPP. Same camera as v9wws8, Show Samantha, threes in background, nervous smile, mouth closed
    with dissolve
    u "Oh!"

    scene v9wws8c
    with dissolve
    sa "You've been so nice, at a time when I really needed a friend."

    scene v9wws8d
    with dissolve
    u "Don't mention it."

    scene v9wws11a # FPP. Show Samantha now infront of an open green in the parkm, neutral face, mouth open
    with dissolve
    sa "I know, I know, Apes stick together."

    scene v9wws11 # FPP. Same camera as v9wws9, Show Samantha now infront of an open green in the park, neutral face, mouth closed
    with dissolve
    u "Always."

    scene v9wws11a
    with dissolve
    sa "It's nice to have that. Cam and I had it rough growing up. It felt like we only had each other."

    scene v9wws11
    with dissolve
    u "And now you have all of us. The whole house is here for you."

    scene v9wws11a
    with dissolve
    sa "It'll take some getting used to."

    scene v9wws10 # FPP. close up of samantha, in park, close to mc, neutral face, mouth closed, open green behind her, mouth closed
    with dissolve
    u "I'm here if you need me. I like this, too."

    scene v9wws10a # FPP. same camera as v9wws10, close up of samantha, in park, close to mc, neutral face, mouth closed, open green behind her, mouth open
    with dissolve
    sa "Took you long enough."

    scene v9wws10
    with dissolve
    u "Apes aren't known for their intellect."

    scene v9wws10b # FPP. same camera as v9wws10, close up of samantha, in park, close to mc, laughing, mouth closed, open green behind her, mouth open
    with dissolve
    sa "*Laughs* True."

    jump v9_walk_w_sam_cont2

label v9_walk_w_sam_cont2:
    scene v9wws11 # FPP. Show Samantha, Smiling, mouth closed, samantha now on the green in the park
    with dissolve
    u "Have you thought about what you're gonna be?"
    u "Wh-when you grow up?"

    scene v9wws11a # FPP. Same camera as v9wws11, Show Samantha, Smiling, mouth open, samantha now on the green in the park
    with dissolve
    sa "Oh! Um, not really. I haven't been thinking much about the future."

    scene v9wws11
    with dissolve
    u "No time like the present to plan for the future."

    scene v9wws11a
    with dissolve
    sa "You read that off an accountant's business card or something?"

    scene v9wws11
    with dissolve
    u "*Laughs* Sounds like it, huh? No, it's something my dad always said."

    scene v9wws11a
    with dissolve
    sa "Must be nice. Only saying I remember from my dad is, \"Jesus, Sam, not again!\""

    scene v9wws11
    with dissolve
    u "I got a few of those, too. Haha."

    scene v9wws5
    with dissolve
    u "It really is a nice day, huh?"

    scene v9wws6
    with dissolve
    sa "Yeah, I hate to go back inside but I told Cam I was just going out for a smoothie. I should head back."

    menu:

        "Ask to go out again":
            $ reputation.add_point(Reputations.BOYFRIEND)
            jump v9_walk_w_sam_walk_again
        "Say goodbye":
            jump v9_walk_w_sam_walk_goodbye

    label v9_walk_w_sam_walk_again:
    u "Thanks for dragging me out here with you. I had a nice time."

    scene v9wws7
    with dissolve
    sa "Hey, I sorta asked."

    scene v9wws7a
    with dissolve
    u "Sorta."
    u "I'd love to go on another trip around the pond with you, next time you're up for it."

    scene v9wws8b
    with dissolve
    sa "That would be nice."

    scene v9wws8a
    with dissolve
    u "Just let me know when you're headed out and I'll meet you."

    jump v9_walk_w_sam_cont3
label v9_walk_w_sam_walk_goodbye:
    scene v9wws8a
    with dissolve
    u "Ugh, same. I have so much homework."

    scene v9wws7
    with dissolve
    u "Don't want Cam to come looking for you."

    scene v9wws7a
    with dissolve
    sa "No, I suppose not. But I'll probably be back out here tomorrow, if you wanna join."

    scene v9wws7
    with dissolve
    u "Sure. Maybe some of the guys will want to join. Make a training session out of it."

    scene v9wws8b
    with dissolve
    # -Samantha frowns-
    sa "Apes stick together."

    scene v9wws8e # FPP. Same camera as v9wws8, Show Samantha, threes in background, dissapointed look, mouth closed
    with dissolve
    u "Yep."

    jump v9_walk_w_sam_cont3

label v9_walk_w_sam_cont3:
    scene v9wws12 # FPP. Show samantha now infront of apes house, smiling, mouth closed
    with dissolve
    u "Nice talking to you."

    scene v9wws12a # FPP. Same camera as v9wws12, Show samantha now infront of apes house, smiling, mouth open
    with dissolve
    sa "You too. I'll text you before my next walk."

    scene v9wws12
    with dissolve
    u "Great."

    scene v9wws12a
    with dissolve
    sa "See ya."

    stop music fadeout 3

    scene v9wws12
    with dissolve
    u "Take care."

    jump v9_room_fri_eve
