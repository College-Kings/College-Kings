init python:
    def addPoint(var, count): # Add "count" number of points to variable "var"
        # Import all the global variables you use in the function
        global bro
        global boyfriend
        global troublemaker
        global loyal
        global popular
        global confident
        global kct # New variable that stores the order of traits

        if var == "bro":
            bro += count
        elif var == "bf":
            boyfriend += count
        elif var == "tm":
            troublemaker += count

        # Update the trait points whenever one of the above variables are changed
        popular = bro * troublemaker / boyfriend
        loyal = bro * boyfriend / troublemaker
        confident = boyfriend * troublemaker / bro

        oldkct = kct

        # Decide the new order of traits based on the updated values
        if popular >= loyal:
            if loyal >= confident:
                kct = "popular"
            else:
                if popular >= confident:
                    kct = "popular"
                else:
                    kct = "confident"
        else:
            if popular >= confident:
                kct = "loyal"
            else:
                if loyal >= confident:
                    kct = "loyal"
                else:
                    kct = "confident"

        if not kct == oldkct:
            renpy.notify("Your KCT has changed to " + kct)
        return
        
