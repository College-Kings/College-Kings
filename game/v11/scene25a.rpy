# SCENE 25a: Hotel Bar
# Location: Hotel Bar
# Characters: MC (Outfit 1), charli (Outfit 1)
# Time: Evening

label v11_hotel_charlie_bar:
    scene v11cmb1 # TPP. Show Charli approaching MC at the bar.
    with dissolve
    play music "music/v11/Track Scene 5_6.mp3" fadein 2
    charli "Wearing that shirt with those pants was a pretty brave choice."

    scene v11cmb2 # FPP. Show charli mouth closed
    with dissolve

    u "*Sighs* What do you want?"

    scene v11cmb2a # FPP. Show charli mouth open
    with dissolve

    charli "What, I can't make conversation? Or do you think I'm gonna try to sleep with your bar stool as well?"

    scene v11cmb2
    with dissolve

    u "You know, I don't know what your deal is. This whole fake nice guy attitude is lowkey pissing me off."

    scene v11cmb2a
    with dissolve

    charli "It's almost fascinating just how narcissistic you are and how heavy you deflect."
    charli "First you thought I was being kind to the girls with a hidden agenda, but now that you know I'm gay, you've lost the ability to connect those dots."

    scene v11cmb2
    with dissolve

    scene v11cmb2a
    with dissolve

    charli "You can't comprehend being nice without an agenda, because you yourself aren't nice without an agenda."

    if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe) and CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(aubrey):
        charli "How many girls have you messed with on this trip alone? Chloe, Aubrey, Lauren?"

    elif CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(aubrey):
        charli "How many girls have you messed with on this trip alone? Aubrey, Lauren, who else?"

    elif CharacterService.is_fwb(aubrey) and CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        charli "How many girls have you messed with on this trip alone? Aubrey, Chloe, who else?"

    elif CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        charli "How many girls have you messed with on this trip alone? Chloe, Lauren, who else?"
        
    scene v11cmb2a
    with dissolve

    charli "Taking time to think about who you're really upset with might be a good idea..."

    scene v11cmb2
    with dissolve

    u "You don't know anything about me, yet you're trying to tell me who I am and what I do. You've been around for like a week bro."
    u "Sure, I may do some dumb shit, but that doesn't make me a horrible person."

    scene v11cmb2a
    with dissolve

    charli "You can make excuses for your actions all you want, but if others are harmed by what you do, especially if these \"others\" are people I've grown close to..."
    charli "...then you can be assured I'm going to have an issue with you regardless of how you may feel."

    scene v11cmb2
    with dissolve

    u "Stay away from my friends and stay away from me. No one asked for you to come around and play superhero, or therapist, or fucking Messiah."

    scene v11cmb2a
    with dissolve

    charli "You can be mad at me all you want, we both know you're really just mad at yourself cause my words resonate."

    scene v11cmb3 # FPP Show charli walking away
    with dissolve

    u "(Fuck him! He doesn't know me! I'm not letting him get to me...)"
    stop music fadeout 3
    if joinwolves:
        jump v11_hotel_bar_wolves
    else:
        jump v11_hotel_bar_apes