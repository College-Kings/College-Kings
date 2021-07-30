init -1 python:
    def addPoint(var, value=1): 

        # Find and update the component variables
        varConversion = { "bro": "bro", "bf": "boyfriend", "tm": "troublemaker" }
        try: setattr(store, varConversion[var], getattr(store, varConversion[var]) + value)
        except KeyError: raise NameError("Name '{}' is not defined".format(var))

        # Update the trait points whenever one of the above variables are changed

        oldKCT = getattr(store, "kct")

        # Decide the new order of traits based on the updated values
        kctDict = {"popular": bro * troublemaker / boyfriend, "confident": boyfriend * troublemaker / bro, "loyal": bro * boyfriend / troublemaker}
        setattr(store, "sortedKCT", [k for k, v in sorted(kctDict.items(), key=lambda item: item[1], reverse=True)])

        if sortedKCT[0] != oldKCT:
            setattr(store, "kct", sortedKCT[0])
            renpy.notify("Your KCT has changed to " + kct)

    def grantAchievement(achieve):
        try:
            renpy.show(achieve, at_list=achievementAtList)
        except TypeError: pass
        achievement.grant(achieve) 
        achievement.sync()
        