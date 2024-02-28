# Steak house with Chloe
# Location: Steak House
# Outfits: MC Outfit 2, Chloe outfit 3
# Time: Tuesday Night

label steak_w_chloe:
    scene v8steak1 # FPP. Sweeping shot of the steak house, so Chloe sat at a table.
    with Fade(0.75, 0.25, 0.75)

    pause 1

    play music music.ck1.mlove
    queue music [music.ck1.mhappy, music.ck1.mindie1]

    scene v8steak2 # TPP. Show MC sitting down at the table with Chloe.
    with dissolve

    pause 0.5

    scene v8steak3 # FPP. Close up Chloe, Chloe smile, mouth open.
    with dissolve

    if CharacterService.is_fwb(chloe):
        cl "It's about time! I'm starving."

        scene v8steak3a # FPP. Same camera as v8steak3, Chloe smile, mouth closed.
        with dissolve

        u "Sorry, had to make myself pretty for you."

        scene v8steak3
        with dissolve

        cl "Worth it."

        scene v8steak3a
        with dissolve

        u "You look delicious yourself."

        scene v8steak3b # FPP. Same camera as v8steak3, Chloe laugh, mouth open.
        with dissolve

        cl "I try. Now let's go. It smells so good."

        scene v8steak3
        with dissolve

        u "It sure does!"

    else:
        cl "Two more minutes and I would have started without you."

        scene v8steak3a
        with dissolve

        u "It smells so good. I wouldn't blame you."

        scene v8steak3
        with dissolve

        cl "Yeah, I smell this place every day on the way back to my room and I just had to give it a try."

        scene v8steak3a
        with dissolve

        u "I'm glad you asked me to join you."

        scene v8steak3
        with dissolve

        cl "Enough chit chat. Let's eat."

    scene v8steak3c # FPP. Same camera as v8steak3, Chloe mouth open, looking around.
    with dissolve

    cl "Wow it's nice in here."

    if CharacterService.is_fwb(chloe):
        scene v8steak3a
        with dissolve

        u "Perfect romantic afternoon with my best girl..."

        scene v8steak3b
        with dissolve

        cl "*giggles* You are such a flirt."

        scene v8steak3a
        with dissolve

        u "What? You're definitely the best at certain things."

        scene v8steak3
        with dissolve

        cl "And you have a lot of experience in that area?"

        scene v8steak3a
        with dissolve

        u "Not nearly enough, but I'm sure we can fix that."

        scene v8steak3b
        with dissolve

        cl "I'm sure you'll try."

    else:
        scene v8steak3a
        with dissolve

        u "Yeah, great place for a platonic lunch date between friends."
        scene v8steak3b
        with dissolve
        cl "*giggles* Definitely."

        scene v8steak3a
        with dissolve

        menu:
            "Flirt with Chloe":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                jump steak_flirt_w_chloe

            "Don't flirt with Chloe":
                jump steak_no_flirt_w_chloe

label steak_flirt_w_chloe:

    grant Achievement("up_for_more", "Flirt with Chloe at the Steakhouse")

    u "Unlesssss..."

    scene v8steak3d # FPP. Same camera as v8steak3, Chloe neutral expression, mouth open.
    with dissolve

    cl "Unlesssss what?"

    scene v8steak3e # FPP. Same camera as v8steak3, Chloe neutral expression, mouth closed.
    with dissolve

    u "Unless one of those friends was up for more."

    scene v8steak3d
    with dissolve

    cl "And which friend would that be up to?"

    scene v8steak3e
    with dissolve

    u "Definitely the hottest one."

    scene v8steak3b
    with dissolve

    cl "I see... No pressure or anything. Haha."

    jump steak_w_chloe_cont

