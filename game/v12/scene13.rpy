# SCENE 13: At the room MC suggest they go to the cafe
# Locations: Hotel room, Hotel corridor, hotel lobby, sidewalk and in front of coffe shop
# Characters: CHLOE (Outfit: 5), MC (Outfit: 5), RILEY (Outfit: 2)
# Time: Morning

label v12_cafe:
    if not v11_riley_roomate:
        scene v12caf1 # TPP. MC sits up in his bed, rubbing his eyes
        with fade

        pause 0.75

        play music music.v12_Track_Scene_13 fadein 2

        scene v12caf2 # FPP. MC sees chloe sitting on her bed going through her phone, mouth opened
        with dissolve

        cl "Morning."

        scene v12caf2a # FPP. Chloe now looking at mc, mouth closed
        with dissolve

        u "Hey, I thought you were gonna wake me up..."

        scene v12caf2b # FPP. Same as 2a, mouth opened
        with dissolve

        cl "I was, but it's still pretty early. I thought I'd let you sleep a little longer."

        scene v12caf2a 
        with dissolve

        u "I wish I could sleep, but..."

        scene v12caf3 # TPP. MC puts his hand on his stomach
        with dissolve

        pause 0.75

        scene v12caf2a
        with dissolve

        u "*Laughs* I'm fucking starving. I honestly have no idea why I'm so hungry."

        scene v12caf2c # FPP. Chloe smiling, mouth opened
        with dissolve

        cl "Haha, well. Let's see... Did you eat yesterday morning before we hopped on the ferry?"

        scene v12caf2a
        with dissolve

        u "Mmm... Nope."

        scene v12caf2b
        with dissolve

        cl "What about on the ferry?"

        scene v12caf2a
        with dissolve

        u "I don't remember... I think I was too busy killing people. *Chuckles*"

        scene v12caf2c
        with dissolve

        cl "Well, there you go. You're \"sooooo\" hungry because you've gone an entire day without eating. *Chuckles*"

        scene v12caf2a
        with dissolve

        u "That's one of those, \"no shit, Sherlock\" type of moments, huh?"

        scene v12caf2c
        with dissolve

        cl "You said it, not me. What do you have an appetite for, a croissant? *Chuckles*"

        scene v12caf2a
        with dissolve

        u "*Chuckles* That actually sounds good, yeah."

        scene v12caf2d # FPP. Chloe stands up, mouth opened
        with dissolve

        cl "Alright, let's go somewhere then."

        scene v12caf2e # FPP. Same as 2d, mouth closed
        with dissolve

        u "Pretty sure I saw a cafe on the ride here."

        scene v12caf2f # FPP. Same as 2d, chloe smiling, mouth opened
        with dissolve

        cl "Perfect, get up and lead the way."

        scene v12caf2e
        with dissolve

        u "*Sighs*"

        scene v12caf4 # TPP. MC gets up
        with dissolve

        pause 0.75

        scene v12caf5 # TPP. MC and chloe leaving the room
        with dissolve

        pause 1

        scene v12caf6 # TPP. MC and chloe in the hotel lobby
        with dissolve

        pause 1

        scene v12caf7 # TPP. MC and chloe in the sidewalk
        with dissolve

        pause 1

        scene v12caf8 # TPP. MC and chloe in front of the cafe
        with dissolve
        
        pause 1

        stop music fadeout 3

        jump v12_chloe_cafe #scene 14

    else:
        scene v12caf1
        with dissolve

        pause 1.25

        play music music.v12_Track_Scene_13 fadein 2

        scene v12caf9 # FPP. Riley humming on her bed
        with dissolve

        ri "*Humming* *Humming* *Humming*"

        scene v12caf9a # FPP. MC looking at riley, mouth closed
        with dissolve

        u "Can you please be quiet."

        scene v12caf9b # FPP. Same as 9a, riley smiling, mouth opened
        with dissolve

        ri "*Laughs* If you don't like my singing you can always leave."

        scene v12caf10 # TPP. MC starts grabbing clothes
        with dissolve

        pause 0.75

        scene v12caf11 # TPP. MC throws clothes on riley, 
        with dissolve

        pause 1

        scene v12caf9a
        with dissolve

        u "Leaving sounds like a good idea."

        scene v12caf9c # FPP. same as 9a, mouth closed
        with dissolve

        ri "Did my singing bother you that much?"

        scene v12caf9a
        with dissolve

        u "*Chuckles* No, I'm starving."

        scene v12caf9c
        with dissolve

        ri "Oh, I was about to say I'm hungry too, so where are we going?"

        scene v12caf9a
        with dissolve

        u "I'm gonna go to that cafe we saw yesterday on the bus ride here."

        scene v12caf9b
        with dissolve

        ri "Then, I guess I am too!"

        scene v12caf9a
        with dissolve

        u "*Sighs* C'mon then. *Chuckles*"

        scene v12caf12 # TPP. MC gets up
        with dissolve

        pause 0.75

        scene v12caf13 # TPP. MC and riley leaving the room
        with dissolve

        pause 1

        scene v12caf14 # TPP. MC and riley in the hotel lobby
        with dissolve

        pause 1

        scene v12caf15 # TPP. MC and riley in the sidewalk
        with dissolve

        pause 1

        scene v12caf16 # TPP. MC and riley in front of the cafe
        with dissolve

        pause 1

        stop music fadeout 3

        jump v12_riley_cafe #scene 14a