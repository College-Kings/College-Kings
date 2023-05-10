# SCENE 10: Airport Arrival/Treasure Hunt
# Location: Airport, boarding area
# Characters: MC (Outfit 1), Riley (Outfit 1), Mr Lee (Outfit 1), Ms Rose (Outift 1), Amber (Outfit 1)
# Time: Morning

label v11_airport_arrival:
    scene v11aira1 # FPP. MC can see Mr Lee talking to the students (Show only Riley, Amber, Mr Lee and in shot, Riley and Amber backs turned to MC, Mr Lee's front is showing), Mr Lee neutral expression, mouth open (Ms Rose is next to Mr Lee, out of shot)
    with fade
    play music music.v11_Track_Scene_10 fadein 2
    pause 0.75

    scene v11aira2 # FPP. Same character positioning as v11aira1, MC is walking up to the group, Mr Lee is still addressing the students, make sure his pose is different from v11aira1, neutral expression, mouth open
    with dissolve

    pause 0.75

    scene v11aira3 # FPP. Same character positioning as v11aira1, MC is standing in between Riley and Amber, Mr Lee looking at MC, slightly annoyed, mouth open (Only Mr Lee in shot)
    with dissolve

    lee "Well, it's nice of you to join us... finally."

    scene v11aira4 # FPP. Same character positioning as v11aira3, MC and Riley looking at each other, she is laughing
    with dissolve

    ri "*Laughs*"

    scene v11aira3a # FPP. Same as v11aira3, Mr Lee now neutral expression, mouth open
    with dissolve

    lee "As I was saying, we will be exploring three locations in Europe. London, Paris, and Amsterdam."

    scene v11aira3
    with dissolve

    lee "I expect you all to behave like adults since that's what you are and even though there are some specific activities we'll attend as a group."

    scene v11aira3a
    with dissolve
    
    lee "Your own exploration will be essential to make the most out of this experience."

    scene v11aira5 # FPP. Same character positioning as v11aira3, MC and Ms Rose looking at each other, Ms Rose slightly smiling, mouth open
    with dissolve

    ro "While on the trip, please remember that all campus rules still apply in Europe... Does anyone have any questions?"

    scene v11aira6 # FPP. Same character positioning as v11aira3, MC looking at Amber, Amber looking at Ms Rose (Ms Rose out of shot, Amber mouth open, slight smile
    with dissolve

    am "Are we free to ditch everything and just do what we want the whole time?"

    scene v11aira3b # FPP. Same as v11aira3, Mr Lee looking towards Amber, Mr Lee mouth open, neutral expression
    with dissolve

    lee "Refer to your own judgment."

    scene v11aira6
    with dissolve

    am "I'll take that as a yes. *Chuckles*"

    scene v11aira5
    with dissolve

    ro "Alright, everyone wait here and talk amongst yourselves while the handlers get your bags."

    scene v11aira3a
    with dissolve

    lee "Riley, [name], may I speak to you for a second?"

    scene v11aira7 # FPP. Same positioning as v11aira3, but Riley and MC are standing close to Mr Lee, MC and Mr Lee looking at each other, Lee mouth closed, slight smile
    with dissolve

    u "What's up, Mr. Lee?"

    scene v11aira7a # FPP. Same as v11aira7, Lee mouth open, slight smile
    with dissolve

    lee "I prepared something for the two of you."

    scene v11aira7
    with dissolve

    u "What do you mean?"

    scene v11aira7a
    with dissolve

    lee "When I was in college I went on an abroad trip similar to this one, but to Asia."

    lee "My professor gave me a map that apparently has some treasure at the end if you follow the riddles."

    scene v11aira8 # FPP. Same character positioning as v11aira7, MC looking at Riley, Riley looking in Mr Lee's direction, RIley mouth open, slight smile
    with dissolve

    ri "What kind of treasure?"

    scene v11aira7b # FPP. Same as v11aira7, Mr Lee now holding a trinket, mouth open, slight smile
    with dissolve

    lee "There's a map for each continent and while in Asia I found this. It's worth quite a lot... I've looked at the riddles and I know the three cities we're visiting each have a piece of information."

    scene v11aira8
    with dissolve

    ri "Wait, why are you telling us all this?"

    scene v11aira7c # FPP. Same as v11aira7b, Mr Lee looking at Riley, Lee mouth open, slight smile
    with dissolve

    lee "Well, I wanted to explore these myself but I won't have the time. And with you two being my brightest and most trusted students-"

    scene v11aira8a # FPP. Same as v11aira8, but Riley looking at MC, slight smile, mouth open
    with dissolve

    ri "[name] must be the most trusted one, he's definitely not the brightest. *Chuckles*"

    scene v11aira8b # FPP. Same as v11aira8a, Riley slight smile, mouth closed
    with dissolve

    u "Funny."

    scene v11aira7b
    with dissolve

    lee "I just felt I could trust you two with the task."

    scene v11aira8
    with dissolve

    ri "Sounds super fun, can I keep the treasure?"

    scene v11aira7c
    with dissolve

    lee "If you find it then it shall be yours. Just make sure to let me know what it is."

    scene v11aira7b
    with dissolve

    lee "And if you need additional motivation, you'd both receive extra credit for this."

    scene v11aira7d # FPP. Same as v11aira7b, Mr Lee mouth closed, slight smile
    with dissolve

    u "Now I'm definitely in..."

    scene v11aira8a
    with dissolve

    ri "The most trusted student definitely needs some extra credit. *Chuckles*"

    scene v11aira7c
    with dissolve

    lee "I'll leave you to it."

    scene v11aira9 # FPP. Same positioning as v11aira7, show Mr Lee handing the treasure map to Riley, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11aira9a # FPP. Same as v11aira9, show Mr Lee walking away, Riley looking at the map
    with dissolve

    pause 0.75

    scene v11aira10 # FPP. MC and Riley looking at each other, Riley holding the map, Riley mouth open, smiling
    with dissolve

    ri "This is gonna be so much fun!"

    scene v11aira10a # FPP. Same as v11aira10, Riley mouth closed, smiling
    with dissolve

    u "*Cough* Nerd... *Cough*"

    scene v11aira10
    with dissolve

    ri "I'm sorry, did the teacher's pet say something?"

    scene v11aira10a
    with dissolve

    u "*Chuckles* So what does it say?"

    scene v11aira10b # FPP. Same as v11aira10, Riley looking down at the map, slight smile, mouth open
    with dissolve

    ri "Hmmm, let's see. \"Deep in London, you'll find Mr. Duncan, not at a luncheon, where gunmen go stunting. Many of targets, be careful in London, a bullet is quick and comes almost too sudden.\""

    scene v11aira10a
    with dissolve

    menu:
        "Be hesitant":
            $ riley.points -= 1

            scene v11aira10a
            with dissolve

            u "That doesn't sound very historic."

            scene v11aira10
            with dissolve

            ri "Oh hush, quit trying to ruin the fun."

        "Be excited":
            $ reputation.add_point(RepComponent.BRO)
            $ riley.points += 1

            scene v11aira10a
            with dissolve

            u "Okay, that actually sounds kinda cool."

            scene v11aira10
            with dissolve

            ri "I'm glad you see the fun in this too... *Chuckles*"

    scene v11aira10b
    with dissolve

    ri "So, it sounds like a gun range... or something with guns. Ooh! It could be the thing where they scream \"PULL\" and you shoot the little disk thing."

    scene v11aira10a
    with dissolve

    u "Skeet shooting? *Laughs*"

    scene v11aira10
    with dissolve

    ri "Yeah that, but it has to be run by a guy named Duncan. *Chuckles*"

    scene v11aira10a
    with dissolve

    am "Hey [name]!"

    scene v11aira11 # FPP. MC is looking behind him, he sees Amber gesticulating at him to come over
    with dissolve

    pause 1.25

    scene v11aira10a
    with dissolve

    u "We'll talk about this more later."

    scene v11aira10
    with dissolve

    ri "Alright."

    scene v11aira12 # TPP. Show MC walking towards Amber's direction
    with dissolve

    pause 0.75
    stop music fadeout 3
    
    jump v11_airport_charli