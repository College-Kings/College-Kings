# SCENE 18: Ms Rose convo (if wolves)
# Location: hotel lobby
# Characters: MC(outfit 1)/Ms Rose(outfit 1)
# Time: Late night

label v11_msrose_convo:
    scene v11roc1 # FPP. Ms Rose and MC are in a secluded area, lookign at each other, Ms Rose is slightly embarrassed, mouth open (Ms Rose should have her back facing a wall, the wall should be relatively close)
    with fade
    play music music.ck1.v11.Track_Scene_3 fadein 2
    ro "I wanted to apologize for my behavior. I shouldn't have let our relationship get inappropriate, and should've never treated you like anything more than a student."

    ro "From now on I'm going to keep things strictly professional."

    scene v11roc1a # FPP. Same as v11roc1, but Ms Rose mouth closed
    with dissolve

    menu:
        "Kiss her":
            $ CharacterService.set_relationship(ms_rose, Relationship.FWB)

            scene v11roc2 # TPP. MC gets very close to Ms Rose, Ms Rose's back is now on the wall, she is slightly smiling, mouth closed, looking at MC
            with dissolve

            pause 0.75

            scene v11roc2a # TPP. Same cam as v11roc2, MC now places his right hand on the wall above her head, he has his left hand on her chin, their mouths are close, they are not kissing yet
            with dissolve

            pause 0.75

            play sound sound.kiss

            scene v11roc2b # TPP. Same as v11roc2a, MC and Ms Rose are now kissing, MC keeps his hand on Ms Rose's chin and on the wall
            with dissolve

            pause 0.75

            scene v11roc3 # TPP. Ms Rose and MC still making out, change their head positioning a bit, Camera should be close to their heads, MC's hands still on wall and her chin
            with dissolve

            pause 0.75

            scene v11roc4 # FPP. Ms Rose and MC break off the kiss, still standing very close, looking at each other, Ms Rose is slightly smiling, mouth open
            with dissolve

            ro "[name], I-"

            scene v11roc5 # TPP. MC and Ms Rose are making out again, MC has his hands on her waist, pulling her close
            with dissolve

            play sound sound.kiss

            pause 0.75

            scene v11roc6 # TPP. MC and Ms Rose continue making out, change head positioning a bit compared to v11roc4, Ms Rose now has her arms wrapped around MC
            with dissolve

            pause 0.75

            scene v11roc7 # TPP. MC now has one hand on Ms Rose's neck, the other stays on her waist, Ms Rose continues to wrap her arm around MC, change head positioning a bit compared to v11roc5
            with dissolve

            pause 0.75

            scene v11roc4a # FPP. Same as v11roc4, but his hands are on her waist (out of shot), Ms Rose is looking down, mouth closed, smiling
            with dissolve

            pause 0.75

            scene v11roc4b # TPP. Same as v11roc4a, Ms Rose is now looking directly at MC, slightly smiling, mouth open, MC
            with dissolve

            ro "Let's go get everyone their keys."

        "Don't kiss her":
            scene v11roc1b # FPP. Same as v11roc1, but Ms Rose slightly smiling, mouth closed
            with dissolve

            u "You don't have to apologize Ms. Rose, I stepped out of line as well. You're a wonderful person, but I agree. We should keep things professional."

            scene v11roc1c # FPP. Same as v11roc1b, but Ms Rose mouth open
            with dissolve

            ro "You'll make a young lady very happy one day."

            scene v11roc1b
            with dissolve

            u "And you'll get the life you've always deserved."

            scene v11roc1c
            with dissolve

            ro "C'mon, I'm sure the keys are ready. Let's get everyone to bed."

    scene v11roc8 # TPP. Show MC walking back to the lobby with everyone else, he is smiling, mouth closed
    with dissolve

    pause 0.75
    stop music fadeout 3
    jump v11_roommate