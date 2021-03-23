init python:
    class CheatItem:
        def __init__(self, catagory, name, variable, kind="Slider", minValue=0, maxValue=0, trueValue=True, falseValue=False):
            self.catagory = catagory
            self.name = name
            self.variable = variable
            if kind == "Slider":
                self.minValue = minValue
                self.maxValue = maxValue
            elif kind == "Button":
                self.trueValue = trueValue
                self.falseValue = falseValue
            else:
                raise Exception("Unsupported Cheat Type")
            self.kind = kind
            cheatItems.append(self)

    def updateCatagory():
        cheatCatagorys = []

        for cheatItem in cheatItems:
            if cheatItem.catagory not in cheatCatagorys:
                cheatCatagorys.append(cheatItem.catagory)

        return cheatCatagorys

    def unlockPhoneContacts():
        for contact in contacts:
            contact.unlock()

    def checkPhoneUnlock():
        if not any([contact.locked for contact in contacts]):
            return True
        else:
            return False

default cheatItems = []

default var1 = CheatItem("General", "Chloe Mad", "chloemad", kind="Button")
default var2 = CheatItem("General", "Nora Mad", "noramad", kind="Button")
default var3 = CheatItem("General", "Lauren Mad", "laurenmad", kind="Button")
default var4 = CheatItem("General", "Penelope Mad", "penelopemad", kind="Button")
default var5 = CheatItem("General", "Imre Mad", "imremad", kind="Button")
default var6 = CheatItem("General", "Lauren Rs", "laurenrs", kind="Button")
default var7 = CheatItem("General", "Aubrey Rs", "aubreyrs", kind="Button")
default var8 = CheatItem("General", "Riley Rs", "rileyrs", kind="Button")
default var9 = CheatItem("General", "Emily Rs", "emilyrs", kind="Button")
default var10 = CheatItem("General", "Evelyn Rs", "evelynrs", kind="Button")
default var11 = CheatItem("General", "Forgive Emily", "forgiveemily", kind="Button")
default var12 = CheatItem("General", "Revenge Adam", "revengeadam", kind="Button")
default var13 = CheatItem("General", "Bowling w/ Penelope", "bowling", kind="Button")
default var14 = CheatItem("General", "Telling Grayson you'll join the Apes", "joinapes", kind="Button")
default var15 = CheatItem("General", "Joining Wolves", "joinwolves", kind="Button")
default var16 = CheatItem("General", "Kissed Chloe if not Chloemad", "fr3chloe", kind="Button")
default var17 = CheatItem("General", "Nora kinda likes you if not Noramad", "fr3nora", kind="Button")
default var18 = CheatItem("General", "You and Nora are close", "noraclose", kind="Button")
default var19 = CheatItem("General", "Met Grayson", "meetgrayson", kind="Button")
default var20 = CheatItem("General", "Make signs with Autumn", "signs", kind="Button")
default var32 = CheatItem("General", "fr3riley", "fr3riley", kind="Button")
default cos1 = CheatItem("General", "Viking Costume", "costume", kind="Button", trueValue=1, falseValue="Cheat Error")
default cos2 = CheatItem("General", "Knight Costume", "costume", kind="Button", trueValue=2, falseValue="Cheat Error")
default cos3 = CheatItem("General", "Cowboy Costume", "costume", kind="Button", trueValue=3, falseValue="Cheat Error")


default kctP = CheatItem("KCT", "KCT = Popular", "kct", kind="Button", trueValue="popular", falseValue="Cheat Error")
default kctL = CheatItem("KCT", "KCT = Loyal", "kct", kind="Button", trueValue="loyal", falseValue="Cheat Error")
default kctC = CheatItem("KCT", "KCT = Confident", "kct", kind="Button", trueValue="confident", falseValue="Cheat Error")

