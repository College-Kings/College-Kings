# SCENE 4: DREAM - VOID
# Locations: A dreamlike void filled with blackness, except for a fighting ring in the middle of nowhere
# Characters: MC (outfit 5), Penelope (Outfit 2), Riley (Outfit 1), Lauren (Outfit 2), Chris (Outfit 1), Imre (Outfit 3), Perry (No preset outfit suitable, use something that can be worn for a fight), Grayson (Outfit 2), Ryan (No preset outfit suitable, use something that can be worn for a fight), Caleb (No preset outfit suitable, use something that can be worn for a fight)
# Time: Tuesday night

### Extra audio files needed (Coded but commented for now) ###
# boo.mp3 - A group of guys booing, should be a short sound like this one https://elements.envato.com/male-group-booing-DTGZ89J
# spotlight.mp3 - Spotlight turning on. Something like this - https://elements.envato.com/spotlight-on-the-stage-Y75JH62
# suck_in_whoosh.mp3 - Something like the first part in this audio https://elements.envato.com/suck-in-whoosh-5VSEHLA (build up and then sudden stop)

label v9_dream:
play music "music/v9/Track Scene 4.mp3" fadein 2
play sound sound.swoosh

scene v9dream1 # TPP (camera from the front so the void is not fully visible yet). MC standing near an open door (as if he just entered it) behind which there is the black void, nervous, mouth closed
with dissolve
pause

scene v9dream2 # TPP. Show a shot of the dreamy empty void. There is nothing but blackness and maybe some random abstract artifacts type of stuff to make it more visually appealing. (The door should not be present in the following renders)
with dissolve
pause

scene v9dream3 # TPP (camera behind MC so we can see what he's looking at). (MC walked into the black void now) Show MC standing confused and anxious, mouth open (face may not be visible fully due to the angle but it's ok)
with dissolve
u "Hello? Anyone here?"
u "(Where is this place?)"

scene v9dream4 # TPP (maintain similar camera angle as v9dream3). Show MC walking in further, looking a bit nervous/anxious, mouth closed
with dissolve
pause 1

scene v9dream5 # TPP (maintain similar camera angle as v9dream3). Show MC standing (after walking in further), looking a bit nervous/anxious and shouting with his hands around his mouth
with dissolve
u "Hello!"

scene v9dream4
with dissolve
u "(Awesome!)"

scene v9dream5
with dissolve
u "I'M ALL ALONE IN HERE!"

play music "music/mhorror.mp3"
"I'm all alone in here...{w=1} {size=-5}I'm all alone in here...{/size}{w=1} {size=-10}I'm all alone in here...{/size}"

scene v9dream2
with dissolve
pause 1

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream6 # TPP. Same as v9dream2 except there is a well-lit fighting ring in the frame now
with hpunch
pause 0.5
u "Whoa!"

scene v9dream7 # TPP. Show MC climbing into the fighting ring
with dissolve
pause 0.7

scene v9dream8 # TPP. Show MC air-boxing confidently inside the ring, mouth closed
with dissolve
pause 1

scene v9dream8a # Different shot of MC air-boxing (maybe punching with the other hand)
with dissolve
pause 0.5

scene v9dream8
with dissolve
pause 1

if joinwolves:
    jump v9_dream_wolves
else:
    jump v9_dream_apes

label v9_dream_wolves:
show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream9 # TPP. Show Chris standing outside the boxing ring clapping for the MC smiling, looking proud, mouth open (similar to an FPP camera from MC's position but maybe a zoomed in a bit, the ring ropes can be seen in shot)
with hpunch
ch "Way to go man! You can do it!"

scene v9dream8
with dissolve
pause 1

scene v9dream8a
with dissolve
pause 0.5

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream9a # Same as v9dream9 but Imre cheering this time. Use a different posture though
with hpunch
imre "Wooo! Look at him go!"

# Punching faster
scene v9dream8
with dissolve
pause 0.5

scene v9dream8a
with dissolve
pause 0.25

scene v9dream8
with dissolve
pause 0.5

scene v9dream8a
with dissolve
pause 0.25

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream9b # Same as v9dream9 but Penelope cheering seductively this time. Use a different posture again
with hpunch
pe "Lookin' sexy [name]!"

scene v9dream8
with dissolve
pause 0.5

scene v9dream8a
with dissolve
pause 0.25

scene v9dream8b # Show MC raising his arms like he's the winner, confident smile, mouth closed
with dissolve
pause 2

$ renpy.music.set_volume(0.4, channel="sound")
# play sound "sounds/boo.mp3"
pause 0.5

scene v9dream8c # MC turned his head to look at someone unseen in the frame, looking confused and offended, mouth closed
with dissolve
u "(Huh?)"

$ renpy.music.set_volume(1, channel="sound")
# play sound "sounds/boo.mp3"

u "(Are they booing me? I'll show them.)"

# play sound "sounds/spotlight.mp3"

scene v9dream10 # TPP. A spotlight shines on MC, the rest of the scene gets relatively darker than before. MC looking confident with his fists up, mouth closed
with Dissolve(0.2)
u "(Now we're talking!)"

