# SCENE 9: WED MORNING WAKING UP IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (Outfit 1)
# Time: Wednesday Night / Wednesday Morning

label room_wed_night:
    if mc.frat == Frat.WOLVES:
        scene v9wnr1 # TPP. Show MC sitting on his Wolves bed looking tired.
        with fade

        play music music.ck1.v9.Track_Scene_9 fadein 2

        pause 1

        scene v9wnr2 # TPP. Show MC now lay on his bed, sighing.
        with dissolve

        u "(Now this was not a bad day. I guess having fun like this is pretty cool too.)"

        scene v9wnr2a # TPP. Same camera as v9wnr2, MC turns to his side and grabs his phone.
        with dissolve

        if CharacterService.is_fwb(aubrey):
            u "(Well I can't really decide on my favorite moment of the day, but dude, Aubrey...)"

        elif CharacterService.is_fwb(riley):
            u "(Well I can't really decide on my favorite moment of the day, but dude, Riley...)"

        else: 
            u "(Well I can't really decide on my favorite moment of the day...)"

        scene v9wnr3 # TPP. Show MC lying on the opposite side to v9wnr2a, slight concerned expression, looking tired, no longer holding phone, mouth closed.
        with dissolve

        u "(The thing I should really be worried about is that Brawl. But after today I think I feel more confident. Day was pretty inspiring.)"

        stop music fadeout 3

        scene black
        with dissolve

        pause 1

        scene v9wnr4 # TPP. Show MC waking up from sleep, yawning, mouth open. TIME NOW MORNING. WEARING UNDERWEAR.
        with fade

        u "That was a damned good sleep."

        scene v9wnr4a # TPP. Same camera as v9wnr4, MC sits up and stretches his arms.
        with dissolve

        u "(If all days would start like this, that would be just awesome.)"

        scene v9wnr5 # TPP. Show MC checking his phone.
        with dissolve

        u "What?! Fuck! I'm gonna be late!"

        scene v9wnr6 # TPP. Show MC springing up from his bed with panic.
        with dissolve

        pause 1

        scene v9wnr7 # TPP. Show MC leaving his room, now dressed wearing outfit 2.
        with dissolve

        jump v9_history_class

    else: 
        scene v9wnr8 # TPP. Show MC sitting on his Apes bed looking tired.
        with fade

        play music music.ck1.v9.Track_Scene_9 fadein 2

        pause 1

        scene v9wnr9 # TPP. Show MC now lay on his bed, sighing.
        with dissolve

        u "(Now this was not a bad day. I guess having fun like this is pretty cool too.)"

        scene v9wnr9a # TPP. Same camera as v9wnr2, MC turns to his side and grabs his phone.
        with dissolve

        if CharacterService.is_fwb(aubrey):
            u "(Well I can't really decide on my favorite moment of the day, but dude, Aubrey...)"

        elif CharacterService.is_fwb(riley):
            u "(Well I can't really decide on my favorite moment of the day, but dude, Riley...)"

        else: 
            u "(Well I can't really decide on my favorite moment of the day...)"

        scene v9wnr10 # TPP. Show MC lying on the opposite side to v9wnr2a, slight concerned expression, looking tired, no longer holding phone, mouth closed.
        with dissolve

        u "(The thing I should really be worried about is that Brawl. But after today I think I feel more confident. Day was pretty inspiring.)"

        stop music fadeout 3

        scene black
        with dissolve

        pause 1

        scene v9wnr11 # TPP. Show MC waking up from sleep, yawning, mouth open. TIME NOW MORNING. WEARING UNDERWEAR.
        with fade

        u "That was a damned good sleep."

        scene v9wnr11a # TPP. Same camera as v9wnr4, MC sits up and stretches his arms.
        with dissolve

        u "(If all days would start like this, that would be just awesome.)"

        scene v9wnr12 # TPP. Show MC checking his phone.
        with dissolve

        u "What?! Fuck! I'm gonna be late!"

        scene v9wnr13 # TPP. Show MC springing up from his bed with panic.
        with dissolve

        pause 1

        scene v9wnr14 # TPP. Show MC leaving his room, now dressed wearing outfit 2.
        with dissolve       

        jump v9_history_class
