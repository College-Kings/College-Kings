# SCENE 12: Hallway
# Locations: Hallway / First aid room
# Characters: MC (Outfit 1), Tough Guy (Outfit 1), Lindsey (Outfit 1), Girl With Lindsey (Outfit 1), Random People in hallway
# Time: Thursday Morning

label v9_hallway:

    scene v9hlw1 # TPP. Show MC walking down the hallway on his own, lost in his own thoughts.
    with dissolve

    u "(Well that was really something, I guess. Who would have thought Mr. Lee's class could be anything more than a huge snorefest?)"

    if CharacterService.is_girlfriend(lauren, Relationship.GIRLFRIEND):
        scene v9hlw2 # TPP. Show MC looking down as he continues to walk.
        with dissolve

        pause 1

    else:
        scene v9hlw3 # FPP. Show super hot girl walking past MC.
        with dissolve

        u "(Ohhh goddamn, honey why are you so hot?)"

        scene v9hlw3a
        with dissolve

        pause 1

    scene v9hlw4 # TPP. Show tough guy bumping into MC, MC looks shocked, tough guy super pissed. Mouths closed.
    with vpunch

    pause 0.5
    
    scene v9hlw5 # FPP. Close up tough guy, looking super pissed off.
    with dissolve

    u "Ouch! What the?!"

    u "(Well, fuck.)"

    menu (fail_label="v9_hall_calm"): 
        "Apologize": 
            $ reputation.add_point(RepComponent.BRO)
            jump v9_hall_apol

        "Tell him to calm down":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            jump v9_hall_calm

label v9_hall_apol:
    u "Sorry, dude. I didn't see you there."

    scene v9hlw5a # FPP. Same camera as v9hlw5a, tough guy looking angrier.
    with dissolve

    u "No hard feelings, huh? We all get carried away sometimes."

    scene v9hlw5b # FPP. Same camera as v9hlw5a, tough guy mouth open.
    with dissolve

    unknown "Watch where you're fucking walking, bitch!"

    play music "music/v9/Track Scene 12_1.mp3" fadein 2

    jump v9_hall_cont1

label v9_hall_calm:
    u "Whoa, that startled me, dude. I guess we ran into each other."

    scene v9hlw5a
    with dissolve

    u "I guess we should watch where we're going. No hard feelings, are we cool?"

    scene v9hlw5b
    with dissolve

    unknown "Fuck you!"

    play music "music/v9/Track Scene 12_1.mp3" fadein 2

    jump v9_hall_cont1

label v9_hall_cont1:
    scene v9hlw6 # TPP. Show the tough guy pushing MC away angrily MC holds his ground, MC looking shocked, tough guy really angry.
    with dissolve

    pause 0.5

    scene v9hlw7 # FPP. Show tough guy, looking SUPER angry, mouth closed.
    with dissolve

    u "Now look, we don't need to do this, okay?"

    scene v9hlw6
    with dissolve

    pause 0.5

    scene v9hlw7a # FPP. Same camera as v9hlw7, tough guy mouth open.
    with dissolve

    unknown "Do what, this? Yeah? You like being pushed around, bitch? Huh?"

    scene v9hlw7
    with dissolve

    u "You got the wrong idea, man."

    scene v9hlw7a
    with dissolve

    unknown "Now you are calling me stupid?"

    unknown "Wanna try another push?"

    scene v9hlw8 # TPP. Show tough guy in MC's face, almost nose to nose.
    with dissolve

    menu (fail_label="v9_hall_no_punch"): 
        "Punch the guy": 
            $ reputation.add_point(RepComponent.BRO)
            $ hl_punch = True
            jump v9_hall_punch

        "Don't punch the guy":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ hl_punch = False
            jump v9_hall_no_punch

