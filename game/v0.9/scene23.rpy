# SCENE 23: Dinner At Ms. Roses
# Locations: Ms. Rose House
# Characters: Ms. Rose(Outfit 1), MC (Outfit 3), Chris(Outfit 2), Imre(Outfit 1), Finn(Outfit 3),
# Time: Friday Afternoon
label v9_dinner_w_rose:
    scene v9damr1 # FPP. Fade in at Ms. Rose's house
    with fade

    scene v9damr2 # FPP. show Chris knocking on Ms. Rose's door
    with fade

    pause 1

    scene v9damr2a # FPP. Same camera as v9damr2, show Ms. Rose opens door with a big smile, mouth closed
    with dissolve

    pause 0.5

    scene v9damr2b # FPP. Same camera as v9damr2, show Ms. Rose opens door with a big smile, mouth closed
    with fade
    ro "Boys! Come in! Thank you for coming."

    scene v9damr2a
    with dissolve
    ch "Thank you for having us."

    scene v9damr2c # FPP. Same camera as v9damr2, show Ms. Rose stood back from door, show Chris walking in door from behind, Ms. Rose mouth closed
    with dissolve

    pause 0.5

    scene v9damr3 # FPP. Show Ms. Rose in living room, Excited look, mouth open
    with dissolve
    ro "I know it's a bit early but I couldn't wait to try out my new kitchen! Can I get anyone a drink?"

    scene v9damr3b # FPP. Show Ms. Rose in living room, Excited look, mouth closed
    with dissolve
    ch "I'll have some water, if you don't mind."
    finn "Nothing for me, thanks."
    imre "Nah, I'm good. Thank you."
    u "I'll take a water, too. Thanks."

    scene v9damr3
    with dissolve
    ro "Coming right up."

    menu:
        "Offer To Help":
            jump v9_dinner_w_rose_help
        "Stay With The Wolves":
            jump v9_dinner_w_rose_stay


label v9_dinner_w_rose_help:

    scene v9damr3b
    with dissolve
    u "Um, here, let me help."

    scene v9damr4 # FPP. Show Ms. Rose in kitchen from behind, near sink
    with dissolve
    ro "You're such a fine young man. Your parents must be proud."

    scene v9damr4a # FPP. Same camera as v9damr4 Show ms rose at sink, glass in hand, mouth closed, looking at camera
    with dissolve
    u "I do my best. And you seem better. How are things?"

    scene v9damr4b # FPP. Same camera as v9damr4 Show ms rose at sink, glass in hand, mouth open, looking at camera
    with dissolve
    ro "It's a process. It'll take time. But I made the right choice and I'm happy."

    scene v9damr5 # FPP. Show Ms. Rose now close to camera, full glass in hand holdin out to camera, mouth closed
    with dissolve

    scene v9damr6 # FPP. Show Chris in living room, taking glass from MC, happy look, mouth closed
    with dissolve

    jump v9_dinner_w_rose_cont1

label v9_dinner_w_rose_stay:
    scene v9damr6a # FPP. Same camera as v9damr6, Show Chris in living room, neutral face, mouth closed
    with dissolve
    u "How do you think she's doing?"

    scene v9damr6b # FPP. Same camera as v9damr6, Show Chris in living room, slight smile, mouth open
    with dissolve
    ch "She sounded great on the phone. And she looks happier."

    scene v9damr6a
    with dissolve
    u "Yeah, she does seem happy now."

    scene v9damr7 # FPP. Show Ms. Rose entering the room with 2 glasses of water in hand, slight smile, mouth closed
    with dissolve
    # -Ms. Rose comes back with the drinks-

    jump v9_dinner_w_rose_cont1

label v9_dinner_w_rose_cont1:
    scene v9damr3
    with dissolve
    ro "I hope you boys are hungry. I may have gone overboard."

    scene v9damr6c # FPP. Same camera as v9damr6, Show Finn in living room, slight smile, mouth open
    with dissolve
    finn "I'm starving."

    scene v9damr6d # FPP. Same camera as v9damr6, Show Imre in living room, slight smile, mouth open
    with dissolve
    imre "You're always starving! You should get checked for a tapeworm!"

    scene v9damr3
    with dissolve
    ro "*laughs* I'll give you an extra helping to be sure it's fed properly."

    scene v9damr3a # FPP. Same camera as v9damr3, Show Ms. Rose in living room, neutral look, mouth open, arm up, palm open, pointing to dining room
    with dissolve
    ro "Everyone take a seat and I'll check on the food. It should be ready."

    scene v9damr3b
    with dissolve
    u "Let me help."

    scene v9damr3
    with dissolve
    ro "No, have a seat. This is a thank you dinner. I can't have you doing more work!"

    scene v9damr8 # FPP. Show MC walking to sit down at dining room table next to imre, imre already seated, mouths closed
    with dissolve

    pause 1

    scene v9damr9 # FPP. MC now sat at table, Show close up of Imre, neutral look, mouth closed
    with dissolve

    menu:
        "Talk About Working Out":
            $ addPoint("bro", 1)
            jump v9_dinner_w_rose_work
        "Talk About Viking Assignment":
            jump v9_dinner_w_rose_viking


