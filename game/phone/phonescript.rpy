default msgApp = Application("Messages", "images/messagesicon.png", "contactsscreen")
default statsApp = Application("Stats", "images/statsicon.png", "stats", locked=True)
default achApp = Application("Achievements", "images/achicon.png", "achievements")
default kiwiiApp = Application("Kiwii", "images/Phone/Kiwii/AppAssets/kiwii.png", "kiwiiApp", locked=True)

default contact_Emily = Contact("Emily", "emilyprofilepic", locked=False)
default contact_Lauren = Contact("Lauren", "laurenprofilepic")
default contact_Julia = Contact("Julia", "juliaprofilepic")
default contact_Ryan = Contact("Ryan", "ryanprofilepic")
default contact_Josh = Contact("Josh", "joshprofilepic")
default contact_Aubrey = Contact("Aubrey", "aubreyprofilepic")
default contact_Chloe = Contact("Chloe", "chloeprofilepic")
default contact_Evelyn = Contact("Evelyn", "evelynprofilepic")
default contact_Amber = Contact("Amber", "amberprofilepic")
default contact_Penelope = Contact("Penelope", "penelopeprofilepic")
default contact_Riley = Contact("Riley", "rileyprofilepic")
default contact_Autumn = Contact("Autumn", "autumnprofilepic")

# Autumn
default autumnMessage1 = Message(contact_Autumn, "Hey, it's Autumn.")
default autumnMessage2 = Message(contact_Autumn, "I'm just about to start making signs. Do you still want to join?")
default autumnMessage3 = Message(contact_Autumn, "Great. I'm at the Deer's House. Do you know how to get there?")
default autumnMessage4 = Message(contact_Autumn, "Alright, see you soon.")

# Riley
default rileyMessage1 = Message(contact_Riley, "Are you and Emily back together?")
default rileyMessage2 = Message(contact_Riley, "Check Kiwii...")
default rileyMessage3 = Message(contact_Riley, "")
default rileyMessage4 = Message(contact_Riley, "Okay... just looked like it")
default rileyMessage5 = Message(contact_Riley, "k")
default rileyMessage6 = Message(contact_Riley, "Hey, how come you're not on Kiwii?")
default rileyMessage7 = Message(contact_Riley, "It's a new social media app, you should give it a try")
default rileyMessage8 = Message(contact_Riley, "Wanna come over? ;)")
default rileyMessage9 = Message(contact_Riley, "Yayyy")
default rileyMessage10 = Message(contact_Riley, "Oh oki")


#Emily
default emilyMessage1 = Message(contact_Emily, "Hey...\nI know we haven’t talked much after we broke up, but I just wanted to let you know that I didn’t get into Stanford, so I’ll be going to San Vallejo as well.\nGuess I’ll see you there. :)")
default emilyMessage2a = Message(contact_Emily, "Cool :)")
default emilyMessage2b = Message(contact_Emily, "Ugh :/")
default emilyMessage3 = Message(contact_Emily, "")
default emilyMessage4 = Message(contact_Emily, "It's okay. You'll get the surprise another time...")

#Lauren
default laurenMessage0 = Message(contact_Lauren, "")
default laurenMessage1 = Message(contact_Lauren, "Yeah sounds good :) Where do you wanna meet?")
default laurenMessage2 = Message(contact_Lauren, "Okay, will do")

default laurenMessage4 = Message(contact_Lauren, "Hey :)\nSorry about today.\n\nCan we talk tomorrow?")
default laurenMessage5a = Message(contact_Lauren, "Cool :)")
default laurenMessage5b = Message(contact_Lauren, "Idk, it's just feels kinda weird now. Can we please just talk tomorrow?")
default laurenMessage6 = Message(contact_Lauren, ":)")

default laurenMessage8a = Message(contact_Lauren, "Are we still on for today? :)")
default laurenMessage8b = Message(contact_Lauren, "Hello?? Can we please talk today?")
default laurenMessage9 = Message(contact_Lauren, "Is everything okay?") # Edited
default laurenMessage10 = Message(contact_Lauren, "Okay...")
default laurenMessage11 = Message(contact_Lauren, "Great, I'll see you then :)")

