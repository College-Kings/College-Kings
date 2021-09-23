init python:
    class KiwiiPost:
        """
        Creates a post for the in game phone app, Kiwii

        Attributes:
            user (str): 
            img (str): 
            message (str, optional):
            mentions (list, optional): 
            numberLikes (int, optional):
        """

        def __init__(self, user, img, message="", mentions=None, numberLikes=renpy.random.randint(250, 500)):
            self.user = user
            self.img = "images/phone/kiwii/posts/{}".format(img)
            self.message = message

            if isinstance(mentions, basestring): self.mentions = [mentions]
            elif isinstance(mentions, list): self.mentions = mentions
            else: self.mentions = []

            self.numberLikes = numberLikes
            self.liked = False

            self.sentComments = []
            self.pendingComments = []

            kiwiiPosts.append(self)

            kiwiiApp.unlock()
            kiwiiApp.notification = True

        @property
        def username(self):
            return kiwiiUsers[self.user]["username"]

        @property
        def profile_picture(self):
            return kiwiiUsers[self.user]["profile_picture"]

        @property
        def replies(self):
            try: return self.sentComments[-1].replies
            except (AttributeError, IndexError): return []

        def toggleLike(self):
            self.liked = not self.liked

            if self.liked: self.numberLikes += 1
            else: self.numberLikes -= 1
            
        def newComment(self, user, message, numberLikes=renpy.random.randint(250, 500), mentions=None, queue=True):
            comment = KiwiiComment(user, message, numberLikes, mentions)
            
            # Add message to queue
            if queue:
                self.pendingComments.append(comment)
            else:
                self.pendingComments = []
                self.sentComments.append(comment)
            
            kiwiiApp.notification = True
            return comment

        def addReply(self, message, func=None, numberLikes=renpy.random.randint(250, 500), mentions=None, disabled=False):
            reply = KiwiiReply(message, func, numberLikes, mentions, disabled)
            
            # Append reply to last sent message
            try:
                if self.pendingComments:
                    self.pendingComments[-1].replies.append(reply)
                else:
                    self.sentComments[-1].replies.append(reply)
            except Exception:
                message = self.newComment("MC", "", queue=False)
                message.replies.append(reply)

            kiwiiApp.notification = True
            return reply

        def selectedReply(self, reply):
            self.newComment("MC", reply.message, reply.numberLikes, reply.mentions, queue=False)
            self.sentComments[-1].reply = reply
            self.sentComments[-1].replies = []

            # Run reply function
            try:
                reply.func()
                reply.func = None
            except TypeError: pass

            # Send next queued message(s)
            try:
                while not self.replies:
                    self.sentComments.append(self.pendingComments.pop(0))
            except IndexError: pass

        def get_message(self):
            usernames = [kiwiiUsers[mention]["username"] for mention in self.mentions]

            message = ", @".join(usernames)
            if usernames: message = "{{color=#3498DB}}{{b}}@{users}{{/b}}{{/color}} {text}".format(users=message, text=self.message)
            else: message = self.message

            return message

        def removePost(self):
            kiwiiPosts.remove(self)

    class KiwiiComment(KiwiiPost):
        def __init__(self, user, message, numberLikes=renpy.random.randint(250, 500), mentions=None):
            self.user = user
            self.message = message
            self.numberLikes = numberLikes

            if isinstance(mentions, basestring): self.mentions = [mentions]
            elif isinstance(mentions, list): self.mentions = mentions
            else: self.mentions = []

            self.liked = False
            self._replies = []
            self.reply = None

        @property
        def replies(self):
            return self._replies

        @replies.setter
        def replies(self, x):
            self._replies = x

    class KiwiiReply(KiwiiComment):
        def __init__(self, message, func=None, numberLikes=renpy.random.randint(250, 500), mentions=None, disabled=False):
            self.message = message
            self.func = func

            if kct == "popular": self.numberLikes = int(numberLikes * 1.5)
            elif kct == "confident": self.numberLikes = int(numberLikes * 1.2)
            else: self.numberLikes = numberLikes

            if isinstance(mentions, basestring): self.mentions = [mentions]
            elif isinstance(mentions, list): self.mentions = mentions
            else: self.mentions = []

            self.disabled = disabled

    def totalLikes():
        total = 0

        for post in kiwiiPosts:
            for comment in post.sentComments:
                if comment.user == "MC":
                    total += comment.numberLikes
            if post.user == "MC":
                total += comment.numberLikes

        return total

init -100:
    define profile_pictures = [
        "images/phone/kiwii/profile_pictures/mcpp1.webp",
        "images/phone/kiwii/profile_pictures/mcpp2.webp",
        "images/phone/kiwii/profile_pictures/mcpp3.webp",
        "images/phone/kiwii/profile_pictures/mcpp4.webp"
        ]
    default profile_pictures_count = 0

    default kiwiiPosts = []
    default liked_kiwiPosts = []

