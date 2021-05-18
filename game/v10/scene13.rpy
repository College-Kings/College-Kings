# SCENE 13: MC at wolves house/redecorate
# Locations: Wolves house
# Characters: MC(Outfit 1 ), Chris(Outfit 1), Perry(Outfit 1), 
# Time: Sunday Morning
label v10_wolves_redec:
    
    if v10s10_hangWLinds: # RCS - variable for MC going to visit Lindsey
        
        scene v10swhr1 # FPP. Show Wolve's House front door as MC approaches, returning from his visit to Lindsey.
        with fade

        u "(Home, sweet home.)"

        scene v10swhr2 # FPP. Show Chris standing in the kitchen (table and living room in background). Chris smiling, mouth closed.
        with dissolve

        u "Hey Chris, I really appreciate the room and all, but I haven't had a chance to make it scream [name] yet. Is it cool if I jazz it up a bit?"

        scene v10swhr2a # FPP. Same camera angle as v10swhr2. Show Chris. Chris smiling, mouth open.
        with dissolve

        ch "*Laughs* I was wondering when you'd get tired of blank walls. There's some supplies in that closet. We're actually getting ready to decorate the whole house."

        scene v10swhr2
        with dissolve

        u "Really!? Good timing haha. Got a theme in mind?"

        scene v10swhr2a
        with dissolve

        ch "Yeah man! Mostly blue with our standard silver trim. Make it scream 'Wolves', you know?"

        scene v10swhr2
        with dissolve

        u "Yeah that sounds great! I'll probably do the same to my room."

        scene v10swhr2a
        with dissolve

        ch "Go for it, man! Have fun."

        scene v10swhr3 # FPP. Show the three doors in the yellow hallway as MC goes to the closest.
        with dissolve
        
        pause 0.5
        
        scene v10swhr4 # TPP. Show MC opening the door to the closet in the hallway.
        with dissolve

        u "(Alright, let's see here.)"

        scene v10swhr4a # TPP. Same camera as v10swhr4. Show MC with door to the closet open. Perry walks in from the side, coming inside from the garage.
        with dissolve
        
        pause 0.5

        scene v10swhr4b # TPP. Same camera as v10swhr4. Show MC with door to the closet open. Perry approaches MC, smiling, mouth open.
        with dissolve
        
        guyd "Hey man..."

        scene v10swhr5 # FPP. Show the closet door open, show Perry standing nearby, smiling, mouth closed.
        with dissolve
        
        u "Hey, feels like you've kinda been hiding since the fight."

        scene v10swhr5a # FPP. Show the closet door open, show Perry standing nearby, smiling, mouth open.
        with dissolve

        guyd "*Laughs* Yeah a little bit. What are you doing in the closet?"

        scene v10swhr5
        with dissolve

        u "I'm getting ready to decorate my room."

        scene v10swhr5a
        with dissolve

        guyd "Oh wow, you want some help?"

        scene v10swhr5
        with dissolve
        
        menu:
            "Accept Help":

                scene v10swhr5
                with dissolve
                
                u "Yeah I'd love some help. Will go much faster haha."

                scene v10swhr4c # TPP. Same camera as v10swhr4. Show MC and Perry grabbing supplies from the closet.
                with fade

                pause 0.5
                
                scene v10swhr6 # TPP. Show MC and Perry standing in MC's room with supplies, looking the place over, getting ready to work.
                with dissolve
                
                u "(Welp, here goes nothing.)"
        
                scene v10swhr6a # TPP. Show MC and Perry working in MC's room. They start by removing any objects from the walls and moving furniture more towards the center of the room.
                with fade

                pause 0.5

                scene v10swhr6b # TPP. Show MC and Perry working in MC's room. They remove/peel/strip the current yellow wallpaper.
                with fade

                pause 0.5

                scene v10swhr7 # FPP. Show Perry in MC's under construction room. Perry has a neutral expression, mouth closed.
                with dissolve

                u "Hey man, hope you don't mind me asking, but what made you back out at the brawl?"

                scene v10swhr7a # FPP. Show Perry in MC's under construction room. Perry has a slight embarrassed expression, mouth open.
                with dissolve

                guyd "I was waiting for you to bring that up. It's kind of embarrassing, man."

                scene v10swhr7b # FPP. Show Perry in MC's under construction room. Perry has a slight embarrassed expression, mouth closed.
                with dissolve
                
                u "Embarassing? What's up?"

                scene v10swhr7a
                with dissolve

                guyd "Well, the reason I ran and chose not to fight isn't because I didn't want to, it's because I couldn't."

                scene v10swhr7b
                with dissolve

                u "What do you mean you couldn't?"

                scene v10swhr7a
                with dissolve

                guyd "Man, I got sick..."

                scene v10swhr7b
                with dissolve

                u "Sick from what?"

                scene v10swhr7a
                with dissolve

                guyd "You know that sushi we had in the fridge for a while?"

                scene v10swhr7b
                with dissolve
                
                u "Yeah."

                scene v10swhr7a
                with dissolve

                guyd "Well, I ate it right before the fight because I was hungry and well, I've never had sushi before. Turns out, I'm allergic."

                scene v10swhr7c # FPP. Show Perry in MC's under construction room. Perry is smiling/looks amused, mouth closed.
                with dissolve

                u "*Laughs* Are you serious!?"

                scene v10swhr7d # FPP. Show Perry in MC's under construction room. Perry is smiling/looks amused, mouth open.
                with dissolve

                guyd "*Laughs* Sadly, yes. Regardless of me sick or not though the guys still weren't happy."

                scene v10swhr7c
                with dissolve

                u "At least you had a good reason."

                scene v10swhr7d
                with dissolve

                guyd "Yeah, next time though I'm going in like a beast."

                scene v10swhr7c
                with dissolve

                u "Glad to hear it."

                scene v10swhr6c # TPP. Show MC and Perry working in MC's room. They paste and prep the walls for wallpaper, etc. 
                with dissolve

                pause 0.5
                
                scene v10swhr6d # TPP. Show MC and Perry working in MC's room. They apply the new wallpaper, finish the walls, etc.
                with dissolve

                pause 0.5

                scene v10swhr7e # FPP. Show Perry in MC's finished, new room. Perry is smiling, mouth open.
                with dissolve
                
                guyd "Well the room looks pretty nice."

                scene v10swhr8 # TPP. Show an angle of MC's new, finished room.
                with fade

                pause 0.5

                scene v10swhr8a # TPP. Show another angle of MC's new, finished room.
                with fade

                pause 0.5

                scene v10swhr8b # TPP. Show MC and Perry standing in MC's new, finished room.
                with fade

                pause 0.5

                scene v10swhr7f # FPP. Show Perry in MC's finished, new room. Perry is smiling, mouth closed.
                with dissolve

                u "Yeah, this is way better, thanks man!"

                scene v10swhr7e
                with dissolve
                
                guyd "Anytime."

            "Decline Help":
                
                scene v10swhr5
                with dissolve

                u "I appreciate it man, but I'm all good. This is gonna require all my focus."

                scene v10swhr5a
                with fade

                guyd "*Laughs* Alright man."

                scene v10swhr4d # TPP. Same camera as v10swhr4. Show MC grabbing supplies from the closet.
                with fade
                
                pause 0.5

                scene v10swhr8
                with fade

                pause 0.5

                scene v10swhr8a
                with fade

                pause 0.5

                scene v10swhr8c # TPP. Show MC standing in his new, finished room.
                with fade
                
                u "(Now that's what I'm talking about!)"

    else: # RCS - MC didn't visit Lindsey

        scene v10swhr9 # TPP. MC is walking down the stairs on the Wolves house.
        with fade
        pause 0.5

        scene v10swhr2
        with dissolve

        u "Hey Chris, I really appreciate the room and all, but I haven't had a chance to make it scream [name] yet. Do you mind if I jazz it up a bit?"

        scene v10swhr2a
        with dissolve

        ch "*Laughs* I was wondering when you'd get tired of blank walls. There's some supplies in that closet, we're actually getting ready to decorate the whole house."

        scene v10swhr2
        with dissolve

        u "Really!?"

        scene v10swhr2a
        with dissolve

        ch "Yeah man!"

        scene v10swhr2
        with dissolve

        u "What do you have in mind?"

        scene v10swhr2a
        with dissolve

        ch "Something that screams 'Wolves'. I'm thinking our trademark Blue with silver highlights. What do you think?"

        scene v10swhr2
        with dissolve

        u "That's perfect! I may do just that to my room."

        scene v10swhr2a
        with fade

        ch "My man! Have fun [name]."

        scene v10swhr3
        with fade

        pause 0.5

        scene v10swhr4
        with dissolve

        pause 0.5

        scene v10swhr4a
        with dissolve
        
        pause 0.5

        scene v10swhr4b
        with dissolve

        guyd "Hey man..."

        scene v10swhr5
        with dissolve

        u "Hey, Perry. Feels like you've kinda been hiding since the fight."

        scene v10swhr5a
        with dissolve

        guyd "*Laughs* Yeah, a little bit. What are you doing in the closet?"

        scene v10swhr5
        with dissolve

        u "I'm getting ready to decorate my room."

        scene v10swhr5a
        with dissolve

        guyd "Oh wow, you want some help?"

        scene v10swhr5
        with dissolve
        menu:
            "Accept Help":
                
                scene v10swhr5
                with dissolve
                
                u "Yeah I'd love some help, man. That'd be great."

                scene v10swhr4c
                with fade

                pause 0.5

                scene v10swhr6
                with fade
                
                u "(Welp, here goes nothing.)"
        
                scene v10swhr6a
                with fade

                pause 0.5

                scene v10swhr6b
                with fade

                pause 0.5

                scene v10swhr7
                with dissolve

                u "Hey man, hope you don't mind me asking, but what made you back out at the brawl?"

                scene v10swhr7a
                with dissolve

                guyd "I was waiting for you to bring that up. It's kind of embarassing, man."

                scene v10swhr7b
                with dissolve

                u "Embarassing? How?"

                scene v10swhr7a
                with dissolve

                guyd "Well, the reason I ran and chose not to fight isn't because I didn't want to, it's because I couldn't."

                scene v10swhr7b
                with dissolve

                u "What do you mean you couldn't?"

                scene v10swhr7a
                with dissolve

                guyd "Man, I got sick..."

                scene v10swhr7b
                with dissolve

                u "Sick from what?"

                scene v10swhr7a
                with dissolve

                guyd "You know that sushi we had in the fridge for awhile?"

                scene v10swhr7b
                with dissolve
                u "Yeah..."

                scene v10swhr7a
                with dissolve

                guyd "Well, I ate it right before the fight because I was hungry and well I've never had sushi before. Come to find out, I'm allergic."

                scene v10swhr7c
                with dissolve

                u "*Laughs* Are you serious!?"

                scene v10swhr7d
                with dissolve

                guyd "*Laughs* Sadly, yes. Regardless of me sick or not though the guys still weren't happy."

                scene v10swhr7c
                with dissolve

                u "At least you had a good reason."

                scene v10swhr7d
                with dissolve

                guyd "Yeah, next time though I'm going in like a beast."

                scene v10swhr7c
                with fade

                u "Glad to hear it."

                scene v10swhr6c
                with fade

                pause 0.5
                
                scene v10swhr6d
                with fade

                pause 0.5

                scene v10swhr7e
                with fade
                
                guyd "Well the room looks pretty nice."

                scene v10swhr8
                with fade

                pause 0.5

                scene v10swhr8a
                with fade

                pause 0.5

                scene v10swhr8b
                with fade

                pause 0.5
                
                scene v10swhr7f
                with dissolve
                
                u "Yeah, this is way better, thanks man!"

                scene v10swhr7e
                with fade

                guyd "Anytime."

            "Decline Help":
                scene v10swhr5
                with dissolve

                u "I appreciate it man, but I'm all good. This is gonna require all my focus."

                scene v10swhr5a
                with fade

                guyd "*Laughs* Alright man."

                scene v10swhr4d
                with fade

                pause 0.5

                scene v10swhr8
                with fade

                pause 0.5

                scene v10swhr8a
                with fade

                pause 0.5

                scene v10swhr8c
                with fade
                
                u "(Now that's what I'm talking about!)"

jump v10_call_with_lauren1
            




