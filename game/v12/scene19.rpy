# SCENE 19: MC wakes up to Chloe / Lindsey argument or Imre's scream
# Locations: Hotel Room, Hotel Room Bathroom, Hotel Room Corridor, Hotel Lobby
# Characters: IMRE (Outfit: 5/2), MC (Outfit: 11/9), NORA (Outfit: 3/1), AUBREY (Outfit: 5/1), CHLOE (Outfit: 2), LINDSEY (Outfit: 1), RILEY (Outfit: 5)
# Time: Morning
# Phone Images: YES
# POST 1 - imre_raccoon.webp - Picture of Imre sleeping on the toilet with the raccoon drawn on his face (check with whoever did scene 18 for the exact drawing). 
# NOTE: v12pwu13a and all other renders after that use the second outfit provided for the character (if there are 2 outfits given)

init python:
    def v12s19_kiwiiReply1():
        v12s19_kiwiiPost1.newComment(amber, _("Hahahaha"), numberLikes=renpy.random.randint(250,350), force_send=True)
        v12s19_kiwiiPost1.newComment(imre, _("Karma's a bitch..."), numberLikes=renpy.random.randint(250,350), force_send=True)

label v12_party_wake_up:
    scene v12pwu1 # TPP. Show MC sleeping, it's morning now, alone in the bed
    with fade

    pause 0.75

    play music "music/v12/Track Scene 19.mp3" fadein 2

    scene v12pwu2 # FPP. MC lying in the bed, looking at the bedroom door
    with vpunch

    imre "What the fuck is on my face!?"

    u "Sounds like someone's awake. *Chuckles*"

    scene v12pwu3 # TPP. Show MC opening the bathroom door and walking in, smiling, mouth closed
    with dissolve
    play sound "sounds/dooropen.mp3"

    pause 0.75

    scene v12pwu4 # FPP. MC in the bathroom, looking at Imre, Imre in front of the mirror, looking at MC, Imre angry, mouth closed, Imre has the raccoon drawing on his face (check with whoever rendered scene 18)
    with dissolve

    u "What's wrong, man?"

    scene v12pwu4a # FPP. Same as v12pwu4, Imre mouth open, angry
    with dissolve

    imre "What do you mean what's wrong?! I look like a damn raccoon! Who did this to me, [name]?"

    scene v12pwu4
    with dissolve

    u "*Chuckles* You don't remember?"

    scene v12pwu4a
    with dissolve

    imre "I remember being drunk and talking to Amber."

    scene v12pwu4
    with dissolve

    u "You don't remem-"

    scene v12pwu4a
    with dissolve

    imre "AMBER! SHE DID THIS!"

    scene v12pwu5 # TPP. Show Imre walking out of the bathroom, very angry, mouth closed
    with dissolve

    pause 0.75

    scene v12pwu5a # TPP. Same camera as v12pwu5, MC walking out of the bathroom, smiling, mouth closed
    with dissolve

    pause 0.75

    scene v12pwu6 # FPP. MC and Imre in the room, MC looking at Imre, Imre looking at MC, Imre angry, mouth open
    with dissolve

    imre "Where's Amber?!"

    scene v12pwu6a # FPP. Same as v12pwu6, Imre angry, mouth closed
    with dissolve

    u "Haha, I think she's already gone."

    scene v12pwu7 # FPP. Same positioning as v12pwu6, Nora standing next to Imre, MC looking at Nora, slight smile, mouth open, Nora looking at Imre's direction
    with dissolve

    no "Aww! Imre, you look like a weird raccoon... Come here, little guy..."

    scene v12pwu8 # TPP. Same positioning as v12pwu7, Nora looking at Imre, Imre looking at Nora, Nora licking her thumb, Imre angry, mouth closed
    with dissolve

    pause 0.75

    scene v12pwu8a # TPP. Same as v12pwu8, Show Nora wiping off the drawing on Imre's face, Imre less annoyed, mouth closed, Nora mouth closed, slight smile
    with dissolve

    pause 1.25

    scene v12pwu9 # FPP. Same positioning as v12pwu8, Aubrey lying on the bed with Riley, Aubrey yawning, she's waking up, Riley still sleeping
    with dissolve

    au "*Yawn*"

    scene v12pwu9a # FPP. Same as v12pwu9, Aubrey looking at Nora's direction, Aubrey slight smile, mouth open
    with dissolve

    au "Someone's being extra nice this morning."

    scene v12pwu7a # FPP. Same as v12pwu7, Nora looking at Aubrey's direction, Nora slight smile, mouth open
    with dissolve

    no "Last night put me in a good mood. It was nice being with just the girls after the guys left."

    scene v12pwu6b # FPP. Same as v12pwu6, Imre looking at Nora's direction, Imre slight smile, mouth open
    with dissolve

    imre "I was here...? So was [name]."

    scene v12pwu7
    with dissolve

    no "Yeah, but you guys didn't cause any issues."

    scene v12pwu7b # FPP. Same as v12pwu7, Nora looking at MC, Nora slight smile, mouth closed
    with dissolve

    u "Thanks?"

    scene v12pwu7c # FPP. Same as v12pwu7b, Nora slight smile, mouth open
    with dissolve

    no "Haha, that was a compliment. You're welcome. What time is it?"

    scene v12pwu9a
    with dissolve

    au "Early. *Chuckles*"

    scene v12pwu7a
    with dissolve

    no "Well, I wanted to go to the French baguette factory today."

    scene v12pwu9b # FPP. Same as v12pwu9a, Aubrey slightly annoyed, mouth open
    with dissolve

    au "Ugh... Why? That sounds so boring."

    scene v12pwu7a
    with dissolve

    no "Do you have anything else planned for today?"

    scene v12pwu9b
    with dissolve

    au "*Scoffs* No."

    scene v12pwu7a
    with dissolve

    no "Then you can come along."

    scene v12pwu7
    with dissolve
    
    no "Imre, you and [name] can come too. If you want?"

    scene v12pwu7b
    with dissolve

    u "I have nothing better to do."

    scene v12pwu6b
    with dissolve

    imre "Hmm... I guess I can get revenge on Amber later."

    scene v12pwu7c
    with dissolve

    no "Alright, let's get changed and go then. Meet you guys in the lobby!"

    if not v11_riley_roomate:

        scene v12pwu10 # TPP. Show MC leaving the hotel room, neutral expression, mouth closed
        with dissolve

        pause 0.75
        
        scene v12pwu11 # TPP. Show MC walking in the hallway, neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v12pwu12 # TPP. Show MC entering his hotel rooom, neutral expression, mouth closed
        with dissolve

        pause 0.75
    
    $ v12s19_kiwiiPost1 = KiwiiPost(amber, "v12/imre_raccoon.webp", _("Happy Birthday, Lindsey!"), numberLikes=419) # Picture of Imre with the raccoon drawing from scene 18 on his face
    $ v12s19_kiwiiPost1.newComment(chris, _("Oh no... What did you guys do to him?"), mentions=[amber], numberLikes=renpy.random.randint(250,350))
    $ v12s19_kiwiiPost1.newComment(amber, _("\"We\" taught him why we shouldn't get too drunk at slumber parties... Hehe"), mentions=[chris], numberLikes=renpy.random.randint(150,300))
    $ v12s19_kiwiiPost1.newComment(imre, _("\"We\"??? Who is we?!?!"), mentions=[amber], numberLikes=renpy.random.randint(250,400))
    $ v12s19_kiwiiPost1.addReply(_("Not cool, Amber... Not cool... ;)"), v12s19_kiwiiReply1, mentions=[amber], numberLikes=renpy.random.randint(250, 330))
    $ v12s19_kiwiiPost1.addReply(_("It's just a prank bro!"), v12s19_kiwiiReply1, mentions=[imre], numberLikes=renpy.random.randint(250, 330))
    
    scene v12pwu13 # TPP. Show MC removing his pajama shirt, pajama pants still on, neutral expression, mouth closed
    with dissolve

    pause 1

    scene v12pwu13a # TPP. Same as v12pwu13, Show MC putting on his regular shirt, regular pants already on, mouth closed, neutral expression
    with fade

    pause 1

    if not v12_told_chloe and not v11_told_aubrey:
        scene v12pwu10a # TPP. Same as v12pwu10, MC wearing regular clothes, neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v12pwu11a # TPP. Same as v12pwu11, MC wearing regular clothes, neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v12pwu14 # TPP. Show MC walking in the hotel lobby, show Nora, Imre and Aubrey waiting for him, all slight smiles, mouths closed, Nora has a bag with her
        with dissolve

        pause 0.75
    
    else:
        scene v12pwu15 # FPP. MC in the room, looking at the door to the hallway
        with vpunch

        cl "HOW IS THAT GOOD?! YOU COULD'VE COME TO ME!"

        scene v12pwu16 # TPP. Lindsey and Chloe in the hallway, looking at each other. Show only Lindsey, Lindsey looking at Chloe, Lindsey angry, mouth open, they are having a heated argument
        with dissolve

        li "How Chloe?! What would you have done differently? I've given you ideas and talked to you about all of this in the past, all you've done is blow me off. And you don't listen to any of the other girls either."

        scene v12pwu17 # TPP. Same as v12pwu16, show only Chloe, Chloe looking at Lindsey, Chloe angry, mouth open
        with dissolve

        cl "We can't just change on the drop of a coin. Things take time!"

        scene v12pwu16
        with dissolve

        li "That's your problem, Chloe. You know exactly what to do, and how to do it, we've told you. Numerous times. Yet you don't do a damn thing..."

        scene v12pwu17
        with dissolve

        cl "Ha! You don't think I'm trying?!"

        scene v12pwu16a # TPP. Same as v12pwu16, different pose
        with dissolve

        li "Sorry Chloe... But no. We have the ability to save this sorority and since you won't, I will!"

        scene v12pwu17a # TPP. Same as v12pwu17, different pose
        with dissolve

        cl "This is not going to help, Lindsey. If anything it's just going to divide the sorority."

        scene v12pwu16a
        with dissolve

        li "You're so blind to the fact that you're the problem and you don't wanna admit it."

        scene v12pwu17a
        with dissolve

        cl "I thought we were friends, Lindsey."

        scene v12pwu16
        with dissolve

        li "We are, but this is a whole other matter. I never wanted this to mess up our friendship."

        scene v12pwu17a
        with dissolve

        cl "Yet you're talking and planning things behind my back..."

        scene v12pwu16
        with dissolve

        li "I've come to you so many times over the past few weeks, Chloe. Opening up to you and all of your decisions in hopes that you'd be even a tiny bit open to what us girls want."
        li "And you just refuse to hear any advice."

        scene v12pwu17
        with dissolve

        cl "We're in Europe right now, what am I supposed to do from here?"

        scene v12pwu16a
        with dissolve

        li "Please don't make any excuses... I know you weren't planning on taking any of my advice. Any time I've ever had a suggestion you've come up with some reason to object to it."

        scene v12pwu17
        with dissolve

        cl "Wow, you really don't get it... When everything blows up, just know you started this!"

        scene v12pwu18 # TPP. Show Chloe walking away from Lindsey in the hallway, Chloe angry, mouth closed, Lindsey worried, mouth open
        with dissolve

        li "*Sighs* CHLOE!"

        scene v12pwu18a # TPP. Same as v12pwu18, Chloe no longer in shot, show Lindsey running towards where Chloe was walking to, Lindsey worried, mouth closed
        with dissolve

        u "(Getting back to campus just got a lot more exciting...)"

        scene v12pwu10a # TPP. Same as v12pwu10, MC wearing regular clothes, neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v12pwu11a # TPP. Same as v12pwu11, MC wearing regular clothes, neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v12pwu14 # TPP. Show MC walking in the hotel lobby, show Nora, Imre and Aubrey waiting for him, all slight smiles, mouths closed, Nora has a bag with her
        with dissolve

        pause 1

        scene v12pwu19 # FPP. MC looking at Nora in the lobby, Nora looking at MC, Nora slight smile, mouth open
        with dissolve

        no "Ready to go?"

        scene v12pwu19a # FPP. Same as v12pwu19, Nora slight smile, mouth closed
        with dissolve

        u "Yeah, let's go."

        scene v12pwu20 # TPP. Show MC and Nora leaving the hotel lobby, both slightly smiling, mouths closed
        with dissolve

        pause 1

    stop music fadeout 3

    jump v12_urban_exploring #scene 20