init python:
    class BaseMessage:
        def __init__(self, content: str):
            self.content = content
            self.message = content
            self.image = content
            self.replies: list[BaseReply] = []
            self.reply: Optional[BaseReply] = None


    class BaseReply(BaseMessage):
        def __init__(self, content: str, func: Optional[Callable[[], None]]):
            self.content = content
            self.func = func


    class Reply(BaseReply):
        def __init__(
            self,
            message: str,
            func: Optional[Callable[[], None]] = None,
            disabled: bool = False,
        ):
            self.message = message
            self.func = func


    class ImgReply(BaseReply):
        def __init__(
            self,
            image: str,
            func: Optional[Callable[[], None]] = None,
            disabled: bool = False,
        ):
            self.image = image
            self.func = func


    class Message(BaseMessage):
        def __init__(self, contact: "Contact", message: str):
            self.contact = contact
            self.message = message
            self.replies: list[BaseReply] = []
            self.reply = None


    class ImageMessage(BaseMessage):
        def __init__(self, contact: "Contact", image: str):
            self.contact = contact
            self.image = image
            self.replies: list[BaseReply] = []
            self.reply = None
