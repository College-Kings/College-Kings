# SCENE 25: Mc wakes up to the phone call from Julia
# Locations: Hotel Room, Hotel Room Corridor
# Characters: MC (Outfit: Boxers/3), JULIA (Outfit: 1)
# Time: Morning in MC shots, Night in Julia shots
# Phone Images: NONE
# NOTE: MC in his boxers in all renders except v12juc6, v12juc7 and v12juc8 (He uses outfit 3 in those 3 shots)

label v12_julia_call:
    scene black
    with fade
    play sound sound.call
    pause 1

    play music music.ck1.v12.Track_Scene_25 fadein 2
    
    scene v12juc1 # TPP. Show MC sleeping in his bed
    with dissolve

    pause 1.5

    scene v12juc1a # TPP. Show MC startled, waking up, mouth closed
    with dissolve

    pause 1.25

    scene v12juc2 # TPP. Show MC sitting on the edge of his bed, holding his phone to his ear, mouth open, slightly annoyed (he's talking on the phone)
    with dissolve

    stop sound
    play sound sound.answer_call
    u "Hello?"

    scene v12juc3 # TPP. Show Julia in her house. Julia slightly worried, mouth open, talking on the phone
    with dissolve

    ju "Hey sweetie, did I wake you?"

    scene v12juc3a # TPP. Same as v12juc3, Julia slightly worried, mouth closed
    with dissolve

    u "Uhh, I mean... Yeah."

    scene v12juc3
    with dissolve

    ju "I'm so sorry honey, I forgot about the time difference... While I have you though, how is your trip going?"

    scene v12juc3b # TPP. Same as v12juc3, Julia smiling, mouth closed, different pose
    with dissolve

    u "It's going really well, we're in Paris right now."

    scene v12juc3c # TPP. Same as v12juc3b, Julia smiling, mouth open
    with dissolve

    ju "Ooo, so exciting! It's been years since I went to Paris. I'd do anything to go back."

    scene v12juc3b
    with dissolve

    u "Wanna switch places with me? *Chuckles*"

    scene v12juc3
    with dissolve

    ju "Umm no, this is your time to enjoy the City of Love! Are you not enjoying yourself?"

    scene v12juc3b
    with dissolve

    u "Haha, no. I'm enjoying myself, I was just kidding."

    scene v12juc3c
    with dissolve

    ju "*Chuckles* Okay, good. Speaking of the City of Love, do you have any field trip romances yet?"

    scene v12juc3d # TPP. Same as v12juc3b, different pose
    with dissolve

    u "What's a field trip romance? *Chuckles*"

    scene v12juc3e # TPP. Same as v12juc3d, Julia smiling, mouth open
    with dissolve

    ju "We all have a field trip romance... That person in which you just feel so much more drawn to out of nowhere while on the trip."

    scene v12juc3d
    with dissolve

    u "Ahh... Got it."

    scene v12juc3e
    with dissolve

    ju "So, who's yours? *Chuckles*"

    call screen v12_girls

# -A menu similar to homecoming pops up and MC chooses between Chloe, Lauren, Nora, Penelope, Samantha, Lindsey, Riley, and Aubrey (Greyed out if not present or mad)-

label v12_jc_riley:
    $ v12_girl = "riley"
    scene v12juc3d
    with dissolve

    u "I guess Riley, we've been spending a lot more time together during a scavenger hunt."

    scene v12juc3e
    with dissolve

    ju "A scavenger hunt? That sounds exciting!"

    scene v12juc3f # TPP. Same as v12juc3d, different pose
    with dissolve

    u "It's definitely been... something. *Chuckles*"

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Riley":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    elif girl == "Riley":
        scene v12juc3g
        with dissolve
        ju "I remember you telling me about her. This sounds promising."

    jump v12_jc_continue

label v12_jc_amber:
    $ v12_girl = "amber"

    scene v12juc3d
    with dissolve

    u "I guess Amber, we drove go karts in London. And had an interesting encounter at the Bank tour..."

    scene v12juc3
    with dissolve

    ju "Sounds like she could be a bit of trouble... Please make sure you're making smart choices."

    scene v12juc3f
    with dissolve

    u "Haha, don't worry. Amber is harmless... (I think.)"

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Amber":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    jump v12_jc_continue

label v12_jc_chloe:
    $ v12_girl = "chloe"
    
    scene v12juc3b
    with dissolve

    u "I guess Chloe, her and I have gotten a lot closer."
    
    if v11_dealership:
        u "We even test drove a luxury car together."

    if volleyball and girl == "Chloe":
        scene v12juc3g
        with dissolve
        ju "Chloe is the we one got the volleyball at the shopping for, right?"
        
        scene v12juc3d
        with dissolve
        u "That's right!"

    elif girl == "Chloe":
        scene v12juc3g
        with dissolve
        ju "I remember you telling me about her. This sounds promising."
        
    scene v12juc3g # TPP. Same as v12juc3f, Julia smiling, mouth open
    with dissolve

    ju "As long as that car is the only thing she's test driving."

    scene v12juc3f
    with dissolve

    u "Yeah, okay. Thanks for that middle school reminder..."

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Chloe":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    jump v12_jc_continue

