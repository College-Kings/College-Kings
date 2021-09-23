init python:
    class BaseCheatItem:
        """
        Base cheat data class for storing the attributes of cheat options

        Attributes:
            catagory (str): Generic catagory name for organising cheat items
            name (str): Display name for cheat option
        """

        def __init__(self, catagory, name):
            self.catagory = catagory
            self.name = name

            cheatItems.append(self)


    class SliderCheat(BaseCheatItem):
        """
        Slider type cheat item

        Attributes:
            variable (str, optional): Attached variable for cheat option. Defaults to ""
            min_value (int, optional): The minimum value the slider type can obtain. Defaults to 0
            max_value (int, optional): The maximum value the slider type can obtain. Defaults to 0
        """

        def __init__(self, catagory, name, variable, min_value=0, max_value=0):
            BaseCheatItem.__init__(self, catagory, name)

            self.variable = variable
            self.min_value = min_value
            self.max_value = max_value


    class ButtonCheat(BaseCheatItem):
        """
        Slider type cheat item

        Attributes:
            variable (str, optional): Attached variable for cheat option. Defaults to ""
            true_value (bool, optional): The value set when the button is selected. Defaults to True
            false_value (bool, optional): The value set when the button is not selected. Defaults to False
        """

        def __init__(self, catagory, name, variable, true_value=True, false_value=False):
            BaseCheatItem.__init__(self, catagory, name)

            self.variable = variable
            self.true_value = true_value
            self.false_value = false_value

    class FunctionCheat(BaseCheatItem):
        def __init__(self, catagory, name, func):
            BaseCheatItem.__init__(self, catagory, name)

            self.func = func


    def get_cheat_catagories():
        seen = set()
        return [item.catagory for item in cheatItems if not (item.catagory in seen or seen.add(item.catagory))]

    def unlockPhoneContacts():
        for contact in contacts:
            contact.unlock()


    cheatItems = []

    ButtonCheat("General", "Chloe Mad", "chloemad")
    ButtonCheat("General", "Nora Mad", "noramad")
    ButtonCheat("General", "Lauren Mad", "laurenmad")
    ButtonCheat("General", "Penelope Mad", "penelopemad")
    ButtonCheat("General", "Imre Mad", "imremad")
    ButtonCheat("General", "Lauren Rs", "laurenrs")
    ButtonCheat("General", "Aubrey Rs", "aubreyrs")
    ButtonCheat("General", "Riley Rs", "rileyrs")
    ButtonCheat("General", "Emily Rs", "emilyrs")
    ButtonCheat("General", "Evelyn Rs", "evelynrs")
    ButtonCheat("General", "Forgive Emily", "forgiveemily")
    ButtonCheat("General", "Revenge Adam", "revengeadam")
    ButtonCheat("General", "Bowling w/ Penelope", "bowling")
    ButtonCheat("General", "Telling Grayson you'll join the Apes", "joinapes")
    ButtonCheat("General", "Joining Wolves", "joinwolves")
    ButtonCheat("General", "Kissed Chloe if not Chloemad", "fr3chloe")
    ButtonCheat("General", "Nora kinda likes you if not Noramad", "fr3nora")
    ButtonCheat("General", "You and Nora are close", "noraclose")
    ButtonCheat("General", "Met Grayson", "meetgrayson")
    ButtonCheat("General", "Make signs with Autumn", "signs")
    ButtonCheat("General", "fr3riley", "fr3riley")
    ButtonCheat("General", "Viking Costume", "costume", true_value=1, false_value="Cheat Error")
    ButtonCheat("General", "Knight Costume", "costume", true_value=2, false_value="Cheat Error")
    ButtonCheat("General", "Cowboy Costume", "costume", true_value=3, false_value="Cheat Error")

    ButtonCheat("KCT", "KCT = Popular", "kct", true_value="popular", false_value="Cheat Error")
    ButtonCheat("KCT", "KCT = Loyal", "kct", true_value="loyal", false_value="Cheat Error")
    ButtonCheat("KCT", "KCT = Confident", "kct", true_value="confident", false_value="Cheat Error")

    ButtonCheat("FR4", "Go alone", "hcGirl", true_value="alone", false_value="Cheat Error")
    ButtonCheat("FR4", "Go with Chloe", "hcGirl", true_value="chloe", false_value="Cheat Error")
    ButtonCheat("FR4", "Go with Emily", "hcGirl", true_value="emily", false_value="Cheat Error")
    ButtonCheat("FR4", "Go with Lauren", "hcGirl", true_value="lauren", false_value="Cheat Error")
    ButtonCheat("FR4", "Go with Penelope", "hcGirl", true_value="penelope", false_value="Cheat Error")
    ButtonCheat("FR4", "Go with Riley", "hcGirl", true_value="riley", false_value="Cheat Error")

    ButtonCheat("FR4", "fr4chloe", "fr4chloe")
    ButtonCheat("FR4", "fr4ryan", "fr4ryan")
    ButtonCheat("FR4", "fr4aubrey", "fr4aubrey")
    ButtonCheat("FR4", "fr4riley", "fr4riley")
    ButtonCheat("FR4", "fr4nora", "fr4nora")
    ButtonCheat("FR4", "fr4nora2", "fr4nora2")
    ButtonCheat("FR4", "fr4grayson", "fr4grayson")
    ButtonCheat("FR4", "Prevent Grayson from spraying", "preventgrayson")
    ButtonCheat("FR4", "Blowjob in bathroom", "bathroomblowjob")
    ButtonCheat("FR4", "Defend Chloe in front of Ryan", "ryandefendchloe")
    ButtonCheat("FR4", "Chloe is sad from Ryan & Grayson", "chloesad")

    ButtonCheat("Phone", "Unlock Kiwii", "kiwiiApp.locked", true_value=False, false_value=True)
    ButtonCheat("Phone", "Unlock Simplr", "simplrApp.locked", true_value=False, false_value=True)

    FunctionCheat("Phone", "Unlock Phone Contacts", unlockPhoneContacts)


