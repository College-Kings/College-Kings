init python:

    class KiwiiPost:
        def __init__(self, user, image, caption="", mentions=None, numberLikes=0, liked=False, comments=None, seen=False):
            self.user = user
            self.image = image

            if not mentions: self.mentions = []
            elif isinstance(mentions, str): self.mentions = [mentions]
            else: self.mentions = mentions

            self.caption = caption
            self.numberLikes = numberLikes
            self.liked = liked

            if comments == None: self.comments = []
            else: self.comments = comments

            self.seen = seen
            self.replies = []

            self.getUsername()
            self.getProfilePicture()

            kiwiiPosts.append(self)

        def toggleLike(self):
            if self.liked:
                self.liked = False
                self.numberLikes -= 1
            else:
                self.liked = True
                self.numberLikes += 1

        def addComment(self, user, text, numberLikes=0, liked=False, mentions=None):
            comment = KiwiiComment(user, text, numberLikes, liked, mentions)
            if comment not in self.comments:
                self.comments.append(comment)

        def addReply(self, reply, label, numberLikes=0, mentions=None):
            reply = KiwiiReply(reply, label, numberLikes, mentions)
            if reply not in self.replies:
                self.replies.append(reply)

        def getUsername(self):
            self.username = kiwiiUsers[self.user]["username"]
            return self.username

        def getProfilePicture(self):
            self.profilePicture = kiwiiUsers[self.user]["profilePicture"]
            return self.profilePicture

        def getCaption(self):
            usernames = [kiwiiUsers[mention]["username"] for mention in self.mentions]

            rv = ", @".join(usernames)
            if usernames: rv = "{{color=#3498DB}}{{b}}@{users}{{/b}}{{/color}} {text}".format(users=rv, text=self.caption)
            else: rv = self.caption
            return str(rv)

        def seenPost(self):
            self.seen = True

        def hidePost(self):
            self.index = kiwiiPosts.index(self)
            kiwiiPosts.remove(self)

    class KiwiiComment(KiwiiPost):
        def __init__(self, user, text, numberLikes=0, liked=False, mentions=None):
            self.user = user
            self.text = text

            if not mentions: self.mentions = []
            elif isinstance(mentions, str): self.mentions = [mentions]
            else: self.mentions = mentions

            self.numberLikes = numberLikes
            self.liked = liked
            self.getUsername()
            self.getProfilePicture()

        def getText(self):
            usernames = [kiwiiUsers[mention]["username"] for mention in self.mentions]

            rv = ", @".join(usernames)
            if usernames: rv = "{{color=#3498DB}}{{b}}@{users}{{/b}}{{/color}} {text}".format(users=rv, text=self.text)
            else: rv = self.text
            return str(rv)

    class KiwiiReply(KiwiiComment):
        def __init__(self, reply, label, numberLikes=0, mentions=None):
            self.reply = reply
            self.label = label

            if not mentions: self.mentions = []
            elif isinstance(mentions, str): self.mentions = [mentions]
            else: self.mentions = mentions


            if kct == "popular": self.numberLikes = int(round(numberLikes * 1.5))
            elif kct == "loyal": self.numberLikes = int(round(numberLikes * 1.0))
            else: self.numberLikes = int(round(numberLikes * 1.2))

        def selectedReply(self, kiwiiPost):
            kiwiiPost.addComment("MC", self.reply, self.numberLikes, mentions=self.mentions)
            kiwiiPost.replies = []


    def totalLikes():
        rv = 0

        for post in kiwiiPosts:
            for comment in post.comments:
                if comment.user == "MC":
                    rv += comment.numberLikes
            if post.user == "MC":
                rv += comment.numberLikes

        return rv


init -1:
    define profilePictures = [ "images/Phone/Kiwii/Profile Pictures/mcpp1.png", "images/Phone/Kiwii/Profile Pictures/mcpp2.png", "images/Phone/Kiwii/Profile Pictures/mcpp3.png", "images/Phone/Kiwii/Profile Pictures/mcpp4.png" ]
    default count = 0

    default kiwiiPosts = []
    default liked_kiwiPosts = []
    default kiwiiUsers = {
            "Adam": {
                "username": "A.D.A.M.",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/adpp.png"
            },
            "Imre": {
                "username": "BadBoyImre",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/impp.png"
            },
            "Mason": {
                "username": "Mason_Mas",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/masonpp.png"
            },
            "Ryan": {
                "username": "Ryanator",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/rypp.png"
            },
            "Cameron": {
                "username": "Cameroon",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/capp.png"
            },
            "Chris": {
                "username": "Chriscuit",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/chpp.png"
            },
            "Elijah": {
                "username": "Elijah_Woods",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/elpp.png"
            },
            "Grayson": {
                "username": "G-rayson",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/grpp.png"
            },
            "Josh": {
                "username": "Josh80085",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/jopp.png"
            },
            "Aubrey": {
                "username": "Aubs123",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/aupp.png"
            },
            "Amber": {
                "username": "Amber_xx",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/ampp.png"
            },
            "Kim": {
                "username": "KimPlausible",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/kimpp.png"
            },
            "Nora": {
                "username": "Nora_12",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/nopp.png"
            },
            "Penelope": {
                "username": "Penelopeeps",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/pepp.png"
            },
            "Lauren": {
                "username": "LoLoLauren",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/lapp.png"
            },
            "Autumn": {
                "username": "Its_Fall",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/autpp.png"
            },
            "Riley": {
                "username": "RileyReads",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/ripp.png"
            },
            "Emily": {
                "username": "emilyyyy",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/empp.png"
            },
            "Chloe": {
                "username": "Chloe101",
                "profilePicture": "images/Phone/Kiwii/Profile Pictures/clpp.png"
            },
            "MC": {
                "username": "MC",
                "profilePicture": profilePictures[0]
            }
        }

