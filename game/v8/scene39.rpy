# Climbing Hospital
# Location: Hospital
# Outfits: MC Outfit 2, Sebastian Outfit 1
# Time: Tuesday Night

label hosp_climb_seb:
    scene v8shos1 # TPP. Show MC and Sebastian stood at the hospital, show the hospital, MC and Sebastian looking up at the top of it. Try and portray the scale of the hospital.
    with Fade(0.75, 0.25, 0.75)

    pause 0.5

    scene v8shos2 # TPP. Show MC and Sebastian, MC looking around slightly nervous, Sebastian looking at MC.
    with dissolve

    pause 0.5

    scene v8shos3 # FPP. Close up Sebastian, Sebastian slight grin, mouth open.
    with dissolve

    se "What's up man? Getting cold feet?"

    scene v8shos3a # FPP. Same camera as v8shos3, Sebastian slight grin, mouth closed.
    with dissolve

    u "What? No. It's just... what if someone sees us?"

    scene v8shos3b # FPP. Same camera as v8shos3, Sebastian neutral expression, shrugging, mouth open.
    with dissolve

    se "True. But look man, no glory comes with zero risk."

    scene v8shos3c # FPP. Same camera as v8shos3, Sebastian neutral expression, shrugging, mouth closed.
    with dissolve

    u "Where's the glory in this?"

    scene v8shos3
    with dissolve

    se "Haha, you got me there. Glory, fun, whatever. If it makes you feel alive, I'm up for it!"

    scene v8shos3a
    with dissolve

    u "I feel pretty alive as it is..."

    scene v8shos4 # FPP. Show Sebastian pointing towards the American flag pole infront of the hospital ambulance entrance, Sebastian neutral expression, mouth open.
    with dissolve

    se "That's our way up."

    scene v8shos5 # TPP. Show Sebastian handing MC a face covering mask, MC concerned expression, Sebastian grin, mouth open.
    with dissolve

    se "Here's little something to cover up that pretty, worried face. In case \"someone sees us\"..."

    scene v8shos6 # FPP. Show Sebastian holding the mask out for MC to grab, Sebastian smile, mouth closed.
    with dissolve

    menu:
        "Climb the hospital" (bro=1.0, troublemaker=1.0):
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ climbwseb = True
            jump climb_the_hos

        "Don't climb the hospital":
            jump watching_seb_climb