default hcGirlNo = CheatItem("FR4", "Go alone", "hcGirl", kind="Button", trueValue="alone", falseValue="Cheat Error")
default hcGirlCl = CheatItem("FR4", "Go with Chloe", "hcGirl", kind="Button", trueValue="chloe", falseValue="Cheat Error")
default hcGirlEm = CheatItem("FR4", "Go with Emily", "hcGirl", kind="Button", trueValue="emily", falseValue="Cheat Error")
default hcGirlLa = CheatItem("FR4", "Go with Lauren", "hcGirl", kind="Button", trueValue="lauren", falseValue="Cheat Error")
default hcGirlPe = CheatItem("FR4", "Go with Penelope", "hcGirl", kind="Button", trueValue="penelope", falseValue="Cheat Error")
default hcGirlRi = CheatItem("FR4", "Go with Riley", "hcGirl", kind="Button", trueValue="riley", falseValue="Cheat Error")

default var21 = CheatItem("FR4", "fr4chloe", "fr4chloe", kind="Button")
default var22 = CheatItem("FR4", "fr4ryan", "fr4ryan", kind="Button")
default var23 = CheatItem("FR4", "fr4aubrey", "fr4aubrey", kind="Button")
default var24 = CheatItem("FR4", "fr4riley", "fr4riley", kind="Button")
default var25 = CheatItem("FR4", "fr4nora", "fr4nora", kind="Button")
default var26 = CheatItem("FR4", "fr4nora2", "fr4nora2", kind="Button")
default var27 = CheatItem("FR4", "fr4grayson", "fr4grayson", kind="Button")
default var28 = CheatItem("FR4", "Prevent Grayson from spraying", "preventgrayson", kind="Button")
default var29 = CheatItem("FR4", "Blowjob in bathroom", "bathroomblowjob", kind="Button")
default var30 = CheatItem("FR4", "Defend Chloe in front of Ryan", "ryandefendchloe", kind="Button")
default var31 = CheatItem("FR4", "Chloe is sad from Ryan & Grayson", "chloesad", kind="Button")

default unlockContacts = CheatItem("Phone", "", "", kind="Button")
default kiwiiUnlock = CheatItem("Phone", "Unlock Kiwii", "kiwiiApp.locked", kind="Button", trueValue=False, falseValue=True)


screen bugTesting_cheatMenu():
    modal True
    zorder 200

    default shownCheatMenu = "general"

    add "#23272a"
    add "/bugTesting/images/cheatMenuBackground.webp"

    fixed:
        xysize (1536, 99)
        pos (85, 13)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for cheatCatagory in updateCatagory():
                textbutton cheatCatagory:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", cheatCatagory)]
                    text_style "modTextButtonHeader"

    for cheatCatagory in updateCatagory():
        if shownCheatMenu == cheatCatagory:
            use bugTesting_cheatMenuValues(cheatMenuChar=cheatCatagory)

    imagebutton:
        action Hide("bugTesting_cheatMenu"), Hide("bugTesting_cheatMenuValues"), SetVariable("quick_menu", True)
        idle "/bugTesting/images/cheatMenuBackButton.webp"
        hover im.MatrixColor("/bugTesting/images/cheatMenuBackButton.webp", im.matrix.brightness(0.2))
        pos (1666, 50)

screen bugTesting_cheatMenuValues(cheatMenuChar="General"):
    tag cheatmenu

    vbox:
        pos (103, 120)
        spacing 100

        vpgrid:
            cols 4
            spacing 100
            for cheatItem in cheatItems:
                if cheatItem.catagory == cheatMenuChar and cheatItem.kind == "Button":
                    vbox:
                        style_prefix "check"
                        textbutton "[cheatItem.name]":
                            action ToggleVariable(cheatItem.variable, true_value=cheatItem.trueValue, false_value=cheatItem.falseValue)
                            text_style "modTextButtonBody"

            if cheatMenuChar == "Phone":
                    vbox:
                        style_prefix "check"
                        textbutton "Unlock All Phone Contacts":
                            action Function(unlockPhoneContacts)
                            selected checkPhoneUnlock()
                            text_style "modTextButtonBody"