label v9_dinner_w_rose_work:
    scene v9damr9
    with dissolve
    u "Hey you wanna catch a workout later?"

    scene v9damr9a # FPP. Same camera as v9damr9, MC now sat at table, Show close up of Imre, neutral look, mouth open
    with dissolve
    imre "You getting nervous about... Saturday?"

    scene v9damr9
    with dissolve
    # -MC looks around to make sure Ms. Rose can't hear-
    u "Just wanna be prepared."

    scene v9damr9a
    with dissolve
    imre "Yeah, I'm nervous too. If I get my ass beat, i'll never get laid again!"

    scene v9damr9
    with dissolve
    u "*laughs* I'm sure some desperate virgin will have pity on you."

    jump v9_dinner_w_rose_cont2

label v9_dinner_w_rose_viking:
    scene v9damr9
    with dissolve
    u "How hard was that viking thing in History class?"

    scene v9damr9a
    with dissolve
    imre "I thought it was fun. A great change from his usual classes."

    scene v9damr9
    with dissolve
    u "Yeah, I had a blast coming up with the scene, but having to get up in front of everyone. And those accents!"

    scene v9damr9a
    with dissolve
    imre "We all sounded horrible. But I'm glad I didn't get stuck with Cameron."

    scene v9damr9
    with dissolve
    u "It's like he was TRYING to fail!"

    scene v9damr9a
    with dissolve
    imre "*laughs* I don't think Cam has to try that hard to fail."

    jump v9_dinner_w_rose_cont2

label v9_dinner_w_rose_cont2:
    # -Ms. Rose comes in with a large lasagne-
    scene v9damr10 # FPP. Show Ms. Rose entering the dining room with a large lasange, slight smile, mouth closed
    with dissolve
    finn "It smells so good!"

    scene v9damr11 # FPP. Show Ms. Rose setting lasange on table, slight smile, mouth closed
    with dissolve
    u "*laughs* Now I think I have a tapeworm, too!"

    scene v9damr12 # FPP. Show Ms. Rose Sat at the end of table, Imre seated to MC's right,neutral expressions,  Ms. Rose mouth open, Imre mouth closed
    with dissolve
    ro "Dig in boys!"

    scene v9damr13 # FPP. Show Chris sat opposite side of table from camera, excited smile, mouth open
    with dissolve
    # -Everyone gets their food and begins to eat-
    ch "Wow, delicious."

    scene v9damr9a
    with dissolve
    imre "It tastes even better than it smells."

    scene v9damr12a # FPP. same camera as v9damr12, neutral expressions,  Ms. Rose mouth closed, Imre mouth closed
    with dissolve
    u "You can always open a restaurant if you get tired of dealing with college kids, Ms. Rose."

    scene v9damr12a2
    with dissolve
    ro "I couldn't imagine life without my students, especially good ones like you boys."

    scene v9damr13
    with dissolve
    ch "We're just glad we could help."

    scene v9damr12a3 #Ms Rose now talking to Chris - mouth open
    with dissolve
    ro "You did help, so much."

    scene v9damr12a
    with dissolve
    u "You're a great teacher, Ms. Rose, and we all want you to be happy. We're here if you need anything."

    scene v9damr12a2
    with dissolve
    ro "What I need now is for you boys to finish off this lasagne-"

    scene v9damr14c # FPP. Show finn, sat to left of mc at table, slight smile, mouth open
    with dissolve
    finn "Yes, ma'am!"

    scene v9damr13
    with dissolve
    ch "Our pleasure!"

    scene v9damr12a
    with dissolve
    u "I'm stuffed."

    scene v9damr13d
    with dissolve
    ch "Me too. I can't move."

    scene v9damr12
    with dissolve
    ro "Don't give up now. I haven't served dessert."

    scene v9damr14c
    with dissolve
    finn "Oooh, dessert!"

    scene v9damr9b
    with dissolve
    imre "Still, Finn? How?"

    scene v9damr12
    with dissolve
    # -Finn shrugs-
    ro "Good! I'll go get it."

    menu:
        "Try Helping Out Again":
            $ addPoint("bf", 1)
            jump v9_dinner_w_rose_help
        "Wait":
            jump v9_dinner_w_rose_wait

