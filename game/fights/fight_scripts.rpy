init python:
    def selectDifficulty(difficulty):
        if difficulty == "easy":
            # Old
            setattr(store, "reactiona", 3.2)
            setattr(store, "larshealth", 5)
            setattr(store, "youHealth", 5)
            # New
            setattr(store, "reaction", 3.5)
            for enemy in enemies:
                enemy.damageMult = 1

        elif difficulty == "normal":
            # Old
            setattr(store, "reactiona", 1.5)
            setattr(store, "larshealth", 6)
            setattr(store, "youHealth", 3)
            # New
            setattr(store, "reaction", 1.5)
            for enemy in enemies:
                enemy.damageMult = 2

        else:
            # Old
            setattr(store, "reactiona", 0.7)
            setattr(store, "larshealth", 8)
            setattr(store, "youHealth", 2)
            # New
            setattr(store, "reaction", 0.5)
            for enemy in enemies:
                enemy.damageMult = 4