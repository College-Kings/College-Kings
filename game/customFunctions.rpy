init -1 python:
    def addPoint(var, value=1): 

        # Find and update the component variables
        varConversion = { "bro": "bro", "bf": "boyfriend", "tm": "troublemaker" }
        try: setattr(store, varConversion[var], getattr(store, varConversion[var]) + value)
        except KeyError: raise NameError("Name '{}' is not defined".format(var))

        # Update the trait points whenever one of the above variables are changed
        popular = bro * troublemaker / boyfriend
        loyal = bro * boyfriend / troublemaker
        confident = boyfriend * troublemaker / bro

        oldKCT = getattr(store, "kct")

        # Decide the new order of traits based on the updated values
        kctDict = { "popular": popular, "confident": confident, "loyal": loyal }
        setattr(store, "sortedKCT", [k for (k, v) in sorted(kctDict.items(), key=lambda k: k[0])])

        if sortedKCT[0] != oldKCT:
            setattr(store, "kct", sortedKCT[0])
            renpy.notify("Your KCT has changed to " + kct)


    # Mark disabled choices
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    def menu_override(items, set_expr, args, kwargs, item_arguments):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]
        return renpy.display.get_info().oldmenu(items, set_expr)
    renpy.exports.menu = menu_override


    def grantAchievement(achieve):
        renpy.show(achieve.replace("_", ""), at_list=achievementAtList)
        achievement.grant(achieve)
        achievement.sync()