label steak_no_flirt_w_chloe:
    u "Good, because if this was a real date I'd be too nervous to eat."

    scene v8steak3d
    with dissolve

    cl "Nervous? I don't see it. You always seem so confident."

    scene v8steak4 # TPP. Show MC offering his hand out to Chloe as if to shake her hand, MC mouth open.
    with dissolve

    u "Hi, my name's [name], I don't believe we've met."

    scene v8steak4a # TPP. Same camera as v8steak4a, Chloe slapping MC's hand away, both laughing, Chloe mouth open.
    with dissolve

    cl "Hush!"

    jump steak_w_chloe_cont

label steak_w_chloe_cont:
    scene v8steak3d
    with dissolve

    cl "Let's order before I eat my chopsticks."

    scene v8steak3e
    with dissolve

    u "Dip it in soy sauce. It'll be delicious."

    scene v8steak3b
    with dissolve

    cl "*giggles* I'm a shrimp sauce kinda girl."

    scene v8steak3a
    with dissolve

    u "Bold choice."

    scene v8steak6 # FPP. Show the waiter coming to at the table ready to take their order, Chloe looking at waiter also, Chloe mouth open.
    with dissolve

    cl "I'll have a large beef ramen with an egg please!"

    scene v8steak7 # FPP. Show Chloe looking at camera, smile, mouth closed.
    with dissolve

    u "Wow, you gonna need help with any of that?"

    scene v8steak7a # FPP. Same camera as v8steak7a, Chloe looking at camera, laugh, mouth open.
    with dissolve

    cl "Most certainly not! Get your own. Haha."

    scene v8steak8 # FPP. Show the waiter looking at camera, waiter smile, mouth closed.
    with dissolve

    u "Okay, then I'll do steak hibachi medium rare with extra steamed vegetables."

    scene v8steak7a
    with dissolve

    cl "Steak and extra veggies?"

    scene v8steak7
    with dissolve

    u "I'm a growing boy."

    scene v8steak9 # TPP. Show MC flexing his muscles, Chloe laughing, MC sarcastic serious, mouths closed. Waiter now gone.
    with dissolve

    menu:
        "Ask to see Chloe's muscles":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            jump steak_w_chloe_muscles

        "Turn the conversation serious":
            jump steak_w_chloe_serious

label steak_w_chloe_muscles:
    scene v8steak3a
    with dissolve

    u "Your turn."

    scene v8steak3f # FPP. Same camera as v8steak3, Chloe confused expression, mouth open.
    with dissolve

    cl "My turn for what?"

    scene v8steak3g # FPP. Same camera as v8steak3, Chloe confused expression, mouth closed.
    with dissolve

    u "Let me see your muscles. All that protein, I bet you're stronger than me."

    scene v8steak10 # FPP. Show Chloe, flexing her muscles, Chloe laughing, mouth closed.
    with dissolve

    u "Wow! Impressive... and terrifying. Remind me to stay on your good side!"

    jump steak_w_chloe_cont_2

label steak_w_chloe_serious:
    scene v8steak3e
    with dissolve

    u "So, how's it going? Anything you wanna talk about?"

    scene v8steak3d
    with dissolve

    cl "Can't a friend invite another friend out for lunch?"

    scene v8steak3e
    with dissolve

    u "Totally... just making sure that's all it is. If you need a shoulder..."

    scene v8steak3b
    with dissolve

    cl "*giggles* I appreciate the offer, but you're off the hook. I just wanted to hang out and gorge myself on sushi."

    scene v8steak3
    with dissolve

    u "Well, I can sure help you there!"

    jump steak_w_chloe_cont_2

