# -Japanese Steakhouse with Chloe, mid-afternoon-
# -MC walks up to restaurant and Chloe is waiting-

label steak_w_chloe:
    if chloers:
        cl "It's about time! I'm starving"

        scene v8s
        with dissolve
        u "Sorry, had to make myself pretty for you"

        scene v8s
        with dissolve
        # -Chloe looks MC over-
        cl "Worth it"

        scene v8s
        with dissolve
        u "You look delicious yourself"

        scene v8s
        with dissolve
        cl "I try. Now let's go. It smells so good"

        scene v8s
        with dissolve
        u "It sure does!"

        scene v8s
        with dissolve

    if not chloers:
        cl "Two more minutes and I would have started without you"

        scene v8s
        with dissolve
        u "It smells so good. I wouldn't blame you"

        scene v8s
        with dissolve
        cl "Yeah, I smell this place every day on the way back to my room and I just had to give it a try"

        scene v8s
        with dissolve
        u "I'm glad you asked me to join you"

        scene v8s
        with dissolve
        cl "Enough chit chat. Let's eat"

        scene v8s
        with dissolve


    if chloerS:
        cl "Wow it's nice in here"

        scene v8s
        with dissolve

        if chloers:
            u "Perfect romantic afternoon with my best girl..."

            scene v8s
            with dissolve
            cl "*giggles* You are such a flirt"

            scene v8s
            with dissolve
            u "What? You're definitely the best at certain things"

            scene v8s
            with dissolve
            cl "And you have a lot of experience in that area?"

            scene v8s
            with dissolve
            u "Not nearly enough, but I'm sure we can fix that"

            scene v8s
            with dissolve
            cl "I'm sure you'll try"

            scene v8s
            with dissolve

    if not chloers:
        u "Yeah, great place for a platonic lunch date between friends"

        scene v8s
        with dissolve
        cl "*giggles* Definitely"

        scene v8s
        with dissolve

        menu:
            "Flirt with Chloe":
                jump steak_flirt_w_chloe
            "Don't flirt with Chloe":
                jump steak_no_flirt_w_chloe

label steak_flirt_w_chloe:
    u "Unlesssss..."

    scene v8s
    with dissolve
    cl "Unlesssss what?"

    scene v8s
    with dissolve
    # -Chloe looks at MC with an expectant look-
    u "Unless one of those friends was up for more"

    scene v8s
    with dissolve
    cl "And which friend would that be up to?"

    scene v8s
    with dissolve
    u "Definitely the hottest one"

    scene v8s
    with dissolve
    # -MC winks at Chloe-
    cl "I see... No pressure or anything. Haha"

    scene v8s
    with dissolve

    jump steak_w_chloe_cont

label steak_no_flirt_w_chloe:
    u "Good, because if this was a real date I'd be too nervous to eat"

    scene v8s
    with dissolve
    cl "Nervous? I don't see it. You always seem so confident"

    scene v8s
    with dissolve
    # -MC looks at Chloe with surprise-
    # -MC puts out his hand for Chloe to shake-
    u "Hi, my name's [name], I don't believe we've met"

    scene v8s
    with dissolve
    # -Chloe slaps his hand away-
    cl "Hush!"

    scene v8s
    with dissolve

    jump steak_w_chloe_cont

label steak_w_chloe_cont:
    cl "Let's order before I eat my chopsticks"

    scene v8s
    with dissolve
    u "Dip it in soy sauce. It'll be delicious"

    scene v8s
    with dissolve
    cl "*giggles* I'm a shrimp sauce kinda girl"

    scene v8s
    with dissolve
    u "Bold choice"

    scene v8s
    with dissolve
    # -Waiter comes over and takes their order-
    cl "I'll have a salmon roll, tuna roll, and volcano roll... oh and some miso soup!"

    scene v8s
    with dissolve
    u "Wow, you gonna need help with any of that?"

    scene v8s
    with dissolve
    cl "Most certainly not! Get your own. Haha"

    scene v8s
    with dissolve
    u "OK, then I'll do steak hibachi medium rare with extra steamed vegetables"

    scene v8s
    with dissolve
    cl "Steak and extra veggies?"

    scene v8s
    with dissolve
    u "I'm a growing boy"

    scene v8s
    with dissolve
    # -MC shows Chloe his muscles-
    # -Chloe laughs-

    menu:
        "Ask to see Chloe's muscles":
            jump steak_w_chloe_muscles
        "Turn the conversation serious":
            jump steak_w_chloe_serious

    # -MC can choose to ask to see her muscles or turn the conversation more serious-

label steak_w_chloe_muscles:
    u "Your turn"

    scene v8s
    with dissolve
    # -Chloe looks shocked-
    cl "My turn for what?"

    scene v8s
    with dissolve
    u "Let me see your muscles. All that sushi protein, I bet you're stronger than me"

    scene v8s
    with dissolve
    # -Chloe laughs but shows her muscle-
    u "Wow! Impressive... and terrifying. Remind me to stay on your good side!"

    scene v8s
    with dissolve

    jump steak_w_chloe_cont_2

