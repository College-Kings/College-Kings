# SCENE 34: Convincing Elijah with Chloe
# Locations: Campus hallway, SVC Times office
# Characters: CHLOE (Outfit: 3), MC (Outfit: 9), ELIJAH (Outfit: x)
# Time: Wednesday

label v16s34: # 34) Talk to Elijah about the cover with Chloe
    scene v16s34_1 # TPP Show MC walking along the school hallway
    with dissolve
    
    pause 0.75

    scene v16s34_2 # FPP Show Chloe (slight smile, mouth open) waiting by a classroom door. Door has a piece of paper that says "SVC Times. KNOCK BEFORE ENTERING"
    with dissolve

    cl "You were quick!"

    scene v16s34_3 # FPP Show Chloe (slight smile, mouth closed) now closer, looking at MC
    with dissolve

    u "When you say jump, I say \"how high?\"."

    scene v16s34_3a # FPP Same angle as 3, Chloe (slight smile, mouth open) looking at MC
    with dissolve

    cl "*Chuckles* Whatever that means."

    scene v16s34_3b # FPP Same angle as 3, Chloe (slight smile, mouth open) looking at the door
    with dissolve

    cl "Let's go in."

    scene v16s34_4 # FPP Show the sign on the door
    with dissolve

    u "It says to knock before entering."

    scene v16s34_3b
    with dissolve

    cl "That's just a stupid sign."

    scene v16s34_3
    with dissolve

    u "If Elijah put it there, wouldn't he want his rules followed?"

    menu:
        "Knock":
            $ v16s34_knock_on_svc_door = True

            play sound "sounds/knock.mp3"

            scene v16s34_5 # FPP Show MC's hand knocking on the door
            with dissolve

            pause 0.75

            scene v16s34_4
            with dissolve

            el "*Muffled* Come in!"

            scene v16s34_3b
            with dissolve

            cl "Yes, your majesty..."

            scene v16s34_3c # FPP Same angle as 3, Chloe (slight smile, mouth closed) looking at the door
            with dissolve

            u "*Chuckles*"

        "Just walk in":
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s34_3c
            with dissolve

            u "Ah, who the fuck cares."

            scene v16s34_3b
            with dissolve

            cl "Exactly. Acting like he's the Dean..."

    scene v16s34_6 # TPP Show door into the office opening, MC holding the door, Chloe entering first with MC right behind her
    with dissolve

    pause 0.75

    # -Elijah is sitting at a desk at a computer (no, don't waste time showing me the computer screen), SVC Times sign is hanging somewhere in the room, 
    # there should be a small nook for Riley in there so it's not a tiny room, its like the newspaper headquarters but he has the largest area. 
    # Think like Michael Scott Paper Company, but a bit bigger. It's obvious that Elijah has taken the time to stock the room business-appropriately-

    scene v16s34_7 # FPP Show Elijah (neutral expression, mouth closed) turning his chair to look at MC and Chloe
    with dissolve

    pause 0.75

    if v16s34_knock_on_svc_door: # IF Knock
        scene v16s34_7a # FPP Same angle as 7, Elijah (slight smile, mouth open) looking at MC
        with dissolve

        el "Thanks for respecting the editor and knocking first. You wouldn't believe the number of idiots that just barge in here."

        scene v16s34_7b # FPP Same angle as 7, Elijah (slight smile, mouth closed) looking at MC
        with dissolve

        u "Civilized people know how to knock before entering a room."

        scene v16s34_7a
        with dissolve

        el "My sentiments exactly!"

        scene v16s34_8 # FPP Show Chloe (rolling her eyes, mouth closed) not looking at MC or Elijah
        with dissolve

        pause 0.75

    else: # IF Just walk in
        scene v16s34_7c # FPP Same angle as 7, Elijah (angry expression, mouth open) looking at MC
        with dissolve

        el "You- Seriously?!"

        scene v16s34_7d # FPP Same angle as 7, Elijah (angry expression, mouth open) looking at MC, but holding his hound out toward the door
        with dissolve

        el "What's the point of putting a sign up if everyone's just going to ignore it?"

        scene v16s34_7e # FPP Same angle as 7, Elijah (angry expression, mouth closed) looking at MC
        with dissolve

        u "What's the matter? Worried we'd catch you jerking off? *Laughs*"

        scene v16s34_7c
        with dissolve

        el "That's not the point, [name]! I've created a protocol here and want it to be followed."

        scene v16s34_7e
        with dissolve

        u "So, you do jerk off in here?"

        scene v16s34_7c
        with dissolve

        el "No!"

        scene v16s34_8a # FPP Same angle as 7, Chloe (slight smile, mouth open) looking at Elijah
        with dissolve

        cl "Sorry, Elijah. We'll make sure it doesn't happen again."

        scene v16s34_7c
        with dissolve

        el "*Sighs* Yes, please do."

        scene v16s34_7f # FPP Same angle as 7, Elijah (neutral expression, mouth open) looking at Chloe
        with dissolve

        el "Sorry for raising my voice, Chloe."

        scene v16s34_8a
        with dissolve

        cl "Oh, it's okay. Don't worry about it."

        scene v16s34_7
        with dissolve

        u "(I bet he jerks off in here.)"

    scene v16s34_7f
    with dissolve

    el "So how can I help you?"

    scene v16s34_8a
    with dissolve

    cl "Right, well... As you know, I'm deep into my presidential campaign right now."

    scene v16s34_7f
    with dissolve

    el "Indeed. I can tell that you and Lindsey are both very committed to being the President of the Chicks."

    scene v16s34_8a
    with dissolve

    cl "Right... I certainly am committed. I just need some help proving to SVC that I'm the most loyal and responsible candidate."

    scene v16s34_7f
    with dissolve

    el "Okay, and?"

    scene v16s34_8a
    with dissolve

    cl "And... With the current hype about the SVC Newspaper, I can tell that your first edition is going to be a major hit."

    scene v16s34_7g # FPP Same angle as 7, Elijah (smiling, mouth open) looking at Chloe
    with dissolve

    el "Oh, why thank you. I'm glad to hear that the student body is reacting well to the idea."

    scene v16s34_8a
    with dissolve

    cl "Oh, for sure."

    menu:
        "Joke about Elijah":
            $ add_point(KCT.TROUBLEMAKER)
            $ v16s34_joke_about_elijah = True
            
            scene v16s34_7
            with dissolve

            u "It is kind of surprising... Everyone liking something that Elijah did? *Laughs*"

            scene v16s34_8b # FPP Same angle as 7, Chloe (neutral expression, mouth closed) looking at MC
            with dissolve

            u "Did we wake up in a parallel universe?"

            scene v16s34_8c # FPP Same angle as 7, Chloe (neutral expression, mouth open) looking at MC
            with dissolve

            cl "[name], no jokes today please."
            
            scene v16s34_8a
            with dissolve
            
            cl "Seriously, this is a cool thing you're doing."

            scene v16s34_7f
            with dissolve

            el "Thank you, Chloe."

            scene v16s34_7c
            with dissolve
            
            el "Fuck you, [name]."

            scene v16s34_7
            with dissolve

            u "Cheers."

            scene v16s34_8c
            with dissolve

            cl "Moving on..."

        "Compliment the idea":
            $ add_point(KCT.BOYFRIEND)

            scene v16s34_7b
            with dissolve

            u "It's true, a lot of people are intrigued by the idea of a school newspaper. Seriously, good idea."

            scene v16s34_7a
            with dissolve

            el "Oh, uh... Thanks. I'm excited to get started on it."

            scene v16s34_8a
            with dissolve

            cl "So, with that being said..."

    scene v16s34_7
    with dissolve

    cl "I would love it if you'd consider my help with the cover for the first edition."

    scene v16s34_7f
    with dissolve

    el "You want to design the cover?"

    scene v16s34_8a
    with dissolve

    cl "With your help, of course. But yeah, this is the perfect opportunity to create a front cover that'll help me win this thing."

    scene v16s34_7h # FPP Same angle as 7, Elijah (hand on his chin, thinking, mouth open) looking at Chloe
    with dissolve

    el "That's a very interesting idea..."

    scene v16s34_7f
    with dissolve

    el "So, you effectively want free reign on the design of the front cover?"

    scene v16s34_7i # FPP Same angle as 7, Elijah (neutral expression, mouth closed) looking at MC
    with dissolve

    u "Pretty much, yes."

    play sound "sounds/vibrate.mp3"

    scene v16s34_9 # FPP Chloe (neutral expression, mouth open) looking down at her phone, in her hand
    with dissolve

    cl "Oh, I really need to take this. I'll just be a minute. Sorry."

    scene v16s34_10 # FPP Show Chloe exiting the office
    with dissolve

    pause 0.75

    scene v16s34_7i
    with dissolve

    u "So, what do you think?"

    scene v16s34_7a
    with dissolve

    el "It sounds like a brilliant idea for Chloe's campaign, but what's in it for me?"

    scene v16s34_7b
    with dissolve

    u "When Chloe wins, you'll feel proud to have helped? Haha."

    scene v16s34_7a
    with dissolve

    el "*Laughs* You think I'll jeopardize the impartiality of my first official paper in its debut issue because I'd feel proud?"

    el "Is that really all you've got?"

    # IF mc did THREE OR MORE OF made fun of Elijah on day one OR Homecoming dance OR in the scene where we meet his mom OR chose Joke About Elijah in this scene
    if v16s34_joke_about_elijah and elijah.relationship <= Relationship.MAKEFUN:
        
        scene v16s34_7j # FPP Same angle as 7, Elijah (neutral expression, mouth open) looking at MC
        with dissolve

        el "We haven't spoken much in the past, [name], but when we do, you always take the opportunity to make fun of me."

        scene v16s34_7i
        with dissolve

        u "It's a little too easy if I'm being honest, man."

        scene v16s34_7a
        with dissolve

        el "Well now the tables have turned."

        scene v16s34_7k # FPP Same angle as 7, Elijah (evil smil, mouth closed) looking at MC
        with dissolve

        u "Have they? *Laughs*"

        scene v16s34_7a
        with dissolve

        el "Here's what's going to happen..."

    scene v16s34_7j
    with dissolve

    el "It seems to me that this is a huge deal for Chloe, and I'd be compromising my journalistic integrity by doing this favor for her."

    scene v16s34_7i
    with dissolve

    u "(Is he speaking English?)"

    scene v16s34_7a
    with dissolve

    el "Which means doing this favor for her will require a large form of payment."

    scene v16s34_7b
    with dissolve

    u "Seriously? You want money? If you're that desperate then I'm sure Chloe can-"

    scene v16s34_7a
    with dissolve

    el "I don't want your money."

    scene v16s34_7b
    with dissolve

    u "What do you want, then?"

    scene v16s34_7l # FPP Same angle as 7, Elijah (embarrassed expression, mouth open) looking down
    with dissolve

    el "Hmm, you see [name]... I'll let you in on an unknown secret. I'm still a virgin."

    scene v16s34_7i
    with dissolve

    u "Ha- *Coughs*"

    scene v16s34_7b
    with dissolve

    u "Um... Alright? (Where the fuck is this going?)"

    scene v16s34_7a
    with dissolve

    el "I want to lose my virginity to the most popular girl at SVC."

    scene v16s34_7b
    with dissolve

    u "(Is he being serious right now?)"

    scene v16s34_7a
    with dissolve

    el "I want Chloe to take my virginity."

    menu:
        "Laugh hysterically":
            scene v16s34_7i
            with dissolve

            u "Pffft, hahaha!"

            scene v16s34_7m # FPP Same angle as 7, Elijah (confused expression, mouth closed) looking at MC
            with dissolve

            u "Haha! You fucking idiot... *Laughs*"

            scene v16s34_7e
            with dissolve

            u "Haha, oh fuck... It hurts..."

            scene v16s34_7c
            with dissolve

            el "Are you done?"

            scene v16s34_7e
            with dissolve

            u "You... *Laughs*"

            u "You're actually serious right now? *Chuckles*"

            scene v16s34_7c
            with dissolve

            el "Of course, I'm serious."

            if chloe.relationship >= Relationship.GIRLFRIEND: # IF ChloeGF
                scene v16s34_7i
                with dissolve

                u "You realize you're asking to fuck my girlfriend?"

                scene v16s34_7j
                with dissolve

                el "I-"

                scene v16s34_7i
                with dissolve

                u "Are you out of your mind, Elijah?"

        "Get aggressive":
            $ v16s34_get_aggressive_with_elijah = True
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s34_7b
            with dissolve

            u "Are you being serious?"

            scene v16s34_7m
            with dissolve

            el "I think you heard me."

            scene v16s34_11 # TPP Show MC (angry expression, mouth open) taking a step toward Elijah with his fists in clenched in front of him
            with dissolve

            u "Have you lost your fucking mind?"

            scene v16s34_7n # FPP Same angle as 7, Elijah (frightened expression, mouth open) leaning back in his chair slightly, looking at MC
            with dissolve

            el "No, I don't think-"

            if chloe.relationship >= Relationship.GIRLFRIEND: # IF ChloeGF
                scene v16s34_7i
                with dissolve

                u "If I didn't have any self-control, I'd shove your head so far up your ass it'd come out of your mouth."

                scene v16s34_7j
                with dissolve

                el "Excuse me?"

                scene v16s34_7i
                with dissolve

                u "I will excuse you. For the way you just spoke about my girlfriend. You're lucky Chloe needs you, you son of a bitch."

    scene v16s34_7j
    with dissolve

    el "At least talk to her about it. See what she thinks?"

    scene v16s34_7i
    with dissolve

    u "You're actually insane."

    scene v16s34_12 # TPP Show MC (neutral expression, mouth closed) exiting the office
    with dissolve

    u "(Wait until Chloe hears what this creepy asshole just said to me...)"


    scene v16s34_13 # FPP Show Chloe (neutral expression, mouth open) in hallway, lower her phone (she's done with the call)
    with dissolve

    pause 0.75

    scene v16s34_13a # FPP Same angle as 13, Chloe (neutral expression, mouth open) now closer, talking to MC (no phone)
    with dissolve

    cl "Did he agree?"

    scene v16s34_13b # FPP Same angle as 13, Chloe (neutral expression, mouth closed) now closer, looking at MC (no phone)
    with dissolve

    u "Not yet."

    scene v16s34_13a
    with dissolve

    cl "What do you mean?"

    if (v16s34_get_aggressive_with_elijah or chloe.relationship >= Relationship.GIRLFRIEND): # IF chose Get Aggressive, or ChloeGF
        scene v16s34_13c # FPP Same angle as 13, Chloe (curious expression, eyebrow raised, mouth open) looking at MC (no phone)
        with dissolve

        cl "And why do you look angry?"

    scene v16s34_13b
    with dissolve

    u "*Sighs* In return for giving us the cover, he wants..."

    scene v16s34_13d # FPP Same angle as 13, Chloe (annoyed/impatient expression, mouth closed) looking at MC (no phone)
    with dissolve

    u "Well... He-"

    scene v16s34_13a
    with dissolve

    cl "Fucking hell. Spit it out, [name]. Please!"

    scene v16s34_13b
    with dissolve

    u "He wants to have sex with you."

    scene v16s34_13e # FPP Same angle as 13, Chloe (shocked, a little angry, mouth open) looking at MC (no phone)
    with dissolve

    cl "What the-"

    scene v16s34_13d
    with dissolve

    u "(I'm about to witness a murder.)"

    scene v16s34_13f # FPP Same angle as 13, Chloe (smiling, mouth open) looking at MC (no phone)
    with dissolve

    cl "*Laughs*"

    scene v16s34_13g # FPP Same angle as 13, Chloe (smiling, mouth closed) looking at MC (no phone)
    with dissolve

    u "Ha... Ha... (We're laughing?)"

    scene v16s34_13f
    with dissolve

    cl "Oh my God... Haha! *Whispers* That's so gross!"

    scene v16s34_13g
    with dissolve

    u "Uh, beyond gross."

    scene v16s34_13f
    with dissolve

    cl "I hope you went easy on him. *Giggles*"

    if v16s34_get_aggressive_with_elijah: # IF chose Get Aggressive
        scene v16s34_13g
        with dissolve

        u "I managed to control myself... Yes..."

        scene v16s34_13f
        with dissolve

        cl "Hehe, my protective boy."

        scene v16s34_13g
        with dissolve

        u "But I may have threatened him."

        scene v16s34_13f
        with dissolve

        cl "Haha, deserved."

    else: # IF chose Laugh Hysterically
        scene v16s34_13g
        with dissolve
        
        u "I almost pissed myself."

        scene v16s34_13f
        with dissolve

        cl "Haha! I would've too! Holy shit... *Chuckles*"

    scene v16s34_13h # FPP Same angle as 13, Chloe (smiling, eyebrow raised, mouth open) looking at MC (no phone)
    with dissolve

    cl "I could make that twerp cum just by looking at him."

    scene v16s34_13g
    with dissolve

    u "Ha. I wouldn't doubt it, honestly."

    scene v16s34_13a
    with dissolve

    cl "*Sighs* Alright, here's the way I see it. We have two choices."

    scene v16s34_13b
    with dissolve

    u "We do?"

    scene v16s34_13a
    with dissolve

    cl "Yes. Either I offer him a kiss-"

    scene v16s34_13b
    with dissolve

    u "Eww."

    if chloe.relationship >= Relationship.GIRLFRIEND: # IF ChloeGf
        scene v16s34_14 # TPP Show Chloe (slight smile, mouth open) placing her hand on MC's (slightly angry, mouth closed) chest to comfort him
        with dissolve

        cl "A simple, premature cum-inducing, peck."

        scene v16s34_13g
        with dissolve

        u "Right..."

    scene v16s34_13f
    with dissolve

    cl "Or we tell him to go fuck himself."

    scene v16s34_13g
    with dissolve

    u "Easy. I've decided."

    scene v16s34_13f
    with dissolve

    cl "Wait, haha. The second option definitely means no front cover, though. So, seriously... What do you think?"

    menu:
        "It's just a kiss":
            $ add_point(KCT.TROUBLEMAKER)
            $ v16s34_chloe_kiss_elijah_for_frontpage = True

            scene v16s34_13b
            with dissolve

            u "It is just a kiss..."

            scene v16s34_13a
            with dissolve

            cl "It is. Just a... Ugh... Just a kiss."

            scene v16s34_13b
            with dissolve

            u "A small price to pay for what we need."

            scene v16s34_13a
            with dissolve

            cl "Real and true. That's what I needed. *Deep breaths* Okay, let's do this."

        "Tell him to fuck off":
            $ add_point(KCT.BOYFRIEND)

            scene v16s34_13b
            with dissolve

            u "He's lucky we're walking away without breaking one of his bones. Or reporting him to the Dean."

            scene v16s34_13f
            with dissolve

            cl "*Laughs* Or both."

            scene v16s34_13g
            with dissolve

            u "Definitely both. I'm thinking we just tell him to get bent, fuck this guy."

            scene v16s34_13a
            with dissolve

            cl "Yeah, that creepy little prick doesn't even deserve the satisfaction of my lips..."

            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v16s34_13b
                with dissolve

                u "No one does. Except me."

                play sound "sounds/kiss.mp3"

                scene v16s34_15 # TPP Show Chloe giving MC a deep, passionate kiss
                with dissolve

                pause 0.75

                scene v16s34_13g
                with dissolve

                pause 0.75

            scene v16s34_13a
            with dissolve

            cl "Let's do this."

    scene v16s34_6
    with dissolve

    pause 0.75

    scene v16s34_16 # FPP Show Elijah, in his seat, putting on chapstick, not looking at them
    with dissolve

    pause 0.75

    scene v16s34_16a # FPP Same angle as 16, Elijah throwing chapstick into a desk draw and looking at MC and Chloe
    with dissolve

    pause 0.75

    scene v16s34_17 # FPP Elijah (neutral expression, mouth open) now standing (visible from waist up) and looking at Chloe
    with dissolve

    el "So? What's your decision?"

    if v16s34_chloe_kiss_elijah_for_frontpage: # IF It's just a kiss
        scene v16s34_18 # FPP Chloe grabbing Elijah by the face and giving him a kiss on the lips. Elijah's body is stiff, clearly shocked
        with dissolve

        pause 0.75

        scene v16s34_17a # FPP Same angle as 17, Elijah (shocked expression, mouth hanging open wide), body stiff, looking at Chloe. There is a visible wet spot on the front of his pants
        with dissolve

        pause 0.75

        scene v16s34_19 # FPP Chloe (slight smile, mouth open) looking at Elijah
        with dissolve

        cl "There. Pleasure doing business with you, freak."

        scene v16s34_17a
        with dissolve

        el "Oh... Oh, my... That was-"

        scene v16s34_17b # FPP Same angle as 17, Elijah (embarrassed expression, mouth closed) covering his crotch with his hands, looking down, face red with embarrasment, knees clenched together
        with dissolve

        u "Did you just fucking cum in your pants?"

        scene v16s34_19
        with dissolve

        cl "I told you!"

        scene v16s34_19a # FPP Chloe (slight smile, mouth closed) looking at Elijah
        with dissolve

        u "You did."

        scene v16s34_17b
        with dissolve
        
        u "She did."

        scene v16s34_17c # FPP Same angle as 17, Elijah (embarrassed expression, mouth open) still covering his crotch and looking away
        with dissolve

        el "Please, just- Go. Now."

        scene v16s34_19
        with dissolve

        cl "Do I have the front cover?"

        scene v16s34_17c
        with dissolve

        el "Yes! Yes, you do! Please, go!"

        scene v16s34_17b
        with dissolve

        u "Gladly. Clean yourself up, buddy. *Chuckles*"

        scene v16s34_17c
        with dissolve

        el "Shut the door behind you, please."

        scene v16s34_20 # TPP Show MC and Chloe leaving the office, big smiles on both of their faces
        with dissolve

        pause 0.75

    else: # IF Tell him to fuck off
        scene v16s34_17d # FPP Same angle as 17, Elijah (neutral expression, mouth closed) looking at MC
        with dissolve

        u "You can go fuck yourself."

        scene v16s34_17
        with dissolve

        el "Oh, can I now?"

        scene v16s34_19
        with dissolve

        cl "Oh, you can. Quite literally."

        scene v16s34_19b # FPP Same angle as 19, Chloe (slight smile, eyebrow raised, mouth open) leaning back with her arms crossed in front of her chest, looking at Elijah
        with dissolve

        cl "I'm still deciding whether I should tell the Dean about your little request, or if I should just share it with the rest of SVC..."

        scene v16s34_17d
        with dissolve

        u "What kind of creep asks for sex in exchange for a favor? Like, holy shit dude..."

        scene v16s34_17
        with dissolve

        el "Report me? I'm one of the top students here. No one would believe anything that comes out of either one of your mouths."

        scene v16s34_17d
        with dissolve

        u "We'll see about that."

        scene v16s34_19b
        with dissolve

        cl "Oh, we won't, but the backbone of the Chicks will. Good luck hearing from Mr. Rose! Later, pervert."

        scene v16s34_21 # TPP Show MC and Chloe (both smiling, mouths closed) leaving the office, Elijah (nervous expression, mouth open) reaching out for them, yelling
        with dissolve

        el "Wait! Chloe! Don't-"

    scene v16s34_13f
    with dissolve

    cl "*Sighs* Well, now that I can mark that off the list... I have about twenty more things to do before tonight."

    scene v16s34_13g
    with dissolve

    u "Ha, you need a break."

    scene v16s34_13f
    with dissolve

    cl "Way too much to do! I'll catch you later."

    if chloe.relationship >= Relationship.GIRLFRIEND: # IF ChloeGF
        play sound "sounds/kiss.mp3"
        
        scene v16s34_15
        with dissolve

        pause 0.75

        if v16s34_chloe_kiss_elijah_for_frontpage: # IF Chloe kissed Elijah
            scene v16s34_13f
            with dissolve

            cl "There. You're the only one that gets the tongue."

            scene v16s34_13g
            with dissolve

            u "Haha, and for free too? I'm the luckiest guy in town."

            scene v16s34_13f
            with dissolve

            cl "That must make me the luckiest girl."

        scene v16s34_13g
        with dissolve

        pause 0.75

    scene v16s34_22 # FPP Show Chloe walking away down the hall
    with dissolve

    pause 0.75

    scene v16s34_23 # FPP Show MC walking the other direction from Chloe, toward the library
    with dissolve

    u "(I hope I don't walk into any more frat drama when I get home!)"

    jump v16s33 # -Transition to Scene 33-