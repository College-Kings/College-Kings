# SCENE 5: WED MORNING WAKING UP IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (wearing the same pair of underwear as in scene 1 and 2)
# Time: Wednesday early morning

label v9_dream_wakeup:
    if joinwolves:
        scene v9dream20 # TPP (maybe from above). MC in his room in Wolves house waking up from sleep suddenly (his head lifted up from pillow) as if from a bad dream, sweating a bit, eyes wide open, mouth open (not because he's talking but because he's hyperventilating)
        with flash
        u "(What the hell was that? Holy shit!)"

        scene v9dream20a # MC turns to the side with his hand supporting his head, neutral expression, mouth closed
        with dissolve
        u "(God I hate dreams. Most of the time, they're good. But sometimes...they really suck.)"

        $ contact_Riley.newMessage("Hey, [name]. You awake?", queue=False)
        $ contact_Riley.addReply("Hey Riley, yeah I'm up, is everything okay?")
        $ contact_Riley.newMessage("A couple of us wanted to go to the lake. Wanna join us?")
        $ contact_Riley.addReply("I dunno, feeling kind of crappy.")
        $ contact_Riley.newMessage("Oh, c'mon, it's gonna be fun! :)")
        $ contact_Riley.addReply("Who's gonna be there?")
        $ contact_Riley.newMessage("Ryan and Aubrey.")
        $ contact_Riley.addReply("I guess I could go. Could use some fresh air.")
        $ contact_Riley.newMessage("You'll love it! Meet you in 30 minutes?")
        $ contact_Riley.addReply("Yeah, see ya soon.")
        $ contact_Riley.newMessage("See you!")

        play sound "sounds/vibrate.mp3"
        u "(Hmm?)"

        scene v9dream20b # MC lying on bed looking at his phone, neutral expression, mouth closed
        with dissolve

    else:
        scene v9dream23 # TPP. Same as v9dream20 but in MC's room in Apes house
        with flash
        u "(What the hell was that? Holy shit!)"

        scene v9dream23a # Same as v9dream20a but in MC's room in Apes house
        with dissolve
        u "(God I hate dreams. Most of the time, they're good. But sometimes...they really suck.)"

        $ contact_Riley.newMessage("Hey, [name]. You awake?", queue=False)
        $ contact_Riley.addReply("Hey Riley, yeah I'm up, is everything okay?")
        $ contact_Riley.newMessage("A couple of us wanted to go to the lake. Wanna join us?")
        $ contact_Riley.addReply("I dunno, feeling kind of crappy.")
        $ contact_Riley.newMessage("Oh, c'mon, it's gonna be fun! :)")
        $ contact_Riley.addReply("Who's gonna be there?")
        $ contact_Riley.newMessage("Ryan and Aubrey.")
        $ contact_Riley.addReply("I guess I could go. Could use some fresh air.")
        $ contact_Riley.newMessage("You'll love it! Meet you in 30 minutes?")
        $ contact_Riley.addReply("Yeah, see ya soon.")
        $ contact_Riley.newMessage("See you!")

        play sound "sounds/vibrate.mp3"
        u "(Hmm?)"

        scene v9dream23b # Same as v9dream20b but in MC's room in Apes house
        with dissolve

label v9_phn_riley1:
    if contact_Riley.getReplies():
        call screen phone
        u "(I should talk to Riley.)"
        jump v9_phn_riley1

    jump v9_phn_riley1_done


label v9_phn_riley1_done:
    if joinwolves:
        scene v9dream21 # TPP. Show MC sitting on the side of his bed while stretching his arms, looking uncertain, mouth closed
        with dissolve
        u "(I wonder what that dream was all about. Why am I that worried about the stupid Brawl thing?)"

        scene v9dream22 # TPP. (MC out of bed now) Show MC doing a quick right hand jab, looking serious with a determined smile, mouth closed
        with dissolve
        u "(But fuck it, I'm not gonna puss out. I can do this!)"
        u "(Gotta get going if I wanna meet the guys in 30.)"

        scene black
        with Dissolve(1)
        pause 0.5

    else:
        scene v9dream24 # TPP. Same as v9dream21 but in MC's room in Apes house
        with dissolve
        u "(I wonder what that dream was all about. Why am I that worried about the stupid Brawl thing?)"

        scene v9dream25 # TPP. Same as v9dream22 but in MC's room in Apes house
        with dissolve
        u "(But fuck it, I'm not gonna puss out. I can do this!)"
        u "(Gotta get going if I wanna meet the guys in 30.)"

        scene black
        with Dissolve(1)
        pause 0.5

    jump drive_to_lake