label v9_hall_punch:
    scene v9hlw8a # TPP. Same camera as v9hlw8, show MC stepping back and looking the tough guy in the face, both angry.
    with dissolve

    $ grant_achievement("back_down")
    u "(Nah, fuck this.)"

    scene v9hlw8b # TPP. Show MC swinging a punch into the tough guys stomach, the tough guy winces in pain.
    with vpunch

    pause 1

    scene v9hlw7b # FPP. Show the tough guy wincing in pain, holding his stomach after having been punched in the stomach.
    with dissolve

    u "Oh sorry, that was a punch. Didn't catch that? Oh, okay, here!"

    scene v9hlw8c # TPP. Same camera as v9hlw8, show MC swinging an uppercut on to the tough guys chin, the tough guy winces back in pain and starts to fall.
    with vpunch

    pause 1

    scene v9hlw9 # FPP. Show tough guy lying on the floor in pain.
    with dissolve

    u "How about that? Had enough?"

    scene v9hlw10 # TPP. Show MC looking around as he's now surrounded by 2/3 random passers by, laughs/happy expressions, one of them mouth open.
    with dissolve

    unknown "Think he's had enough?"

    scene v9hlw11 # FPP. Show the passers by who stopped and surrounded MC, looking at camera, all mouths closed.
    with dissolve

    if reputation() == Reputations.LOYAL:
        u "(Actually, that might be one of the stupidest things I've done lately. Fuck it, [name]! That guy was a jerk, but did I really have to knock him out in front of everybody?)"

    elif reputation() == Reputations.POPULAR:
        u "I tried to stop this guys. Guess he wasn't smart enough to listen."

    else: 
        u "But you've seen it, guys. He was asking for it. And totally deserved what he got. One less douchebag in the hallways, I guess."

    stop music fadeout 3
    
    scene v9hlw12 # FPP. Show Lindsey and another girl who are a distance away from the camera, Lindsey looking at camera (MC). Lindsey smile.
    with dissolve

    play music "music/v9/Track Scene 12_2.mp3" fadein 2

    pause 1

    scene v9hlw12a # FPP. Same camera as v9hlw12, show the girl Lindsey is with pulling her arm, Lindsey trying to resist.
    with dissolve

    pause 1

    scene v9hlw12b # FPP. Same camera as v9hlw12, just before Lindsey is about to be pulled out of view by her friend, she glances at camera, bits her lip and then leaves.
    with dissolve

    pause 1

    scene v9hlw13 # TPP. Show the the people who surrounded MC walking away, MC continues to walk down the hallway.
    with dissolve

    u "(Now talk about random shit going on.)"

    scene v9hlw14 # TPP. Show MC continuing to walk down the hallway, slight confused expression about what just happened.
    with dissolve

    u "(I should not let things catch me off guard. Ever. And I will not.)"

    scene v9hlw15 # TPP. Show the girl who Lindsey was with tapping MC on the shoulder, MC begins to turn around in confusion.
    with dissolve

    u "(What the?!)"

    scene v9hlw16 # FPP. Show the girl Lindsey was with, bored expression, holding out a piece of paper as if she's trying to pass it to MC, mouth open.
    with dissolve

    unknown "I was told to give you this. *Sigh*"

    scene v9hlw16a # FPP. Same camera as v9hlw16, show the girl now walking away from the camera.
    with dissolve

    u "What the hell?"

    scene v9hlw18 # FPP. Show MC holding the piece of paper in his hand (as if he is looking at it), on the paper it says "Lindsey" and a phone number.
    with dissolve

    u "(Well, well, talk about random things...)"

    scene v9hlw19 # TPP. Show MC continuing to walk down the hallway, smile, holding the small piece of paper in his hand.
    with dissolve

    u "(I guess I will call you, Lindsey. Maybe. A bit later. Now I should get back to my room.)"

    stop music fadeout 3

    jump thurs_aft_room
    
