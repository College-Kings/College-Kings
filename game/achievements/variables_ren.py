from typing import Callable

from game.achievements.Achievements_ren import Achievement

_: Callable[[str], str] = lambda x: x

"""renpy
init python:
"""

# region v1
open_wound = Achievement("open_wound", _("Tell off Emily")).register()
no_hard_feelings = Achievement("no_hard_feelings", _("Play nice with Emily")).register()
# endregion v1

# region v2
mixed_feelings = Achievement("mixed_feelings", _("Decline Lauren")).register()
# endregion v2

# region v8
text_with_an_s = Achievement("text_with_an_s", _("Return to sender")).register()
# endregion v8
