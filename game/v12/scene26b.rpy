# SCENE 26b: MC Chases After Nora
# Locations: 
# Characters: MC (Outfit: 3), NORA (Outfit: 1), LINDSEY (Outfit: 1)
# Time: morning
# Phone Images: 

label v12_chase_nora:
    scene v12cn1 # TPP Show MC chasing running down hotel hallway after Nora
    with dissolve
    
    pause 0.5

    play music "music/v12/Track Scene 26b.mp3" fadein 2
    
    scene v12cn2 # TPP Show MC, at Nora's door, opening it
    with dissolve
    
    pause 0.5
    
    scene v12cn3 # FPP MC in Nora's room, in doorway, looking at Nora, sitting on her bed crying, with Lindsey next to her with her hand on Nora's shoulder
    with dissolve

    pause 0.75

    scene v12cn4 # TPP MC sits down on bed on other side of Nora from Lindsey
    with dissolve

    pause 0.75

    scene v12cn5 # FPP MC looking at Nora, who is crying and looking down. Lindsey is on Nora's other side, looking at Nora in concern
    with dissolve

    u "Please tell me you aren't hurt..."

    scene v12cn5a # FPP Same angle as v12cn5, Nora still looking down with tears on her face, her mouth open
    with dissolve

    no "*Crying* I'm fine, [name]."

    scene v12cn5b # FPP Same angle as v12cn5, Nora still looking down and crying, mouth closed, Lindsey looking at Nora, angry expression, mouth open
    with dissolve

    li "Quit saying that, you're not fine! What he did to you was WAY out of line. And don't give me that \"I hit him first\" bullshit, he shouldn't have pushed you like that."

    scene v12cn5a
    with dissolve

    no "*Crying* I don't understand why I can't just be in a normal, happy relationship. I'm so fucking tired of always fighting."

    scene v12cn5b
    with dissolve

    li "Then be done with it. Who cares how great he was or how wonderful it used to be. It's who he is right now that matters."

    scene v12cn5c # FPP Same angle as v12cn5, Nora still looking down and crying, mouth closed, Lindsey looking at Nora, sad expression, mouth open
    with dissolve

    li "And right now, he's hurting you. Hurting you mentally, emotionally and well... Now, physically."

    scene v12cn5a
    with dissolve

    no "*Crying* It's not that simple Lindsey..."
    no "Chris and I have been together forever. *Crying* We've spent most of our lives with each other."

    scene v12cn5d # FPP Same angle as v12cn5, Nora looking at Lindsey, mouth open (back of her head visible to MC)
    with dissolve

    no "The bad stuff is all you see but, there's a lot of good under the surface. Chris isn't a bad guy, he's just not being a good boyfriend. *Sobs*"

    scene v12cn5c
    with dissolve

    li "*Sighs* I don't see how you can just let the past blind you from the present."

    scene v12cn5d
    with dissolve

    no "*Crying* I get you're trying to help me, but blaming Chris for everything isn't helping."

    scene v12cn5a
    with dissolve

    no "It makes sense for him to want to spend time with his friends, just like I did the other day. I may have acted a bit selfish, and I..."
    no "I probably shouldn't have done all that in public. Fuck! *Sobs*"

    scene v12cn5c
    with dissolve

    li "I'm a girl, so I'm not going to sit here and act like I understand a guy's perspective, but I feel like most people in this situation could work through it without pushing you to the ground."
    li "Ask [name], he's a guy."

    scene v12cn5e # FPP Same angle as v12cn5, Nora looking at MC, tears on her face, mouth open
    with dissolve

    no "*Crying* Am I in the wrong, [name]? If you were in the same position as Chris, what would you do?"

    scene v12cn5f # FPP Same angle as v12cn5, Nora and Lindsey looking at MC, both mouths closed
    with dissolve

    menu:
        "Support Nora":
            $ nora.points += 1

            u "I'll be honest, I have nothing against Chris as a person. But since we've been in Europe, I've gotten to see into your relationship a bit more, and it makes me look at him a little differently."
            u "A man should never put his hands on his woman, no excuses."

            scene v12cn5
            with dissolve

            u "A man should be putting his woman above all else and she should be able to feel it."
            u "So if she's asking for more attention, then that's what you need to give her, 'cause somehow you're not giving her enough."

            scene v12cn5c
            with dissolve

            li "And that's... A man."

            scene v12cn4a # TPP Same angle as v12cn4, Nora leans over, wraps her arms around MC's waist, and puts her head in his lap. MC looks shocked, Nora is crying
            with dissolve

            no "*Crying*"

            scene v12cn4b # TPP Same angle as v12cn4, Nora's head is in MC's lap and she's crying, MC has one hand on Nora's head, the other is raised in confusion as he looks at Lindsey
            with dissolve

            pause 0.75

            scene v12cn6 # FPP MC looks down at Nora, who has her head in his lap
            with dissolve
            
            u "It's okay to take time to gather your thoughts and emotions but, you can't run in circles forever."

            scene v12cn6a # FPP Same angle as v12cn6, Nora's head is still in MC's lap, but she has turned it to sort of look at him as he talks
            with dissolve

            u "You have to resolve things at some point. I'm not telling what to do, I'd never do that."
            u "but it doesn't seem like Chris is understanding anything you tell him, so I don't see how trying to talk through this is going to help."

            scene v12cn5g # FPP Same angle as v12cn5, Nora out of frame (at least mostly) with her head in MC's lap, Lindsey looking down at her, mouth open
            with dissolve

            li "With most people it does, but Chris is being stubborn. He doesn't even try to see your perspective of things."

            scene v12cn6b # FPP Same angle as v12cn6, Nora's head in MC's lap, looking away. Nora crying with her mouth open
            with dissolve

            no "*Crying* How did I get like this?"

            scene v12cn4c # FPP Same angle as v12cn4, Nora sitting up in between MC and Lindsey, crying with her mouth open
            with dissolve

            no "*Crying* Like the girls from the movies who cry over the way some stupid jock is treating them..."

            scene v12cn5c
            with dissolve

            li "Nora, you know I love you, so everything I'm saying is coming from a good place. You wound up here because you let Chris run all over you, and that was clear when he left you at the church."
            li "We all felt horrible for you. The reason you're so bold and have this guard up towards everyone else is because you take so much shit from him, you can't stand to take it from anyone else."

            scene v12cn5h # FPP Same angle as v12cn5, Nora is wiping the tears from her eyes, mouth open
            with dissolve

            no "So, you guys feel like what I did was justified?"

            scene v12cn5i # FPP Same angle as v12cn5, Lindsey looking at Nora with a slight smile, mouth open
            with dissolve

            li "I would've done a lot more than what you did. *Chuckles* And probably a lot sooner. You've put up with way too much shit."

            scene v12cn5j # FPP Same angle as v12cn5, Nora looking down but more composed, Lindsey looking at Nora, both mouths closed
            with dissolve

            u "I think you were right to be upset, what you've been asking for is more than reasonable."

        "Support Chris":
            $ reputation.add_point(RepComponent.BRO)

            u "I try to play the safe zone, so I'm not gonna point fingers at anyone. I will say this though, nothing you're asking of him is unreasonable and nothing he's doing is unreasonable."

            scene v12cn5
            with dissolve

            u "It's very clear that Chris cares about you, you just pointed out how much he does. I genuinely believe Chris is just busy right now."
            u "If you want your relationship to work out I think you just accept what time he is able to give you, so he can invest in what he has planned for the future."

            scene v12cn5f
            with dissolve

            u "When it's all over you'll have him to yourself."

            scene v12cn5k # FPP Same angle as v12cn5, Nora looking down and crying, Lindsey looking at MC with an angry expression, mouth open
            with dissolve

            li "Good speech, [name], but I still think that's bullshit. Why should she have to wait around while he does what he wants to do?"

            scene v12cn5f
            with dissolve

            u "We all make sacrifices for those we love, and correct me if I'm wrong, but I'm pretty sure he's doing all of this with yours and his future in mind."

            scene v12cn5h
            with dissolve

            no "Yes, he wants to work hard as frat President because the frat alumni have promised him a career, as long as he continues to fulfill his responsibilities."

            scene v12cn5j
            with dissolve

            u "See? So, just try to let him do what he needs to do. It may not be pretty right now, but this is the necessary road, right?"
            u "You two love each other, no matter what. At the end of the day that's always a fact."

            scene v12cn5l # FPP Same angle as v12cn5, Nora has her face in her hands
            with dissolve

            no "*Sighs* I shouldn't have let my emotions get the best of me. I'm such an idiot."

            scene v12cn5m # FPP Same angle as v12cn5, Nora has her face in her hands, Lindsey is looking at Nora, angry with her mouth open
            with dissolve

            li "What!? This is ridiculous! You're seriously blaming yourself when the guy literally just pushed you to the floor?"

            scene v12cn5l
            with dissolve

            no "I hit him first, Lindsey. It's true. I also said some things that I knew would aggravate him. I went too far..."

            scene v12cn5m
            with dissolve

            li "Classic victim blaming, I'll never understand it."

            scene v12cn5d
            with dissolve

            no "I'm sorry, but I'm not going to act like what I did was okay."

            scene v12cn5b
            with dissolve

            li "I would've done a lot worse and a lot sooner. I would've done something back at the church when he left you at the altar for a PHONE CALL."

    scene v12cn7 # TPP Show Nora standing up from the bed, wiping the tears from her eyes, mouth open
    with dissolve

    no "Look guys, I appreciate everything, I really do. I'm pretty sure I know how I'm gonna move forward with this situation."

    scene v12cn7a # TPP Same angle as v12cn7, MC and Lindsey also standing up, Nora's looking at Lindsey, mouth open
    with dissolve

    no "You guys think you could give me some time alone? I need to think."

    scene v12cn8 # FPP View of Nora and Lindsey, both standing with mouths closed. Lindsey looking at Nora, Nora looking at MC
    with dissolve

    u "Of course."

    scene v12cn8a # FPP Same angle as v12cn8, Nora looking at Lindsey, Lindsey with mouth open
    with dissolve

    li "For now I will, but I'll be checking up on you later."

    scene v12cn8b # FPP Same angle as v12cn8, Lindsey with mouth closed, Nora with slight smile, mouth open
    with dissolve

    no "*Chuckles* Thanks guys."

    scene v12cn9 # TPP Show MC leaving Nora's room, with Lindsey close behind
    with dissolve

    pause 0.5

    scene v12cn10 # TPP Show MC walking into the hotel lobby
    with dissolve

    pause 0.5

    stop music fadeout 3

    if mc.frat == Frat.WOLVES:
        jump v12s27 # scene 27
    else:
        jump v12s27a