label v9_hall_no_punch:

    scene v9hlw20 # TPP. ! RETURN CHARACTERS TO V9HLW8 ! Show the tough guy punching MC in the face, MC winces in pain and begins to drop to the ground.
    with vpunch

    pause 0.5

    scene v9hlw21 # TPP. Show MC lying on his back on the ground in pain.
    with dissolve

    u "(What the fuck!?)"

    scene v9hlw22 # FPP. Show the tough guy stood over MC looking down at MC (Camera). Tough guy angry mouth open, make image blurry if possible.
    with dissolve

    unknown "Fucking asshole."

    scene v9hlw22a # FPP. Same camera as v9hlw22, show the guy walking away from camera. Slightly less blurry.
    with dissolve

    pause 0.5

    scene v9hlw22b # FPP. Same camera as v9hlw22, tough guy now gone, show Lindsey walking towards camera. Even less blurry.
    with dissolve

    u "(Shit.)"

    stop music fadeout 3

    scene v9hlw23 # TPP. Show MC now sat up against the wall with a bleeding nose, Lindsey kneeling infront of MC, Lindsey concerned, mouth open.
    with dissolve

    play music "music/v9/Track Scene 12_2.mp3" fadein 2

    li "Are you okay?"

    scene v9hlw24 # FPP. Close up Lindsey, concerned expression, mouth closed.
    with dissolve

    u "I dunno, you tell me. Do I look like I'm okay?"

    scene v9hlw24a # FPP. Same camera as v9hlw24, smile, mouth open.
    with dissolve

    li "Heh, I've seen worse."

    scene v9hlw24b # FPP. Same camera as v9hlw24, smile, mouth closed.
    with dissolve

    u "And I've felt worse. That prick, catching me off guard. That stings the most. Ouch."

    scene v9hlw24a
    with dissolve

    li "I think something else stings more at the moment. Come, let me help you."

    scene v9hlw23a # TPP. Same camera as v9hlw23, Lindsey now helping MC get on his feet.
    with dissolve

    li "Let me take you to the first aid room."

    scene v9hlw25 # TPP. Show MC and Lindsey walking next to eachother, MC slight limp camera from behind.
    with dissolve

    u "I can walk, but how could I refuse such an offer."

    scene v9hlw26 # TPP. Show MC and Lindsey in the first aid room, Lindsey looking at MC, MC walking over to a medical bed to sit on it.
    with fade

    li "Sit on that bed and give me a second."

    scene v9hlw27 # FPP. MC now sat on bed, show Lindsey getting some cotton wool from a counter.
    with dissolve

    pause 1

    scene v9hlw28 # TPP. Show Lindsey placing the cotton wool on MC's bleeding nose, MC acting in pain, Lindsey mouth open.
    with dissolve

    li "Now keep it still, we gotta wait until the bleeding stops."

    scene v9hlw29 # FPP. Close up of Lindsey looking at camera, Lindsey slight focused expression, mouth closed.
    with dissolve

    u "Alright, alright."

    scene v9hlw29a # FPP. Same camera as v9hlw29, Lindsey mouth open.
    with dissolve

    li "Doesn't seem like your nose is broken or anything."

    scene v9hlw29
    with dissolve

    u "Hah, you got the entirely wrong idea."

    scene v9hlw28a # TPP. Same camera as v9hlw28, show MC holding to cotton wool on his nose, Lindsey mouth open.
    with dissolve

    li "Hold this firmly."

    li "The bleeding should stop in the next few minutes."

    scene v9hlw27a # FPP. Same camera as v9hlw27, Show Lindsey writing on a small piece of paper, Lindsey mouth open.
    with dissolve

    li "But in case it gets worse, here's my number. If it's an emergency, you can drop me a message."
    
    scene v9hlw29b # FPP. Same camera as v9hlw29, Lindsey stood futher away from the camera, mouth closed.
    with dissolve

    u "Emergency only? To be honest, it feels like it's gonna take some time to fully recover."

    scene v9hlw29c # FPP. Same camera as v9hlw29, Lindsey mouth open.
    with dissolve

    li "I'm gonna be counting on it. Haha."

    scene v9hlw29b
    with dissolve

    u "I bet you are."

    scene v9hlw29c
    with dissolve

    li "Now if you will excuse me, I'm pissed off for being late as it is. I'll see you around."

    scene v9hlw30 # FPP. Show Lindsey leaving walking to the door of the first aid room.
    with dissolve

    u "That you will."

    scene v9hlw30a # FPP. Same camera as v9hlw30, Lindsey turns around and looks at camera, mouth open.
    with dissolve

    li "Bye."

    scene v9hlw30b # FPP. Same camera as v9hlw30, Lindsey still turned around, blows a kiss to MC (Camera).
    with dissolve

    pause 1

    scene v9hlw31 # TPP. Show MC lying down on the bed.
    with dissolve
     
    u "(Well fuck it, if it wasn't the best punch outcome I have ever had.)"

    scene v9hlw31a # TPP. Same camera as v9hlw31, MC checking his nose with his hand, nose no longer bleeding.
    with dissolve

    u "(I think the bleeding has stopped. At least for now.)"

    scene v9hlw31b # TPP. Same camera as v9hlw31, MC getting up from the hospital bed, preparing to leave.
    with dissolve

    u "(I should go back to my room.)"

    pause 0.8

    scene v9hlw32 # TPP. Show MC leaving the first aid room.
    with dissolve

    stop music fadeout 3

    pause 1

    jump thurs_aft_room