screen kiwiiTemplate():
    use phoneTemplate:
        add Transform("images/Phone/Kiwii/AppAssets/Background.jpg", size=(376, 744)) at truecenter

        transclude

        button:
            xysize(56, 55)
            pos (932, 845)
            action Show("kiwiiApp")

        button:
            xysize(30, 30)
            pos (1023, 870)
            action Show("liked_kiwii")

        button:
            xysize(30, 30)
            pos (1085, 870)
            action Show("kiwiiPreferences")

        button:
            xysize(30, 30)
            pos (1086, 220)
            action Show("contactsscreen")

        button:
            xysize(30, 30)
            pos (800, 870)
            action Show("kiwiiApp")

screen kiwiiPreferences():
    tag phoneTag

    $ kiwiiUsers["MC"]["profilePicture"] = profilePictures[count]

    use kiwiiTemplate:

        add Transform(kiwiiUsers["MC"]["profilePicture"], zoom=0.2) align(0.5, 0.3)

        hbox:
            spacing 50
            align(0.5, 0.48)

            textbutton "<":
                if count > 0:
                    action SetVariable("count", count - 1)
                text_style "kiwii_PrefTextButton"

            textbutton ">":
                if count + 1 < len(profilePictures):
                    action SetVariable("count", count + 1)
                text_style "kiwii_PrefTextButton"

        vbox:
            align (0.5, 0.58)

            text "Username:" style "kiwii_ProfileName" xalign 0.5
            input:
                value DictInputValue(kiwiiUsers["MC"], "username")
                default kiwiiUsers["MC"]["username"]
                length 15
                color "#006400"
                outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]
        vbox:
            align (0.5, 0.7)
            spacing 3

            text "Total Likes:" style "kiwii_ProfileName" at truecenter
            text str(totalLikes()) at truecenter:
                color "#006400"
                outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]



screen kiwiiApp():
    tag phoneTag

    python:
        for post in kiwiiPosts:
            post.seenPost()

    use kiwiiTemplate:

        vpgrid:
            cols 1
            mousewheel True
            draggable True
            xysize(350, 575)
            xalign 0.5
            ypos 265
            spacing 10

            for post in reversed(kiwiiPosts):
                fixed:
                    xysize (350, 350)
                    add "images/Phone/Kiwii/AppAssets/Post.png"

                    hbox:
                        spacing 10
                        xoffset 20
                        yoffset 20

                        add Transform(post.getProfilePicture(), zoom=0.05)
                        text post.getUsername() style "kiwii_ProfileName" yalign 0.5

                    vbox:
                        align(0.5, 0.5)
                        yoffset 18
                        spacing 5

                        imagebutton:
                            idle Transform(post.image, zoom=0.17)
                            action Show("kiwii_image", img=post.image)
                        text post.getCaption() style "kiwii_CommentText" xalign 0.5

                    hbox:
                        xoffset 20
                        yoffset 220
                        spacing 5

                        imagebutton:
                            idle "images/Phone/Kiwii/AppAssets/Like.png"
                            hover "images/Phone/Kiwii/AppAssets/LikePress.png"
                            selected_idle "images/Phone/Kiwii/AppAssets/LikePress.png"
                            selected post.liked
                            action Function(post.toggleLike)
                        frame:
                            background "#fff"
                            yalign 0.5
                            padding (5, 2)

                            text "{}".format(post.numberLikes) style "kiwii_LikeCounter"

                    imagebutton:
                        idle "images/Phone/Kiwii/AppAssets/Comment.png"
                        hover "images/Phone/Kiwii/AppAssets/CommentHover.png"
                        action Show("kiwiiPost", post=post)
                        xoffset 290
                        yoffset 220


