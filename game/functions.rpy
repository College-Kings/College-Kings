init -1 python:
    def addPoint(var, count = 1): # Add "count" number of points to variable "var"
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
        
    # mark disabled choices
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    def menu_override(items, set_expr, args, kwargs, item_arguments):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]
        return renpy.display.get_info().oldmenu(items, set_expr)
    renpy.exports.menu = menu_override
