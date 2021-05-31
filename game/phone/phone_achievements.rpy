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