screen kiwiiTemplate():
    modal True
    zorder 200

    use phoneTemplate:
        add Transform("images/phone/kiwii/AppAssets/Background.webp", size=(376, 744)) at truecenter

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
    modal True
    zorder 200

    $ kiwiiUsers["MC"]["profile_picture"] = profile_pictures[profile_pictures_count]

    use kiwiiTemplate:

        add Transform(kiwiiUsers["MC"]["profile_picture"], zoom=0.2) align(0.5, 0.3)

        hbox:
            spacing 50
            align(0.5, 0.48)

            textbutton "<":
                if profile_pictures_count > 0:
                    action SetVariable("profile_pictures_count", profile_pictures_count - 1)
                text_style "kiwii_PrefTextButton"

            textbutton ">":
                if profile_pictures_count + 1 < len(profile_pictures):
                    action SetVariable("profile_pictures_count", profile_pictures_count + 1)
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
    zorder 200

    $ kiwiiApp.notification = False

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
                    add "images/phone/Kiwii/AppAssets/Post.webp"

                    hbox:
                        spacing 10
                        xoffset 20
                        yoffset 20

                        add Transform(post.profile_picture, size=(55, 55))
                        text post.username style "kiwii_ProfileName" yalign 0.5

                    vbox:
                        align(0.5, 0.5)
                        yoffset 18
                        spacing 5

                        imagebutton:
                            idle Transform(post.img, zoom=0.17)
                            action Show("kiwii_image", img=post.img)
                        text post.get_message() style "kiwii_CommentText" xalign 0.5

                    hbox:
                        xoffset 20
                        yoffset 220
                        spacing 5

                        imagebutton:
                            idle "images/phone/Kiwii/AppAssets/Like.webp"
                            hover "images/phone/Kiwii/AppAssets/LikePress.webp"
                            selected_idle "images/phone/Kiwii/AppAssets/LikePress.webp"
                            selected post.liked
                            action Function(post.toggleLike)
                        frame:
                            background "#fff"
                            yalign 0.5
                            padding (5, 2)

                            text "{}".format(post.numberLikes) style "kiwii_LikeCounter"

                    imagebutton:
                        idle "images/phone/Kiwii/AppAssets/Comment.webp"
                        hover "images/phone/Kiwii/AppAssets/CommentHover.webp"
                        action Show("kiwiiPost", post=post)
                        xoffset 290
                        yoffset 220


screen kiwiiPost(post):
    tag phoneTag
    zorder 200

    use kiwiiTemplate:

        imagebutton:
            xalign 0.5
            ypos 265
            idle Transform(post.img, size=(376, 212))
            action Show("kiwii_image", img=post.img)

        viewport:
            mousewheel True
            draggable True
            xysize(350, 362)
            xalign 0.5
            ypos 485
            
            vbox:
                spacing 20

                for comment in post.sentComments:
                    if comment.message.strip():
                        vbox:
                            spacing 5

                            hbox:
                                spacing 10

                                add Transform(comment.profile_picture, size=(55, 55))
                                text comment.username style "kiwii_ProfileName" yalign 0.5

                            hbox:
                                xsize 275
                                spacing 5

                                text comment.get_message() style "kiwii_CommentText"

                            hbox:
                                spacing 5

                                imagebutton:
                                    idle "images/phone/Kiwii/AppAssets/Like.webp"
                                    hover "images/phone/Kiwii/AppAssets/LikePress.webp"
                                    selected_idle "images/phone/Kiwii/AppAssets/LikePress.webp"
                                    selected comment.liked
                                    action Function(comment.toggleLike)
                                text "[comment.numberLikes]" style "kiwii_LikeCounter" yalign 0.5

    if post.replies:
        vbox:
            xpos 1200
            yalign 0.84
            spacing 15

            for reply in post.replies:
                textbutton reply.message:
                    text_style "kiwii_ReplyText"
                    if reply.disabled:
                        style "reply_disabled"
                    else:
                        style "kiwii_reply"
                        action Function(post.selectedReply, reply)

screen liked_kiwii():
    tag phoneTag
    zorder 200

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
                    add "images/phone/Kiwii/AppAssets/Post.webp"

                    hbox:
                        spacing 10
                        xoffset 20
                        yoffset 20

                        add Transform(post.profile_picture, size=(55, 55))
                        text post.username style "kiwii_ProfileName" yalign 0.5

                    vbox:
                        align(0.5, 0.5)
                        yoffset 18
                        spacing 5

                        imagebutton:
                            idle Transform(post.img, zoom=0.17)
                            action Show("kiwii_image", img=post.img)
                        text post.message style "kiwii_CommentText" xalign 0.5

                    hbox:
                        xoffset 20
                        yoffset 220
                        spacing 5

                        imagebutton:
                            idle "images/phone/Kiwii/AppAssets/Like.webp"
                            hover "images/phone/Kiwii/AppAssets/LikePress.webp"
                            selected_idle "images/phone/Kiwii/AppAssets/LikePress.webp"
                            selected post.liked
                            action Function(post.toggleLike)
                        frame:
                            background "#fff"
                            yalign 0.5
                            padding (5, 2)

                            text "{}".format(post.numberLikes) style "kiwii_LikeCounter"

                    imagebutton:
                        idle "images/phone/Kiwii/AppAssets/Comment.webp"
                        hover "images/phone/Kiwii/AppAssets/CommentHover.webp"
                        action Show("kiwiiPost", post=post)
                        xoffset 290
                        yoffset 220

screen kiwii_image(img):
    modal True
    zorder 300

    imagebutton:
        idle Transform(img, zoom=0.85)
        action Hide("kiwii_image")
        align (0.5, 0.5)