# SCENE 34: MC calls Penelope
# Locations: Wolves Room/Apes room, Penelope's room.
# Characters: MC (Outfit: 2)
# Time: Night

label v14s34:
    if joinwolves: 
        scene v14s34_1 # TPP. MC sitting on his bed in his wolves room, slight smile, mouth closed.
        with dissolve

        u "(Hmm, I wonder if Penelope would be down for a little date night tonight. I'll give her a call.)"

        play music "music/v13/Track Scene 40_2.mp3" fadein 2

    else:
        scene v14s34_3 # TPP. MC sitting on his bed in his Apes room, slight smile, mouth closed.
        with dissolve

        u "(Hmm, I wonder if Penelope would be down for a little date night tonight. I'll give her a call.)"

        play music "music/v13/Track Scene 40_2.mp3" fadein 2

    $ jenny.messenger.newMessage(_("Hey [name], you busy right now?"), force_send=True)
    $ jenny.messenger.addReply(_("Why, what's up?"))
    $ jenny.messenger.newMessage(_("Well, I've been wanting to swimming in this little lagoon I found."))
    $ jenny.messenger.addReply(_("You're wanting to go now?"))
    $ jenny.messenger.newMessage(_("Yeah, why not? ;) Are you down?"))
    play sound "sounds/vibrate.mp3"

    pause 0.75

    if joinwolves:
        scene v14s33_2a
        with dissolve

    else:
        scene v14s33_4a
        with dissolve

    u "(What the...)"

    label v14s34_PhoneContinue:
        if jenny.messenger.replies:
            call screen phone
        if jenny.messenger.replies:
            u "(I should check my phone.)"
            jump v14s34_PhoneContinue

    u "(Damn, what a timing. I think I will...)"

    menu:
        "Accept Jenny's invite":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)
            $ jenny.messenger.addReply(_("Okay sure, where's this lagoon at?"))
            $ jenny.messenger.newImgMessage("images/v14/Scene 35/v14s35_lagoon_pic.webp") #Picture of the Lagoon, somehow with a location marker in the photo
            $ jenny.messenger.newMessage(_("See you soon!"))

            label v14s34_PhoneContinue2:
                if jenny.messenger.replies:
                    call screen phone
                if jenny.messenger.replies:
                    u "(I should reply to Jenny.)"
                    jump v14s34_PhoneContinue2
        
            stop music fadeout 3
            
            jump v14s35_afterinvite

        "Decline Jenny's invite":
            $ add_point(KCT.BOYFRIEND)
            $ jenny.messenger.addReply(_("Sorry, I was already planning to go out with Penelope tonight."))
            $ jenny.messenger.newMessage(_("Oh!"))
            $ jenny.messenger.newMessage(_("No worries, that's fine. I'm happy for both of you actually!"))
            $ jenny.messenger.newMessage(_("We'll catch up some other day :)"))

            label v14s34_PhoneContinue3:
                if jenny.messenger.replies:
                    call screen phone
                if jenny.messenger.replies:
                    u "(I should reply to Jenny.)"
                    jump v14s34_PhoneContinue3

    if joinwolves:
        scene v14s33_2a
        with dissolve
        
        u "(Luckily she seems to have taken that in good spirits. Now to call Penelope...)"
    
        scene v14s34_2 # TPP. Show MC holding the phone to his ear in his wolves room, slight smile, mouth closed.
        with dissolve
    
    else:
        scene v14s33_4a
        with dissolve
        
        u "(Luckily she seems to have taken that in good spirits. Now to call Penelope...)"
    
        scene v14s34_4 # TPP. Show MC holding the phone to his ear in his Apes room, slight smile, mouth closed.
        with dissolve


    play sound "sounds/calling.mp3"

    pause 0.75

    scene v14s34_5 # TPP. Penelope wearing cute Pajamas, Show a sleepy Penelope holding the phone to her ear. slight tired smile, mouth open.
    with dissolve

    pause 0.75

    stop sound
    play sound "sounds/answercall.mp3"
    pe "H-hello?"

    scene v14s34_5a # TPP. Same as v14s34_5, Penelope slight tired smile, mouth closed.
    with dissolve

    menu:

        "Hey Princess":
            $ add_point(KCT.BOYFRIEND)
            u "Hey, princess. Did I wake you?"

        "Hey Penelope":
            $ add_point(KCT.BRO)
            u "Hey, Penelope. Did I wake you?"

    scene v14s34_6 # TPP. Penelope sitting up in her bed holding the phone to her ear, one of her boobs popping out of her shirt, slight smile, mouth open
    with dissolve

    pe "Nope, not at all..."

    pe "I'm actually wide awake."

    scene v14s34_6a # TPP. Same as v14s34_6, Penelope slight smile, mouth closed.
    with dissolve
    
    u "*Chuckles* Good, because I was thinking we could try going on that date we talked about in London."

    scene v14s34_7 # TPP. Penelope standing up on her bed with the phone to her ear, slight smile, mouth closed.
    with dissolve

    pe "R-Right now?"

    scene v14s34_7a # TPP. Same as v14s34_7, Penelope mid-jump off of her bed holding the phone to her ear, slight smile, mouth closed.
    with dissolve

    u "Yeah, right now. I mean, we're both free so we might as well, right?"

    scene v14s34_8 # TPP. Show most of Penelope's room. Penelope holding the phone to her ear. Penelope looking at her closet in an excited stance, excited smile, mouth open.
    with dissolve

    pe "Well, okay, sure. Um..."

    scene v14s34_8a # TPP. Same as v14s34_8, Penelope's phone sitting on her nightstand on speaker phone, Penelope taking her shirt off, slight smile, mouth open.
    with dissolve

    pe "Where to?"

    scene v14s34_8b # TPP. Same as v14s34_8a, Penelope shirtless with no bra, Penelope taking her pants off, slight smile, mouth closed.
    with dissolve

    u "I thought I'd let you pick."

    scene v14s34_8c # TPP. Same as v14s34_8b, Penelope only in her panties, slight smile, mouth open.
    with dissolve

    pe "How about that really nice place, on Stevenson?"

    scene v14s34_8d # TPP. Same as v14s34_8c, Show Penelope slipping on her v14s37 date dress, slight smile, mouth closed.
    with dissolve

    u "They aren't closed?"

    scene v14s34_9 # TPP. Close up of Penelope in her dress with the phone to her ear again, slight smile, mouth open.
    with dissolve

    pe "Nope! They stay open pretty late."

    scene v14s34_9a # TPP. Same as v14s34_9, Penelope slight smile, mouth closed.
    with dissolve

    u "Sounds like a plan, then. Meet you there in twenty?"

    scene v14s34_9
    with dissolve

    pe "Yes. Sounds perfect."

    scene v14s34_9a
    with dissolve

    u "Alright. Bye."

    scene v14s34_9
    with dissolve

    pe "*Chuckles* Bye."

    play sound "sounds/rejectcall.mp3"

    if joinwolves: 
        scene v14s34_10 # TPP. Show MC standing in his Wolves room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s34_10a # TPP. Same as v14s34_10, Show MC standing in his wolves room wearing nicer clothes for his date with Penelope, slight smile, mouth closed.
        with fade

        pause 0.75

    else: 
        scene v14s34_11 # TPP. Show MC standing in his apes room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s34_11a # TPP. Same as v14s34_11, Show MC standing in his apes room wearing nicer clothes for his date with Penelope, slight smile, mouth closed.
        with fade

        pause 0.75

    scene v14s34_12 # TPP. Show MC outside walking towards the restraunt in his nice clothes, slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s37