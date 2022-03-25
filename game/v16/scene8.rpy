# SCENE 8: Outside, Chloe is crying on a bench surrounded by a few people
# Locations: Park Bench just outside of the School
# Characters: MC (Outfit: 5), CHLOE (Outfit: 2), LINDSEY (Outfit: 3)
# Time: Morning
# Render Count: 11 Unique Renders 49

label v16s8:
    scene v16s8_1 # TPP. MC walks outside. He sees Chloe sitting on a bench, crying. There is an empty seat next to her, but A few people, Random Characters, (2 Males, 1 Female) are standing around her the female is standing closest to Chloe, making sure she's okay, all of them with concerned/worried expressions on their faces.
    with dissolve

    menu:
        "Play along":
            scene v16s8_2 # FPP. Show Chloe in the same position and people around her from v16s8_1, Mc has gotten closer to them
            with dissolve

            u "(Wow, she's good at acting, haha. I'd better play along for now...)"

            scene v16s8_3 # TPP. Show MC sitting next to Chloe no expression, mouth is closed, looking at Chloe, Chloe is looking at MC tears in her eyes, mouth closed, looking at MC, The other Random Characters have given MC space to sit down, but are still there
            with dissolve

            pause 0.75

            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v16s8_4 # FPP. Show just Chloe looking at MC, tears in her eyes, sad expression, mouth is closed, looking at MC
                with dissolve

                u "Hey..."

                scene v16s8_3a # TPP. He pulls Chloe in for a hug as she sobs, Chloe is still crying, mouth is closed, MC no expression, mouth is closed, Other Random Characters still present looking at them
                with dissolve

                pause 0.75

                scene v16s8_4a # FPP. Show Chloe slight smile, tears still in her eyes, mouth is open
                with dissolve

                cl "I'm so happy to see you..."

            else:
                scene v16s8_4
                with dissolve

                u "Hey, Chloe... how are you doing?"

                scene v16s8_4b # FPP. Show Chloe no expression, tears still in her eyes, mouth is open
                with dissolve

                cl "I've been better... *Sniffles*"

            scene v16s8_4c # FPP. Show Chloe no expression, tears still in her eyes, mouth is closed
            with dissolve

            u "I can't believe Lindsey said those things about you."

            scene v16s8_4b
            with dissolve

            cl "I can't either, [name]. *Sobs* It's so awful."

            scene v16s8_4c
            with dissolve

            u "It's definitely not the best behavior for a presidential candidate."

            scene v16s8_3b # TPP. The 2 Male Random Characters lean into listen to them better, MC is looking at the Male Characters strangely, The Female Random character holds Chloe's hand in solidarity, Chloe looks at the Random Female Character
            with dissolve

            pause 0.75

            scene v16s8_3c # TPP. Chloe looks back towards MC, tears still in her eyes, mouth is still closed, Mc looks at Chloe, no expression, mouth is closed, The Random Characters all look at each other with concerned/worried expressions
            with dissolve

            pause 0.75

        "Just listen for now":
            scene v16s8_4d # FPP. Chloe has a sad expression, tears still in her eyes, mouth is open, looking at MC
            with dissolve

            cl "I can't believe she said those things about me. It's so... disappointing. *Sobbing*"

            cl "I'm just trying my best, you know? I do everything I can for the Chick's, and this..."

            scene v16s8_4e # FPP. Chloe starts crying again holding her hands to her face
            with dissolve

            cl "I've never been bullied before. I guess this is what it feels like. *Cries*"

    if not v15_lindsey_recording == 6:
        scene v16s8_4d
        with dissolve

        cl "It's not my fault I was born with such huge boobs. They're not even fake! They're completely natural!"

        if chloe.relationship >= Relationship.GIRLFRIEND:
            scene v16s8_4c
            with dissolve

            u "I know..."

            scene v16s8_4f # FPP. Chloe raises an eyebrow at MC, and a "suspicious expression," mouth is still closed
            with dissolve

            pause 0.75

            scene v16s8_4g # FPP. Chloe gives MC a "don't you dare look," mouth is still closed
            with dissolve

            u "I mean, I can... I've felt... Nevermind."

        scene v16s8_3d # TPP. Chloe still looks sad mouth is closed, MC Chloe Random Female and Random Guy 2 look at Random Guy 1 all of their mouths are closed no expressions, Random Guy 1's mouth is open and he has a slight smile
        with dissolve

        rg1 "Ignore Lindsey! We love your boobs!"

        scene v16s8_4h # FPP Show Chloe no expression, no tears in her eyes, mouth is closed
        with dissolve

        u "*Sighs* What he said."

        scene v16s8_4i # FPP. Chloe has a disgusted expression on her face, mouth is open, looking at MC
        with dissolve

        cl "*Scoffs*"

    scene v16s8_4h
    with dissolve

    u "Just ignore her. You need to stay strong."

    if not v15_lindsey_recording == 6:
        scene v16s8_3e # TPP. same as v16s8_3c Random Guy 2's mouth is open slight smile looking at Chloe, and everyone is looking at him
        with dissolve

        rg2 "That's right Chloe! We believe in you!"

        scene v16s8_3c
        with dissolve

        rg1 "You and your non-fake tits!"

        scene v16s8_3f # TPP. same as v16s8_3c Everyone has a disgusted expression on their face looking at Random Guy 1, Random Guy 2 has a "what did I do?" look on his face
        with dissolve

        u "(Who the hell are these people?)"
        
    scene v16s8_3g # TPP. Everyone looks a little surprised and sees Lindsey approaching with an angry face, straight up to Chloe
    with dissolve

    li "What the fuck, Chloe?! How the hell did you get that recording?"

    scene v16s8_3h # TPP. Chloe stands up from the bench, Chloe and Lindsey have angry expressions looking at each other, mouths are closed, MC also stands up from the bench, MC and the others have stepped back from Chloe and Lindsey slightly shocked expressions looking at Chloe and Lindsey
    with dissolve

    pause 0.75

    scene v16s8_5 # FPP. Show just Chloe and Lindsey, full body images, looking at each other with angry expressions, Chloe's mouth is open, Lindsey's mouth is closed
    with dissolve

    cl "Are you serious right now? You're coming to kick me while I'm down?"

    cl "I have no idea who recorded you, but at least now everyone knows what kind of person you are."

    scene v16s8_5a # FPP Lindsey steps closer to Chloe, Lindsey's anger intensifies, both of their mouths are closed Chloe still has an angry expression
    with dissolve

    pause 0.75

    scene v16s8_5b # FPP same v16s8_5a Chloe's mouth is closed, Lindsey's mouth is open
    with dissolve

    li "That's bullshit! You're such a fucking liar!"

    li "You're the only person who has anything to gain by broadcasting something that makes me sound like a bitch."

    scene v16s8_3i # TPP. same as v16s8_3h Lindsey is standing closer to Chloe, looking at MC and the random characters, her mouth is open, still an angry expression
    with dissolve

    li "And for everyone's information-"

    li "I was drunk and talking shit, sue me! I didn't mean anything by it, and I definitely never intended for the entire campus to get involved."

    scene v16s8_5c # FPP. same as v16s8_5b Chloe's mouth is open, Lindsey's mouth is closed
    with dissolve

    cl "You-"

    scene v16s8_5d # FPP. Lindsey is now face to face with Chloe raising a finger in Chloe's Face, Lindsey has a fully Angry Expression, Chloe has a fully angry expression, Lindsey's mouth is open, Chloe's mouth is closed
    with dissolve

    li "And for your fucking information, Chloe, I said a lot of nice things about you that night. It's kinda funny how none of that made the tape, huh?"

    scene v16s8_5d
    with dissolve

    menu:
        "Stop the argument":
            scene v16s8_6 # TPP. Show MC from the back, MC steps between Chloe and Lindsey render can look like v16s8_5 just with MC stepping between them
            with dissolve

            pause 0.75

            scene v16s8_6
            with dissolve

            u "Lindsey. Chloe. Both of you need to stop."

            scene v16s8_7 # FPP. Show Chloe with an angry expression looking at MC, mouth is open
            with dissolve

            cl "No, she needs to stop!"

            scene v16s8_7a #FPP. Show Chloe with an angry expression looking at MC, mouth is closed
            with dissolve

            u "This isn't a good look for either of you."

            scene v16s8_8 # FPP. Show Lindsey with an angry expression looking at MC, mouth is open
            with dissolve

            li "You're telling me?! She's the one who went public with this!"

            scene v16s8_8a # FPP. Show Lindsey with an angry expression looking at MC, mouth is closed
            with dissolve

            u "Seriously guys, calm down before this gets ugly."

            scene v16s8_7
            with dissolve

            cl "I don't think she could get any uglier."

            scene v16s8_6a # TPP. same as v16s8_6 Lindsey Archs back her arm like she's going to hit Chloe looking at Chloe, Chloe has a shocked expression looking at Lindsey, MC stands with his back towards Chloe and facing Lindsey getting in the way of Lindsey hitting Chloe, angry expression, mouth is closed, attempting to grab Lindsey's arm
            with dissolve

            li "*Gasps* You bitch!"

            scene v16s8_6b # TPP. same as v16s8_6a Mr. Lee is now standing behind Chloe and MC with his arms crossed looking at Lindsey, no expression, mouth is closed, Lindsey has stopped trying to hit Chloe and has lowered both her arms to here sides she has a shocked expression as she looks at Mr. Lee., MC's hands are now at his side, Chloe and MC are looking at Lindsey with no expressions, mouths are closed.
            with dissolve

            pause 0.75

            scene v16s8_6c # TPP. same as v16s8_6b MC and Chloe turn around and see Mr. Lee they both have a slightly shocked expression looking at Mr. Lee, Lindsey is still in the same position as v16s8_6b but she has no expression, Mr. Lee is looking at Chloe, no expression, mouth is closed, arms are still crossed
            with dissolve

            pause 0.75

            scene v16s8_6d # TPP. same as v16s8_6c Mr. Lee has a slight smile mouth is open looking at MC, Chloe, MC, and Lindsey all have no expressions, mouths closed all looking at Mr. Lee
            with dissolve

            lee "You're starting to take after your old Mr. Lee, [name]. I'm proud."

            scene v16s8_6d
            with dissolve

            u "(Oh, shit. Where did he come from?)"

        "Let it continue":
            scene v16s8_5e # FPP. same as v16s8_5d Chloe now has her finger in Lindsey's face and Lindsey has lowered finger
            with dissolve

            cl "You're a spiteful, two-faced whore Lindsey. I don't believe a single word that comes out of your mouth anymore."

            scene v16s8_5d
            with dissolve

            li "And you're a scheming psychopath! You've got no respect for my privacy or for me as a person in general."

            scene v16s8_5b
            with dissolve

            li "I mean what kind of low-life records people like that? When they're defenseless?"

            scene v16s8_5c
            with dissolve

            u "(Easy now... I'm not that low in life.)"

            scene v16s8_5e
            with dissolve

            cl "You need to get the fuck out of my face right now."

            scene v16s8_5b
            with dissolve

            li "I'm not walking away until you apologize."

            scene v16s8_5f # FPP. Chloe angrily laughs at Lindsey
            with dissolve

            cl "HA! Me?! Apologize? Are you fucking crazy?"

            scene v16s8_5c
            with dissolve

            cl "Everyone just heard what you've been saying about me. I'm the one who deserves an apology."

            scene v16s8_5d
            with dissolve

            li "Fuck that and fuck you! I don't owe you shit."

            scene v16s8_5g # FPP. Lindsey Archs back her arm like she's going to hit Chloe looking at Chloe, Lindsey has a fully angry expression, Chloe has a shocked expression looking at Lindsey
            with dissolve

            pause 0.75

            scene v16s8_5h # FPP. same as v16s8_5g Mr. Lee is now standing behind Chloe with his arms crossed looking at Lindsey, no expression, mouth is closed, Lindsey has stopped trying to hit Chloe and has lowered both her arms to here sides she has a shocked expression as she looks at Mr. Lee., Chloe has a concenred expression looking at Lindsey
            with dissolve
        
            pause 0.75

            scene v16s8_5i # FPP. Chloe turns around and sees Mr. Lee, Chloe has a slightly shocked expression looking at Mr. Lee, Mr. Lee is looking at Chloe, no expression, mouth is closed, arms are still crossed, Lindsey still has the same expression and posture from render v16s8_5h
            with dissolve

            pause 0.75

            scene v16s8_5j # FPP. Chloe and Lindsey both have no expressions looking at Mr. Lee mouths are closed, Mr. Lee is looking at both of them, no expression, mouth is open
            with dissolve

            lee "Let's break it up, girls. In a few months you'll be painting each other's toenails again."
        
            scene v16s8_5k # FPP. Chloe and Lindsey look at each other disgustingly, Mr. Lee rolls his eyes
            with dissolve

            pause 0.75

            scene v16s8_5k
            with dissolve

            u "(Oh, shit. Where did he come from?)"

    scene v16s8_9 # FPP. Show just the top halves of Mr. Lee, Chloe and Lindsey, Mr. Lee is looking at Chloe and Lindsey no expression, mouth is open. Chloe and Lindsey are looking at Mr. Lee no expressions mouths are closed. Chloe and Lindsey are standing next to each other
    with dissolve

    lee "Ladies, this is not the type of behavior I expect from two presidential candidates."

    scene v16s8_9a # FPP. same as v16s8_9 Chloe's mouth is open, Mr. Lee's mouth is closed
    with dissolve

    cl "Mr. Lee, you have to listen-"

    scene v16s8_9
    with dissolve

    lee "Enough. Please, both of you come with me."

    scene v16s8_9b # FPP. same as v16s8_9 Lindsey's mouth is open, Mr. Lee's mouth is closed
    with dissolve

    li "But Mr. Lee, she's the one who-"

    scene v16s8_9
    with dissolve

    lee "Lindsey, please. We will discuss this in my office."

    scene v16s8_10 # TPP. Mr. Lee walks away with Chloe and Lindsey following no expression his mouth is closed. Chloe and Lindsey look at each other with concerned expressions their mouths are closed, MC watches them go, no expression mouth is closed.
    with dissolve

    pause 0.75

    scene v16s8_11 # TPP. Show just MC sitting on the bench no expression mouth is closed as the random characters from renders v16s8_3 walk away from MC talking with each other, all slightly shocked expressions
    with dissolve

    u "(Damn, I can't tell if that was a win or a loss for Chloe. Either way, I'm in the clear, I think. Time to get to class.)"

    scene v16s8_11a # TPP. Show just MC standing up and walking away, no expression, mouth is clsoed, the other random characters are already gone.
    with dissolve

    pause 0.75

    jump v16s9 # -Transition to Scene 9-