screen bugTesting_cheatMenu():
    tag cheat_menu
    modal True
    zorder 300

    default cheat_catagory = "General"
    default cheat_catagories = get_cheat_catagories()

    add "#23272a"
    add "/bugTesting/images/cheatMenuBackground.webp"

    fixed:
        xysize (1536, 99)
        pos (85, 13)

        hbox:
            align (0.5, 0.5)
            spacing 100
            for cheatCatagory in cheat_catagories:
                textbutton cheatCatagory:
                    action [Function(renpy.retain_after_load), SetScreenVariable("cheat_catagory", cheatCatagory)]
                    text_style "modTextButtonHeader"

    use bugTesting_cheatMenuValues(cheat_catagory=cheat_catagory)

    imagebutton:
        action Hide("bugTesting_cheatMenu"), Hide("bugTesting_cheatMenuValues"), SetVariable("quick_menu", True)
        idle "/bugTesting/images/cheatMenuBackButton.webp"
        hover im.MatrixColor("/bugTesting/images/cheatMenuBackButton.webp", im.matrix.brightness(0.2))
        pos (1666, 50)


screen bugTesting_cheatMenuValues(cheat_catagory="General"):
    tag cheat_menu
    modal True
    zorder 300

    vpgrid:
        cols 4

        xalign 0.5
        ypos 120
        xspacing 100
        yspacing 60

        for cheat_item in cheatItems:
            if cheat_item.catagory == cheat_catagory:
                vbox:
                    style_prefix "check"

                    if isinstance(cheat_item, SliderCheat):
                        pass

                    elif isinstance(cheat_item, ButtonCheat):
                        textbutton cheat_item.name:
                            action ToggleVariable(cheat_item.variable, true_value=cheat_item.true_value, false_value=cheat_item.false_value)
                            text_style "modTextButtonBody"

                    elif isinstance(cheat_item, FunctionCheat):
                        textbutton cheat_item.name:
                            action Function(cheat_item.func)
                            text_style "modTextButtonBody"