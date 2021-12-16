# SCENE 48: Customize Lindsey's online listing
# Locations: Cafe
# Characters: MC (Outfit: 1), LINDSEY (Outfit: 3)
# Time: Evening

label v14s48:
    play music "music/v13/Track Scene 25.mp3" fadein 2
    scene v14s48_1 # TPP. Show MC and Lindsey entering the coffee shop, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v14s48_2 # FPP. MC and Lindsey at the counter, standing next to each other, looking at each other, Lindsey smiling, mouth closed
    with dissolve

    u "*Sniffs* Ahh..."

    scene v14s48_2a # FPP. Same as v14s48_2, Lindsey smiling, mouth open
    with dissolve

    li "Always smells so good in here."

    scene v14s48_3 # TPP. Show the barista arriving with MC and Lindey's coffee, all smiling, mouths closed
    with dissolve

    pause 0.75

    if v14s03a_take_wallet:
        scene v14s48_3a # TPP. Same camera as v14s47_3aShow Lindsey going to hand money to the barista, coffees on the counter, all smiling, mouths closed
        with dissolve

        pause 0.75

        scene v14s48_2
        with dissolve

        u "Oh, don't worry. I got it."

        scene v14s48_3b # TPP. Same as v14s47_3a, MC handing money to the Barista instead
        with dissolve

        pause 0.75

    else:
        scene v14s48_3a
        with dissolve

        pause 0.75

    scene v14s48_4 # TPP. Show MC and Lindsey heading to their table, coffees in hand, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v14s48_5 # TPP. Show MC and Lindsey sitting at their table, next to each other, coffees on the table, both smiling, mouths closed
    with dissolve

    pause 0.75

    if v14s03a_take_wallet and lindsey.relationship.value >= Relationship.FWB.value:
        scene v14s48_5a # TPP. Same as v14s48_5, show Lindsey reaching over and kissing MC on the cheek
        with dissolve

        pause 1.75

        scene v14s48_6 # FPP. MC and Lindsey sitting at the table, looking at each other, Lindsey smiling, holding her coffee, mouth open
        with dissolve

        li "Thank you for the coffee..."

        scene v14s48_6a # FPP. Same as v14s48_6, Lindsey mouth closed
        with dissolve

        u "Of course."

    elif v14s03a_take_wallet:
        scene v14s48_6
        with dissolve

        li "Thanks for the coffee by the way. I should be the one treating you though, don't you think?"

        scene v14s48_6a
        with dissolve

        u "Okay, you can buy it next time."

        scene v14s48_6
        with dissolve

        li "Oooh, next time? *Chuckles*"

        scene v14s48_6a
        with dissolve

        u "*Laughs*"

    else:
        scene v14s48_6a
        with dissolve

        u "Thanks for the coffee."

        scene v14s48_6
        with dissolve

        li "Oh, don't worry about it. After today, I owe you at least a cup of coffee."

        scene v14s48_6a
        with dissolve

        u "*Chuckles*"

    scene v14s48_7 # TPP. Show MC looking at his phone, smiling, mouth open (don't show the screen), Lindsey taking a sip of her coffee, looking a tMC's phone as well, mouth closed
    with dissolve

    u "Okay, so... I've created a draft listing for your highly-collectable, highly desirable vintage vehicle."

    scene v14s48_6b # FPP. Same as v14s48_6, Lindsey different pose
    with dissolve

    li "*Laughs* I see you're practicing your salesman skills already."

    scene v14s48_6c # FPP. Same as v14s48_6b, Lindsey mouth closed
    with dissolve

    u "You could say I'm \"Getting them into gear\"."

    li "..."

    scene v14s48_6a
    with dissolve

    u "Into gear... Like a car? Get it?"

    scene v14s48_6
    with dissolve

    li "I think grandpa's car might've rubbed some of his humor off on you. *Laughs*"

    scene v14s48_6a
    with dissolve

    u "*Chuckles* I have more."

    scene v14s48_6b
    with dissolve

    li "Please, keep them to yourself."

    scene v14s48_6c
    with dissolve

    u "Fine, your loss."

    scene v14s48_6b
    with dissolve

    li "So, how's it looking?"

    scene v14s48_7
    with dissolve

    u "Well, we've got some choices to make on how we're going to sell this rust bucket. Here, take a look at the photos first."

    call screen iBuy


