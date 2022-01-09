# SCENE 13: MC at wolves house/redecorate
# Locations: Wolves house/MC Wolves Room/MC New Wolves Room
# Characters: MC (Outfit 1), Chris (Outfit 1), Perry (Outfit 1)
# Time: Sunday Morning
# If you need paint and brush use industrial clutter 2: https://mega.nz/file/4YgihJxL#CC_JVYehPM-krceVG1d7x-0K8MNhwfIAfwtLVDjrQ3I

label v10_wolves_redec:
    if v10s10_hangWLinds:
        scene v10swhr1 # TPP. Show MC walking through the front door of the Wolves house.
        with Fade(1, 0, 1)

        play sound "sounds/dooropen.mp3"

    else:
        scene v10swhr8 # TPP. Show MC walking down the stairs of the Wolves house.
        with Fade(1, 0, 1)

    pause 0.75

    play music "music/v10/Track Scene 13.mp3" fadein 2

    scene v10swhr2 # FPP. Show Chris stood in the Wolves hallway this angle must make sense for both whr1 & whr8, Chris neutral, mouth closed.
    with dissolve

    u "Hey Chris, I really appreciate the room and all, but I haven't had a chance to make it scream [name] yet. It cool if I jazz it up a bit?"

    scene v10swhr2a # FPP. Same as whr2, Chris neutral, mouth open.
    with dissolve

    ch "I was wondering when you'd get tired of blank walls. There's some supplies in the closet in your room. We're actually getting ready to decorate the whole house."

    scene v10swhr2
    with dissolve

    u "Really!? Good timing haha. Got a theme in mind?"

    scene v10swhr2a
    with dissolve

    ch "Yeah man! Make it scream \"Wolves\", you know?"

    scene v10swhr2
    with dissolve

    u "Yeah, that sounds great!"

    scene v10swhr2a
    with dissolve

    ch "Go for it, man! Have fun."

    scene v10swhr3 # TPP. Show MC looking for supplies in his closet in his room, in the closet there should be some tins of paint and brushes.
    with fade

    pause 0.75
    
    scene v10swhr4 # FPP. Show Perry stood at the door of MC's room, Perry neutral, mouth open.
    with dissolve

    guyd "Hey man..."

    scene v10swhr4a # FPP. Same as whr4, Perry neutral, mouth closed.
    with dissolve

    u "Hey, feels like you've kinda been hiding since the fight."

    scene v10swhr4
    with dissolve

    guyd "Yeah, a little bit. What are you doing in the closet?"

    scene v10swhr4a
    with dissolve

    u "I'm getting ready to decorate my room."

    scene v10swhr4b # FPP. Same as whr4, Perry smile, mouth open.
    with dissolve

    guyd "Oh wow, you want some help?"

    scene v10swhr4c # FPP. Same as whr4, Perry smile, mouth closed.
    with dissolve

    menu:
        "Accept help":
            $ add_point(KCT.BRO)

            u "Yeah I'd love some help. Will go much faster haha."

            scene v10swhr5 # TPP. Show Perry and MC stood near a wall both looking around thinking about where to start, paint brushes in hand and tins of white paint next to them on the floor.
            with fade

            pause 0.75

            scene v10swhr6 # FPP. Show Perry, neutral expression, mouth closed.
            with dissolve

            u "Hey man, hope you don't mind me asking, but what made you back out at the brawl?"

            scene v10swhr6a # FPP. Same as whr6, slight embarrassed expression, mouth open.
            with dissolve

            guyd "I was waiting for you to bring that up. It's kind of embarrassing, man."

            scene v10swhr6b # FPP. Same as whr6, slight embarrassed expression, mouth closed.
            with dissolve

            u "Embarassing? What's up?"

            scene v10swhr6a
            with dissolve

            guyd "Well, the reason I ran and chose not to fight isn't because I didn't want to, it's because I couldn't."

            scene v10swhr6b
            with dissolve

            u "What do you mean you couldn't?"

            scene v10swhr6a
            with dissolve

            guyd "Man, I got sick..."

            scene v10swhr6b
            with dissolve

            u "Sick from what?"

            scene v10swhr6a
            with dissolve

            guyd "You know that sushi we had in the fridge for a while?"

            scene v10swhr6b
            with dissolve

            u "Yeah."

            scene v10swhr6a
            with dissolve

            guyd "Well, I ate it right before the fight because I was hungry and well I've never had sushi before. Turns out, I'm allergic."

            scene v10swhr6b
            with dissolve

            u "Are you serious!?"

            scene v10swhr6a
            with dissolve

            guyd "Sadly, yes. Regardless of me sick or not though the guys still weren't happy."

            scene v10swhr6b
            with dissolve

            u "At least you had a good reason."

            scene v10swhr6c # FPP. Same as whr6, smile, mouth open.
            with dissolve

            guyd "Yeah, next time though I'm going in like a beast."

            scene v10swhr6d # FPP. Same as whr6, smile, mouth closed.
            with dissolve

            u "Glad to hear it."

            scene v10swhr7 # TPP. Show wide shot of MC's new wolves room.
            with Fade(1, 0, 1)

            guyd "Well the room looks pretty nice."

            u "Yeah, this is way better, the carpet and curtains really finish it off. Thanks man!"

            guyd "Anytime."

        "Decline help":
            u "I appreciate it man, but I'm all good. This is gonna require all my focus."

            scene v10swhr4b
            with dissolve

            guyd "Alright man."

            scene v10swhr3
            with dissolve

            pause 0.75

            scene v10swhr7 # TPP. Show wide shot of MC's new wolves room.
            with Fade(1, 0, 1)             

            u "(Now that's what I'm talking about!)"    
            
    stop music fadeout 3  

    jump v10_call_with_lauren1