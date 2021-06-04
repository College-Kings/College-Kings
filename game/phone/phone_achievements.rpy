init python:
    achievements = []

    class Achievement:
        def __init__(self, achieve, text, condition):
            self.achieve = achieve
            self.text = text
            self.condition = condition

            achievements.append(self)

            # Add achievements to renpy/steam
            achievement.register(achieve.replace(" ", "_"))
            achievement.sync()

        def checkCondition(self):
            return getattr(store, self.condition)

# ACHIEVEMENT ITEMS HERE
    # v1.0
    Achievement("open wound", "Tell off Emily", "openwound")
    Achievement("no hard feelings", "Play nice with Emily", "nohardfeelings")
    Achievement("keep it moving", "Hit on Nora", "keepitmoving")
    Achievement("romeo", "Kiss Lauren", "romeo")
    Achievement("big mouth", "Threaten Cameron", "bigmouth")

    # v2.0
    Achievement("mixed feelings", "Decline Lauren", "mixedfeelings")
    Achievement("the notorious", "Win your first fight", "thenotorious")
    Achievement("a new beginning", "Lauren likes you", "anewbeginning")
    Achievement("over it", "Let Benjamin make a move", "overit")

    # v3.0
    Achievement("not now, mom", "Decline Julia's call", "notnowmom")
    Achievement("lips don't lie", "Kiss Riley in the Park", "lipsdontlie")
    Achievement("truth hurts", "Tell Lauren about Aubrey", "truthhurts")

    # v4.0
    Achievement("relight the fire", "Tell Julia about Emily", "relightthefire")
    Achievement("rematch", "Buy Chloe the volleyball", "rematch")
    Achievement("keen eye", "Pick the muffin", "keeneye")
    
    # v5.0
    Achievement("on the low", "Deny PDA with Lauren", "onthelow")
    Achievement("peta public enemy", "Kill dog as animal lover", "petapublicenemy")
    Achievement("snitch", "Tell the school", "snitch")

    # v6.0
    Achievement("bros before hoes", "Help Imre", "brosbeforehoes")
    Achievement("monkey business", "Join the Apes", "monkeybusiness")
    Achievement("not my business", "Don't disturb Ms. Rose", "notmybusiness")
    Achievement("reignition", "Kiss Emily back", "reignition")
    Achievement("credulous", "Trust Chloe", "credulous")
    Achievement("seems fishy", "Don't meet Grayson", "seemsfishy")
    Achievement("strike", "Kiss Penelope", "strike")

    # v7.0
    Achievement("true to self", "Walk home with Riley", "truetoself")
    Achievement("silverback", "Pledge to the Apes", "silverback")
    Achievement("wolfpack", "Pledge to the Wolves", "wolfpack")
    Achievement("lee way", "Pull down Mr. Lee's pants", "leeway")
    Achievement("ecstatic", "Bunk homecoming with Amber", "ecstatic")
    Achievement("slow and steady", "End homecoming with Lauren", "slowandsteady")
    Achievement("playing with fire", "End homecoming with Riley", "playingwithfire")
    Achievement("homecoming queen", "End homecoming with Chloe", "homecomingqueen")
    
    # v8.0
    Achievement("get a room", "Stay With Amber at Josh's", "get_a_room")
    Achievement("ip man", "Win The Alley Fight", "ip_man")
    Achievement("thick and thin", "Help Penelope", "thick_and_thin")
    Achievement("up for more", "Flirt With Chloe", "up_for_more")
    Achievement("text with an s", "Return to sender", "text_with_an_s") #m
    Achievement("lucky 7", "Flashing lights at the arcade", "lucky_7") #m
    Achievement("helping hand", "Help Nora hand out flyers for the trip", "helping_hand") #m

    # v9.0
    Achievement("back down", "Punch the guy in the hallway", "down_for_the_count")
    Achievement("second date", "Get a second date with Evelyn", "second_date")
    Achievement("relaxing day", "Have fun with Aubrey at the lake", "lake_hj")
    #Achievement("the king", "Recognise the king", "the_king")
    Achievement("king of the north", "The King is heading North", "king_of_the_north") #m
    Achievement("cheat day", "Skip the gym and get with Riley"), "cheat_day") #m
    Achievement("the wrong time", "Don't kiss Lindsey", "the_wrong_time")

    # v10.0
    #Achievement("friends first", "Refuse to fight a friend", "friends_first")
    Achievement("fright club", "Don't fight Ryan at the Brawl", "fright_club") #m
    Achievement("bros before blows", "Don't fight Imre at the Brawl", "bros_before_blows") #m
    Achievement("goldenboy", "Beat Imre on Hard difficulty at the Brawl", "goldenboy") #m
    Achievement("lights out", "Beat Ryan on Hard difficulty at the Brawl", "lights_out") #m
    Achievement("rough rider", "Have fun at the skatepark", "rough_rider") #m
    Achievement("family secrets", "Find out Nora and Ms. Rose are family", "family_secrets") #m
    Achievement("getting clean", "Have fun in the bathroom", "bathroom_sex")
    Achievement("forbidden romance", "Kiss Ms. Rose", "kiss_teacher")
    Achievement("hard decisions", "Tell Chloe what Nora said", "chloe_over_nora")
    Achievement("rawr im a lion!", "Tell Lauren you like Lions", "im_a_lion")
    Achievement("on the court", "Have a rematch with Chloe", "on_the_court")

screen achievements():
    tag phoneTag
    zorder 200
    
    use phoneTemplate:

        add "images/phone/whiteBackground.webp" at truecenter

        text "achievements":
            color "#000000"
            font "fonts/Freshman.ttf"
            size 45
            ypos 200
            xalign 0.5

        viewport:
            pos (780, 280)
            xysize (358, 600)
            mousewheel True
            draggable True

            vbox:
                spacing 10
                
                for achievement in achievements:
                    if achievement.checkCondition():
                        vbox:
                            spacing -10
                            
                            textbutton achievement.achieve style "ach"
                            textbutton achievement.text style "ach2"
                    else:
                        textbutton achievement.achieve style "ach3"
