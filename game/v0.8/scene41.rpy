# Walking back w Seb
# Location: Park
# Outfits: MC Outfit 2, Sebastian Outfit 1
# Time: Tuesday Night
# Please be sure to save scenes as v8sbws10 continues from v8sbws1.

label walk_home_hosp:
    if climbwseb:
        scene v8sbws1 # TPP. Show MC and Sebastian walking together next to eachother through the park.
        with fade

        pause 0.5

        scene v8sbws2 # FPP. Show Sebastian looking to his side at camera, sebastian grinning, mouth open.
        with dissolve

        se "I guess we were a little bit too loud, huh?"

        scene v8sbws2a # FPP. Same camera as v8sbws2, Sebastian looking forward, smile, mouth closed.
        with dissolve

        u "I thought a nurse was gonna show up and catch us."

        scene v8sbws2b # FPP. Same camera as v8sbws2, Sebastian turning to look back at camera, neutral expression, mouth open.
        with dissolve

        se "You think she'd really call the cops?"

        scene v8sbws2a
        with dissolve

        u "Nah, I think she was bluffing."

        scene v8sbws2c # FPP. Same camera as v8sbws2, Sebastian turning to look back at camera, laugh, mouth open.
        with dissolve

        se "Good thing we've pulled out the thunder bolt!"

        scene v8sbws2a
        with dissolve

        u "By quickly striking back to the ground?"

        scene v8sbws2c
        with dissolve

        se "Zackly!"

        se "And you were worried about descending... a free fall would be slower than the way you've climbed down!"

        scene v8sbws2a
        with dissolve

        u "Well I guess I've learned a few important lessons tonight..."

        scene v8sbws2b
        with dissolve

        se "Like what?"

        scene v8sbws2d # FPP. Same camera as v8sbws2, Sebastian turning to look back at camera, neutral expression, mouth closed.
        with dissolve

        u "Hanging out with you is fun."

        scene v8sbws2e # FPP. Same camera as v8sbws2, Sebastian turning to look back at camera, smile, mouth open.
        with dissolve

        se "Haha, and?"

        scene v8sbws2b
        with dissolve

        u "And to always carry a spare set of binoculars."

        scene v8sbws2c
        with dissolve

        se "Okay, okay, I don't think we should speak of that failure again."

        scene v8sbws3 # TPP. Show MC and Sebastian walking next to eachother at a different location in the park, both mildly smiling, camera from behind.
        with dissolve

        u "You know..."

        scene v8sbws4 # TPP. Show MC and Sebastian both looking at eachother, MC serious expression, Sebastian curious expression, Sebastian mouth open.
        with dissolve


        se "What is it, [name]?"

        scene v8sbws5 # FPP. Show Sebastian looking at camera (MC), Sebastian neutral expression, mouth closed.
        with dissolve

        u "Joining the Wolves... I was not so sure at first. But it turns out it was a great thing to do."

        scene v8sbws5a # FPP. Same camera as v8sbws5, Sebastian smile, mouth open.
        with dissolve

        se "You can say that again, bro."

        scene v8sbws5b # FPP. Same camera as v8sbws5, Sebastian smile, mouth closed.
        with dissolve

        u "Fun is great, girls are hot, but most of all... This kind of puts the \"brother\" in the \"brotherhood\"."

        scene v8sbws5a
        with dissolve

        se "Nothing breaks a wolf pack, man." #-puts on a mild smile on a serious face, and shows a firm fist while contracting the biceps-

        scene v8sbws5b
        with dissolve

        u "I think we've litteraly reached the peak, so let's stop before the entire talk becomes too... happy, you know what I mean?"

        scene v8sbws5a
        with dissolve

        se "I have an even greater idea!"

        scene v8sbws5b
        with dissolve

        u "Oh, another one? This ought to be good."

        scene v8sbws5c # FPP. Same camera as v8sbws5, Sebastian neutral expression, mouth open.
        with dissolve

        se "Some wolves take pride in their strength and some in being attractive."

        scene v8sbws5
        with dissolve

        u "I know you don't do the latter."

        scene v8sbws5d # FPP. Same camera as v8sbws5, Sebastian laugh, mouth open.
        with dissolve

        se "Shut up, pretty boy! No! I take my pride in one thing."

        scene v8sbws5b
        with dissolve

        u "Yes?"

        scene v8sbws6 # FPP. Show Sebastian beginning to jog infront of MC, turning his head back towards camera, slight laugh, mouth open.
        with dissolve

        se "Last one home is a stinking, dirty ape!"

        scene v8sbws7 # FPP. Show Sebastian now fully sprinting, Sebastian turns back to look at MC, waving middle finger, Sebastian laugh, mouth open.
        with dissolve

        se "And it's not gonna be me!"

        scene v8sbws7a # FPP. Same camera as v8sbws7, Sebastian now turns looking back forward, fully sprinting.
        with dissolve

        u "You think I will fall for such a childish thing?!"

        scene v8sbws8 # TPP. Show MC now running after Sebastian, Sebastian still running in the distance.
        with dissolve

        u "Damn you!!"

        scene v8sbws9 # TPP. Show MC catching up to Sebastian sprinting, Sebastian looking behind him laughing at MC.
        with dissolve

        jump v8_ending

    else:
        scene v8sbws10 # TPP. ! RETURN CHARACTERS TO SAME POSITIONS AS V8SBWS1 ! Show MC and Sebastian, Sebastian walking slightly infront of MC.
        with dissolve

        u "You know..."

        scene v8sbws11a # FPP. Show Sebastian slightly ahead of MC, Sebastian stops and turns behind him to look at camera, Sebastian neutral expression, mouth closed.
        with dissolve

        se "Sup, cub?"

        scene v8sbws11 # FPP. Same camera as v8sbws11, Sebastian neutral expression, mouth open.
        with dissolve

        u "Alright, stop calling me a cub! I wasn't scared, alright?"

        scene v8sbws11a
        with dissolve

        se "Sure."

        scene v8sbws11
        with dissolve

        u "It's just... what's with the stupid roof anyway?"

        scene v8sbws11a
        with dissolve

        se "Someday, you might just find out."

        scene v8sbws12 # TPP. Show Sebastian turning to carry on walking, MC jogs slightly to catch up.
        with dissolve

        pause 0.5

        scene v8sbws13 # FPP. Show Sebastian, camera closer to him as MC now stood closer to him, Sebastian looking at camera, neutral expression, mouth closed.
        with dissolve

        u "I sure hope everything is okay with Marcus' father."

        scene v8sbws13a # FPP. Same camera as v8sbws13, neutral expression, mouth open.
        with dissolve

        se "Yeah..."

        scene v8sbws13
        with dissolve

        u "But no matter what, next time I'm heading up with you."

        scene v8sbws13b # FPP. Same camera as v8sbws13, Sebastian chuckle, mouth open.
        with dissolve

        se "You know, it's just like you said it earlier today. Wolves stick together."

        scene v8sbws13c # FPP. Same camera as v8sbws13, Sebastian smile, mouth open.
        with dissolve

        se "No matter what we did, you did come with me and I appreciate it. That's how Marcus and I do things. That's how all wolves do things."

        scene v8sbws13d # FPP. Same camera as v8sbws13, Sebastian smile, mouth closed.
        with dissolve

        u "I agree."

        scene v8sbws14 # TPP. Show Sebastian and MC fist bumping, both smiling.
        with dissolve

        pause 1

        scene v8sbws13a
        with dissolve

        se "You know, being in the Wolves is much like climbing that hospital."

        scene v8sbws13
        with dissolve

        u "How so?"

        scene v8sbws13c
        with dissolve

        se "First you need to grow some balls and choose to do it. That's how you are getting initiated."

        scene v8sbws13a
        with dissolve

        se "Then you start to fucking climb. And each damn step up is a step towards earning respect and power."

        scene v8sbws13c
        with dissolve

        se "Each next floor is making everyone else looking smaller to you. You grow, dude. Litteraly, above everyone else..."

        scene v8sbws13d
        with dissolve

        u "I get it."

        scene v8sbws13c
        with dissolve

        se "And then the rooftop! As the ultimate prize of them all, it awaits..."

        scene v8sbws13d
        with dissolve

        u "Awaits what?"

        scene v8sbws13b
        with dissolve

        se "Pussy, man, what else!"

        scene v8sbws13d
        with dissolve

        u "There was... pussy on the roof?"

        scene v8sbws13a
        with dissolve

        se "Well, yeah... you could say that."

        scene v8sbws13
        with dissolve

        u "Umm... are you talking about cats?"

        scene v8sbws13b
        with dissolve

        se "I'm not talking about no fucking cats!"

        scene v8sbws13d
        with dissolve

        u "Right, haha..."

        scene v8sbws13c
        with dissolve

        se "I'm talking about real life, live action, smoking hot, tits and all - pussy!"

        scene v8sbws13d
        with dissolve

        u "I'm messing with you, man. But I still don't see what kind of pussy could wait for you on the roof, haha."

        scene v8sbws13a
        with dissolve

        se "And that's why you're still a cub..."

        scene v8sbws13
        with dissolve

        u "Hey!"

        scene v8sbws15 # TPP. Camera from behind, show MC and Sebastian walking into the distance next to eachother, Sebastian turns his head to look at MC. MC looking at Sebastian, both smiles, Sebastian mouth open.
        with dissolve

        se "Anyway, how's your sex life?"

        scene v8sbws15a # TPP. Same camera as v8sbws15, MC mouth open, Sebastian mouth closed.
        with dissolve

        u "Haha, seriously? Well to be honest... That's one crazy story so far."

        jump tue_night_in_room
