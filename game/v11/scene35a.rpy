# SCENE 35a: Chloe hotel room making out amber phone call
# Location: chloe's hotel room, ambers hotel room, hotel corridor
# Characters: MC (Outfit 9), Chloe (Outfit 2), Aubrey (Outfit 1), Amber (Outfit 2)
# Time: Day

label v11_chloe_hotel_room_amber_call:
    play music "music/v10/Track Scene 40_2.mp3" fadein 2
    if CharacterService.is_mad(chloe) and not v11_riley_roomate:
        scene v11hrc1 # TPP. MC is inside his hotel room, next to the door, mouth closed
        with fade
        
        play sound sound.call

        u "(I literally just got to my room, who could be calling me?)"

        scene v11hrc2 # TPP. MC moves to his bed, mouth opened
        with dissolve

        stop sound
        u "Hello?"

        scene v11hrc3 # TPP. Amber is laying on her bed in her hotel room, mouth opened
        with dissolve

        am "Hey, loser."

        scene v11hrc4 # TPP. MC is now sitting on his bed, mouth opened
        with dissolve

        u "What's up?"

        scene v11hrc3 
        with dissolve

        am "I just wanna know what's up with Lauren."

        if v11_lauren_caught_aubrey:
            scene v11hrc3 
            with dissolve

            am "She's pissed at you."

            scene v11hrc4 
            with dissolve

            u "What is she saying?"

            scene v11hrc3 
            with dissolve

            am "Fuck [name] this, and fuck [name] that."

            scene v11hrc4
            with dissolve

            u "Damn..."

            scene v11hrc3
            with dissolve

            am "This is why you should learn to keep it in your pants, pretty boy. Personally, I don't care. I'm not the type of girl that cares where the dog is when I'm not around, but she's pretty fired up."

            scene v11hrc4
            with dissolve

            u "Should I try to talk to her again?"

            scene v11hrc3
            with dissolve

            am "Do I look like a counselor to you? I didn't call to give you advice, I called to give you information. What you do with it is your own choice. I would just leave her alone for now though, if you ask me."

            scene v11hrc4
            with dissolve

            u "*Sighs* I really fucked this one up."

            scene v11hrc3
            with dissolve

            am "You sure did, good luck!"

            scene v11hrc5 # FPP, Amber hangs up
            with dissolve

            u "(I gotta fix this.)"

        else: 

            scene v11hrc3
            with dissolve

            am "She's acting all bubbly."

            scene v11hrc4
            with dissolve

            u "When is she not?"

            scene v11hrc3
            with dissolve

            am "...You got me there, but she's like... extra bubbly."

            scene v11hrc4
            with dissolve

            u "Her and I just had a really good day today."

            scene v11hrc3
            with dissolve

            am "You sure that's all?"

            scene v11hrc4
            with dissolve

            u "That's all I'm saying."

            scene v11hrc3a # TPP. amber looks uneasy, mouth opened
            with dissolve

            am "*Sighs* Fine, if I can't squeeze it out of you, I'll squeeze it out of her."

            scene v11hrc4a # TPP. MC is laughing, mouth opened
            with dissolve

            u "*Chuckles* Good luck with that."

            scene v11hrc3
            with dissolve

            am "Later."

            scene v11hrc5 
            with dissolve

            pause 0.75

    scene v11hrc6 # TPP. MC is now laid in bed trying to sleep, eyes closed
    with dissolve

    u "(Sleep, that's what I need. Sleep.)"

    scene v11hrc7 # TPP. Same as 6, he moved a little bit on his sleeping position
    with dissolve

    pause 0.75
    
    stop music fadeout 3
    play music "music/v10/Track Scene 15.mp3" fadein 2

    scene v11hrc8 # TPP. Chloe is shaking mc, waking him up
    with fade

    pause 0.75

    scene v11hrc9 # FPP. MC is looking at chloe still layed down, mouth opened
    with dissolve

    cl "Wake up, you can't just sleep all day!"

    scene v11hrc10 # TPP. MC is now sitting up in his bed yawning
    with dissolve

    u "*Yawn*"

    scene v11hrc11a # FPP. Mc still siting on the bed looking at chloe, mouth opened
    with dissolve

    cl "Mr. Lee has something planned tonight so if there's anything you want to do, do it during the day."

    scene v11hrc11 # FPP. Same as 11, mouth closed
    with dissolve

    u "Thanks."

    scene v11hrc11a
    with dissolve

    cl "Yep."

    if CharacterService.is_friend(chloe) and not CharacterService.is_mad(chloe): #if car dealership (===chloe not mad) but chloe not rs either
        scene v11hrc11a
        with dissolve

        cl "\"Such a beautiful couple\", that guy was so sweet to us. He thought he had a sale though, now I feel bad..."

        scene v11hrc11
        with dissolve

        u "Well honey, once the stock market reaches expectations I'll buy you that car."

        scene v11hrc11a
        with dissolve

        cl "Oh husband... will you really?"

        scene v11hrc11b # FPP. Same as 11, smile on her face, mouth closed
        with dissolve

        u "Of course, anything for my wife. *Chuckles*"

        scene v11hrc11c # FPP. same as 11b, mouth opened
        with dissolve

        cl "Haha, I'm glad you know how to have fun without taking things too seriously."

        scene v11hrc11b
        with dissolve

        u "I am too. *Chuckles*"

        play sound sound.knock

        pause 0.5

        scene v11hrc12 # FPP. chloe walks to answer the door
        with dissolve

        pause 0.75

        scene v11hrc13 # FPP. Door is now opened and aubrey is outside and chloe's back is turned to the camera, mouth opened
        with dissolve

        au "Chloe..."

        scene v11hrc13a # FPP, same as 13, mouth closed
        with dissolve

        cl "*Sighs* One sec."

    elif CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe) and not v11_riley_roomate: 
        scene v11hrc11
        with dissolve

        u "C'mon, over here."

        scene v11hrc11d # FPP. MC pulls chloe to him, mouth closed
        with dissolve

        pause 0.75

        scene v11hrc11e # FPP. MC kisses chloe
        with dissolve

        play sound sound.kiss

        pause 0.75

        scene v11hrc11c
        with dissolve

        cl "This may just have been the best day of my life, [name]."

        scene v11hrc11b
        with dissolve

        u "Mine too. Are you tired?"

        scene v11hrc11c
        with dissolve

        cl "Very much so... you wanna get ready for bed with me?"

        scene v11hrc11b
        with dissolve

        u "I was thinking maybe we could-"

        play sound sound.knock

        pause 0.5

        scene v11hrc12 
        with dissolve

        pause 0.75

        scene v11hrc13
        with dissolve

        au "Chloe..."

        scene v11hrc13a
        with dissolve

        cl "*Sighs* One sec. Sounds like the kids don't know what mommy and daddy time is. *Chuckles*"

    scene v11hrc14 # TPP. Aubrey walks in the room, chloe is behind her, mc is sitting down in the bed
    with dissolve

    pause 0.75

    scene v11hrc15 # TPP. Aubrey begins grabbing pajamas
    with dissolve

    pause 0.75

    scene v11hrc16 # TPP. Aubrey puts all of chloes belongings in a bag
    with dissolve

    pause 0.75

    scene v11hrc17 # FPP. Aubrey is still holding the bag, looking at mc while chloe is besides her, aubrey's mouth opened
    with dissolve

    au "Sorry if you guys had something planned, but I'm stealing Chloe for the night. All of us girls are having a girls night. Lindsey's idea... and I love it."

    scene v11hrc17a # FPP. Same as 16, aubreys mouth closed, chloe making a tired expression, mouth opened
    with dissolve

    cl "I'm really tired, Aubrey."

    scene v11hrc17
    with dissolve

    au "You won't be soon."

    scene v11hrc17b # FPP. Aubrey drags chloe out of the room, mouth opened
    with dissolve

    au "Bye, [name]!"

    scene v11hrc6 
    with dissolve

    u "(*Sighs* Guess I'll just go to bed then, I know the guys aren't doing anything.)"

    scene v11hrc7
    with dissolve

    pause 0.75

    if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        scene v11hrc18 # TPP. MC wakes up with chloe sitting on top of him
        with fade

        pause 0.75

        scene v11hrc19 # FPP. Mc is looking at chloe on top of him, mouth opened
        with dissolve

        cl "Wake up sleepy head! I'm the one that had a late night. *Chuckles*"

        scene v11hrc19a # FPP MC kisses chloe's forehead, mouth closed
        with dissolve

        play sound sound.kiss

        pause 0.75

        scene v11hrc19
        with dissolve

        u "Good morning, beautiful."

        scene v11hrc19
        with dissolve

        cl "C'mon, get up. Mr. Lee has something planned tonight. I'm not sure what it is, but if there's anything else you wanna do today, you should get to it now."

    elif not CharacterService.is_mad(chloe):
        scene v11hrc9b # FPP. same as 9, chloe is smiling
        with fade

        cl "Wake up, [name]! How do you not feel the light shining right on your face? *Chuckles*"

        scene v11hrc9 
        with dissolve

        u "I'm a deep sleeper I guess."

        scene v11hrc9b
        with dissolve

        cl "Well get up deep sleeper, Mr. Lee has plans for us tonight, so the daytime is the only freedom we have."

        scene v11hrc10
        with dissolve

        pause 0.75

        scene v11hrc11
        with dissolve
        
        u "*Yawn* Alright... I'm getting up."

    if not v11_riley_roomate:
        scene v11ris7 # TPP. Show MC sitting up on his bed now, in his boxers, he is yawning and stretching (day)
        with dissolve

        pause 0.75

        scene v11ris7a # TPP. Same cam as v11ris7, MC is startled, mouth closed, still sitting down, looking at the door to the hallway direction (day)
        with vpunch

        play sound sound.fall

        pause 0.75

        imre "GET THE FUCK OFF ME!"

        scene v11ris8 # TPP. Show MC getting up from his bed, he is startled, mouth closed (day)
        with dissolve

        pause 0.75

        scene v11ris9 # TPP. Show MC putting his shirt on (he already has pants on) (day)
        with dissolve

        pause 0.75

        scene v11ris10 # TPP. Show MC opening the door to the hallway, he is startled, mouth closed (day)
        with dissolve

        pause 0.75

        scene v11ris11 # TPP. Show MC looking down the hallway, very startled, mouth closed (day)
        with dissolve

        pause 0.75

    stop music fadeout 3
    jump v11_imre_ryan_grapple