label v14s48_continue:
    scene v14s48_7a # TPP. Same as v14s48_7, Lindsey mouth open, MC mouth closed, Lindsey not sipping on coffee
    with dissolve

    li "The photos look so good!"

    scene v14s48_6a
    with dissolve

    u "Thanks. I'm a natural..."

    if v14_pics_with_linds:
        scene v14s48_6
        with dissolve

        li "Who's the hot girl?"

        scene v14s48_6c
        with dissolve

        u "I don't know, but I hope she comes with the car."

        scene v14s48_6b
        with dissolve

        li "*Laughs* Let's hope they want that too."
    
    else:
        scene v14s48_6
        with dissolve

        li "You can see all the fine details without a beautiful blonde distraction, haha."

        scene v14s48_6c
        with dissolve

        u "True, let's hope there's someone out there who can see its potential."

    scene v14s48_6
    with dissolve

    li "So, how are we describing the car?"

    scene v14s48_6a
    with dissolve

    u "I was thinking something like \"Shit car for sale. Loaded with rust and includes a rattling engine for free. Please take this piece of junk off our hands\"."

    scene v14s48_6b
    with dissolve

    li "[name], this is serious! *Chuckles*"

    scene v14s48_6c
    with dissolve

    u "Okay, okay. Let me think..."

    scene v14s48_7
    with dissolve

    u "We basically have two choices. We can lie or we can be honest..."

    call screen iBuy

# -Bring up the iBuy app with Honest and Lie description boxes. Player chooses one and then clicks continue, money scale still greyed out-

# -Middle section is a description box with two choices-

# -LIE: Modern, imported, classic sports car. One previous owner. All original and in excellent condition. Engine runs very smoothly. Low mileage. Incredible value. Buy now while you still can!-

# -BE HONEST: Classic car from the 1970s. A great restoration project. Ideal for collectors and enthusiasts. Runs OK but in desperate need of some TLC. Still, a great deal for the right person!-

label v14s48_continue2:
    if v14s48_car_description == CarDescription.LIE: # PLACEHOLDER - CHECK WITH OSCAR THE VARIABLE IN THE APP!
        scene v14s48_7
        with dissolve

        u "I'm voting for this one."

        scene v14s48_6d # FPP. Same as v14s48_6, Lindsey worried, mouth open
        with dissolve

        li "You think we should lie?!"

        scene v14s48_6e # FPP. Same as v14s48_6d, Lindsey mouth closed
        with dissolve

        u "You want to sell it, don't you?"

        scene v14s48_6d
        with dissolve

        li "Yeah, but..."

        scene v14s48_6c
        with dissolve

        u "That poor thing needs all the help it can get, Linds. Hopefully with a few white lies we can get a decent price for it."

        scene v14s48_6b
        with dissolve

        li "Yeah, I guess you're right. Let's go for it then. I just don't want them to be angry at us when they see the car in person, haha."

        scene v14s48_6c
        with dissolve

        u "If they look at those photos and honestly think that this is an imported sports car, they deserve to be scammed..."

        scene v14s48_6b
        with dissolve

        li "[name]... *Chuckles*"

        scene v14s48_6a
        with dissolve

        u "Let them be mad, I'll deal with it."

        scene v14s48_7
        with dissolve

        u "Now for the big question. What price are we going to charge these fools?"
    
    else:
        scene v14s48_7
        with dissolve

        u "I think we should be honest and tell people up front that they shouldn't expect anything amazing."

        scene v14s48_6b
        with dissolve

        li "Yeah, I agree. If we aren't honest, we could end up with no money. All of this for nothing."

        scene v14s48_6c
        with dissolve

        u "Exactly. Honesty is the best policy. *Chuckles* Now we just need to decide the price."

    scene v14s48_6d
    with dissolve

    li "Okay. Now remember, this is a free advert but only for 24 hours. I can't afford their fees beyond that, so we need to sell it fast..."

    li "Let's not put people off by asking for too much."

    scene v14s48_6a
    with dissolve

    u "So, what are you thinking? A hundred bucks?"

    scene v14s48_6
    with dissolve

    li "No! *Laughs* It's worth more than that!"

    scene v14s48_6c
    with dissolve

    u "It would sell fast though... I would think!"

    scene v14s48_6b
    with dissolve

    li "Haha, true."

    if v14_pics_with_linds:
        scene v14s48_6c
        with dissolve

        u "Seriously, I don't think we'll get any more than like six hundred bucks. And that's being generous."

        scene v14s48_6b
        with dissolve

        li "But I think it depends on the customer who's buying, no?"

        scene v14s48_6
        with dissolve

        li "If this person is only interested in buying because of me, they might spend more money based on how much they like the photos. Right?"

        scene v14s48_6a
        with dissolve

        u "I guess so, yeah. Maybe we can ask for a bit extra based on how well we think our photoshoot went. We can get six hundred for sure though, I know it."
    
    else:
        scene v14s48_6a
        with dissolve

        u "I really think we can get a solid four hundred bucks for it."
        u "It's turning to rust, but they know that from the pictures and our description. At least it still runs. *Chuckles*"

    scene v14s48_6d
    with dissolve

    li "Okay, I just don't want to risk a total loss."

    scene v14s48_6e
    with dissolve

    u "Don't worry, I got this. If there's one thing I know about, it's deciding how much old cars are worth."

    scene v14s48_6d
    with dissolve

    li "Really?"

    scene v14s48_6c
    with dissolve

    u "Nope. No idea. *Laughs*"

    scene v14s48_6b
    with dissolve

    li "*Laughs* Come on, loser. Let's make a decision."

    call screen iBuy

