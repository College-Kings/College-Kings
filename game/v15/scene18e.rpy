# Scene 18e: Possible Lauren Sex Scene
# Locations: Lauren's Room
# Characters: MC (Outfit: Stripper Costume/Naked), LAUREN (Outfit: Spider Costume/Naked)
# Time: Night 

label v15s18e:
    $ sceneList.add("v15_lauren")
    
    play sound "sounds/dooropen.mp3"

    scene v15s18e_1 # TPP. Show MC and Lauren entering Lauren's room, her door open, Both slight smile, mouth closed.
    with dissolve

    pause 0.75

    if config_censored:
        call screen censoredPopup("v15s18e_nsfwSkipLabel1")

    play sound "sounds/doorclose.mp3"

    scene v15s18e_2 # TPP. MC and Lauren in the room with the door closed, MC pulling off Lauren's costume, MC slight smile, mouth closed, Lauren biting her lip.
    with dissolve
    
    pause 0.75

    scene v15s18e_3 # TPP. Of just Lauren's costume landing somewhere on the floor after being tossed off.
    with dissolve

    pause 0.75

    scene v15s18e_4 # TPP. MC and Lauren now in the middle of the room, Lauren pulling off MC's costume, MC slight smile, mouth closed, Lauren with a flirty expression, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18e_3a # TPP. Just MC's costume landing next to Lauren's after being tossed off.
    with dissolve

    pause 0.75

    scene v15s18e_4a # TPP. MC and Lauren in the middle of the room, naked, and kissing.
    with dissolve

    pause 0.75

    scene v15s18e_5 # TPP. Lauren laying on the bed naked. Her boobs, neck, feet, and vagina need to be visibl(Need to be clicked on for freeroam)
    with dissolve

    u "(Hmm... Where should I start?)"

    call screen sex_overlay([
        [("Neck", "v15s18e_neck"), ("Boobs", "v15s18e_boobs"), ("Feet", "v15s18e_feet"), ("Vagina", "v15s18e_vagina")]
    ], continue_label="v15s18e_end")

label v15s18e_neck:
    $ v15s18e_frneck = True

    scene v15s18ene_1 # TPP. Close up of Lauren's bare neck 
    with dissolve

    menu:
        "Kiss":
            scene v15s18ene_2 # TPP. Show MC kissing Lauren's neck, Lauren flirty, mouth open.
            with dissolve

            la "Ooh... That feels nice, hehe."

            la "*Moans* I like it when you kiss me there."

            scene v15s18ene_3 # FPP. MC ontop of Lauren them face to face, Lauren flirty biting her lip.
            with dissolve

            u "Well, I definitely like kissing you there..."

            u "And here..."

            scene v15s18ene_4 # TPP. Show MC kissing the other side of Lauren's neck, Lauren flirty, mouth open.
            with dissolve

            la "*Giggles* Sorry, it kinda tickles, but..."

            la "Mainly, it's turning me on, haha."

            scene v15s18ene_3
            with dissolve

            u "Ha, good."

        "Choke":
            scene v15s18ene_1a # TPP. Show MC's hand on Lauren's neck
            with dissolve

            la "Oh-"

            scene v15s18ene_5 # TPP. Close up side view of MC kissing lauren as he has his hand on her neck holding it.
            with dissolve

            pause 0.75

            scene v15s18ene_3a # FPP. MC ontop of Lauren them face to face, Lauren flirty, mouth open.
            with dissolve

            la "Wow, I..."

            scene v15s18ene_3
            with dissolve

            u "Is this okay?"

            scene v15s18ene_3a
            with dissolve

            la "Yeah, yeah... I just wasn't expecting it. *Chuckles*"

            scene v15s18ene_5a # TPP. MC not kissing Lauren, MC's hand on Lauren's neck, MC looking in Lauren's eyes, MC slight smile, mouth closed. Lauren biting her lip.
            with dissolve

            pause 0.75

            scene v15s18ene_5
            with dissolve

            pause 0.75

            scene v15s18ene_5a 
            with dissolve
            
            pause 0.75

            scene v15s18ene_3a
            with dissolve

            la "Holy shit..."

            la "I always wondered what that felt like."

            la "I didn't know if I'd like it."

            scene v15s18ene_3
            with dissolve

            u "Well... Do you?"

            scene v15s18ene_3a
            with dissolve

            la "I..."

            la "Yes. I do."

            scene v15s18ene_3
            with dissolve

            u "Ha, me too."

    call screen sex_overlay([
        [("Neck", "v15s18e_neck"), ("Boobs", "v15s18e_boobs"), ("Feet", "v15s18e_feet"), ("Vagina", "v15s18e_vagina")]
    ], continue_label="v15s18e_end")