label climb_the_hos:
    u "Fuck it, man. Let's do this thing."

    scene v8shos7 # TPP. Show MC grabbing the mask from Sebastian and putting it on, Sebastian smile, mouth open.
    with dissolve

    se "Looks like our cub is climbing his way up to becoming a Wolf. Hell yeah!"

    scene v8shos8 # FPP. Show Sebastian beginning to walk towards the flag pole, Sebastian now wearing black mask(mask 9) also, Sebastian, smile, mouth closed.
    with dissolve

    u "At least keep your voice down, man!"

    scene v8shos9 # TPP. Show MC following Sebastian towards the flag pole, Sebastian turns to MC, Sebastian neutral expression, mouth open.
    with dissolve

    se "There's no one around! Relax, bro."

    scene v8shos10 # FPP. Show Sebastian starting to climb the flag pole.
    with dissolve

    pause 0.5

    scene v8shos11 # TPP. Show MC beginning to climb the flag pole, Sebastian now stood on the glass roof next to flag pole, Sebastian looking down at MC offering him a safety hook, Sebastian mouth open.
    with dissolve

    se "Here, let me attach this to you..."

    scene v8shos12 # FPP. Show Sebastian leaning over the glass roof looking at camera as if MC is climbing the pole and looking up at him. Sebastian neutral expression, holding the safety hook, mouth closed.
    with dissolve

    u "Hell no, man. We're doing this the right way."

    scene v8shos13 # TPP. Show MC now stood on the glass roof with Sebastian, Sebastian looking at MC laughing.
    with dissolve

    se "Haha, don't let your big balls drag you to the ground, mister."

    scene v8shos14 # TPP. Show MC and Sebastian starting to scale the hospital, Sebastian slightly further up then MC.
    with fade

    pause 1

    scene v8shos15 # TPP. Show MC and Sebastian scaling the hospital, now further up than v8shos14.
    with dissolve

    pause 1

    scene v8shos16 # TPP. Show MC and Sebastian scaling the hospital, now about half way up the hospital, Sebastian slightly further up than MC.
    with dissolve

    pause 1

    scene v8shos17 # FPP. Show Sebastian looking down to his side into camera as he is climbing (as if MC is looking up to him), Sebastian mouth open.
    with dissolve

    se "Everything okay down there?"

    scene v8shos17a # FPP. Same camera as v8shos17, Sebastian mouth closed.
    with dissolve

    u "Yeah, it's just this..."

    scene v8shos18 # TPP. Show MC slipping whilst climbing, he is only holding on with one hand, MC terrified expression, Sebastian looking down worried expression.
    with dissolve

    pause 0.5

    scene v8shos18a # TPP. Same camera as v8shos18, Sebastian reaches and grabs MC's arm and begins to pull him up, MC gets a grip on one of the windows again.
    with dissolve

    pause 0.5

    scene v8shos19 # FPP. Sebastian has now pulled MC up so that they are level with eachother, Sebastian looking to his side towards camera, slight shocked expression, mouth closed.
    with dissolve

    u "Holy fuck, I felt pretty dead back there... but now I feel more alive than ever!"

    scene v8shos19a # FPP. Same camera as v8shos19, Sebastian smile, mouth open.
    with dissolve

    se "I feel you, bro! Now you know why this is not my first time here."

    scene v8shos20 # TPP. Show MC and Sebastian climbing further up the hospital, they are now both level with eachother, about 3/4 of the way up.
    with dissolve

    pause 1

    scene v8shos21 # TPP. Show MC and Sebastian climbing further up the hospital, they are now near the top.
    with dissolve

    pause 1

    scene v8shos22 # TPP. Show MC and Sebastian climbing over the ledge at the top of the hospital.
    with dissolve

    pause 1

    scene v8shos23 # FPP. MC and Sebastian now stood on the roof of the hospital. Show Sebastian, Sebastian looking at camera, Sebastian smile, mouth open
    with dissolve

    se "And they arise!"

    scene v8shos23a # FPP. Same camera as v8shos23, Sebastian looking around taking in the view, mouth closed.
    with dissolve

    u "That they do. How to descend is another question."

    scene v8shos23b # FPP. Same camera as v8shos23, Sebastian looking back at camera, waving his hand to come over, Sebastian neutral expression, mouth open.
    with dissolve

    se "Come here."

    scene v8shos24 # TPP. Show Sebastian sitting down on the edge of the hospital roof with his legs dangling over the edge, MC walking over to join him.
    with dissolve

    pause 0.5

    scene v8shos25 # TPP. Show MC and Sebastian both sat on the edge of the hospital roof, legs dandling over the edge.
    with dissolve

    pause 1

    scene v8shos26 # FPP. Sebastian turns to look at camera (MC) Sebastian neutral expression, mouth open.
    with dissolve

    se "This, my friend, is the cherry on tops."

    scene v8shos26a # FPP. Same camera as v8shos26, Sebastian turns his head back forward, taking in and admiring the view, Sebastian smile, mouth closed.
    with dissolve

    pause 0.5

    scene v8shos26
    with dissolve

    se "If this was my hundredth time to reach this spot, I'd still love doing it."

    scene v8shos26a
    with dissolve

    u "What's so special about it?"

    scene v8shos26
    with dissolve

    se "This roof holds many secrets, one of them being the view."

    scene v8shos27 # FPP. Show Sebastian looking forward and pointing to somewhere distant.
    with dissolve

    pause 0.5

    scene v8shos26
    with dissolve

    se "A perfect angle to the dorm of the hottest babes around! And with a little bit of luck..."

    scene v8shos26b # FPP. Same camera as v8shos26, Sebastian looking to his side at camera, slight devastation expression, mouth open.
    with dissolve

    se "Noooooo! I forgot my binoculars!"

    scene v8shos26c # FPP. Same camera as v8shos26, Sebastian looking to his side at camera, sad expression, mouth closed.
    with dissolve

    u "Hahah, oh my God, that \"Noooo\" almost sounded like a howl of the saddest Wolf ever!"

    scene v8shos26d # FPP. Same camera as v8shos26. Sebastian looking to his side at camera, Sebastian laughing, mouth open as if he is howling.
    with dissolve

    se "You mean like this? Aaaah-ooooooooh!"

    scene v8shos26e # FPP. Same camera as v8shos26, Sebastian looking to his side at camera, Sebastian smile, mouth closed.
    with dissolve

    u "Haha, yeah! Aaaah-ooooooh! Poor Wolf won't be feasting his eyes on any Little Red Riding Hoods tonight, haha!"

    scene v8shos28 # TPP. Show Sebastian punching MC softly on the shoulder, both laughing as they're sat on the edge of the hospital roof.
    with dissolve

    pause 0.5

    jump walk_home_hosp

