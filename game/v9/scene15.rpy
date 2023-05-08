# SCENE 15: Your Room Cam & Samantha
# Locations: MC Apes Room
# Characters: MC (Outfit 1), Cameron (Outfit 2), Samantha (Outfit 1)
# Time: Thursday Evening

label v9_thur_room_w_cam:
    scene v9trc1 # TPP. Show MC laid on bed, eyes closed, mouth shut
    with fade

    play music music.ck1.v9.Track_Scene_14 fadein 2
    
    pause 1

    scene v9trc2 # TPP. Show Cameron and Samantha entering bedroom, 
    with dissolve

    pause 1

    scene v9trc3 # TPP. Show MC stood up by bed, surprised expression, mouth closed
    with dissolve

    pause 1

    if hl_punch:
        jump v9_thur_room_w_cam_punch
    else:
        jump v9_thur_room_w_cam_no_punch

label v9_thur_room_w_cam_punch:
    scene v9trc4 # FPP. Show Cameron and samantha side by side, cameron with 2 beers in hand arms raised,cameron and samantha excited, Cameron mouth open, samantha mouth closed
    with dissolve
    ca "[name], You're fucking famous!"

    scene v9trc4a # FPP. Same camera as v9trc3, Cameron placing 2 beers on table, both still excited
    with dissolve
    # -Cameron raises the two beers in a cheer then puts them on the table-
    u "Huh?"

    scene v9trc4b # FPP. Same camera as v9trc3, cam and samantha arms down, excited look, mouths closed
    with dissolve
    u "What are you talking about?"

    scene v9trc4c # FPP. Same camera as v9trc3, excited look, Cameron mouth open, Samantha mouth closed
    with dissolve
    ca "No time for modesty now. You're hot shit right now!"

    scene v9trc4b
    with dissolve
    u "Seriously, what are you talking about?"

    scene v9trc4d # FPP. Same camera as v9trc3, excited look, Cameron mouth closed, Samantha mouth open
    with dissolve
    sa "Haven't you seen Kiwii?"

    scene v9trc4b
    with dissolve
    u "What? No. I've just been chilling. What's going on?"

    $ v9s15KiwiiPost1 = KiwiiPost(grayson, "v9/Scene 12/v9hlw8c.webp", "That's my boy! Go [name]! Fuck yeah!", number_likes=renpy.random.randint(100, 200))
    $ v9s15KiwiiPost1.newComment(cameron, "Fuckin' A!", number_likes=renpy.random.randint(100, 200))
    $ v9s15KiwiiPost1.newComment(riley, "Knew he had it in him!", number_likes=renpy.random.randint(200, 250))

    call screen phone

    menu:
        "Brag":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            jump v9_thur_room_w_cam_brag
        "Be humble":
            jump v9_thur_room_w_cam_humble
        

label v9_thur_room_w_cam_brag:
    scene v9trc4b
    with dissolve
    u "Shit! Didn't know it was caught on camera, but the guy deserved it."

    scene v9trc4e # FPP. Same camera as v9trc3, neutral look, Cameron mouth open, Samantha mouth closed
    with dissolve
    ca "What the hell happened?"

    scene v9trc4f # FPP. Same camera as v9trc3, neutral look, Cameron mouth closed, Samantha mouth open
    with dissolve
    sa "Are you OK?"

    scene v9trc5 # FPP. Close up on samantha, Worried look, mouth open
    with dissolve

    pause 1

    scene v9trc6 #FPP. Close up on Cameron, Proud look, mouth closed
    with dissolve
    u "I'm great! Don't worry."
    u "You saw, man. He ran his mouth and I taught him a lesson!"

    scene v9trc6a #FPP. Same camera as v9trc6, Close up on Cameron, Proud look, mouth open
    with dissolve
    ca "Didn't stand a chance!"

    jump v9_thur_room_w_cam_cont1

label v9_thur_room_w_cam_humble:
    scene v9trc4g #FPP. Same camera as v9trc3, cam and samantha arms down, neutral look, mouths closed
    with dissolve
    u "He started it and I finished it. What can I say?"

    scene v9trc4e
    with dissolve
    # -Cameron laughs-
    ca "You can say you'll do that again Saturday!"

    scene v9trc4g
    with dissolve
    u "I'll do my best."

    scene v9trc4f
    with dissolve
    sa "Those Wolf cubs don't stand a chance."

    scene v9trc4g
    with dissolve
    u "Honestly, I don't know what happened. It all went so fast."

    scene v9trc4e
    with dissolve
    ca "You hulked out!"

    scene v9trc4g
    with dissolve
    u "Something like that."

    jump v9_thur_room_w_cam_cont1

    # -Continue after choices-