default laurenMessage12 = Message(contact_Lauren, "Hey")
default laurenMessage13 = Message(contact_Lauren, "Wanna do the personality tests today at noon?")
default laurenMessage14 = Message(contact_Lauren, "Great :) Meet me at our economics' classroom.")

default laurenMessage15 = Message(contact_Lauren, "I saw what Emily posted. I really thought you liked me...")
default laurenMessage16 = Message(contact_Lauren, "I guess we're done now, so please just delete my number.")
default laurenMessage17 = Message(contact_Lauren, "What is there to talk about? How could you betray me like that?!")
default laurenMessage18 = Message(contact_Lauren, "Fine. I'm in my dorm, we can talk now.")

default laurenMessage19 = Message(contact_Lauren, "Wanna go now?")
default laurenMessage20 = Message(contact_Lauren, "Wanna go now babe?")
default laurenMessage21 = Message(contact_Lauren, "Hey :)")
default laurenMessage22 = Message(contact_Lauren, "You wanna go to the beach today?")
default laurenMessage23 = Message(contact_Lauren, "How about now?")
default laurenMessage24 = Message(contact_Lauren, "Great :)")
default laurenMessage25 = Message(contact_Lauren, "You wanna go to the beach today?")
default laurenMessage26 = Message(contact_Lauren, "Oh okay, another time then.")


#Julia
default juliaMessage1 = Message(contact_Julia, "Hey honey,\nenjoy your time in college.\nStay safe and don't forget to visit me.\nLove you")
#Ryan
default ryanMessage1 = Message(contact_Ryan, "Hey man, it's Ryan.\nThe Apes' rush party is tonight at 9. You're coming, right???")
default ryanMessage2 = Message(contact_Ryan, "Haha, trust me, you're not gonna want to leave once you see all the hot chicks there.")
default ryanMessage3 = Message(contact_Ryan, "Just meet me in front of the Apes' frat house at 9.")
default ryanMessage4 = Message(contact_Ryan, "You okay?")
default ryanMessage5 = Message(contact_Ryan, "Look, I know what Grayson did was a dick move, but he was just being overprotective of Chloe")
default ryanMessage6 = Message(contact_Ryan, "Sorry...")
default ryanMessage7 = Message(contact_Ryan, "Wish I could land a girl like Emily lol")
default ryanMessage8 = Message(contact_Ryan, "She's a straight hottie!")
#Josh
default joshMessage1 = Message(contact_Josh, "Dude, I talked to this Aubrey chick the entire night and guess who's number she wanted...")
default joshMessage2 = Message(contact_Josh, "YOURS")
default joshMessage3 = Message(contact_Josh, "What a bitch...")
default joshMessage4 = Message(contact_Josh, "It's fine, you go get her.")
default joshMessage5 = Message(contact_Josh, "Nah, you don't want a bitch like her.")
default joshMessage6 = Message(contact_Josh, "Hahaha, I'm just kidding, yo.")
default joshMessage7 = Message(contact_Josh,"Of course I gave her your number.")

default joshMessage8 = Message(contact_Josh, "Hey man, you wanna hang out with me and some friends tonight?")
default joshMessage9 = Message(contact_Josh, "Dope")
default joshMessage10 = Message(contact_Josh, "Come by 995 Sereno Drive at 8, it's my friends house.")
default joshMessage11 = Message(contact_Josh, "Aww, come on. You'll be back by 11.")
default joshMessage12a = ImageMessage(contact_Josh, "images/text1.jpg")
default joshMessage12 = Message(contact_Josh, "I told my friend Amber about you and she really wants to meet you.")
default joshMessage13 = Message(contact_Josh, "Remember how you told me in high school that you felt like you always missed out on all the crazy stories?")
default joshMessage14 = Message(contact_Josh, "Don't miss out now.")
default joshMessage15 = Message(contact_Josh, "This guy")
#Aubrey
default aubreyMessage1 = Message(contact_Aubrey, "Hey,\nJosh gave me your number\n\nI hope your face is feeling better after the shit that Grayson pulled...")
default aubreyMessage2 = Message(contact_Aubrey, "He's not even dating Chloe and you guys didn't even do anything so I don't know what he was thinking.\n\nAnyway, do you wanna like... hang out tomorrow?")
default aubreyMessage3 = Message(contact_Aubrey,"Yeah, I mean they had a thing a while ago but she broke it off 'cause he lied about some shit.")
default aubreyMessage4 = Message(contact_Aubrey,"So... tomorrow?")
default aubreyMessage5 = Message(contact_Aubrey,"I've got dance practice tonight :(")
default aubreyMessage7 = Message(contact_Aubrey,"Oh wow, that's spontaneous, I like it haha.\n\nI guess come to the Chicks' house whenever you're ready and then we can go costume shopping.")

