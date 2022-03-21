init python:
    class KiwiiPost:
        """
        Creates a post for the in game phone app, Kiwii

        Attributes:
            user (NonPlayableCharacter): 
            image (str): 
            message (str, optional):
            mentions (list<NonPlayableCharacter>, optional): 
            numberLikes (int, optional):
        """

        def __init__(self, user, image, message="", mentions=None, numberLikes=renpy.random.randint(250, 500)):
            self.user = user
            self.image = "images/phone/kiwii/posts/{}".format(image)
            self.message = message

            if isinstance(mentions, basestring): self.mentions = [mentions]
            elif isinstance(mentions, list): self.mentions = mentions
            else: self.mentions = []

            self.numberLikes = numberLikes

            self.liked = False

            self.sentComments = []
            self.pendingComments = []

            kiwiiPosts.append(self)

            kiwii.unlock()

        @property
        def username(self):
            return self.user.username

        @property
        def profile_picture(self):
            return self.user.profile_picture

        @property
        def replies(self):
            try: return self.sentComments[-1].replies
            except (AttributeError, IndexError): return []

        def toggleLike(self):
            self.liked = not self.liked

            if self.liked: self.numberLikes += 1
            else: self.numberLikes -= 1
            
        def new_comment(self, user, message, numberLikes=renpy.random.randint(250, 500), mentions=None, force_send=False):
            comment = KiwiiComment(user, message, numberLikes, mentions)
            
            # Add message to queue
            if not force_send:
                self.pendingComments.append(comment)
            else:
                self.pendingComments = []
                self.sentComments.append(comment)
            
            kiwii.notification = True
            return comment

        def add_reply(self, message, func=None, numberLikes=renpy.random.randint(250, 500), mentions=None, disabled=False):
            reply = KiwiiReply(message, func, numberLikes, mentions, disabled)
            
            # Append reply to last sent message
            try:
                if self.pendingComments:
                    self.pendingComments[-1].replies.append(reply)
                else:
                    self.sentComments[-1].replies.append(reply)
            except Exception as e:
                message = self.newComment(mc, "", force_send=True)
                message.replies.append(reply)

            kiwii.notification = True
            return reply

        def selected_reply(self, reply):
            self.newComment(mc, reply.message, reply.numberLikes, reply.mentions, force_send=True)
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
            usernames = [mention.username for mention in self.mentions]

            message = ", @".join(usernames)
            if usernames: message = "{{color=#3498DB}}{{b}}@{users}{{/b}}{{/color}} {text}".format(users=message, text=self.message)
            else: message = self.message

            return message

        def remove_post(self):
            kiwiiPosts.remove(self)
            del self

        # Backwards compatibility.
        def newComment(self, user, message, numberLikes=renpy.random.randint(250, 500), mentions=None, force_send=False):
            return self.new_comment(user, message, numberLikes, mentions, force_send)

        def addReply(self, message, func=None, numberLikes=renpy.random.randint(250, 500), mentions=None, disabled=False):
            return self.add_reply(message, func, numberLikes, mentions, disabled)

        def selectedReply(self, reply):
            return self.selected_reply(reply)


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
            try: self._replies
            except AttributeError: self._replies = []

            return self._replies

        @replies.setter
        def replies(self, value):
            self._replies = value


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

    def get_total_likes():
        return sum(post.numberLikes for post in kiwiiPosts if post.user == mc) + sum(
            comment.numberLikes
            for post in kiwiiPosts
            for comment in post.sentComments
            if comment.user == mc
        )

    def find_kiwii_post(image=None, message=None):
        for post in kiwiiPosts:
            if post.image == image: return post
            if post.message == message: return post


default kiwiiPosts = []
default liked_kiwiPosts = []


screen kiwii_base():
    modal True

    default image_path = "images/phone/kiwii/app-assets/"

    use base_phone:
        frame:
            background image_path + "background.webp"

            transclude

            hbox:
                ysize 72
                xalign 0.5
                ypos 843
                spacing 45

                imagebutton:
                    idle image_path + "home-button-idle.webp"
                    hover image_path + "home-button-hover.webp"
                    action Show("kiwii_home")
                    yalign 0.5

                null width 25

                null width 45

                imagebutton:
                    idle image_path + "liked-button-idle.webp"
                    hover image_path + "liked-button-hover.webp"
                    action Show("kiwii_home", posts=filter(lambda post: post.liked, kiwiiPosts))
                    yalign 0.5

                imagebutton:
                    idle Transform(mc.profile_picture, xysize=(30, 30))
                    action Show("kiwii_preferences")
                    yalign 0.5


