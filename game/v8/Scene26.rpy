# Opticians With Riley
# Location: Opticians
# Outfits: MC Outfit 3, Riley Outfit 2, Aubrey Outfit 3
# Time: Monday Afternoon

label s26:
    scene v8sopt1 # FPP. Sweeping shot of Riley and Aubrey in the Opticians looking at glasses.
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    play music "music/mindie4.mp3" fadein 2
    queue music "music/mchill2.mp3"

    if CharacterService.is_girlfriend(lauren):
        u "(Ahhh, there's Aubrey and Riley')"

    else:
        u "(Just look how hot they are)"

    scene v8sopt2 # FPP. Now closer to where Riley and Aubrey are, close up but both in view. Riley and Aubrey looking at Camera, Riley is wearing the Half Frame glasses with black material. Riley and Aubrey both smiling, Riley mouth open.
    with dissolve

    ri "Hey [name]! What do you think?"

    scene v8sopt2a # FPP. Same camera as v8sopt2, Riley and Aubrey both smiling, mouth closed.
    with dissolve

    if CharacterService.is_fwb(riley):
        u "Gorgeous!"

    else:
        u "They look great!"

    scene v8sopt3 # FPP. Show Aubrey reaching for a set of glasses from the display (Standard Issue Glasses with Gold Material)
    with dissolve

    pause 0.5

    scene v8sopt2b # FPP. Same camera as v8sopt2, Aubrey now wearing Standard Issue Glasses with Gold Material, both smiling, Aubrey and Riley looking at eachother, Aubrey mouth open, Riley mouth closed.
    with dissolve

    au "I like these!"

    scene v8sopt2c # FPP. Same camera as v8sopt2, Aubrey and Riley now looking back at camera, still wearing their glasses, mouths closed.
    with dissolve

    if CharacterService.is_fwb(riley) and CharacterService.is_fwb(aubrey):
        u "Hot! You both look amazing."

    else:
        u "You both really suit them."

    scene v8sopt2d # FPP. Same camera as v8sopt2, Aubrey flirty expression with slight wink, Aubrey mouth open.
    with dissolve

    au "Are you getting a naughty librarian vibe?"

    scene v8sopt4 # TPP. Show MC grabbing glasses from the display (Cat Eye Glasses with Black Material), MC mouth open.
    with dissolve

    u "Definitely with these."

    scene v8sopt5 # TPP. Show MC passing Aubrey the glasses he picked from the display.
    with dissolve

    pause 0.5

    scene v8sopt6 # FPP. Close up of Aubrey wearing Cat Eye Glasses with Black Material), Aubrey mouth open, flirty smile.
    with dissolve

    au "What do you think? Do you like it?"

    scene v8sopt6a # FPP. Same camera as v8sopt6, Aubrey mouth closed.
    with dissolve

    u "A lot."

    scene v8sopt2e # FPP. Same camera as v8sopt2, Riley and Aubrey looking at eachother, Riley smile, mouth open. Aubrey wearing Cat Eye Glasses with Black Material.
    with dissolve

    ri "Oh, those look amazing on you! Let me try some."

    scene v8sopt7 # FPP. Show Riley getting some glasses from the display (Cat Eye Glasses with Tortoise Shell Material)
    with dissolve

    pause 0.5

    scene v8sopt2f # FPP. Same camera as v8sopt2, Riley and Aubrey both looking at the camera, both wearing Cat Eye Glasses with Black Material, both smiling, Riley mouth open.
    with dissolve

    ri "How do they look?"

    scene v8sopt8 # FPP. Show Aubrey playfully nuding Riley, both laughing, Aubrey mouth open, both wearing Cat Eye Glasses.
    with dissolve

    au "Damn, girl. Makes me feel a bit naughty."

    scene v8sopt9 # TPP. Show MC stood infront of Riley and Aubrey who are both wearing cat eye glasses, MC laughing, pointing at Riley and Aubrey. Aubrey and Riley smile, MC mouth open.
    with dissolve

    u "So it's settled! You both get a pair!"

    scene v8sopt2f
    with dissolve

    ri "Not so fast... I need a pair I can wear out in public."

    scene v8sopt2g # FPP. Same camera as v8sopt2, Riley and Aubrey both looking at the camera, both wearing Cat Eye Glasses, both smiling, both mouth closed.
    with dissolve

    u "Yeah, probably wouldn't get much done if I saw you in those every day."

    scene v8sopt2f
    with dissolve

    ri "Both of us?"

    scene v8sopt2g
    with dissolve

    u "Now who's feeling naughty?"

    scene v8sopt6a
    with dissolve

    au "Me!"

    scene v8sopt10 # Close up of Riley wearing cat eye glasses, Riley smile, mouth open.
    with dissolve

    ri "Me!"

    scene v8sopt6a
    with dissolve

    au "Oh! I know..."

    scene v8sopt11 # TPP. Show Aubrey getting a pair of glasses for MC to wear, MC looking at Aubrey, Riley looking at Aubrey.
    with dissolve

    pause 0.5

    scene v8sopt12 # FPP. Show Aubrey offering the pair of glasses she just selected, Aubrey looking at Camera, smile, mouth open.
    with dissolve

    au "I bet you'd look super hot in these."

    scene v8sopt12a # FPP. Same camera as v8sopt12, Aubrey smile, mouth closed.
    with dissolve

    menu:
        "Take the glasses":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            jump take_aub_glasses
        "Find a better pair":
            jump no_take_aub_glasses