scene v9dream11 # FPP. Same as v9dream10 but in FPP. MC's fists can be seen in the frame
with dissolve
u "(Come on, [name], let's give 'em a good show.)"

scene v9dream9
with dissolve
ch "Who do you wanna fight [name]? Ryan or Caleb?"

menu:
    "Ryan":
        $ dreamFightChoice = "ryan"

        u "Ryan."

        scene v9dream11
        with dissolve
        pause 0.5

        show glitch
        play sound "sounds/glitch.mp3"
        pause 0.1
        hide glitch

        scene v9dream11a # Same as v9dream11 but Ryan standing in front of the MC now, looking confident, fists up, mouth closed
        with dissolve
        pause

        play sound sound.hit

        scene v9dream12 # TPP. Show MC punching Ryan in the ring. (It should be a weak punch and Ryan isn't too shaken by it)
        with hpunch
        pause 1

        # play sound "sounds/boo.mp3"

        scene v9dream13 # TPP. Close up shot of Chris (standing outside the ring like before) looking disappointed, mouth open
        with dissolve
        ch "Man, you call that a punch?"

        scene v9dream13a # Same as v9dream13 but this time it's Penelope laughing (as if making fun of you), mouth open
        with dissolve
        pe "My grandma can hit harder than that! *Laughs*"

        play sound sound.hit

        scene v9dream12a # Show Ryan punching MC back very hard
        with hpunch
        pause 1

        play sound "sounds/fall.mp3"

        scene v9dream12b # Show Ryan knocking the MC to the ground and locking him, MC in pain
        with hpunch
        pause 1

        scene v9dream13
        with dissolve
        ch "I told you guys we shouldn't have let him into the Wolves. He's gonna lose the whole thing for us."

        scene v9dream12c # Show MC fallen on the ground (ring's surface I mean), bleeding a little. Ryan hands raised, posing like the winner beside the MC, mouth closed
        with dissolve
        pause

    "Caleb":
        $ dreamFightChoice = "caleb"

        u "Caleb."

        scene v9dream11
        with dissolve
        pause 0.5

        show glitch
        play sound "sounds/glitch.mp3"
        pause 0.1
        hide glitch

        scene v9dream11b # Same as v9dream11a but instead of Ryan it's Caleb
        with dissolve
        pause

        play sound sound.hit

        scene v9dream14 # TPP (Use same camera as v9dream12. I used different frame numbering for ease of understanding). Same as v9dream12 but instead of Ryan, it's Caleb
        with hpunch
        pause 1

        # play sound "sounds/boo.mp3"

        scene v9dream13
        with dissolve
        ch "Man, you call that a punch?"

        scene v9dream13a
        with dissolve
        pe "My grandma can hit harder than that! *Laughs*"

        play sound sound.hit

        scene v9dream14a # Same as v9dream12a but instead of Ryan, it's Caleb
        with hpunch
        pause 1

        play sound "sounds/fall.mp3"

        scene v9dream14b # Same as v9dream12b but instead of Ryan, it's Caleb
        with hpunch
        pause 1

        scene v9dream13
        with dissolve
        ch "I told you guys we shouldn't have let him into the Wolves. He's gonna lose the whole thing for us."

        scene v9dream14c # Same as v9dream12c but instead of Ryan, it's Caleb
        with dissolve
        pause

pe "Never letting a pussy like that near mine."
u "(Fuck! Let's turn this mess around, [name]!)"

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream12d # Continuation of v9dream12c. Ryan now disappeared and MC (still bleeding) is trying to get up and stand (as if like a comeback after losing), looking angry but confident, mouth closed
with dissolve
pause

scene v9dream11
with dissolve
u "Who's next?"
"..."
u "I SAID WHO'S NEXT!?" with hpunch

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream13b # Same as v9dream13 but this time it's Lauren looking disappointed, mouth open
with dissolve
if CharacterService.is_girlfriend(lauren):
    la "You risked our relationship to join a fighting frat and you aren't even GOOD at it? What the hell?"
else:
    la "I'm so glad I didn't waste my time on you."

scene v9dream15 # TPP. Showing the MC hands to his head, screaming. He should be bleeding like in v9dream12c
with dissolve
u "(I don't like this dream anymore.)"
u "Wake up, [name]. WAKE UP!"

# play sound "sounds/suck_in_whoosh.mp3"
# pause n # (Pause length should be precisely the length of the above audio clip)
stop music

scene black
with Dissolve(0.1)
pause 1

jump v9_dream_wakeup

label v9_dream_apes:
show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream16 # TPP (Preferably use same camera as v9dream9. I used different frame numbering for ease of understanding). Same as v9dream9 but instead of Chris, it's Grayson clapping with a proud and arrogant smile, mouth open
with hpunch
gr "Way to go man! You can do it! I knew you were the right dude!"

scene v9dream8
with dissolve
pause 1

scene v9dream8a
with dissolve
pause 0.5

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream16a # Same as v9dream16 but Ryan cheering this time. Use a different posture though
with hpunch
ry "Wooo! Look at him go!"