screen kiwii_preferences():
    tag phone_tag
    modal True

    default profile_pictures_index = 0

    use kiwii_base:
        vbox:
            xalign 0.5
            ypos 175
            spacing 25

            vbox:
                xalign 0.5
                spacing 5

                add Transform(mc.profile_picture, xysize=(200, 200)) xalign 0.5

                hbox:
                    spacing 50
                    align (0.5, 0.45)

                    textbutton "<":
                        if profile_pictures_index > 0:
                            action [SetScreenVariable("profile_pictures_index", profile_pictures_index - 1),
                                SetField(mc, "profile_picture", mc.profile_pictures[profile_pictures_index])]
                        text_style "kiwii_PrefTextButton"

                    textbutton ">":
                        if profile_pictures_index + 1 < len(mc.profile_pictures):
                            action [SetScreenVariable("profile_pictures_index", profile_pictures_index + 1),
                                SetField(mc, "profile_picture", mc.profile_pictures[profile_pictures_index])]
                        text_style "kiwii_PrefTextButton"

            vbox:
                xalign 0.5

                text "Username:" style "kiwii_ProfileName" xalign 0.5
                input:
                    value FieldInputValue(mc, "username")
                    default name
                    length 15
                    color "#006400"
                    outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]
                    xalign 0.5

            vbox:
                xalign 0.5

                text "Total Likes:" style "kiwii_ProfileName" at truecenter
                text str(get_total_likes()) at truecenter:
                    color "#006400"
                    outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]


screen kiwii_home(posts=kiwiiPosts):
    tag phone_tag

    default image_path = "images/phone/kiwii/app-assets/"

    $ kiwii.notification = False

    use kiwii_base:

        viewport:
            mousewheel True
            draggable True
            ypos 152
            ysize 692

            vbox:
                xalign 0.5
                xsize 416

                null height 20

                for post in reversed(posts):
                    frame:
                        xalign 0.5
                        xsize 386
                        padding (10, 10)

                        has vbox

                        hbox:
                            xsize 366

                            hbox:
                                spacing 10

                                add Transform(post.profile_picture, xysize=(55, 55))
                                text post.username style "kiwii_ProfileName" yalign 0.5

                            hbox:
                                spacing 5
                                align (1.0, 0.5)

                                add image_path + "static-button-1.webp"
                                add image_path + "static-button-2.webp"

                        null height 10

                        vbox:
                            spacing 5

                            imagebutton:
                                idle Transform(post.image, xysize=(366, 206))
                                action Show("kiwii_image", img=post.image)
                                xalign 0.5
                            text post.get_message() style "kiwii_CommentText" xalign 0.5

                        null height 10

                        hbox:
                            xsize 366

                            hbox:
                                imagebutton:
                                    idle image_path + "like.webp"
                                    hover image_path + "like-press.webp"
                                    selected_idle image_path + "like-press.webp"
                                    selected post.liked
                                    action Function(post.toggleLike)

                                text "{}".format(post.numberLikes) style "kiwii_LikeCounter" yalign 0.5

                            imagebutton:
                                idle image_path + "comment.webp"
                                hover image_path + "commenthover.webp"
                                action Show("kiwiiPost", post=post)
                                xalign 1.0


screen kiwiiPost(post):
    tag phone_tag
    zorder 200

    default image_path = "/images/phone/kiwii/app-assets/"

    use kiwii_base:
        imagebutton:
            idle Transform(post.image, xysize=(416, 234))
            action Show("kiwii_image", img=post.image)
            xalign 0.5
            ypos 152
            
        viewport:
            mousewheel True
            draggable True
            xysize (357, 400)
            pos (20, 386)

            vbox:
                spacing 20

                null

                for comment in post.sentComments:
                    if comment.message.strip():
                        vbox:
                            spacing 5

                            hbox:
                                spacing 10

                                add Transform(comment.profile_picture, xysize=(55, 55))
                                text comment.username style "kiwii_ProfileName" yalign 0.5

                            text comment.get_message() style "kiwii_CommentText"

                            hbox:
                                spacing 5

                                imagebutton:
                                    idle image_path + "like.webp"
                                    hover image_path + "like-press.webp"
                                    selected_idle image_path + "like-press.webp"
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


screen kiwii_image(img):
    modal True

    imagebutton:
        idle Transform(img, zoom=0.85)
        action Hide("kiwii_image")
        align (0.5, 0.5)