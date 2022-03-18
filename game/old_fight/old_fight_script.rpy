init python:
    class DefensiveMove:
        def __init__(self, move):
            self.move = move

    class FightMove:
        def __init__(self, move, damage, counter):
            self.move = move
            self.damage = damage
            self.counter = counter

        def playHitAnimation(self, attacker, defender):
            renpy.scene()
            if attacker.name == "MC":
                renpy.show("MC_{}_{}_hit".format(defender.name, self.move))
                renpy.pause(1)
            else:
                renpy.show("{}_{}_hit".format(attacker.name, self.move))
                renpy.with_statement(hpunch, always=True)
                renpy.pause(1)

        def playBlockAnimation(self, attacker, defender):
            renpy.scene()
            if attacker.name == "MC":
                renpy.show("MC_{}_{}_block".format(defender.name, self.move))
                renpy.pause(1)
            else:
                renpy.show("{}_{}_block".format(attacker.name, self.move))
                renpy.with_statement(hpunch, always=True)
                renpy.pause(1)

    class FightCharacter:
        def __init__(self, name, health, damageMult=1, attacks=None, defences=None):
            self.name = name
            self.health = health
            self.damageMult = damageMult
            
            if isinstance(attacks, list): self.attacks = attacks
            else: self.attacks = [kick, bodyJab, jab, hook] # Default attacks

            if isinstance(defences, list): self.defences = defences
            else: self.defences = [kneeBlock, highGuard, lowGuard, sideGuard]       

        def attack(self, target):
            self.selectedAttack = renpy.random.choice(self.attacks)

            # If defender counters, block attack
            if self.selectedAttack.counter == target.selectedDefence:
                self.selectedAttack.playBlockAnimation(self, target)
            else:
                self.selectedAttack.playHitAnimation(self, target)
                target.health -= self.selectedAttack.damage * self.damageMult

        def selectDefence(self):
            self.selectedDefence = renpy.random.choice(self.defences)

    def getCurrentAttacker():
        players.append(players.pop(0))
        return players[-1]

    def getCurrentDefender():
        players.insert(0, players.pop(-2))
        return players[0]

    def selectDifficulty(difficulty):
        if difficulty == "easy":
            # Old
            setattr(store, "reactiona", 3.2)
            setattr(store, "enemyhealth", 5)
            setattr(store, "youHealth", 5)
            # New
            setattr(store, "reaction", 3.5)
            # for enemy in enemies:
            #     enemy.damageMult = 1

        elif difficulty == "normal":
            # Old
            setattr(store, "reactiona", 1.5)
            setattr(store, "enemyhealth", 6)
            setattr(store, "youHealth", 3)
            # New
            setattr(store, "reaction", 1.5)
            # for enemy in enemies:
            #     enemy.damageMult = 2

        else:
            # Old
            setattr(store, "reactiona", 0.7)
            setattr(store, "enemyhealth", 8)
            setattr(store, "youHealth", 2)
            # New
            setattr(store, "reaction", 0.5)
            # for enemy in enemies:
            #     enemy.damageMult = 4