default aubreyMessage8 = Message(contact_Aubrey, "Hey, are you nearby?")
default aubreyMessage9 = Message(contact_Aubrey, "Oh, okay. Guess we'll have to postpone the costume buying.")
default aubreyMessage10 = Message(contact_Aubrey,"Good :)")

# if costumeaubrey == True: # did you meet aubrey?

# if caughtpeekingaubrey == True:
# if caughtpeekingaubreycounter  == True:
default aubreyMessage11 = Message(contact_Aubrey,  "I wanna talk about what happened yesterday.")
default aubreyMessage12 = Message(contact_Aubrey, "Any chance that you could come over now?")
default aubreyMessage13 = Message(contact_Aubrey, "My room has a window facing the backyard. Can you climb in through there? I'll leave it open.")
default aubreyMessage14 = Message(contact_Aubrey, "I'd prefer if none of the girls saw you.")
# else:
default aubreyMessage11a = Message(contact_Aubrey,  "Hey, I really need your help.")
default aubreyMessage12a = Message(contact_Aubrey, "Any chance that you could come over now?")
default aubreyMessage13a = Message(contact_Aubrey, "My room has a window facing the backyard. Can you climb in through there instead of using the front door?")
default aubreyMessage14a = Message(contact_Aubrey, "I'll leave it open.")
# else:
default aubreyMessage11b = Message(contact_Aubrey, "Hey, you know how you had to cancel on me yesterday and you really want to make it up to me?")
default aubreyMessage12b = Message(contact_Aubrey, "Wanna come over now?")
default aubreyMessage13b = Message(contact_Aubrey, "My room has a window facing the backyard. Can you climb in through there instead of using the front door?")
default aubreyMessage14b = Message(contact_Aubrey, "I'll leave it open.")

default aubreyMessage16 = Message(contact_Aubrey, "Hey, I know it's late... but wanna come over?")
default aubreyMessage17 = Message(contact_Aubrey, ":)")
default aubreyMessage18 = Message(contact_Aubrey, "Oh, okay")

default aubreyMessage19b = ImageMessage(contact_Aubrey, "images/text3.jpg")
default aubreyMessage19 = Message(contact_Aubrey, "Still shaking from earlier")
default aubreyMessage19a = Message(contact_Aubrey, "You missed out today")


#Chloe

default chloeMessage1 = Message(contact_Chloe,"")
default chloeMessage3 = Message(contact_Chloe,"I'm really busy today, but I could do tonight after 11 or so.")
default chloeMessage4 = Message(contact_Chloe,"Sounds good :)")

default chloeMessage4a = Message(contact_Chloe, "I got some free time right now :)")
default chloeMessage5 = Message(contact_Chloe, "Wanna go swimming?")
default chloeMessage6 = Message(contact_Chloe, "I'm busy later tonight and I'm pretty much booked for the entire week :/")

default chloeMessage6a = Message(contact_Chloe,"")
default chloeMessage7 = Message(contact_Chloe, "That's what I like to hear :*")
default chloeMessage8 = Message(contact_Chloe, "Meet me at the school's swimming pool")

