init python:
    from enum import Enum


    class KCT(Enum):
        BRO = "bro"
        BOYFRIEND = "boyfriend"
        TROUBLEMAKER = "troublemaker"


    def add_point(var, value=1):
        # Update the KCT variables
        setattr(store, var.value, getattr(store, var.value) + value)
        
        old_kct = kct

        # Sort KCT values
        kctDict = {"popular": bro * troublemaker / boyfriend, "confident": boyfriend * troublemaker / bro, "loyal": bro * boyfriend / troublemaker}
        setattr(store, "sortedKCT", [k for k, v in sorted(kctDict.items(), key=lambda item: item[1], reverse=True)])
        
        # Update KCT
        setattr(store, "kct", sortedKCT[0])

        # Notify user on KCT change
        if sortedKCT[0] != old_kct:
            renpy.notify("Your KCT has changed to " + kct)