label steak_w_chloe_cont_2:
    scene v8steak11 # TPP. Show the waiter walking over to the table holding Chloe and MC's food, Both looking at the waiter, both smile, Chloe mouth open.
    with dissolve

    cl "Ohh, yours smells yummy. I hope it tastes as good as it smells."

    scene v8steak12 # TPP. Show the waiter placing the food down on the table, Waiter smile, Chloe and MC looking at food, mouths closed.
    with dissolve

    pause 0.5

    scene v8steak13 # FPP. Show Chloe, food on table infront of Chloe, Chloe looking at her food, Chloe neutral expression, mouth closed.
    with dissolve

    if ending == "chloe":
        u "You'd taste better."

        scene v8steak13a # FPP. Same camera as v8steak13, Chloe looking at camera, flirty smile, mouth open.
        with dissolve

        cl "You sure did."

        scene v8steak13b # FPP. Same camera as v8steak13, Chloe looking at camera, flirty smile, mouth closed.
        with dissolve

        u "Oh, God. You're insanely hot."

        scene v8steak13a
        with dissolve

        cl "Maybe someday soon you'll find out."

        scene v8steak13b
        with dissolve

        u "Find out what? How insane you are or how you taste?"

        scene v8steak13d # FPP. Same camera as v8steak13, Chloe chuckling, mouth open.

        with dissolve

        cl "*giggles* Both!"

    else:
        u "Here try it."

        scene v8steak14 # TPP. Show MC offering a piece of his food out to Chloe.
        with dissolve

        pause 0.5

        scene v8steak13e # TPP. Same camera as v8steak13, Chloe looks like she's chewing food, mouth closed.
        with dissolve

        u "(Oh, God that's hot)"

        scene v8steak13d

        with dissolve

        cl "Delicious!"

    scene v8steak13f # FPP. Same camera as v8steak13, Chloe neutral expression, mouth open.
    with dissolve

    cl "You all caught up on your homework?"

    scene v8steak13g # FPP. Same camera as v8steak13, Chloe neutral expression, mouth closed.
    with dissolve

    u "Is that even possible?"

    scene v8steak13d

    with dissolve

    cl "No, probably not. Haha."

    scene v8steak13d
    with dissolve

    u "I expected it to be hard work but..."

    scene v8steak13h # FPP. Same camera as v8steak13, Chloe slight wink, mouth open.
    with dissolve

    cl "Well, you could always do some... extra credit..."

    scene v8steak13d
    with dissolve

    u "I've done everything!"

    scene v8steak13h
    with dissolve

    pause 0.5

    scene v8steak13d
    with dissolve

    u "Oh... you mean... Nooo."

    scene v8steak13h
    with dissolve

    cl "Prude."

    scene v8steak13d
    with dissolve

    u "It's not so easy for guys. People aren't storming castles to get at us."

    scene v8steak13d
    with dissolve
    
    cl "Castles? *giggles*"

    scene v8steak13d
    with dissolve

    u "Yeah! If I was a knight, I'd slay a hundred dragons to get to you."

    scene v8steak13f
    with dissolve

    cl "Only a hundred, huh? Noted."

    scene v8steak13g
    with dissolve

    u "Thousands!"

    scene v8steak15 # FPP. Show Chloe looking at camera, looking full, mouth open. EMPTY PLATES.
    with fade

    cl "Oh... I'm stuffed."

    scene v8steak15a # FPP. Same camera as v8steak15, chloe mouth closed.
    with dissolve

    if CharacterService.is_fwb(chloe):
        menu:
            "Say a dirty joke":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                jump steak_w_chloe_dirty
                
            "Don't say a joke":
                jump steak_w_chloe_dirty_no

    else:
        u "Yeah, I was so hungry, I think I ordered too much."

        scene v8steak15b # FPP. Same camera as v8steak15, Chloe smile, mouth open.
        with dissolve

        cl "Don't worry about it. You're a growing boy!"

        jump steak_w_chloe_cont_3

