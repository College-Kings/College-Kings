# SCENE 1: 
# Locations: Hotel Cafe, Hotel Lobby
# Characters: RILEY (Outfit: 2), MC (Outfit: 1)
# Time: Morning
# Phone Images: NONE

label v13_start:
    scene v13s1_1 # FPP. MC and Riley sitting in front of each other at the cafe table, Riley slightly angry, mouth open
    with dissolve

    play music music.v13_Track_Scene_1_1 fadein 2

    ri "Since he decided to take something special from me and ruin it... Let's ruin something special of his. He thinks it's entertaining to not only frame someone, but also embarrass a so-called friend in the process."

    scene v13s1_1a # FPP. Same as v13s1_1, Riley slight grin, mouth open
    with dissolve

    ri "So, let's give him a taste of his own medicine..."

    scene v13s1_1b # FPP. Same as v13s1_1a, Riley slight grin, mouth closed
    with dissolve

    u "You already know I'm down, what do you have in mind?"

    scene v13s1_1c # FPP. Same as v13s1_1a, Riley big grin, mouth slightly open
    with dissolve

    ri "*Chuckles*"

    scene v13s1_1b
    with dissolve

    u "What? *Laughs*"

    scene v13s1_1a
    with dissolve

    ri "Sorry, I'm just imagining all of this going down... My plan is pretty messed up, haha."

    scene v13s1_1b
    with dissolve

    u "Perfect. Let's hear it."

    scene v13s1_1a
    with dissolve

    ri "Well, Charli technically still has no idea that I know it was him. As far as he's concerned, I'm still completely pissed at you."

    scene v13s1_1d # FPP. Same as v13s1_1a, Riley different pose
    with dissolve

    ri "While using that to my advantage, I'm going to distract him for as long as possible."
    
    scene v13s1_1e # FPP. Same as v13s1_1, Riley rubbing her hands, making an evil face, mouth closed
    with dissolve
    ri "While I'm playing decoy, you get to do the dirty work. *Chuckles*"

    scene v13s1_1b
    with dissolve
    u "*Laughs* Okay, I'm also enjoying this, but please don't make that face. I can't take you seriously when you do that... *Chuckles*"

    scene v13s1_1d
    with dissolve

    ri "It's my evil mastermind face! *Chuckles*"

    scene v13s1_1b
    with dissolve

    u "If that's what you wanna call it... *Laughs*"

    u "So... What's the dirty work you have in mind?"

    scene v13s1_1a
    with dissolve

    ri "I want you to sneak into Charli's room and destroy his suitcase."

    scene v13s1_1b
    with dissolve

    u "Okay, but... Why his suitcase?"

    scene v13s1_1d
    with dissolve

    ri "Charli told me back in London that his grandmother gave it to him when he came out to her, so it's extremely special to him. That's what makes it the perfect target."

    scene v13s1_1b
    with dissolve

    u "This is a bit of a dark side for you, you know? I thought you were a nice girl... *Chuckles*"

    scene v13s1_1a
    with dissolve

    ri "Nope, never claimed to be! I just act accordingly. If people are nice to me I'll be an angel, but the minute they cross me, I cross them."

    scene v13s1_1b
    with dissolve

    u "Seems fair. *Chuckles*"

    scene v13s1_1a
    with dissolve

    ri "And fairness is exactly why I assumed you'd wanna help."

    scene v13s1_1d
    with dissolve

    ri "I know Charli's been a pain in your ass since the moment you met him, so I didn't think you'd second-guess helping. Especially when you consider the fact that he tried framing you."

    scene v13s1_1b
    with dissolve

    u "Oh, don't worry. I've been waiting for a moment like this."

    scene v13s1_1a
    with dissolve

    ri "That's what I thought. *Chuckles* Now, I'm not sure when we'll be able to do it... Once I get the layout of Amsterdam's hotel I'll let you know. Remember this though... Bleach."

    scene v13s1_1b
    with dissolve

    u "Bleach?"

    scene v13s1_1a
    with dissolve

    ri "Yep. There's been some in every hotel we've stayed at so far, under the sink in the bathrooms... You can ruin anything with a little bleach."

    scene v13s1_1b
    with dissolve

    u "Perfect, I'll keep that in mind. Do you know when we're leaving for Amsterdam? I thought we'd be going early this morning."

    scene v13s1_1d
    with dissolve

    ri "As far as I know, we-"

    scene v13s1_1f # FPP. Same as v13s1_1d, Riley startled, mouth closed, looking at the door
    with vpunch

    ro "ALRIGHT STUDENTS! LET'S GET OUR THINGS AND GET ON THE BUS!"

    stop music fadeout 3
    play music music.v13_Track_Scene_1_2 fadein 2

    scene v13s1_1b
    with dissolve

    u "Guess that answers my question. *Chuckles*"

    scene v13s1_2 # FPP. Show MC and Riley halfway through standing up, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v13s1_3 # FPP. MC and Riley standing in front of each other, MC looking at Riley, Riley slightly smiling, mouth open
    with dissolve

    ri "See you on the bus! I'm sure it's like a seven or eight hour ride so you'll be able to sleep most of the way. No murder to commit this time. *Chuckles*"

    scene v13s1_3a # FPP. Same as v13s1_3, Riley slightly smiling, mouth closed
    with dissolve

    u "Thank God! Haha, I'll catch you later."

    scene v13s1_3b # FPP. Same as v13s1_3, Riley slightly sad, mouth open
    with dissolve

    ri "Umm, actually..."

    scene v13s1_3c # FPP. Same as v13s1_3b, Riley different pose
    with dissolve

    ri "I hope you know that I really am sorry, [name]. I'm doing my best to act fine but, how I treated you is still really bothering me."

    scene v13s1_3d # FPP. Same as v13s1_3b, Riley slightly sad, mouth closed
    with dissolve

    menu:
        "Don't let it happen again":
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            u "Just don't let it happen again, okay? I don't like being blamed for shit I didn't do."

            scene v13s1_3c
            with dissolve

            ri "Of course, and I know you're a true friend. I won't jump to conclusions so quickly in the future."

        "Apology accepted":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ riley.points += 1

            scene v13s1_3d
            #with dissolve

            u "It's fine Riley, really. Of course I was pissed at first, it's a little upsetting to have one of your best friends calling you a liar but... I can't stay mad at you forever. Apology accepted."

            scene v13s1_3c
            with dissolve

            ri "Well... It's not fine, and I shouldn't have jumped to conclusions like that so fast. Your forgiveness means everything to me, though."

    scene v13s1_4 # TPP. Show Riley hugging MC
    with dissolve

    pause 1.25

    scene v13s1_3
    with dissolve

    ri "I promise I'll make it up to you."

    scene v13s1_3a
    with dissolve

    u "Your Charli plan is a pretty good start, haha."

    scene v13s1_3
    with dissolve

    ri "*Chuckles* See you later, and thanks again... For being a friend."

    scene v13s1_3a
    with dissolve

    u "Of course."

    scene v13s1_3e # FPP. MC watching Riley walking towards the door, slight smile, mouth closed (if she has her back to MC then ignore the facial expression)
    with dissolve

    u "(Unlimited access to Charli's room... This is gonna be interesting. *Laughs*)"

    scene v13s1_5 # TPP. Show MC walking out of the cafe, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s1_6 # TPP. Show MC walking in the hotel lobby, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s2