label v15s18e_boobs:
    $ v15s18e_frboobs = True

    scene v15s18ebo_1 # TPP. Close up shot of Lauren's boobs
    with dissolve
    
    menu:
        "Massage":
            scene v15s18ebo_2 # TPP. MC ontop of Lauren, his hand massaging her breast as he looks at Lauren, Lauren flirty, mouth open, MC slight smile, mouth closed.
            with dissolve

            la "Mmm..."

            scene v15s18ebo_2a # TPP. MC ontop of Lauren, his hand massaging her breast pushing them up as he looks at Lauren, Lauren biting her lip, MC slight smile, mouth open.
            with dissolve

            u "You have the most amazing tits, Lauren."

            scene v15s18ebo_2
            with dissolve

            la "Haha, thank you... *Moans*"

            scene v15s18ebo_2a
            with dissolve

            u "They're so fucking big."

            scene v15s18ebo_2
            with dissolve

            la "Mmm, your hands feel good on them too."

            scene v15s18ebo_2a
            with dissolve

            u "I could do this for hours."

            scene v15s18ebo_2
            with dissolve

            la "Ha... I wouldn't have a problem with that at all."

            scene v15s18ebo_3 # FPP. MC looking at Lauren's boobs, his hand on her boobs.
            with dissolve

            u "(I bet you wouldn't... Hehe.)"

        "Suck":
            scene v15s18ebo_4 # TPP. Show MC sucking on Lauren's boob, Lauren flirty, mouth open.
            with dissolve

            la "Oh, fuck..."

            la "*Moans* Yes, [name]..."

            la "I love that..."
            
            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s18ebo_5 # FPP. MC looking up at Lauren his boobs in his face, Lauren biting her lip.
                with dissolve

                u "I love you..."

                scene v15s18ebo_5a # FPP. MC looking up at Lauren his boobs in his face, Lauren flirty, mouth open.
                with dissolve

                la "Mmm, I love you too."

            scene v15s18ebo_5
            with dissolve

            u "They're so soft..."

            scene v15s18ebo_4
            with dissolve

            la "Ha."

            scene v15s18ebo_5 
            with dissolve

            pause 0.75

            scene v15s18ebo_5a
            with dissolve

            la "Please..."

            la "Do something else to me."

            scene v15s18ebo_5
            with dissolve

            u "Yes ma'am."

    call screen sex_overlay([
        [("Neck", "v15s18e_neck"), ("Boobs", "v15s18e_boobs"), ("Feet", "v15s18e_feet"), ("Vagina", "v15s18e_vagina")]
    ], continue_label="v15s18e_end")