label take_aub_glasses:
    scene v8sopt13 # TPP. Show MC wearing the glasses Aubrey picked for him, Aubrey and Riley giggle, Riley mouth open.
    with dissolve

    ri "You're so adorable."

    scene v8sopt13a # TPP. Same camera as v8sopt13, Aubrey mouth open, Riley mouth closed.
    with dissolve

    au "Isn't he?"

    scene v8sopt14 # FPP. Show Riley getting a pair of red glasses from the display, Riley mouth open.
    with dissolve

    ri "Here how about these?"

    scene v8sopt15 # TPP. Show MC holding the pair of glasses Aubrey picked for him whilst Riley places a pair of red glasses on him.
    with dissolve

    u "(Uh...)"

    scene v8sopt16 # FPP. Show Aubrey and Riley giggling, Aubrey mouth open.
    with dissolve

    au "*giggles* Sexy."

    scene v8sopt16a # FPP. Same camera as v8sopt16, Riley turns to look at Aubrey, Riley mouth open, Aubrey mouth closed.
    with dissolve

    ri "Right? Even better than the other ones."

    scene v8sopt16b # FPP. Same camera as v8sopt16, Riley looking back at the camera, both mouths closed.
    with dissolve

    u "Aren't we here getting you glasses? Not me?"

    scene v8sopt16a
    with dissolve

    ri "This is way more fun!"

    jump after_glasses_choice

label no_take_aub_glasses:
    scene v8sopt17 # TPP. Show MC grabbing a pair of sunglasses from the display stand, MC mouth open, Riley and Aubrey both looking at MC.
    with dissolve

    u "I think these would be better."

    scene v8sopt18 # TPP. Show MC wearing the pair of sunglasses he selected from the stand, Riley and Aubrey laughing. MC mouth open.
    with dissolve

    u "How awesome is this?"

    scene v8sopt19 # FPP. Show Aubrey showing MC the pair of glasses that she picked for MC in v8sopt11, Aubrey smile, mouth open.
    with dissolve

    au "Meh, I still like these."

    scene v8sopt19a # FPP. Same camera as v8sopt19, Aubrey smile, mouth closed.
    with dissolve

    u "Those look like girl glasses."

    scene v8sopt19b # FPP. Same camera as v8sopt19, Aubrey slight wink, mouth open.
    with dissolve

    au "So... you're pretty. You can pull it off."

    scene v8sopt19a
    with dissolve

    u "(Pretty? That's not good)"

    scene v8sopt2g
    with dissolve

    u "What do you think, Riley?"

    scene v8sopt2f
    with dissolve

    ri "I agree with Aubrey. You're very pretty."

    scene v8sopt2g
    with dissolve

    u "(This isn't going like I planned)"

    jump after_glasses_choice