default chloeMessage9 = Message(contact_Chloe, "I guess we'll do it another time...")
default chloeMessage10 = Message(contact_Chloe, "Okay.")
#Amber
# if kissamber == True:
default amberMessage1 = Message(contact_Amber,"Hey, it's Amber")
default amberMessage2 = Message(contact_Amber,"Josh gave me your number")
default amberMessage3 = Message(contact_Amber, "You know, you never came back, I thought we were having a good time xx")
default amberMessage4 = Message(contact_Amber,"Oh really? How are you gonna do that?")
default amberMessage5 = Message(contact_Amber, "Oh okay, hope everything's okay xx")
default amberMessage6 = Message(contact_Amber,"That does sound enticing ;)")
default amberMessage7 = Message(contact_Amber,"Deal xx")

# else:

# if jorep14 == 2:
default amberMessage1a = Message(contact_Amber,"Hey, it's Amber")
default amberMessage2a = Message(contact_Amber,"Josh gave me your number")
default amberMessage3a = Message(contact_Amber, "How come you didn't show up yesterday? Everything okay? xx")
default amberMessage4a = Message(contact_Amber,"Oh wow, I was just checking. :P")
default amberMessage5a = Message(contact_Amber, "Oh okay, hope you're good xx")
default amberMessage6a = Message(contact_Amber,"Was hoping xx")
default amberMessage7a = Message(contact_Amber,"That's good xx")

# else:
default amberMessage1b = Message(contact_Amber,"Hey, it's Amber")
default amberMessage2b = Message(contact_Amber,"Josh gave me your number")
default amberMessage3b = Message(contact_Amber, "You know, you never came back, everything okay?")
default amberMessage4b = Message(contact_Amber,"Oh shut up, I was just checking in")
default amberMessage5b = Message(contact_Amber, "Oh okay, hope you're good xx")
default amberMessage6b = Message(contact_Amber,"Was hoping xx")
default amberMessage7b = Message(contact_Amber,"That's good xx")

default amberMessage8 = Message(contact_Amber, "Hey, you alone? xx")
default amberMessage9 = Message(contact_Amber, "Go somewhere where you're completely alone xx")
default amberMessage10 = Message(contact_Amber, "I got a surprise for you ;)")

default amberMessage11a = Message(contact_Amber,"")
default amberMessage12 = ImageMessage(contact_Amber, "images/text2.jpg")
default amberMessage13 = Message(contact_Amber, "I'm playing drink or dare and got dared to send an underwear pic to a guy.")
default amberMessage14 = Message(contact_Amber, "Maybe I picked someone at random ;)")
default amberMessage15 = Message(contact_Amber, "Maybe if you're lucky xx")
default amberMessage16 = Message(contact_Amber, "I'm glad you like it xx")

default amberMessage17 = Message(contact_Amber, "I guess you didn't want my surprise :/")
default amberMessage18 = Message(contact_Amber,"")
default amberMessage19 = Message(contact_Amber, "Moment's passed...")
default amberMessage20 = Message(contact_Amber, "You better xx")

default amberMessage21 = Message(contact_Amber, "Hey, you alone? xx")

default amberMessage22 = Message(contact_Amber,"Heyy, what are you up to? xx")
default amberMessage23 = Message(contact_Amber, "Going to my next lecture x_x")
default amberMessage24 = Message(contact_Amber, "Which gym do you go to? Maybe we can go together at some point")
default amberMessage25 = Message(contact_Amber, "Awww I'm SV Fitness :(")
default amberMessage26 = Message(contact_Amber, "Yeah maybe we should xx")
#penelope
default penelopeMessage0 = Message(contact_Penelope, "")
default penelopeMessage1 = Message(contact_Penelope,"Yeah, sounds good :)")
default penelopeMessage2 = Message(contact_Penelope,"I have a lecture at 2:30 but I can go straight to the bowling alley afterwards")
default penelopeMessage3 = Message(contact_Penelope,"Meet there at 4?")
default penelopeMessage4 = Message(contact_Penelope,"I didn't know you and Emily were a thing...")
default penelopeMessage5 = Message(contact_Penelope,"Okay...")