label v9_dinner_w_rose_help:
    scene v9damr12f # FPP. Same camera as v9damr12, Show Ms. Rose now stood at the end of table, Imre seated to MC's right,neutral expressions,  Ms. Rose mouth closed, Imre mouth closed
    with dissolve
    u "Please, let me help. I need to get up and move around."

    scene v9damr12b # FPP. Same camera as v9damr12, Show Ms. Rose now stood at the end of table, Imre seated to MC's right,neutral expressions,  Ms. Rose mouth open, Imre mouth closed
    with dissolve
    ro "Alright, you can help."

    scene v9damr4c # FPP. Same camera as v9damr4, Show Ms. Rose, stood at the counter, apple pie infront of her, knife in hand, looking at camera, slight smile, mouth closed
    with dissolve
    # -MC gets up and follows Ms. Rose to the kitchen-
    u "It smells so good. What is it?"

    scene v9damr4d # FPP. Same camera as v9damr4, Show Ms. Rose, stood at the counter, apple pie infront of her, knife in hand, looking at camera, slight smile, mouth open
    with dissolve
    ro "My grandmother's famous Caramel Apple Pie."

    scene v9damr4c
    with dissolve
    u "Wow, you did all thise while unpacking? I would have burned the house down."

    scene v9damr4d
    with dissolve
    ro "I was very careful. You guys helped me when I really needed it, so this dinner is special to me. I couldn't mess it up."

    scene v9damr4c
    with dissolve
    u "You certainly overdid yourself, Ms. Rose."

    scene v9damr4d
    with dissolve
    ro "Wait 'til you taste it first! Haha."

    scene v9damr15 # TPP. Show MC entering dining room from Chris' POV, 2 bowls in hand, slight smile
    with dissolve

    pause 1

    # -They both sit down-
    jump v9_dinner_w_rose_cont3
label v9_dinner_w_rose_wait:

    scene v9damr9
    with dissolve
    u "(I wanna help but she said not to get up)"

    scene v9damr9a
    with dissolve
    imre "It feels strange sitting here and not helping."

    scene v9damr9
    with dissolve
    u "That's what I was just thinking!"

    scene v9damr14
    with dissolve
    finn "Did she look sad for a second when we were talking earlier?"

    scene v9damr14a # FPP. same camera as v9damr14, Show finn, sat to left of mc at table, slight smile, mouth closed
    with dissolve
    u "Kinda. I hope everything's OK."

    jump v9_dinner_w_rose_cont3