screen kiwiiPost(post):
    tag phoneTag

    use kiwiiTemplate:

        add Transform(post.image, size=(376, 212)) xalign 0.5 ypos 265

        vpgrid:
            cols 1
            mousewheel True
            draggable True
            xysize(350, 362)
            xalign 0.5
            ypos 485
            spacing 15

            for comment in post.comments:
                fixed:
                    xsize 350
                    ymaximum 90

                    vbox:
                        xsize 300
                        spacing 5

                        hbox:
                            spacing 10

                            add Transform(comment.getProfilePicture(), zoom=0.05)
                            text comment.getUsername() style "kiwii_ProfileName" yalign 0.5

                        text comment.getText() style "kiwii_CommentText"

                    hbox:
                        align(0.95, 1.0)

                        imagebutton:
                            idle "images/Phone/Kiwii/AppAssets/Like.png"
                            hover "images/Phone/Kiwii/AppAssets/LikePress.png"
                            selected_idle "images/Phone/Kiwii/AppAssets/LikePress.png"
                            selected comment.liked
                            action Function(comment.toggleLike)


                        text "{}".format(comment.numberLikes) style "kiwii_LikeCounter" yalign 0.5 xoffset 5

            null

    if post.replies:
        vbox xpos 1200 yalign 0.84 spacing 15:

            for reply in post.replies:
                textbutton reply.reply:
                    style "kiwii_reply"
                    text_style "kiwii_ReplyText"
                    action [Function(reply.selectedReply, post), Jump(reply.label)]

screen liked_kiwii():
    tag phoneTag

    $ liked_kiwiPosts = filter(lambda post: post.liked, kiwiiPosts)

    use kiwiiTemplate:

        vpgrid:
            cols 1
            mousewheel True
            draggable True
            xysize(350, 575)
            xalign 0.5
            ypos 265
            spacing 10

            for post in reversed(liked_kiwiPosts):
                fixed:
                    xysize (350, 350)
                    add "images/Phone/Kiwii/AppAssets/Post.png"

                    hbox:
                        spacing 10
                        xoffset 20
                        yoffset 20

                        add Transform(post.getProfilePicture(), zoom=0.05)
                        text post.getUsername() style "kiwii_ProfileName" yalign 0.5

                    vbox:
                        align(0.5, 0.5)
                        yoffset 18
                        spacing 5

                        imagebutton:
                            idle Transform(post.image, zoom=0.17)
                            action Show("kiwii_image", img=post.image)
                        text post.caption style "kiwii_CommentText" xalign 0.5

                    hbox:
                        xoffset 20
                        yoffset 220
                        spacing 5

                        imagebutton:
                            idle "images/Phone/Kiwii/AppAssets/Like.png"
                            hover "images/Phone/Kiwii/AppAssets/LikePress.png"
                            selected_idle "images/Phone/Kiwii/AppAssets/LikePress.png"
                            selected post.liked
                            action Function(post.toggleLike)
                        frame:
                            background "#fff"
                            yalign 0.5
                            padding (5, 2)

                            text "{}".format(post.numberLikes) style "kiwii_LikeCounter"

                    imagebutton:
                        idle "images/Phone/Kiwii/AppAssets/Comment.png"
                        hover "images/Phone/Kiwii/AppAssets/CommentHover.png"
                        action Show("kiwiiPost", post=post)
                        xoffset 290
                        yoffset 220

screen kiwii_image(img):
    modal True

    imagebutton:
        idle Transform(img, zoom=0.85)
        action Hide("kiwii_image")
        align (0.5, 0.5)

label kiwii_firstTime:
    $ kiwii_firstTime = False
    play sound "sounds/vibrate.mp3"
    if emilyrs:
        $ contact_Riley.newMessage(rileyMessage3)
    if bowling and emilyrs:
        $ contact_Penelope.newMessage(penelopeMessage4)
    if emilyrs and laurenrs:
        $ contact_Lauren.newMessage(laurenMessage15)
        $ contact_Lauren.newMessage(laurenMessage16)
    call screen kiwiiPreferences()

style kiwii_PrefTextButton is button_text:
    font "fonts/OpenSans-Bold.ttf"
    size 50

style kiwii_ProfileName is text:
    font "fonts/OpenSans-Bold.ttf"
    size 16
    color "#000"
    bold True

style kiwii_CommentText is text:
    font "fonts/OpenSans-Bold.ttf"
    size 14
    color "#000"

style kiwii_LikeCounter is text:
    font "fonts/OpenSans-Bold.ttf"
    size 14
    color "#000"

style kiwii_ReplyText is text:
    font "fonts/OpenSans-Bold.ttf"
    size 20
    color "#000"

style kiwii_reply is button:
    background "#fff"
    xpadding 15
    ypadding 5
    xmaximum 350