label v15s18e_feet:
    $ v15s18e_frfeet = True
    
    scene v15s18efe_1 # FPP. Lauren's feet in MC's face, MC looking up from her feet seeing her naked body, Lauren biting her lip.
    with dissolve

    menu:
        "Massage":
            scene v15s18efe_2 # FPP. MC's view a little further back, MC looking up from her feet we are able to see her face, Lauren flirty, mouth open.
            with dissolve

            la "Oooh... Okay... *Chuckles*"

            scene v15s18efe_2a # FPP. MC's view a little further back, MC looking up from her feet we are able to see her face, Lauren biting her lip.
            with dissolve

            u "How does this feel?"

            scene v15s18efe_2
            with dissolve

            la "I've never had a foot massage before."

            la "But... Is it supposed to make me horny? *Laughs*"

            scene v15s18efe_2a
            with dissolve

            u "Haha... You like some foot attention, huh?"

            scene v15s18efe_2
            with dissolve

            la "I think so, yeah..."

            la "Wherever you touch me, though. It's just making me hornier..."

            scene v15s18efe_2a
            with dissolve

            u "Ha. Perfect."

            scene v15s18efe_2
            with dissolve

            la "*Moans*"

            scene v15s18efe_2a
            with dissolve

            u "(Let's give her something else to moan about...)"

        "Suck":
            scene v15s18efe_3 # TPP. Show MC kissing Lauren's feet, Lauren's face visible, Lauren shocked, mouth open.
            with dissolve

            la "Ah! What are you- Oh...?"

            scene v15s18efe_3a # TPP. Show MC kissing Lauren's feet, Lauren's face visible, Lauren flirty, mouth open.
            with dissolve

            la "Haha, wow..."

            la "Now that was a nice surprise, hehe."

            scene v15s18efe_1
            with dissolve

            u "Was it?"

            scene v15s18efe_1a # FPP. Lauren's feet in MC's face, MC looking up from her feet seeing her naked body, Lauren flirty, mouth open.
            with dissolve

            la "You're really spoiling me, handsome..."

            scene v15s18efe_1
            with dissolve

            u "It is your birthday, after all."

            scene v15s18efe_3a
            with dissolve

            la "*Moans*"

            la "Haha, sorry... It-"

            scene v15s18efe_1
            with dissolve

            u "Tickles? *Laughs*"

            scene v15s18efe_1a
            with dissolve

            la "A little..."

            scene v15s18efe_1
            with dissolve

            u "We can move on then."

    call screen sex_overlay([
        [("Neck", "v15s18e_neck"), ("Boobs", "v15s18e_boobs"), ("Feet", "v15s18e_feet"), ("Vagina", "v15s18e_vagina")]
    ], continue_label="v15s18e_end")

label v15s18e_vagina:
    scene v15s18eva_1 # FPP. MC looking at Lauren's vagina
    with dissolve

    u "(Now for the finale... Haha.)"

    jump v15s18e_end

