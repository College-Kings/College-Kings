# SCENE 35: Aubrey and MC Sex Shop
# Locations: Sex Shop
# Characters: MC (Outfit: 5), AUBREY (Outfit: 2), LINDSEY (Outfit: 1)
# Time: Afternoon 

label v13s35_buy_item_dialog(item):
    scene v13s35_sex_shop

    if (cuffs not in mc.inventory) and (mc.money - item.cost < cuffs.cost):
        u "Only have a bit of money left, better get the cuffs."
    else:
        $ mc.inventory.add_item(item)
        $ mc.money -= item.cost

    call screen v13s35_adult_shop

label v13s35:
    scene v13s35_1 # TPP. Show MC and Aubrey outside the Sex shop, MC slight smile, mouth open, Aubrey slight smile, mouth closed.
    with dissolve

    u "Aubrey wanting to go to a sex shop? Not surprised. *Chuckles*"

    play music "music/v13/Track Scene 35_1.mp3" fadein 2

    scene v13s35_2 # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
    with dissolve

    au "Why not? *Chuckles* Sounded interesting."

    scene v13s35_2a # FPP. Same as v13s35_2, Aubrey slight smile, mouth closed.
    with dissolve

    u "Are you looking for something specific?"

    scene v13s35_2
    with dissolve

    au "Not really, but I didn't wanna go in and walk around by myself."

    scene v13s35_2a
    with dissolve

    u "Well, let's go in then."

    scene v13s35_2
    with dissolve

    au "*Chuckles* You don't even have to walk around with me, I prefer to look around myself. But, just stay close?"

    scene v13s35_2a
    with dissolve

    u "Are you scared or something? What's wrong?"

    scene v13s35_2b # FPP. Same as v13s35_2, Aubrey different pose, slight smile, mouth open.
    with dissolve

    au "Well, no. Not really, but I don't wanna end up in a situation like Nora."

    scene v13s35_2a
    with dissolve

    u "Oh, so you just want some secret protection?"

    scene v13s35_2b
    with dissolve

    au "Bingo."

    scene v13s35_2a
    with dissolve

    u "Haha, c'mon then. I've got you covered."

    scene v13s35_3 # TPP. Show Aubrey and MC starting to walk into sex shop, both slight smile, mouths closed.
    with dissolve

    pause 0.75

    scene v13s35_4 # TPP. Show MC and Aubrey inside of the sex shop, both slight smile, mouths closed.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 35_2.mp3" fadein 2

    scene v13s35_4a # TPP. Same as v13s35_4, Show Aubrey walking away from mc.
    with dissolve

    if chloe.relationship >= Relationship.FWB:
        u "(Guess I could look around a bit...)"
        
        menu:
            "Look around":
                pass
            
            "Not for me":
                jump v13s35_no_shop

        scene v13s35_5 # FPP. MC looking at the general view of the shop.
        with dissolve

        u "(Chloe said she had some fantasies, maybe I can get some things and we could play around...)"

        scene v13s35_6 # FPP. Close up of the handcuffs.
        with dissolve

        u "(What to get, what to get...)"

        scene v13s35_7 # FPP. Close up of the butt plug.
        with dissolve

        $ mc.money = 100
        call screen v13s35_adult_shop
        
        label v13s35_adult_shop_continue:
        scene v13s35_6
        with dissolve
        
        u "(She'll be happy with these, I think. We're gonna have some fun... *Chuckles*)"

        $ mc.inventory.add_item(cuffs)
        $ mc.money -= 10

    else:
        label v13s35_no_shop:
        u "(Guess I'll just post up here...)"

    scene v13s35_8 # TPP. Show MC waiting by the door, slight smile, mouth closed.
    with fade

    pause 0.75

    scene v13s35_8a # TPP. Same as v13s35_8. MC different pose.
    with fade

    pause 0.75

    scene v13s35_9 # FPP. Aubrey infront of MC at the sex shop door, Aubrey full smile, mouth closed.
    with dissolve

    u "What's that face for? *Chuckles* Get some good stuff?"

    scene v13s35_9a # FPP. Same as v13s35_9. Aubrey full smile, mouth open.
    with dissolve

    au "Oh, I got some really, really good stuff. *Chuckles*"

    scene v13s35_9
    with dissolve

    u "Oooh, okay... *Laughs* So, is that it?"

    scene v13s35_9a
    with dissolve

    au "Yeah, that's it."

    scene v13s35_9
    with dissolve

    u "I don't know why I was expecting so much more. It's so clean and... innocent here."

    scene v13s35_9a
    with dissolve

    au "Sorry to disappoint. *Chuckles*"

    scene v13s35_9
    with dissolve

    u "Haha, c'mon."

    scene v13s35_10 # TPP. Show MC and Aubrey walking down the side walk, both slight smile, mouths closed.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 35_3.mp3" fadein 2

    scene v13s35_11 # FPP. Show Lindsey walking towards MC and Aubrey on the side walk, all slight smile, mouths closed
    with dissolve

    pause 0.75

    scene v13s35_11a # FPP. Same as v13s35_11, Lindsey looking at MC, Lindsey infront of MC and Aubrey, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s35_12 # FPP. MC looking at Aubrey, Aubrey looking at Lindsey, Aubrey slight smile, mouth open.
    with dissolve

    au "Hey Lindsey, where are you headed?"

    scene v13s35_11b # FPP. Same as v13s35_11a, Lindsey looking at Aubrey, Lindsey slight smile, mouth open.
    with dissolve

    li "Chris set up a little get together for a few people, you guys should come!"

    scene v13s35_12
    with dissolve

    au "I can't, actually. I'm on my way to chill with Chloe for a bit, but you can take [name] off my hands."

    scene v13s35_11c # FPP. Same as v13s35_11b, Lindsey looking at MC, slight smile, mouth open.
    with dissolve

    li "I'd love to... *Chuckles* You cool with that?"

    scene v13s35_11a
    with dissolve

    u "Sure."

    scene v13s35_11b
    with dissolve

    li "Alright, then. See you, babe."

    scene v13s35_12
    with dissolve

    au "Later guys."

    scene v13s35_12a # FPP. Same as v13s35_12, Aubrey slight smile, mouth closed.
    with dissolve

    u "Later, Aubs."

    scene v13s35_13 # TPP. Show Aubrey walking away from Lindsey and MC, slight smile, mouth closed.
    with dissolve

    # -Aubrey walks off-
    pause 0.75

    stop music fadeout 3
    jump v13_walk_garden
    # -Transition to Scene 36-