# -Bring up the iBuy app with the bottom of the page showing a price slider that goes left to right in $25 increments, from $100 to $800. Previous choices are greyed out. Continue button when finished-

# -Price is chosen, see Desc. /Price sheet in transcribing channel for details on what their outcome would be based on their choices. Keep variables noted for outcome-

# -Once concluded the screen disappears-

label v14s48_end:
    scene v14s48_7
    with dissolve

    u "Done!"

    scene v14s48_6
    with dissolve

    li "Finally, the advert is live! I didn't realize selling a car would take so fucking long."

    scene v14s48_6a
    with dissolve

    u "It's certainly a long process."

    if lindsey.relationship.value >= Relationship.FWB.value:
        scene v14s48_8 # TPP. Show Lindsey kissing MC (with tongue if possible)
        with dissolve

        pause 1.75

        scene v14s48_6c
        with dissolve

        u "Mmmm... Caramel."

    scene v14s48_6
    with dissolve

    li "Thanks for all your help."

    scene v14s48_6a
    with dissolve

    u "We haven't sold it yet."

    scene v14s48_6b
    with dissolve

    li "I know but, thank you anyway. I really enjoy spending time with you."

    scene v14s48_6c
    with dissolve

    u "I'm enjoying it too. We make a pretty good team."

    scene v14s48_6b
    with dissolve

    li "We do..."

    scene v14s48_6
    with dissolve

    li "But the work never stops, and I need to go now."

    scene v14s48_6a
    with dissolve

    u "Of course you do. *Chuckles*"

    scene v14s48_6
    with dissolve

    li "Thank you again."

    if lindsey.relationship.value >= Relationship.FWB.value:
        scene v14s48_9 # TPP. Show Lindsey giving MC a peck on the lips
        with dissolve

        pause 1.75

    scene v14s48_10 # TPP. Show Lindsey getting up, MC still sitting down, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v14s48_11 # FPP. MC sitting down, Lindsey at the cafe door, ready to leave, looking at MC, waving at him, smiling, mouth open
    with dissolve

    li "See you."

    scene v14s48_11a # FPP. Same as v14s48_11, Lindsey not waving, smiling, mouth closed
    with dissolve

    u "Later, Linds."

    scene v14s48_12 # FPP. MC watches as Lindsey walks away (show her walking on the sidewalk through the glass), smiling, mouth closed, giving MC a little wave
    with dissolve

    pause 0.75

    stop music fadeout 3

    if joinwolves:
        jump v14s52
    else:
        jump v14s53