label watching_seb_climb:
    u "I don't think I can do it."

    scene v8shos29 # FPP. ! CONTINUATION FROM V8SHOS6 ! Show Sebastian dropping the mask he was holding for MC and shurgging, dissapointed expression, mouth open.
    with dissolve

    se "Alright, cub. Let this Wolf show you how it's done..."

    scene v8shos30 # FPP. Show Sebastian now wearing the black mask (mask 9), walking towards the American flagpole infront of the hospital ambulance entrance.
    with dissolve

    u "(What's the point anyway...)"

    scene v8shos31 # FPP. Show the black face mask Sebastian had for MC lying on the floor.
    with dissolve

    pause 0.5

    scene v8shos32 # FPP. Show MC picking up the black mask, regret expression, mouth closed.
    with dissolve

    pause 0.5

    scene v8shos33 # TPP. Show Sebastian who is already climbing the hospital making good progress about half way up. TPP for more camera freedom.
    with dissolve

    pause 1

    scene v8shos34 # TPP. Show Sebastian who is now almost at the top of the hospital. TPP for more camera freedom.
    with dissolve

    pause 1

    scene v8shos35 # TPP. Show Sebastian who has now reached the top of the hospital, climing onto the roof.
    with dissolve

    pause 1

    scene v8shos36 # FPP. Camera showing Sebastian who is now stood at the top of the hospital waving down, Sebastian smile mouth open. Camera as if MC is looking up at Sebastian.
    with dissolve

    se "How's down there, little ant cub?"

    scene v8shos37 # TPP. Show MC waving back up at Sebastian, MC bored expression, mouth closed.
    with dissolve

    u "(Man, this is boring.)"

    scene v8shos36a # FPP. Same camera as v8shos36, Sebastian hands around his mouth like he is shouting down, mouth open.
    with dissolve

    se "Now if you'll excuse me, I've got some HOT business to do."

    scene v8shos38 # TPP. Show MC kicking an imaginary rock, looking a little pissed off and bored.
    with dissolve

    u "(Just great... Why did I even go out with him. Just to keep guard and bore myself to sleep?)"

    scene v8shos39 # TPP. Show MC walking around in circles looking really bored.
    with dissolve

    u "How? When? Why?"

    scene v8shos40 # TPP. Show Sebastian now back behind MC, tapping MC on the shoulder.
    with dissolve

    pause 0.5

    scene v8shos41 # FPP. Close up Sebastian, Sebastian looks depressed, mouth open.
    with dissolve

    se "Nevermind. I forgot something and blew all the fun."

    scene v8shos41a # FPP. Same camera as v8shos41, Sebastian looking depressed, mouth closed.
    with dissolve

    u "Forgot what?"

    scene v8shos41
    with dissolve

    se "I don't want to talk about it. Let's just leave."

    jump walk_home_hosp