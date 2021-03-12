init -1 python:
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
        
    # mark disabled choices
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    def menu_override(items, set_expr, args, kwargs, item_arguments):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]
        return renpy.display.get_info().oldmenu(items, set_expr)
    renpy.exports.menu = menu_override
    
    #achievements
    achievement.register("open_wound")
    achievement.register("no_hard_feelings")
    achievement.register("keep_it_moving")
    achievement.register("romeo")
    achievement.register("big_mouth")
    achievement.register("mixed_feelings")
    achievement.register("the_notorious")
    achievement.register("a_new_beginning")
    achievement.register("over_it")
    achievement.register("not_now_mom")
    achievement.register("lips_dont_lie")
    achievement.register("truth_hurts")
    achievement.register("relight_the_fire")
    achievement.register("rematch")
    achievement.register("keen_eye")
    achievement.register("on_the_low")
    achievement.register("peta_public_enemy")
    achievement.register("snitch")
    achievement.register("bros_before_hoes")
    achievement.register("monkey_business")
    achievement.register("not_my_business")
    achievement.register("reignition")
    achievement.register("credulous")
    achievement.register("seems_fishy")
    achievement.register("strike")
    achievement.register("ecstatic")
    achievement.register("homecomingqueen")
    achievement.register("lee_way")
    achievement.register("playing_with_fire")
    achievement.register("silverback")
    achievement.register("slow_and_steady")
    achievement.register("true_to_self")
    achievement.register("wolfpack")
    achievement.sync()
