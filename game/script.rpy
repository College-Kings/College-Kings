define config.enable_steam = False
define config.developer = True
define config.console = True
define config_debug = False
define config_censored = False

define config.version = get_version(14, 0, 0)

define config.steam_appid = 1463120

define config.gl2 = True
define _quit_slot = "99-1"


# The game starts here.
label start:
    $ setup()

    $ naomi.messenger.newMessage("Hey, [name]! This is Naomi. The one and only... Lol.", force_send=True)

    if "v15_naomi" in sceneList:
        $ naomi.messenger.newMessage("Just wanted to say, as much as I enjoyed our little bathroom break, don't read too much into it. I just wanted to piss off Aubrey and well... mission succeeded!")
        $ naomi.messenger.newMessage("Anyway, maybe I'll message you again...")
        $ naomi.messenger.newMessage("Maybe I won't ;)")

    else:
        $ naomi.messenger.newMessage("Just wanted to say, as much as I would've enjoyed getting closer with you at the wedding, don't read too much into it. I just wanted to piss off Aubrey, haha. Definitely not into you like that.")
        $ naomi.messenger.newMessage("Still can't believe you turned me down, though?? Things must be serious between you two... Gross.")
        $ naomi.messenger.newMessage("Either way, no second chances ;)")
    
    $ naomi.messenger.addReply("Aw, come on... I saw that look in your eyes all night, we can have some fun together I think? ;)", v16s4_reply1)
    $ naomi.messenger.addReply("Please don't text me again. Thanks.", v16s4_reply2)


    call screen real_life_mode

label end_credits: # for compatibility
label gameEnd:
    stop music fadeout 3
    play music "music/vocal.mp3"

    call screen end_screen