label steak_w_chloe_serious:
    u "So, how's it going? Anything you wanna talk about?"

    scene v8s
    with dissolve
    # -Chloe looks surprised-
    cl "Can't a friend invite another friend out for lunch?"

    scene v8s
    with dissolve
    u "Totally... just making sure that's all it is. If you need a shoulder..."

    scene v8s
    with dissolve
    # -MC shrugs his shoulders twice-
    cl "*giggles* I appreciate the offer, but you're off the hook. I just wanted to hang out and gorge myself on sushi"

    scene v8s
    with dissolve
    u "Well, I can sure help you there!"

    scene v8s
    with dissolve

    jump steak_w_chloe_cont_2

    # -Continue after choice-
    # -Waiter comes with their food-
    cl "Ohh, yours smells yummy. I hope it tastes as good as it smells"

    scene v8s
    with dissolve

    if chloers:
        u "You'd taste better"

        scene v8s
        with dissolve
        cl "You sure did"

        scene v8s
        with dissolve
        u "Oh, God. You're insanely hot"

        scene v8s
        with dissolve
        cl "Maybe someday soon you'll find out"

        scene v8s
        with dissolve
        u "Find out what? How insane you are or how you taste?"

        scene v8s
        with dissolve
        cl "*giggles* Both!"

        scene v8s
        with dissolve

    if not chloers:
        u "Here try it"

        scene v8s
        with dissolve
        # -Mc gives Chloe a bite of his food-
        # -MC watches her mouth as she takes the bite-
        u "(Oh, God that's hot)"

        scene v8s
        with dissolve
        cl "Delicious!"

        scene v8s
        with dissolve

    # -Continue eating-
    cl "You all caught up on your homework"

    scene v8s
    with dissolve
    u "Is that even possible?"

    scene v8s
    with dissolve
    cl "No, probably not. Haha"

    scene v8s
    with dissolve
    u "I expected it to be hard work but..."

    scene v8s
    with dissolve
    cl "Well, you could always do some... extra credit..."

    scene v8s
    with dissolve
    # -Chloe winks-
    u "I've done everything!"

    scene v8s
    with dissolve
    # -Chloe winks again and smiles-
    u "Oh... you mean... Nooo"

    scene v8s
    with dissolve
    cl "Prude"

    scene v8s
    with dissolve
    u "It's not so easy for guys. People aren't storming castles to get at us"

    scene v8s
    with dissolve
    cl "Castles? *giggles*"

    scene v8s
    with dissolve
    u "Yeah! If I was a knight, I'd slay a hundred dragons to get to you"

    scene v8s
    with dissolve
    cl "Only a hundred, huh? Noted"

    scene v8s
    with dissolve
    u "Thousands!"

    scene v8s
    with dissolve
    # -They both laugh-
    # -Eating montage-
    # -Chloe leans back-
    cl "Oh... I'm stuffed"

    scene v8s
    with dissolve

    # -If ChloeRS-
    if chloers:
        menu:
            "Say a dirty joke":
                jump steak_w_chloe_dirty
            "Don't say a joke":
                jump steak_w_chloe_dirty_no

    if not chloers:
        u "Yeah, I was so hungry, I think I ordered too much"

        scene v8s
        with dissolve
        cl "Don't worry about it. You're a growing boy!"

        scene v8s
        with dissolve
        # -They both laugh-

label steak_w_chloe_dirty:
    u "I can make you more stuffed"

    scene v8s
    with dissolve
    # -MC gestures toward his crotch-
    cl "Promise?"

    scene v8s
    with dissolve
    u "Yes! And we'd go to my room. No interruptions!"

    scene v8s
    with dissolve
    cl "Do guys really put a sock on their door or is that only in the movies"

    scene v8s
    with dissolve
    u "I don't have a roommate so I don't need one. But if I had you in my room, I'd barricade the door and booby trap it"

    scene v8s
    with dissolve
    cl "You said booby"

    scene v8s
    with dissolve

    jump steak_w_chloe_cont_3

label steak_w_chloe_dirty_no:
    u "Me too. Those extra veggies really did it"

    scene v8s
    with dissolve
    cl "Now you just have to work it off!"

    scene v8s
    with dissolve
    u "(I'd love to work it off with you)"

    scene v8s
    with dissolve
    cl "You have a training session after this, right?"

    scene v8s
    with dissolve
    u "Uh, yeah, always"

    scene v8s
    with dissolve

    jump steak_w_chloe_cont_3

label steak_w_chloe_cont_3:
    cl "I better get back to the house. The girls go nuts when I'm not there to keep them in order"

    scene v8s
    with dissolve
    u "Really? They don't sit around braiding each other's hair and having tea parties?"

    scene v8s
    with dissolve
    cl "*giggles* That's only on Tuesdays"

    scene v8s
    with dissolve
    # -They get up from the table and start walking out-
    u "Thanks for inviting me. It was really good. I think I found my new favorite place"

    scene v8s
    with dissolve
    cl "Me too. Maybe we can make this a regular thing"

    scene v8s
    with dissolve
    u "I'd love that!"

    scene v8s
    with dissolve

    if chloers:
        cl "And maybe we can make something else a regular thing"

        scene v8s
        with dissolve
        # -Chloe moves closer to kiss MC-
        u "I have a feeling that alone time with you is anything but regular"

        scene v8s
        with dissolve
        cl "You have no idea"

        scene v8s
        with dissolve
        # -Chloe kisses MC-
        u "I've imagined plenty, especially after Friday! But that's nothing compared to the real thing"

        scene v8s
        with dissolve
        cl "You're right. The real thing is so much more fun"

        scene v8s
        with dissolve
        u "(Oh God)"

        scene v8s
        with dissolve
        # -MC kisses Chloe-

    if not chloers:
        cl "I'll text you next time I'm craving sushi"

        scene v8s
        with dissolve
        u "Please do"

        scene v8s
        with dissolve

    # -Continue at Chloe's door-
    u "Take care of yourself"

    scene v8s
    with dissolve
    cl "You too"

    scene v8s
    with dissolve

    if chloers:
        pass
    # -MC kisses Chloe-

    if not chloers:
        pass
    # -MC waves at Chloe-

    # -Continue after Chloe-
    # -Mc walks back to his dorm-
    jump v8_julia_call
