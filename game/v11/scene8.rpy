# SCENE 08: At the Chicks house
# Locations: Chicks house, sidewalk
# Characters: MC (outfit 9), Aubrey (Outfit 1), Lindsey(Outfit 1)
# Time: afternoon
label v11_chicks_house:

    scene v11chh1 # FPP. Show aubrey in hallway at chicks house, slight smile, mouth closed
    with fade
    play music "music/v11/Track Scene 3.mp3" fadein 2
    u "I'm thirsty."

    scene v11chh1a # FPP. same 1, holding arms forward, mouth open
    with dissolve

    au "Here, give me those bags. Go get something from the kitchen."

    scene v11chh1b # FPP. same 1a, bags in hand mouth closed
    with dissolve

    u "Alright."

    scene v11chh1c # FPP. same 1, Aubrey in hallway walking to her room, with bags. back to camera
    with dissolve

    pause 0.75

    scene v11chh2 # FPP. MC walking to kitchen, mouth closed
    with dissolve

    pause 1.25

    scene v11chh3 # FPP. Show Chicks kitchen, show broken chair in kitchen
    with dissolve

    pause 0.75

    scene v11chh3a # FPP. Lindesy walks in with slight frown in her face mouth closed
    with dissolve

    pause 0.75
    
    scene v11chh3b # FPP. same 3a, mouth open
    with dissolve
    
    li "Oh be careful, I'm getting ready to clean that up."

    scene v11chh3a
    with dissolve

    u "What happened?"

    scene v11chh3b
    with dissolve

    li "*Sighs* Chloe and Nora got into it last night. They were throwing shit everywhere and now I'm stuck here cleaning it up."

    scene v11chh4 # FPP. (change camera angle from 3) Lindesy starts cleaning up, mouth closed 
    with dissolve

    u "What were they fighting about?"

    scene v11chh4a #FPP. Same 4, mouth open
    with dissolve

    li "I have no idea. They're always fighting about something."

    scene v11chh4
    with dissolve

    u "You're not the first person to bring that up. Plus, I think we all got a taste of it at the charity event."

    scene v11chh4a
    with dissolve

    li "It's honestly a fucking embarrassment. This isn't what we're supposed to be about."

    scene v11chh4
    with dissolve

    u "Are all the girls feeling the same way?"

    scene v11chh4a
    with dissolve

    li "Yeah, pretty much. They honestly need to calm down."

    scene v11chh5 # FPP. Aubrey walks in, mouth opened 
    with dissolve

    au "Hey [name], it was nice hanging with you. I would hang out longer, but my sister is getting ready to call and I haven't had a chance to speak with her in a while."

    scene v11chh5a # FPP. same 5, mouth closed
    with dissolve

    u "Alright, sounds good."

    scene v11chh5b # FPP. aubrey leaving the room, back to camera
    with dissolve

    u "Sorry, I was hanging with Aubrey earlier."

    scene v11chh6 # FPP. now in front of lindesy mouth opened 
    with dissolve

    li "No, you're good."

    scene v11chh6a # FPP. same as 6, mouth closed
    with dissolve

    u "So what's the plan?"

    scene v11chh6
    with dissolve

    li "What do you mean?"

    scene v11chh6a
    with dissolve

    u "What's the plan to get the Chicks back together?"

    scene v11chh6
    with dissolve

    li "I don't know, but Chloe needs to do something. She's the President. I understand balancing friendships and running everything can be complicated, but that's part of the job."

    scene v11chh6a
    with dissolve

    u "Have you spoken to her about it?"

    scene v11chh6
    with dissolve

    li "No, but others have."

    scene v11chh6a
    with dissolve

    u "And?"

    scene v11chh6b # FPP. same 6, Change stance, mouth open
    with dissolve

    li "And we are where we are now."

    scene v11chh6c # FPP. same 6b, mouth closed
    with dissolve

    u "Oh."

    scene v11chh6b
    with dissolve

    li "I don't know if she's really the best person to be President."

    scene v11chh6c
    with dissolve

    u "Who is then?"

    scene v11chh6b
    with dissolve

    li "I don't know."

    scene v11chh6c
    with dissolve

    u "What about Aubrey?"

    scene v11chh6b
    with dissolve

    li "Haha, she's happy where she is. I wish I could be as content as she is. Aubrey's always just happy with life as it is."
    li "I wish I was more like that, but I feel like I always need to be doing more."

    scene v11chh6c
    with dissolve

    u "What do you mean?"

    scene v11chh6b
    with dissolve

    li "Is it bad if I'm thinking about running for President?"
    li "Like, I'm friends with Chloe and I wouldn't want me running to get between us. There's just so many people that are unhappy with her."

    scene v11chh6c
    with dissolve

    menu:
        "You should run":
            if lindsey.relationship >= Relationship.KISS:
                $ add_point(KCT.BOYFRIEND)
            elif chloe.relationship >= Relationship.FWB:
                $ add_point(KCT.TROUBLEMAKER)
            
            scene v11chh6a
            with dissolve

            u "I think you'd make a good President. And the only way to find out if the rest of the girls support you is by running and seeing how they vote."

            scene v11chh6
            with dissolve

            li "And if I lose the vote I'll just have a target on my back and divide the sorority even more."

            scene v11chh6a
            with dissolve

            u "Maybe, but if you think you'd be best then it's only right that you run."

            scene v11chh6
            with dissolve

            li "That is some good advice."

        "I don't know":
            scene v11chh6a
            with dissolve

            u "I don't know what's best."

            scene v11chh6
            with dissolve

            li "You and I both."

    scene v11chh6c
    with dissolve
    
    u "Heard anything about any other girls wanting to run?"

    scene v11chh6b
    with dissolve

    li "No I haven't. Most of them think we just have to wait until Chloe graduates."

    scene v11chh6c
    with dissolve

    u "Is that so bad?"

    scene v11chh6b
    with dissolve

    li "By that time the reputation of the Chicks could be beyond repair. Next semester they'll be preparing for recruiting season and we don't want to do that with all this bad blood."

    scene v11chh6a
    with dissolve

    u "Oh yeah, that makes sense."

    scene v11chh6
    with dissolve

    li "I better stop talking before one of the girls walks in. I wouldn't want to continue this conversation with one of them right now."

    scene v11chh6a
    with dissolve

    u "Haha, I need to head home anyway. I'll see you around Linds."

    scene v11chh6
    with dissolve

    li "Haha, see ya."

    scene v11chh7 # TPP. MC leaving kitchen
    with dissolve

    pause 1

    scene v11chh8 # TPP. MC leaving chicks house front door
    with dissolve

    pause 1

    scene v11chh9 # TPP. MC on the sidewalk heading home
    with dissolve
    
    pause 1
    
    stop music fadeout 3
    
    if joinwolves:
        jump v11_wolves_seb_prank
    else:
        jump v11_apes_manhunt