label v9_thur_room_w_cam_cont1:
    scene v9trc4e
    with dissolve
    # -Cameron grabs MC's shoulder-
    ca "I know where to put my money in the Freshman Brawl!"

    scene v9trc4f
    with dissolve
    sa "Everyone's gonna be scared of you now. It was a smart move."

    scene v9trc4g
    with dissolve
    u "I didn't do it on purpose. It just happened, but yeah, won't hurt."

    scene v9trc4c
    with dissolve
    ca "We need to celebrate! Thirsty? I think this deserves a toast."

    scene v9trc4a
    with dissolve

    menu:
        "Drink":
            $ reputation.add_point(RepComponent.BRO)
            jump v9_thur_room_w_cam_drink
        "Don't drink":
            jump v9_thur_room_w_cam_no_drink
        
label v9_thur_room_w_cam_drink:
    u "Just one!"

    scene v9trc4i # FPP. Same camera as v9trc4, Cameron drinking beer,samantha stood by side, samantha worried look, mouths closed
    with dissolve

    pause 1

    scene v9trc4j # FPP. Same camera as v9trc4, cam neutral look, samantha worried look, Cameron mouth closed, Samantha mouth closed
    with dissolve

    u "Aw shit!"

    u "I'm sorry, Sam. Cam, get those bottles out of here!"

    scene v9trc4k # FPP. Same camera as v9trc4, cam neutral look samantha nervous smile, Cameron mouth closed, Samantha mouth open
    with dissolve
    sa "It's okay. I have to get used to being around it. Besides, beer wasn't my thing anyway."
    jump v9_thur_room_w_cam_cont2

label v9_thur_room_w_cam_no_drink:
    u "I don't think we should."

    scene v9trc4k # FPP. Close up on samantha, Worried look, mouth open
    with dissolve
    sa "Don't do that on my account. I can handle it."

    scene v9trc4i # FPP. Close up on Cameron, neutral look, mouth closed
    with dissolve
    u "Nah, I need to keep a clear head for... studying."

    scene v9trc4i
    with dissolve

    pause 1

    jump v9_thur_room_w_cam_cont2

label v9_thur_room_w_cam_cont2:
    scene v9trc4f
    with dissolve
    sa "You're gonna have your pick of the Apes groupies now."

    scene v9trc4g
    with dissolve
    u "(We have groupies?)"
    u "It'll blow over soon. Next time Cam gets drunk and kisses a tree..."

    scene v9trc4c
    with dissolve
    ca "Who told you about that? Grayson? That dick!"

    scene v9trc4g
    with dissolve
    u "I was just joking! Seemed like something you'd do, though."

    jump v9_thur_room_w_cam_cont5

label v9_thur_room_w_cam_no_punch:
    scene v9trc4e # FPP. Same camera as v9trc2, Cameron mouth open, samantha mouth closed
    with dissolve
    ca "[name], what the fuck?"

    scene v9trc4f
    with dissolve
    sa "Are you OK?"

    scene v9trc4g
    with dissolve
    u "What?"

    scene v9trc4e
    with dissolve
    ca "It's all over school. You're a laughing stock! You've been an Ape for how long? Already embarrassing the house!"

    scene v9trc4g
    with dissolve
    u "What are you talking about?"

    scene v9trc4f
    with dissolve
    sa "You haven't seen Kiwii?"

    scene v9trc4g
    with dissolve
    u "No. I was just chilling, until King Kong over here barged in."

    scene v9trc4f
    with dissolve
    sa "You better check it."

    $ v9s15KiwiiPost2 = KiwiiPost(sebastian, "v9/Scene 12/v9hlw20.webp", "", number_likes=renpy.random.randint(100, 200))
    $ v9s15KiwiiPost2.newComment(chris, "Wow, hope he's OK!", number_likes=renpy.random.randint(100, 200))
    $ v9s15KiwiiPost2.newComment(cameron, "Ahhhh! Preview of Saturday's Freshman Brawl!", number_likes=renpy.random.randint(150, 170))

    call screen phone
    
    menu:
        "Shrug it off":
            jump v9_thur_room_w_cam_shrugg_off
        "Get defensive":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            jump v9_thur_room_w_cam_defensive

label v9_thur_room_w_cam_shrugg_off:
    scene v9trc4g
    with dissolve
    u "Aww it's not that bad."

    scene v9trc4c
    with dissolve
    ca "Not that bad? The whole fucking school saw you get knocked out!"

    scene v9trc4k
    with dissolve
    sa "The important thing is that you're alright, [name]. You are, aren't you?"

    scene v9trc5a
    with dissolve
    u "Yeah, I'm fine. It really wasn't that big a deal. It'll blow over."

    scene v9trc6c # FPP. Same camera as v9trc6 Close up on Cameron, annoyed look, mouth open
    with dissolve
    ca "You better fucking hope so!"

    jump v9_thur_room_w_cam_cont3