label v9_dinner_w_rose_cont3:
    scene v9damr13a #FPP Chris rubbing hands together looking at his pie
    with dissolve
    ch "OK, you convinced me. I'll have some dessert!"

    scene v9damr12a4
    with dissolve
    ro "Nobody can resist Grandma Ruth's famous Caramel Apple Pie!"

    scene v9damr12g # TPP - Closeup of Rosa looking down the table (not into camera), mouth open slight smile
    with dissolve
    u "Best pie I've ever had!"

    scene v9damr9a
    with dissolve
    imre "I'd be the size of a sumo wrestler if I frew up with Grandma Ruth!"

    scene v9damr12a4
    with dissolve
    ro "She did her best to make sure my dad was! Haha."

    scene v9damr13b #FPP Chris full smile/chuckle looking at Ms Rose mouth open. Miss Rose smiling mouth closed looking towards Finn (Out of shot)
    with dissolve
    ch "Whoa! You actually filled Finn up, Ms. Rose! I don't think that's ever happened!"

    scene v9damr14b # FPP Finn mouth open chuckling towards Mr Rose (out of shot) slouching holding stomach
    with dissolve
    finn "I don't either!"

    scene v9damr12g
    with dissolve
    ro "Grandma Ruth would be so proud."

    scene v9damr12c # FPP. Same camera as v9damr12,slight smile,both raising glass of water in air,  Ms. Rose mouth closed, Imre mouth closed
    with dissolve
    # -MC raises his water to toast-
    u "To Grandma Ruth!"

    scene v9damr12d # FPP. Same camera as v9damr12,slight smile,both raising glass of water in air,  Ms. Rose mouth open, Imre mouth closed
    with dissolve
    ro "And to you boys. My Wolves in shining armor."

    scene v9damr12a
    with dissolve

    pause 1

    scene v9damr13c # TPP. Same camera as v9damr13, Show Chris trying to stand opposite side of table from camera, excited smile, closed Ms Rose halting him mouth open pleading
    with dissolve
    ro "No, no, no. Sit."

    scene v9damr12e # FPP. same camera as v9damr12, Show Ms. Rose leaving room, Imre seated to MC's right,neutral expressions,  Ms. Rose mouth closed, Imre mouth closed
    with dissolve

    pause 1

    scene v9damr12h
    with dissolve
    ro "How about a quick tour before the evening ends?"

    scene v9damr12a
    with dissolve
    u "Great idea."

    scene v9damr16 # FPP. Show Ms. Rose in corridor,there is a line of pictures in frames,image descriptions: Ms. Rose stnading in front of a car. Her parents hugging. An old woman in an apron, Ms. Rose  pointing to the last picture on the wall, slight smile, mouth open
    with dissolve
    ro "There she is, the chef herself."

    scene v9damr17 # FPP. Show close up of picture of Grandma Rose, on wall in corridoor
    with dissolve
    finn "Thanks for the excellent pie, Grandma Ruth."

    scene v9damr6e # FPP. Same camera as v9damr6, Show Tv in living room, show imre facing away from camera, imre facing tv
    with dissolve
    imre "Nice TV, Ms. Rose. Is it new?"

    scene v9damr16a
    with dissolve
    ro "Yes. I dropped the one you helped me move. Got it all the way here and tipped it over when I was plugging it in."

    scene v9damr6a2
    with dissolve
    ch "Oh, no! Well, at least you got an upgrade out of the deal. I wish we'd have stayed to help you setup, though."

    scene v9damr16a
    with dissolve
    ro "Nonsense. You boys helped so much! Really, I'm so thankful."

    scene v9damr18 # FPP. Show Ms. Rose stood at the front door (from inside house), door open, mouth closed
    with dissolve
    imre "Thanks for the dinner. I don't think I'll be able to eat for a whole day."

    scene v9damr18a # FPP. same camera as v9damr18, Show Finn close up, by front door (from inside), finn mouth open
    with dissolve
    finn "I wouldn't go that far! But it was delicious!"

    scene v9damr19 # FPP. Show rear shot of Chris and Imre leaving the house
    with dissolve

    pause 1

    scene v9damr2a
    with dissolve

    if consoledRose:
        jump v9_dinner_w_rose_cont4

    else:
        jump v9_room_fri_eve

label v9_dinner_w_rose_cont4:
    # -Ms. Rose pulls MC aside-
    scene v9damr2f2 # TPP - Rosa Grabbing MC's arm gently as he walks out the door, her mouth open, nervous expression. MC turning to look at Rosa neutral face. Eyes locked to eachother
    with dissolve
    ro "Um, [name], can I talk to you for a moment?"

    scene v9damr2f3 # TPP - Same as 2f2 MC head turned towards the door and mouth open almost shouting.
    with dissolve
    u "Sure. Guys, I'll catch up to you."

    scene v9damr2f # FPP Closeup of rosa, nervous eyes into camera mouth open a if talking quietly.
    with dissolve
    ro "I just wanted to say an extra thank you to you."

    scene v9damr2d # FPP same as 2f, mouth closed.
    with dissolve
    u "For what?"

    scene v9damr2f
    with dissolve
    ro "You've helped me a lot, even more than the rest of the boys. When you took the time to really talk to me while we were moving, it meant a lot."

    scene v9damr2d
    with dissolve
    u "Aww, well you're welcome. You're such a great teacher... a great person. I just want to make sure you're OK."

    scene v9damr2f
    with dissolve
    ro "And I appreciate it. I was having a hard time and you cheered me up. You're so helpful."

    scene v9damr2d
    with dissolve
    u "What's the point of being part of a community if you can't help your fellow man...or woman. Haha."

    scene v9damr2e # TPP , show Ms. Rose opens door with a nervous smile, reaching out to place hand on MC arm, mouth open
    with dissolve
    ro "You're going to be an excellent contribution to society. Your parents did a great job with you, [name]."

    scene v9damr2g # Same cam as 2d but ms rose much closer, hand down now shy smile mouth closed.
    with dissolve
    u "I'll be sure to tell them you said so."

    scene v9damr2h ## Same cam as 2d but ms rose much closer, hand down now shy smile mouth open.
    with dissolve
    ro "You take care heading back to the dorms. Hope I didn't keep you too long."

    scene v9damr2g
    with dissolve
    u "I'm sure they're waiting for me up ahead. We stick together."

    scene v9damr2h
    with dissolve
    ro "Good. You have a good night."

    scene v9damr2g
    with dissolve
    u "You too."

    scene v9damr20 # FPP. Show Rear shot of Imre, outside Ms. Rose house
    with dissolve

    pause

    jump v9_room_fri_eve