# Punching faster
scene v9dream8
with dissolve
pause 0.5

scene v9dream8a
with dissolve
pause 0.25

scene v9dream8
with dissolve
pause 0.5

scene v9dream8a
with dissolve
pause 0.25

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream16b # Same as v9dream16 but Riley cheering seductively this time. Use a different posture again
with hpunch
ri "Lookin' sexy [name]!"

scene v9dream8
with dissolve
pause 0.5

scene v9dream8a
with dissolve
pause 0.25

scene v9dream8b
with dissolve
pause 2

$ renpy.music.set_volume(0.4, channel="sound")
# play sound "sounds/boo.mp3"
pause 0.5

scene v9dream8c
with dissolve
u "(Huh?)"

$ renpy.music.set_volume(1, channel="sound")
# play sound "sounds/boo.mp3"

u "(Are they booing me? I'll show them.)"

# play sound "sounds/spotlight.mp3"

scene v9dream10
with Dissolve(0.2)
u "(Now we're talking!)"

scene v9dream11
with dissolve
u "(Come on, [name], let's give 'em a good show.)"

scene v9dream16
with dissolve
gr "Whose ass you wanna beat [name]? Imre or Perry?"

menu:
    "Imre":
        $ dreamFightChoice = "imre"

        u "Imre."

        scene v9dream11
        with dissolve
        pause 0.5

        show glitch
        play sound "sounds/glitch.mp3"
        pause 0.1
        hide glitch

        scene v9dream11c # Same as v9dream11a but instead of Ryan it's Imre
        with dissolve
        pause

        play sound sound.hit

        scene v9dream17 # TPP (Use same camera as v9dream12. I used different frame numbering for ease of understanding). Same as v9dream12 but instead of Ryan, it's Imre
        with hpunch
        pause 1

        # play sound "sounds/boo.mp3"

        scene v9dream13c # Same as v9dream13 but this time it's Grayson looking disappointed, angry, mouth open
        with dissolve
        gr "Man, you call that a punch?"

        scene v9dream13d # Same as v9dream13a but instead of Penelope, it's Riley
        with dissolve
        ri "My grandma can hit harder than that! *Laughs*"

        play sound sound.hit

        scene v9dream17a # Same as v9dream12a but instead of Ryan, it's Imre
        with hpunch
        pause 1

        play sound "sounds/fall.mp3"

        scene v9dream17b # Same as v9dream12b but instead of Ryan, it's Imre
        with hpunch
        pause 1

        scene v9dream13c
        with dissolve
        gr "I made a huge mistake letting this guy into the Apes. He's gonna lose the whole thing for us."

        scene v9dream17c # Same as v9dream12c but instead of Ryan, it's Imre
        with dissolve
        pause

    "Perry":
        $ dreamFightChoice = "perry"

        u "Perry."

        scene v9dream11
        with dissolve
        pause 0.5

        show glitch
        play sound "sounds/glitch.mp3"
        pause 0.1
        hide glitch

        scene v9dream11d # Same as v9dream11a but instead of Ryan it's Perry
        with dissolve
        pause

        play sound sound.hit

        scene v9dream18 # TPP (Use same camera as v9dream12. I used different frame numbering for ease of understanding). Same as v9dream12 but instead of Ryan, it's Perry
        with hpunch
        pause 1

        # play sound "sounds/boo.mp3"

        scene v9dream13c
        with dissolve
        gr "Man, you call that a punch?"

        scene v9dream13d
        with dissolve
        ri "My grandma can hit harder than that! *Laughs*"

        play sound sound.hit

        scene v9dream18a # Same as v9dream12a but instead of Ryan, it's Perry
        with hpunch
        pause 1

        play sound "sounds/fall.mp3"

        scene v9dream18b # Same as v9dream12b but instead of Ryan, it's Perry
        with hpunch
        pause 1

        scene v9dream13c
        with dissolve
        gr "I made a huge mistake letting this guy into the Apes. He's gonna lose the whole thing for us."

        scene v9dream18c # Same as v9dream12c but instead of Ryan, it's Perry
        with dissolve
        pause

ri "Never letting a pussy like that near mine."
u "(Fuck! Let's turn this mess around, [name]!)"

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream12d
with dissolve
pause

scene v9dream11
with dissolve
u "Who's next?"
"..."
u "I SAID WHO'S NEXT!?" with hpunch

show glitch
play sound "sounds/glitch.mp3"
pause 0.1
hide glitch

scene v9dream13b
with dissolve
if CharacterService.is_girlfriend(lauren):
    la "You risked our relationship to join a fighting frat and you aren't even GOOD at it? What the hell?"
else:
    la "I'm so glad I didn't waste my time on you."

scene v9dream15
with dissolve
u "(I don't like this dream anymore.)"
u "Wake up, [name]. WAKE UP!"

# play sound "sounds/suck_in_whoosh.mp3"
# $ renpy.pause(renpy.music.get_duration(channel="sound")) 
stop music fadeout 3

# scene black
# with Dissolve(0.1)
# pause 1

jump v9_dream_wakeup