label v15s18e_end:
    #scene v15s18eend_1 # Reuse scene v15s18ene_3
    scene v15s18ene_3
    with dissolve

    u "You just back and relax, birthday girl."

    #scene v15s18eend_1a # Reuse scene v15s18ene_3a
    scene v15s18ene_3a
    with dissolve

    la "*Giggles* Okay."

    image v15lauor = Movie(play="images/v15/Scene 18e/v15lauor.webm", loop=True, image="images/v15/Scene 18e/v15lauorStart.webp", start_image="images/v15/Scene 18e/v15lauorStart.webp")
    image v15lauor2 = Movie(play="images/v15/Scene 18e/v15lauor2.webm", loop=True, image="images/v15/Scene 18e/v15lauor2Start.webp", start_image="images/v15/Scene 18e/v15lauor2Start.webp")

    scene v15lauor # Ignore as anim
    with dissolve
    
    pause 0.75

    la "*Whispers* Fuck..."

    la "*Gasps* My God, [name]..."

    scene v15lauor2 # Ignore as anim
    with dissolve
    
    pause 0.75

    la "*Moans*"

    if "v12_lauren" in sceneList:
        la "This is... This feels..."

        la "It's even more amazing than our first time..."

    la "*Panting* Mmm, fuuuuck..."

    la "*Moans* Stop."

    scene v15s18eend_3 # FPP. MC looking up at Lauren, Lauren looking at MC, Lauren biting her lip.
    with dissolve

    u "What?"

    scene v15s18eend_3a # FPP. MC looking up at Lauren, Lauren looking at MC, Lauren flirty, mouth open.
    with dissolve

    la "Stand up."

    scene v15s18eend_4 # TPP. Show MC standing by the bed, slight smile, mouth closed, Lauren 
    with dissolve

    pause 0.75

    scene v15s18eend_5 # FPP. MC looking down at Lauren, Lauren looking at MC, Lauren sitting on the edge of the bed, Lauren flirty, mouth open.
    with dissolve

    la "Let me taste you now. Please?"

    image v15laubj = Movie(play="images/v15/Scene 18e/v15laubj.webm", loop=True, image="images/v15/Scene 18e/v15laubjStart.webp", start_image="images/v15/Scene 18e/v15laubjStart.webp")
    image v15laubjf = Movie(play="images/v15/Scene 18e/v15laubjf.webm", loop=True, image="images/v15/Scene 18e/v15laubjStart.webp", start_image="images/v15/Scene 18e/v15laubjStart.webp")
    image v15laubj2 = Movie(play="images/v15/Scene 18e/v15laubj2.webm", loop=True, image="images/v15/Scene 18e/v15laubj2Start.webp", start_image="images/v15/Scene 18e/v15laubj2Start.webp")
    image v15laubj2f = Movie(play="images/v15/Scene 18e/v15laubj2f.webm", loop=True, image="images/v15/Scene 18e/v15laubj2Start.webp", start_image="images/v15/Scene 18e/v15laubj2Start.webp")

    scene v15laubj # Ignore as anim
    with dissolve

    pause 0.75

    la "*Gagging*"

    u "*Moans* Oh, fuck! (She took it so deep straight away...)"

    scene v15laubjf # Ignore as anim
    with dissolve

    pause 0.75

    la "Mhmm..."

    u "You like that?"

    scene v15laubj2 # Ignore as anim
    with dissolve

    pause 0.75

    la "*Gagging* Mhmm!"

    u "Ahh, shit..."

    scene v15laubj2f # Ignore as anim
    with dissolve

    pause 0.75

    u "Fuck Lauren... *Moans*"

    u "You... You're going to make me-"

    scene v15s18eend_5a # MC looking down at Lauren, Lauren sitting on the edge of the bed, Lauren sucking MC's dick.
    with vpunch

    u "Lauren... Lauren!"

    scene v15s18eend_5b # FPP. MC looking down at Lauren, Lauren sitting on the edge of the bed, Lauren biting her lip.
    with dissolve

    la "Hmm? What?"

    scene v15s18eend_5a
    with dissolve

    u "You're gonna make me cum, haha."

    scene v15s18eend_5b
    with dissolve

    la "Oh... Well then, get in me already, would you?"

    image v15lausf = Movie(play="images/v15/Scene 18e/v15lausf.webm", loop=True, image="images/v15/Scene 18e/v15lausfStart.webp", start_image="images/v15/Scene 18e/v15lausfStart.webp")
    image v15lausff = Movie(play="images/v15/Scene 18e/v15lausff.webm", loop=True, image="images/v15/Scene 18e/v15lausfStart.webp", start_image="images/v15/Scene 18e/v15lausfStart.webp")
    image v15lausf2 = Movie(play="images/v15/Scene 18e/v15lausf2.webm", loop=True, image="images/v15/Scene 18e/v15lausf2Start.webp", start_image="images/v15/Scene 18e/v15lausf2Start.webp")
    image v15lausf2f = Movie(play="images/v15/Scene 18e/v15lausf2f.webm", loop=True, image="images/v15/Scene 18e/v15lausf2Start.webp", start_image="images/v15/Scene 18e/v15lausf2Start.webp")

    scene v15lausf # Ignore as anim
    with dissolve

    pause 0.75

    la "I... *Moans* I love this position."

    u "*Panting* Yeah?"

    scene v15lausff # Ignore as anim
    with dissolve

    pause 0.75

    la "*Moans*"

    la "You're so... fucking deep inside of me..."

    scene v15lausf2 # Ignore as anim
    with dissolve

    pause 0.75

    la "*Whispers* Oh, fuck..."

    u "You're so fucking wet, ha..."

    scene v15s18eend_6 # TPP. Show MC grabbing Lauren's boob as he fucks her from behind, Lauren flirty, mouth open.
    with dissolve

    la "*Moans*"

    la "Grab all of me..."

    scene v15s18eend_6a # TPP. Show MC grabbing Lauren's boob as he fucks her from behind, Lauren biting her lip.
    with dissolve

    u "They're almost too big..."

    scene v15s18eend_6
    with dissolve

    la "They fit perfectly in your hands-"

    la "Oh! *Moans*"

    scene v15s18eend_6a
    with dissolve

    u "Everything about you fits perfectly in my hands..."

    scene v15s18eend_6
    with dissolve

    la "Ha... Mmm..."

    scene v15s18eend_6a
    with dissolve

    u "You're absolutely stunning..."

    scene v15lausf2f # Ignore as anim
    with dissolve

    pause 0.75

    la "Yes... I'm gonna-"

    la "I'm about to... *Moans*"

    scene v15s18eend_7 # FPP. MC looking down seeing Lauren's ass and pulling his dick out of Lauren.
    with dissolve

    u "(Not yet you aren't.)"

    la "Hmm?"

    image v15laum = Movie(play="images/v15/Scene 18e/v15laum.webm", loop=True, image="images/v15/Scene 18e/v15laumStart.webp", start_image="images/v15/Scene 18e/v15lausfStart.webp")
    image v15laumf = Movie(play="images/v15/Scene 18e/v15laumf.webm", loop=True, image="images/v15/Scene 18e/v15laumStart.webp", start_image="images/v15/Scene 18e/v15lausfStart.webp")
    image v15laum2 = Movie(play="images/v15/Scene 18e/v15laum2.webm", loop=True, image="images/v15/Scene 18e/v15laum2Start.webp", start_image="images/v15/Scene 18e/v15lausf2Start.webp")
    image v15laum2f = Movie(play="images/v15/Scene 18e/v15laum2f.webm", loop=True, image="images/v15/Scene 18e/v15laum2Start.webp", start_image="images/v15/Scene 18e/v15lausf2Start.webp")

    scene v15laum # Ignore as anim
    with dissolve

    pause 0.75

    la "Oh, fuck..."

    u "Is this okay?"

    scene v15laumf # Ignore as anim
    with dissolve

    pause 0.75

    la "It's- *Moans*"

    u "(Fuck, she's so tight...)"

    scene v15laum2 # Ignore as anim
    with dissolve

    pause 0.75

    la "You feel so good, [name]."

    la "Fuck me! *Moans* Please, [name]!"

    scene v15laum2f # Ignore as anim
    with dissolve

    pause 0.75

    u "I'm gonna cum..."

    la "Cum inside of me."

    scene v15s18eend_8 # FPP. MC fucking Lauren in Missionary, Don't show lower body so can be reused later, MC looking at Lauren, Lauren looking at MC, Lauren biting her lip.
    with dissolve

    u "What?"

    scene v15s18eend_8a # FPP. MC fucking Lauren in Missionary, Don't show lower body so can be reused later, MC looking at Lauren, Lauren looking at MC, Lauren flirty, mouth open.
    with dissolve

    la "I want to feel it..."

    la "Please, [name]."

    scene v15s18eend_8
    with dissolve

    u "Shiittt... *Moans*"

    u "(Should I give her what she wants?)"

    menu:
        "Cum inside her":
            $ v15s18e_cum_in_lauren = True
            
            scene v15s18eend_8
            with dissolve

            u "(As you wish.)"

            scene v15s18eend_8
            with vpunch

            u "Oh, Laur-"

            scene v15s18eend_8a
            with dissolve

            la "*Gasps* Yes, [name]... Yes! *Moans*"

        "Pull out":
            scene v15s18eend_9 # FPP. MC looking down and pulling his cock out of Lauren.
            with dissolve

            u "(Not taking any chances tonight... Sorry, Lauren.)"

            scene v15s18eend_9a # FPP. Show MC cumming on Lauren's stomach
            with vpunch

            pause 0.75

    scene v15s18eend_8
    with dissolve

    u "*Panting* Ssshhhit..."

    scene v15s18eend_8a
    with dissolve

    la "Haha... Oh my-"

    scene v15s18eend_8
    with dissolve

    u "Fuck."

    scene v15s18eend_8a
    with dissolve

    la "That was the perfect way to end my birthday..."

    scene v15s18eend_8
    with dissolve

    u "Haha, agreed."

    scene v15s18eend_8a
    with dissolve

    la "I'm gonna go clean up, I'll meet you under the sheets?"

    scene v15s18eend_8
    with dissolve

    u "Sounds great."

    scene v15s18eend_10 # FPP. Show Lauren getting out of bed, Lauren slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18eend_11 # TPP. Close up of naked lauren entering the bathroom
    with dissolve

    pause 0.75

    scene v15s18end_12 # FPP. MC looking at the empty room.
    with dissolve

    $ checklist[0].complete = True

    $ lauren.relationship = Relationship.GIRLFRIEND

    u "(What a fucking party...) *Laughs*"

    jump v15s18f