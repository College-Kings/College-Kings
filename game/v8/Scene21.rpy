# Talking To The Dean
# Location: MC Apes Room, MC Wolves Room, College, Dean's Office
# Outfits: MC Outfit 3, Scretary Outfit 1, Dean Outfit 1
# Time: Monday Morning
# de = Dean

label mon_morning_room:
    if mc.frat == Frat.WOLVES:
        scene v8sdea1 # TPP. Show MC waking up on his bed in Wolves room.
        with Fade(0.75, 0.25, 0.75)

        u "(I gotta go talk to the dean today about Penelope. I better get ready)"

        play music "music/mindie2.mp3" fadein 2

        scene v8sdea2 # TPP. Show MC getting ready in his Wolves room.
        with dissolve

        pause 1

        jump walk_to_dean

    else:
        scene v8sdea3 # TPP. Show MC waking up on his bed in Apes room.
        with Fade(0.75, 0.25, 0.75)

        u "(I gotta go talk to the dean today about Penelope. I better get ready)"

        play music "music/mindie2.mp3" fadein 2

        scene v8sdea4 # TPP. Show MC getting ready in his Apes room.
        with dissolve

        pause 1

        jump walk_to_dean

    label walk_to_dean:
        scene v8sdea5 # TPP. Show MC walking through the College on his way to the dean's office. MC looking slightly nervous.
        with Fade(0.75, 0.25, 0.75)

        u "(Excuse me, Dean, can I... no, that won't work.)"

        u "(Good morning, Dean. Might I have a minute of your time?)"
        u "(Yeah, that's better.)"

        scene v8sdea6 # FPP. Show MC inside the Dean's office where the dean is talking to her secretary.
        with fade

        u "I gotta show her I'm serious. Ok, here we go."

        scene v8sdea7 # FPP. Now closer to the dean and the secretary, the dean turns to face the camera, dean slight smile, mouth open.
        with dissolve

        de "Good morning."

        scene v8sdea7a # FPP. Same camera as v8sdea7, dean slight smile, mouth closed.
        with dissolve

        u "Good morning Mrs. Harrison. My name is [name]. Might I have a-a minute of your time?"

        scene v8sdea7b # FPP. Same camera as v8sdea7, dean looking at her watch on her wrist, mouth closed.
        with dissolve

        u "(Fuck, I'm nervous.)"

        scene v8sdea7
        with dissolve

        de "I can spare a few minutes. Come on in."

        scene v8sdea8 # TPP. Show the Dean gesturing MC to take a seat at her desk. Dean mouth open.
        with dissolve

        pause 1

        scene v8sdea9 # TPP. Show the Dean now sat at her desk with MC sat opposite her.
        with dissolve

        pause 0.5

        scene v8sdea10 # FPP. Close up dean, neutral expression, mouth open.
        with dissolve

        de "What can I do for you, young man?"

        scene v8sdea10a # FPP. Same camera as v8sdea10, neutral expression, mouth closed.
        with dissolve

        u "Well ma'am, I am here on behalf of a friend who is in a bit of trouble."

        scene v8sdea10
        with dissolve

        de "I see. Does this friend have a name?"

        scene v8sdea10a
        with dissolve

        u "Oh, yes ma'am. Her name is Penelope. I'm sure you know who she is?"

        scene v8sdea10b # FPP Same camera as v8sdea10, slightly concerned expression, mouth open.
        with dissolve

        de "Ah, yes. I believe so. She is definitely in some serious trouble."

        scene v8sdea10a
        with dissolve

        u "Yes ma'am, I'm aware of that."

        scene v8sdea10b
        with dissolve

        de "And you came here to ask if I can drop the charges?"

        scene v8sdea10a
        with dissolve

        u "Well ma'am, that would be great but I know that won't happen. I just came here to..."

        scene v8sdea10c # FPP. Same camera as v8sdea10, dean places her hands on the desk and leans forward slightly, neutral expression, mouth open.
        with dissolve

        de "Let me spare you the effort. We cannot drop the charges, you understand? If we do, how does that make us look? We'd be encouraging that kind of behavior in others..."

        de "And we don't want that, do we?"

        scene v8sdea10a
        with dissolve

        u "No ma'am, not at all, but I would like..."

        scene v8sdea10c
        with dissolve

        de "And quite frankly, I wouldn't want to be on the side of someone who committed such a grievous error in judgment, would you?"

        scene v8sdea10d # FPP. Same camera as v8sdea10, dean places her hands on the desk and leans forward slightly, neutral expression, mouth closed.
        with dissolve

        u "(Fuck this bitch!)"

        scene v8sdea10a
        with dissolve

        u "Ma'am, I am asking you to understand that not everyone is perfect, that we all make mistakes. I am asking that you be lenient with her. She did what she did from a good place. From her heart."

        u "Wouldn't you do stupid things for those you care about...? Ma'am."

        scene v8sdea10e # FPP. Same camera as v8sdea10, slight smile, mouth open.
        with dissolve

        de "You know, you remind me of me back in my time here. Your coming here was ill-advised and I doubt the Disciplinary Committee will change their minds..."

        scene v8sdea10f # FPP. Same camera as v8sdea10, empathetic expression, mouth open.
        with dissolve

        de "However... it takes a special kind of friend and man to put your neck on the line the way you are doing now. I like that. In fact, that's what makes a person a good one."

        de "I will take what you said under advisement and relay my own thoughts on the matter to the Disciplinary Committee. Will that be satisfactory, [name]?"

        scene v8sdea10a
        with dissolve

        u "Yes ma'am. Thank you. I appreciate this."

        scene v8sdea10
        with dissolve

        de "Well, I must be getting on. Lots to do today, and I'm sure you have studying to do?"

        scene v8sdea10a
        with dissolve

        u "Yes ma'am, I do."

        scene v8sdea10
        with dissolve

        de "Well, let's get to it, shall we? Thank you for your candor in this matter."

        scene v8sdea10a
        with dissolve

        u "Thank you for your time ma'am."

        scene v8sdea11 # TPP. Show MC getting up from the deans desk about to leave her office, both mouthes closed.
        with dissolve

        pause 0.5

        scene v8sdea11a # TPP. Same camera as v8sdea11, MC looking at the dean again, dean mouth open.
        with dissolve

        de "Oh, and [name]?"

        scene v8sdea11b # TPP. Same camera as v8sdea11, MC looking at the dean again, MC mouth open, dean mouth closed.
        with dissolve

        u "Ma'am?"

        scene v8sdea11a
        with dissolve

        de "Make sure you tell your friend to stay away from any thought of doing something like this again. You catch my drift?"

        scene v8sdea11b
        with dissolve

        u "Yes ma'am. Completely. Thank you."

        scene v8sdea11a
        with dissolve

        de "Good day, [name]."

        scene v8sdea12 # TPP. Show MC leaning the dean's office, MC smiling.
        with dissolve

        u "(Holy shit, I did it! Now I gotta call Penelope when I get back.)"

        # -Fade to MC back in his room and start of scene 22-
        jump s22