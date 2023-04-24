# SCENE 44: Lindsey At Warehouse
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Lindsey (Outfit 1)
# Time: Saturday Night

label v9_warehouse_lindsey:
    scene v9wwl1 # TPP. Show MC walking through the warehouse towards a board on the wall. Near the exit/entrance of the warehouse.
    with fade

    u "(I need a breather. I should go see what this lineup looks like. Prepare myself for the night.)"

    play music "music/v9/Track Scene 7.mp3" fadein 2

    scene v9wwl2 # TPP. Show MC continuing to walk, he bumps into Lindsey as he is walking.
    with dissolve

    pause 1

    scene v9wwl3 # FPP. Show Lindsey, neutral, mouth closed.
    with dissolve

    if not hangOutWithLindsey:
        u "Oh, Linds! Hey!"

        u "You alright? Sorry, I was distracted."

        scene v9wwl3a # FPP. Same camera as v9wwl3, Lindsey mouth open.
        with dissolve

        li "I'm fine."

        scene v9wwl3
        with dissolve

        u "(Uh oh.)"

        u "Um, thanks for coming."

        scene v9wwl3a
        with dissolve

        li "I'm here with some friends."

        scene v9wwl3
        with dissolve

        u "Oh, yes of course." 

        scene v9wwl4 # FPP. Show Lindsey walking away.
        with dissolve

        menu:
            "Stop her":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Um... Lindsey?"

                scene v9wwl4a # FPP. Same camera as v9ww4, Lindsey turns back around.
                with dissolve

                pause 0.75

                scene v9wwl3
                with dissolve

                u "I just wanted to say I'm sorry for not coming over. I've been so distracted with this fight. It's really gotten in my head."

                scene v9wwl3a
                with dissolve

                li "Yeah, it's a lot bigger deal than I expected."

                scene v9wwl3
                with dissolve

                u "Me too! I'm scared shitless right now!"

                scene v9wwl3b # FPP. Same camera as v9wwl3, Lindsey smile, mouth open.
                with dissolve

                li "I'm sure you'll do great. I gotta get back to my friends."

                scene v9wwl3c # FPP. Same camera as v9wwl3, Lindsey smile, mouth closed.
                with dissolve

                u "Yes, of course. Can I text you later?"

                scene v9wwl3b
                with dissolve
                # -Lindsey looks like she's thinking-
                li "Sure, why not?"

                scene v9wwl4b # FPP. Same camera as v9wwl4, Lindsey now gone out of view.
                with dissolve

            "Let her go":
                scene v9wwl4b # FPP. Same camera as v9wwl4, Lindsey now gone out of view.
                with dissolve

                u "(You really screwed that one up. But you gotta get your head in the game.)"

    elif lindsey.relationship >= Relationship.KISSED:
        u "Oh, shit! Hey! Are you alright?"

        scene v9wwl3b
        with dissolve

        li "Wow you were on another planet there."

        scene v9wwl3c
        with dissolve

        u "Yeah, sorry. You sure you're alright?"

        scene v9wwl3d # FPP. Same camera as v9wwl3, Lindsey flirt, mouth open.
        with dissolve

        li "If you slam into me that hard later tonight I will be."

        scene v9wwl3e # FPP. Same camera as v9wwl3, Lindsey flirt, mouth closed.
        with dissolve

        u "Mmm. Maybe I should forfeit and get started now."

        scene v9wwl6 # FPP. Show MC grabbing Lindsey's hand in a (ooo come here) kind of way, Lindsey looks confused.
        with dissolve

        pause 1

        scene v9wwl3f # FPP. Same camera as v9wwl3, Lindsey confused, mouth open.
        with dissolve

        li "What?"

        scene v9wwl3g # FPP. Same camera as v9wwl3, Lindsey confused, mouth closed.
        with dissolve

        menu:
            "It was a joke":
                $ reputation.add_point(RepComponent.BRO)
                
                u "Aww, don't worry. No cold feet here. You're just very hard to resist."
                
                scene v9wwl3d
                with dissolve

                li "So are you."

                scene v9wwl3e
                with dissolve

                u "Mmmm."

                scene v9wwl3d
                with dissolve

                li "So, what do you say we continue where we left off after the fight?"

                scene v9wwl3e
                with dissolve

                u "Win or lose, I'll be a happy man."

                scene v9wwl3b
                with dissolve

                li "You're so sweet. But you won't lose. I believe in you."

                scene v9wwl3c
                with dissolve

                u "Now who's the sweet one?"

                scene v9wwl3b
                with dissolve

                li "Guess you'll have to wait and see."

                scene v9wwl7 # TPP. Show Lindsey grazing MC's crotch with her hand as she walks away, Lindsey flirt, mouth open.
                with dissolve

                li "Text me later."

                scene v9wwl8 # TPP. Show Lindsey walking away, MC watching her walk away.
                with dissolve
    
            "Be serious":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Sorry, I'm just getting in my head. There's a lot riding on this fight."

                scene v9wwl3b
                with dissolve

                li "You're gonna do great. You've been training hard..."

                li "...so much that you even ran out on this really hot chick who was dying to see you naked."

                scene v9wwl3c
                with dissolve

                u "Oh, really?"

                scene v9wwl3b
                with dissolve

                li "Really."

                scene v9wwl3c
                with dissolve

                u "My alarm went off."

                scene v9wwl3b
                with dissolve

                li "I say, when you come see me after the fight, you leave that phone in your room."

                scene v9wwl3c
                with dissolve

                u "You gonna nurse me back to health if I lose?"

                scene v9wwl3d
                with dissolve

                li "If you lose, I'll make you forget all about the fight."

                li "BUT!"

                li "WHEN you win, I'll pamper you good."

                li "Real good."

                scene v9wwl3e
                with dissolve

                u "Then I'm definitely gonna win."

                scene v9wwl3b
                with dissolve

                li "That's my boy. Now you go kick some ass!"

                scene v9wwl3c
                with dissolve

                u "I'll text you after."

                scene v9wwl3b
                with dissolve
                li "I know you will."

                scene v9wwl8
                with dissolve

    else:
        u "Oh, hey! You alright? Sorry about that."

        scene v9wwl3b
        with dissolve

        li "It's okay. You were totally spaced out."

        scene v9wwl3c
        with dissolve

        u "Yeah, getting my head right before the fight."

        scene v9wwl3b
        with dissolve

        li "Well, I'll let you do that."

        scene v9wwl4
        with dissolve
        
        menu:
            "Let her go":
                pause 0.75

                scene v9wwl4b
                with dissolve

                u "(Am I nuts or was that a cold shoulder? Damn. I really want to fix it but I have to get ready.)"

            "Stop her":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Um, I'm sorry about earlier. I..."

                scene v9wwl4a
                with dissolve

                pause 0.75

                scene v9wwl3
                with dissolve

                u "This night's kinda getting to me."

                scene v9wwl3a
                with dissolve

                li "Looks intense."

                scene v9wwl3
                with dissolve

                u "You have no idea."

                u "Can we catch up after the fight?"

                scene v9wwl3b
                with dissolve

                li "Guess that depends on what shape you're in after the fight."

                scene v9wwl3c
                with dissolve

                u "Haha. Yeah, guess I won't be much fun if I get my ass kicked."

                scene v9wwl3b
                with dissolve

                li "I'm sure you won't. But yeah, why don't you text me if you're feeling up to it after the fight?"

                scene v9wwl3c
                with dissolve

                u "I'd like that."

                scene v9wwl3b
                with dissolve

                li "Me too. I have to get back to my friends."

                scene v9wwl3c
                with dissolve

                u "Sure. Sure. I, uh, have to get back to...worrying. Haha."

                scene v9wwl3b
                with dissolve

                li "I'll be rooting for you."

                scene v9wwl5 # TPP. Show Lindsey giving MC a quick kiss on the cheek.
                with dissolve

                pause 1

                scene v9wwl4
                with dissolve

                pause 0.75

                scene v9wwl4b
                with dissolve

    pause 1

    scene v9wwl1 # TPP. Show MC continuing to walk through the warehouse, he should be near the entrance of the warehouse.
    with dissolve

    u "(Focus.)"

    stop music fadeout 3

    jump v9_ending