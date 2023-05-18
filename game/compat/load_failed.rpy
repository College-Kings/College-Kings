label load_failed:
    renpy.execute_default_statement()

    call after_load

    python:
        try:
            for i in reversed(list(label_history)):
                if renpy.has_label(i) and i.startswith("v"):
                    renpy.jump(i)
        except NameError: pass

        renpy.jump("v1_start")