label v12_jc_lauren:
    $ v12_girl = "lauren"

    scene v12juc3b
    with dissolve

    u "I guess Lauren, her and I did go to this wizard thing together and it was really nice."

    scene v12juc3c
    with dissolve

    ju "Did she invite you?"

    scene v12juc3f
    with dissolve

    u "Yeah she did."

    scene v12juc3g
    with dissolve

    ju "Ooo, she may really like you."

    scene v12juc3d
    with dissolve

    u "I hope so."

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Lauren":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    elif girl == "Lauren":
        scene v12juc3g
        with dissolve
        ju "I remember you telling me about her. This sounds promising."

    jump v12_jc_continue

label v12_jc_nora:
    $ v12_girl = "nora"

    scene v12juc3f
    with dissolve

    u "I guess I'd say Nora, her and I have definitely gotten a lot closer, but she already has a boyfriend."

    scene v12juc3g
    with dissolve

    ju "Your father had a wife when I met him, but his marriage didn't work out and then we got closer. You have no idea what may happen, just be a good friend to her right now."

    scene v12juc3f
    with dissolve

    u "I'm sure I can do that."

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Nora":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    jump v12_jc_continue

label v12_jc_penelope:
    $ v12_girl = "penelope"

    if v11_pen_goes_europe:
        scene v12juc3d
        with dissolve

        u "I guess Penelope, we haven't been able to spend much time together because she's busy being the assistant chaperone, but she invited me to watch the stars with her the other day back in London."

        scene v12juc3e
        with dissolve

        ju "How romantic!"

    else:
        scene v12juc3b
        with dissolve

        u "I guess Penelope, but... She didn't get to come on the trip. We've only spoken a bit since I've left."

        scene v12juc3c
        with dissolve

        ju "Well, it sounds like she's important if she's all you can think about."

    scene v12juc3b
    with dissolve

    u "She's great, yeah."

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Penelope":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    elif girl == "Penelope":
        scene v12juc3g
        with dissolve
        ju "I remember you telling me about her. This sounds promising."

    jump v12_jc_continue

label v12_jc_samantha:
    $ v12_girl = "samantha"

    scene v12juc3d
    with dissolve

    u "I guess Samantha... She's a wild one for sure, but we've had some good talks when I've been able to get her away from her brother."

    scene v12juc3
    with dissolve

    ju "Gotta be careful with those overprotective brothers..."

    scene v12juc3d
    with dissolve

    u "I'm trying to be. *Chuckles*"

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Samantha":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    jump v12_jc_continue

label v12_jc_lindsey:
    $ v12_girl = "lindsey"

    scene v12juc3d
    with dissolve

    u "I guess Lindsey. As a matter of fact, she invited me to celebrate her birthday with her when we got to Paris."

    scene v12juc3g
    with dissolve

    ju "That's nice of her to want you of all people to tag along."

    scene v12juc3f
    with dissolve

    u "Yeah, she's really sweet."

    if not girl == "Lindsey":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    jump v12_jc_continue

label v12_jc_aubrey:
    $ v12_girl = "aubrey"

    scene v12juc3f
    with dissolve

    u "I guess Aubrey. We haven't done too much, but anytime we are together it's something major."

    if girl == "Emily":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]?"
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."    
   
    elif not girl == "Aubrey":
        scene v12juc3g
        with dissolve
        ju "What happened with [girl]? You told me about her last time."
        
        scene v12juc3d
        with dissolve
        u "It's complicated..."

    elif girl == "Aubrey":
        scene v12juc3g
        with dissolve
        ju "I remember you telling me about her. This sounds promising."

    scene v12juc3g
    with dissolve

    ju "There's some people you can go years without seeing, but when you do, it's as if things never changed."

    jump v12_jc_continue

label v12_jc_continue:
    scene v12juc3c
    with dissolve

    ju "Well, I'm so happy to hear you're enjoying all that Europe has to offer and that you're not doing it all alone."

    scene v12juc3b
    with dissolve

    u "Haha, thanks... I am almost ready to be back in America, though. *Laughs*"

    scene v12juc3e
    with dissolve

    ju "And when you're back I may or may not come visit you..."

    scene v12juc3d
    with dissolve

    u "You don't have to do that, Julia."

    scene v12juc3c
    with dissolve

    ju "Oh, but I do."

    scene v12juc3f
    with dissolve

    u "Haha, okay."

    scene v12juc3g
    with dissolve

    ju "I should let you go honey, these international calls aren't cheap."

    scene v12juc3d
    with dissolve

    u "Alright, bye!"

    scene v12juc3e
    with dissolve

    ju "Bye, honey! Love you!"

    scene v12juc2a # TPP. Same as v12juc2, MC not on his phone anymore, just looking at the wall, mouth closed, slight smile
    with dissolve

    u "(Might as well get up now.)"

    scene v12juc4 # FPP. MC is sitting on the edge of his bed, he is looking at his roommate's bed, which has no one on it
    with dissolve

    u "(Looks like I'm not the only one that isn't asleep. *Chuckles*)"

    scene v12juc5 # TPP. Show MC getting up from his bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12juc6 # TPP. Show MC putting on his shirt, pants already on, slight smile, mouth clsoed
    with dissolve

    pause 0.75

    scene v12juc7 # TPP. Show MC walking out of his hotel room door, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12juc8 # TPP. Show MC walking in the hotel room corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12_nora_chris_fight #scene 26