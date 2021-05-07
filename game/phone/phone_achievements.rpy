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

    ## ACHIEVEMENT ITEMS HERE
    Achievement("open wound", "Tell off Emily", "openwound")
    Achievement("no hard feelings", "Play nice with Emily", "nohardfeelings")
    Achievement("keep it moving", "Hit on Nora", "keepitmoving")
    Achievement("romeo", "Kiss Lauren", "romeo")
    Achievement("big mouth", "Threaten Cameron", "bigmouth")
    Achievement("mixed feelings", "Decline Lauren", "mixedfeelings")
    Achievement("the notorious", "Win your first fight", "thenotorious")
    Achievement("a new beginning", "Lauren likes you", "anewbeginning")
    Achievement("over it", "Let Benjamin make a move", "overit")
    Achievement("not now, mom", "Decline Julia's call", "notnowmom")
    Achievement("lips don't lie", "Kiss Riley in the Park", "lipsdontlie")
    Achievement("truth hurts", "Tell Lauren about Aubrey", "truthhurts")
    Achievement("relight the fire", "Tell Julia about Emily", "relightthefire")
    Achievement("rematch", "Buy Chloe the volleyball", "rematch")
    Achievement("keen eye", "Pick the muffin", "keeneye")
    Achievement("on the low", "Deny PDA with Lauren", "onthelow")
    Achievement("peta public enemy", "Kill dog as animal lover", "petapublicenemy")
    Achievement("snitch", "Tell the school", "snitch")
    Achievement("bros before hoes", "Help Imre", "brosbeforehoes")
    Achievement("monkey business", "Join the Apes", "monkeybusiness")
    Achievement("not my business", "Don't disturb Ms. Rose", "notmybusiness")
    Achievement("reignition", "Kiss Emily back", "reignition")
    Achievement("credulous", "Trust Chloe", "credulous")
    Achievement("seems fishy", "Don't meet Grayson", "seemsfishy")
    Achievement("strike", "Kiss Penelope", "strike")
    Achievement("get a room", "Sleep With Amber at Josh's", "get_a_room")
    Achievement("ip man", "Win The Alley Fight", "ip_man")
    Achievement("thick and thin", "Help Penelope", "thick_and_thin")
    Achievement("up for more", "Flirt With Chloe", "up_for_more")

screen achievements():
    tag phoneTag
    
    use phoneTemplate:

        add "phone/images/whiteBackground.webp" at truecenter

        text "achievements":
            color "#000000"
            font "fonts/Freshman.ttf"
            size 45
            ypos 200
            xalign 0.5

        vpgrid:
            cols 1
            spacing 10
            pos (780, 280)
            xysize (358, 600)
            mousewheel True
            draggable True

            for achievement in achievements:
                if achievement.checkCondition():
                    vbox:
                        spacing -10
                        
                        textbutton achievement.achievement style "ach"
                        textbutton achievement.text style "ach2"
                else:
                    textbutton achievement.achievement style "ach3"