label after_glasses_choice:
    scene v8sopt20 # TPP. Show MC grabbing a pair of glasses (RW ASG Rectangle Thin Frame) from the stand, MC mouth open, smile, Riley and Aubrey looking at MC.
    with dissolve

    u "Riley, these would look so amazing on you!"

    scene v8sopt21 # TPP. Show MC passing the RW ASG Rectangle Thin Frame glasses to Riley, Aubrey looking at Riley, Riley taking the glasses from MC. Aubrey mouth open smile.
    with dissolve

    au "He's right! With your hair color those would look so hot."

    scene v8sopt22 # FPP. Show Aubrey looking at Riley, Riley wearing RW ASG Rectangle Thin Frame glasses, Aubrey smile, Riley smile, both mouths closed.
    with dissolve

    if CharacterService.is_fwb(riley):
        u "(She looks so kissable)"

    else:
        u "You really suit them, Riley!"

    scene v8sopt22a # FPP. Same camera as v8sopt22, Aubrey still looking at Riley, Aubrey mouth open.
    with dissolve

    au "See, we made the right choice asking [name] to come, didn't we Riley?"

    scene v8sopt22b # FPP. Same camera as v8sopt22, Riley now also looking at Aubrey, Riley mouth open, Aubrey mouth closed.
    with dissolve

    ri "Yes we did. He sure knows what a girl wants."

    scene v8sopt22c # FPP. Same camera as v8sopt22, both now looking back at camera, Aubrey flirty expression mouth open, Riley mouth closed.
    with dissolve

    au "Or girls..."

    scene v8sopt22
    with dissolve

    u "(Am I dreaming this? They can't mean...)"

    scene v8sopt23 # FPP. Show Riley grabbing a different pair of glasses from the display stand, Riley mouth open.
    with dissolve

    ri "I kinda like these too."

    scene v8sopt24 # FPP. Show Aubrey looking at Riley who is now holding the pair of glasses she selected in v8sopt23, Aubrey mouth open
    with dissolve

    au "Try 'em on."

    scene v8sopt24a # FPP. Same camera as v8sopt24, Riley now wearing glasses from v8sopt23, Riley and Aubrey now looking at camera, both smiling, Riley mouth open.
    with dissolve

    ri "What do you think?"

    scene v8sopt24b # FPP. Same camera as v8sopt24, Riley and Aubrey smiling, both mouths closed.
    with dissolve

    if CharacterService.is_fwb(riley):
        u "Those look really hot, but I still think the last pair matches your hair, like Aubrey said."

    else:
        u "Those look really good, but I think the last pair looks better."

    scene v8sopt24c # FPP. Same camera as v8sopt24, Riley and Aubrey smiling, Aubrey mouth open.
    with dissolve

    au "Yeah, they were just so gorgeous."

    scene v8sopt24a
    with dissolve

    ri "Last pair it is!"

    if CharacterService.is_fwb(riley) or CharacterService.is_fwb(aubrey):
        scene v8sopt24d # FPP. Same camera as v8sopt24, Riley curious expression, Aubrey neutral expression, Riley mouth open.
        with dissolve

        ri "Which pair would you rather see on your nightstand?"

        scene v8sopt24b
        with dissolve

        u "(Don't fuck this up, [name])"

        menu:
            "Riley's glasses":
                u "Those... tonight?"

                scene v8sopt24e
                with dissolve

                ri "You dog!"

                scene v8sopt24a
                with dissolve

                ri "I think I'll go with the last pair."

                jump opti_end

            "Both glasses":
                u "Both"

                scene v8sopt24f # FPP. Same camera as v8sopt24, Riley and Aubrey look at eachother confused.
                with dissolve

                u "I have two nightstands. One for your glasses and one for Aubrey's."

                scene v8sopt24g # FPP. Same camera as v8sopt24, Riley and Aubrey looking back at camera, shocked smile, aubrey mouth open.
                with dissolve

                au "Bold! I like it!"

                scene v8sopt25 # TPP. Show Riley whispering in MC's ear, MC slight smile, Riley flirty smile, slight mouth open (whispering)
                with dissolve

                ri "*whispers* Careful what you wish for."

                jump opti_end
    else:
        jump opti_end

label opti_end:
    scene v8sopt26 # FPP. Show Aubrey placing the glasses she was wearing back on the stand, Riley mouth open.
    with dissolve

    ri "I think I'm gonna take these ones."

    scene v8sopt27 # FPP. Close up of Aubrey and Riley now stood near the exit of the opticians, Riley wearing  RW ASG Rectangle Thin Frame glasses, both neutral expressions, Riley mouth open.
    with dissolve

    ri "Thanks for coming. I feel better about needing glasses now."

    scene v8sopt27a # FPP. Same camera as v8sopt27, Riley mouth closed, Aubrey mouth open.
    with dissolve

    au "Yeah, you're a good guy, [name]."

    scene v8sopt27b # FPP. Same camera as v8sopt27, both mouths closed.
    with dissolve

    u "I had a lot of fun."

    scene v8sopt27a
    with dissolve

    au "We should do this again soon."

    scene v8sopt27b
    with dissolve

    u "I can't wait!"

    scene v8sopt27
    with dissolve

    ri "We have other errands to run, but I'll text you soon."

    scene v8sopt27b
    with dissolve

    u "Great!"

    scene v8sopt27a
    with dissolve

    au "See ya."

    scene v8sopt27b
    with dissolve

    u "Bye."

    jump mon_eve_room_josh