label steak_w_chloe_dirty:
    u "I can make you more stuffed."

    scene v8steak15b
    with dissolve

    cl "Promise?"

    scene v8steak15c # FPP. Same camera as v8steak15, Chloe Smile, mouth closed.
    with dissolve

    u "Yes! And we'd go to my room. No interruptions!"

    scene v8steak15b
    with dissolve

    cl "Do guys really put a sock on their door or is that only in the movies."

    scene v8steak15c
    with dissolve

    u "I don't have a roommate so I don't need one. But if I had you in my room, I'd barricade the door and booby trap it."

    scene v8steak13d # FPP. Same camera as v8steak15, Chloe laugh, mouth open.

    with dissolve

    cl "You said booby."

    jump steak_w_chloe_cont_3

label steak_w_chloe_dirty_no:
    u "Me too. Those extra veggies really did it."

    scene v8steak13d # FPP. Same camera as v8steak15, Chloe laugh, mouth open.

    with dissolve

    cl "Now you just have to work it off!"

    scene v8steak15c
    with dissolve

    u "(I'd love to work it off with you)"

    scene v8steak15b
    with dissolve

    cl "You have a training session after this, right?"

    scene v8steak15c
    with dissolve

    u "Uh, yeah, always."

    jump steak_w_chloe_cont_3

label steak_w_chloe_cont_3:

    scene v8steak13f # FPP. Same camera as v8steak15, Chloe neutral expression, mouth open.

    with dissolve

    cl "I better get back to the house. The girls go nuts when I'm not there to keep them in order."

    scene v8steak15 # FPP. Same camera as v8steak15, Chloe neutral expression, mouth closed.
    with dissolve

    u "Really? They don't sit around braiding each other's hair and having tea parties?"

    scene v8steak15b
    with dissolve

    cl "*giggles* That's only on Tuesdays."

    scene v8steak16 # TPP. Show Chloe and MC getting up from their seats preparing to leave.
    with dissolve

    pause 0.5

    scene v8steak17 # FPP. Show Chloe, smile, mouth closed.
    with dissolve

    u "Thanks for inviting me. It was really good. I think I found my new favorite place."

    scene v8steak17a # FPP. Same camera as v8steak17, mouth open.
    with dissolve

    cl "Me too. Maybe we can make this a regular thing."

    scene v8steak17
    with dissolve

    u "I'd love that!"

    if CharacterService.is_fwb(chloe):
        scene v8steak17b # FPP. Same camera as v8steak17, flirty expression, mouth open.
        with dissolve

        cl "And maybe we can make something else a regular thing."

        scene v8steak17c # FPP. Same camera as v8steak17, flirty expression, mouth closed.
        with dissolve

        u "I have a feeling that alone time with you is anything but regular."

        scene v8steak17b
        with dissolve

        cl "You have no idea."

        scene v8steak17c
        with dissolve

        u "I've imagined plenty, especially after Friday! But that's nothing compared to the real thing."

        scene v8steak17b
        with dissolve

        cl "You're right. The real thing is so much more fun."

        scene v8steak17c
        with dissolve

        u "(Oh God)"

        scene v8steak18 # FPP. Show Chloe and MC kissing.
        with dissolve

    else:
        scene v8steak17 # FPP. Same camera as v8steak17, smile, mouth open.
        with dissolve

        cl "I'll text you next time I'm craving sushi."

        scene v8steak17 # FPP. Same camera as v8steak17, smile, mouth closed.
        with dissolve

        u "Please do."

    scene v8steak19 # FPP. Show Chloe at her front door.
    with fade

    u "Take care of yourself."

    scene v8steak19a # FPP. Show Chloe at her front door.

    with dissolve

    cl "You too."

    if CharacterService.is_fwb(chloe):
        scene v8steak20 # TPP. Show MC and Chloe kissing.
        with dissolve

        pause 0.5

        scene v8steak21 # FPP. Show Chloe entering her house.
        with dissolve

        pause 0.5

        scene v8steak22
        with dissolve

        pause 0.5
        jump v8_julia_call

    else:
        scene v8steak21 # FPP. Show Chloe entering her house.
        with dissolve

        pause 0.5

        scene v8steak22
        with dissolve

        pause 0.5

        jump v8_julia_call