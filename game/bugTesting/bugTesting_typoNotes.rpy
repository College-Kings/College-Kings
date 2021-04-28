init python:

    def enterNote():
        note = renpy.input("Enter Note:", screen="input_note")
        return note


    def addTypo():
        filename = "_bugTesting.txt"

        with open(os.path.join(config.basedir, "game", "bugTesting", filename), 'a' ) as f:
            f.write("Typo at {}:\n{}\n\n".format(renpy.get_filename_line(), _last_say_what))
 
        renpy.notify("Successfully logged typo to {}.".format(filename))


    def addNote():
        filename = "_bugTesting.txt"
        note = renpy.invoke_in_new_context(enterNote)

        if note:
            with open(os.path.join(config.basedir, "game", "bugTesting", filename), 'a' ) as f:
                f.write("Note created at {}:\n{}\n\n".format(renpy.get_filename_line(), note))

            renpy.notify("Successfully logged typo to {}.".format(filename))
            return
        renpy.notify("Note cancelled.")

image typoNotesBackground = "bugTesting/images/typoNotesBackground.webp"

screen input_note(prompt):
    modal True
    style_prefix "input"
    add "#000"

    vbox:
        align (0.5, 0.1)
        xsize 950

        text "Enter Note Below" xalign 0.5
        input id "input"

screen typoNotesOverlay():
    $ fileLine = renpy.get_filename_line()
    text "[fileLine!q]" xalign 0.99 color "#0f0"

    vbox:
        textbutton "Add Note":
            action Function(addNote)

        textbutton "Log Typo":
            action Function(addTypo)
