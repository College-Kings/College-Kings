init python:
    class RepComponent(Enum):
        BRO = enum.auto()
        BOYFRIEND = enum.auto()
        TROUBLEMAKER = enum.auto()


    class Reputations(Enum):
        POPULAR = enum.auto()
        CONFIDENT = enum.auto()
        LOYAL = enum.auto()

        BRO = "bro"
        BOYFRIEND = "boyfriend"
        TROUBLEMAKER = "troublemaker"

        @classmethod
        def _missing_(cls, value):
            return cls.POPULAR


    class Reputation:
        def __init__(self):
            self.components = {
                RepComponent.BRO: 10,
                RepComponent.BOYFRIEND: 20,
                RepComponent.TROUBLEMAKER: 20,
            }

        def __call__(self):
            bro = self.components[RepComponent.BRO]
            boyfriend = self.components[RepComponent.BOYFRIEND]
            troublemaker = self.components[RepComponent.TROUBLEMAKER]

            # Sort reputation values
            reputation_dict = {
                Reputations.POPULAR: bro * troublemaker / float(boyfriend),
                Reputations.CONFIDENT: boyfriend * troublemaker / float(bro),
                Reputations.LOYAL: bro * boyfriend / float(troublemaker),
            }

            return max(reputation_dict, key=lambda k: reputation_dict[k])

        @property
        def sorted_reputations(self):
            bro = self.components[RepComponent.BRO]
            boyfriend = self.components[RepComponent.BOYFRIEND]
            troublemaker = self.components[RepComponent.TROUBLEMAKER]

            # Sort reputation values
            reputation_dict = {
                Reputations.POPULAR: bro * troublemaker / float(boyfriend),
                Reputations.CONFIDENT: boyfriend * troublemaker / float(bro),
                Reputations.LOYAL: bro * boyfriend / float(troublemaker),
            }

            return [k for k, v in sorted(reputation_dict.items(), key=helper_sorted_key, reverse=True)]

        def add_point(self, var: Reputations, value: int = 1):
            # Don't update reputation if reputation is locked
            if locked_reputation or _in_replay:
                return

            if pb_reputation_notification:
                renpy.show_screen("popup", message=f"{var.name.capitalize()} point added")

            old_reputation = self()

            self.components[var] += value

            # Notify user on reputation change
            if self() != old_reputation:
                renpy.notify(f"Your reputation has changed to {self().name}")

        def change_reputation(self, target_reputation: Reputations):
            if target_reputation == Reputations.POPULAR:
                self.components = {
                    RepComponent.BRO: 20,
                    RepComponent.TROUBLEMAKER: 20,
                    RepComponent.BOYFRIEND: 10,
                }

            elif target_reputation == Reputations.LOYAL:
                self.components = {
                    RepComponent.BRO: 20,
                    RepComponent.TROUBLEMAKER: 10,
                    RepComponent.BOYFRIEND: 20,
                }

            elif target_reputation == Reputations.CONFIDENT:
                self.components = {
                    RepComponent.BRO: 10,
                    RepComponent.TROUBLEMAKER: 20,
                    RepComponent.BOYFRIEND: 20,
                }


# Reputation Screens
screen reputation_choice_hint():
    style_prefix "reputation_choice"

    frame:
        xalign 1.0
        xoffset -100

        background "gui/reputation/background_{}.webp".format(reputation().name.lower())

        hbox:
            spacing 5
            align (0.5, 0.5)
            xoffset 20

            add Transform("gui/reputation/logo.webp", zoom=0.2382) yalign 0.5

            text reputation().name yalign 0.5

style reputation_choice_text is syne_extra_bold_22


screen reputation_popup(required_reputation=None):
    modal True
    zorder 300

    if required_reputation is None or required_reputation == reputation():
        $ message = "Congratulations! Your reputation {{b}}{}{{/b}} has just changed the outcome of a decision someone was making.".format(reputation().name)
    else:
        $ message = "Unfortunately, your reputation {{b}}{}{{/b}} did not change the outcome of this decision.".format(reputation().name)

    use alert_template(message):
        textbutton "OK":
            align (0.5, 1.0)
            action Return()

    if config_debug:
        timer 0.1 action Return()