label v9_thur_room_w_cam_defensive:
    scene v9trc6d # FPP. Same camera as v9trc6a Close up on Cameron, annoyed look, mouth closed
    with dissolve
    u "He blindsided me. What the fuck was I supposed to do?"

    scene v9trc6c 
    with dissolve
    # -MC gets in Cameron's face-
    ca "You were supposed to knock his ass out like a real Ape!"

    scene v9trc6d
    with dissolve
    u "And get expelled in my first semester? No thank you!"

    scene v9trc6c
    with dissolve
    ca "How can we count on you this weekend if you can't handle one fucking guy?"

    scene v9trc6e # FPP. Same camera as v9trc6a Close up on Samantha, annoyed look, mouth open
    with dissolve
    # -Samantha breaks them apart-
    sa "*Yelling* OK! Stop! Both of you! Jesus. You're both clearly mindless apes. Congratulations."

    pause 1

    jump v9_thur_room_w_cam_cont3

label v9_thur_room_w_cam_cont3:
    scene v9trc4f
    with dissolve
    sa "Sit down. I want to check you out."

    scene v9trc6c
    with dissolve
    ca "Gross!"

    menu:
        "Protest":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            jump v9_thur_room_w_cam_protest
        "Follow orders":
            jump v9_thur_room_w_cam_follow
        
label v9_thur_room_w_cam_protest:
    scene v9trc4g
    with dissolve
    u "Really, I'm fine."

    scene v9trc4k
    with dissolve
    sa "I won't shut up until I know for sure. You helped me when I needed it. Let me return the favor."
    jump v9_thur_room_w_cam_cont4


label v9_thur_room_w_cam_follow:
    scene v9trc4g # FPP. Same camera as v9trc4, cam neutral look samantha nervous smile, Cameron mouth closed, Samantha mouth closed
    with dissolve
    u "(Yes, ma'am, I'll move to the bed... even if your asshole brother's standing right there!)"

    scene v9trc7 # FPP. Show samantha from MC perspective now sat on bed,samantha slight smile, mouth closed
    with dissolve
    u "If it will make you feel better."

    scene v9trc8 # FPP. Close up on samantha now stood infront of mc who is sat down, flirty smile, mouth open
    with dissolve
    sa "It will. You took care of me and now I want to take care of you."

    scene v9trc9 # FPP. Show Samantha right infront of mc bent down(from MC's Perspective sat on bed), Show cameron behind her,Sam flirty smile, Cameron annoyed look, sam mouth closed, cameron mouth open
    with dissolve
    ca "Ugh. Get a room."

    scene v9trc9a # FPP. Same camera as v9trc9 Show Samantha right infront of mc bent down, Show cameron behind her,Sam flirty smile, Cameron annoyed look, sam mouth closed, cameron mouth closed
    with dissolve
    u "*Laughing* We have one. You just happen to be in it."

    jump v9_thur_room_w_cam_cont4

label v9_thur_room_w_cam_cont4:
    scene v9trc9b # FPP. Same camera as v9trc9 Show Samanta stood up next to Cameron (from MC's Perspective sat on bed), Samantha happy smile, Cameron neutral look, Mouths closed
    with dissolve
    u "See, nothing to worry about."

    scene v9trc9d # FPP. Same camera as v9trc9 Show Samanta stood up next to Cameron (from MC's Perspective sat on bed), Samantha happy smile, Cameron annoyed look look, cam mouth closed, samantha mouth open
    with dissolve
    ca "You better be ready for the Brawl. That's all I got to say."

    if sideWithCameron:
        scene v9trc9b
        with dissolve
        u "(So much for all that bonding we did... Maybe he'll calm down after the Brawl.)"

        jump v9_thur_room_w_cam_cont5
    else:
        scene v9trc9b
        with dissolve
        u "Good, I've had more than enough of you. Why don't you leave so me and your sister can get better acquainted?"

        scene v9trc9c
        with dissolve
        sa "You look fine. But please take care of yourself. Get some rest before the fight."

        scene v9trc9b
        with dissolve
        u "Of course. Thank you."
        jump v9_thur_room_w_cam_cont5

label v9_thur_room_w_cam_cont5:
    scene v9trc9c
    with dissolve
    sa "Come on, Cam. Let's leave [name] to whatever he was doing."

    scene v9trc9d # FPP. Same camera as v9trc9 Show Samanta stood up next to Cameron (from MC's Perspective sat on bed), Samantha happy smile, Cameron annoyed look look, cam mouth open, samantha mouth closed
    with dissolve
    ca "I bet I know what he was doing, alright."

    scene v9trc9e # FPP. Same camera as v9trc9 Show Samanta stood up next to Cameron (from MC's Perspective sat on bed),Cameron grabbing crotch, Samantha happy smile, Cameron neutral look, Mouths closed
    with dissolve
    u "(Not a bad idea.)"
    u "Goodnight."

    scene v9trc9c
    with dissolve
    sa "Goodnight. I'll check on you again soon."

    scene v9trc10 # FPP. Show Cameron and Samantha leaving room, neutral faces, mouths closed
    with dissolve

    stop music fadeout 3

    pause 1

    jump v9_room_thur_night